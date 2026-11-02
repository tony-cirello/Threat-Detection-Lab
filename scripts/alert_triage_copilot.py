import os
import json
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client (expects OPENAI_API_KEY environment variable)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SOC_ANALYST_SYSTEM_PROMPT = """
You are an elite Tier 2 Senior SOC Analyst and Incident Responder. Your job is to analyze 
raw Microsoft Sentinel security alerts and provide an immediate, structured triage brief 
for junior analysts or automated response pipelines. 

Always structure your response in clear Markdown with the following sections:
1. **Executive Summary:** A 2-sentence plain-English description of what happened.
2. **Threat Assessment & Risk Level:** Evaluate the potential impact (Low, Medium, High, Critical) and justify why.
3. **Key Indicators of Compromise (IoCs):** Extract specific accounts, IPs, hostnames, or command-line strings from the payload.
4. **Recommended Triage Actions:** Provide 3 concrete, prioritized steps for a human analyst to validate whether this is a true positive or false positive.
"""

@app.route("/triage", methods=["POST"])
def triage_alert():
    try:
        # Parse incoming JSON payload from Azure Sentinel / Logic App webhook
        alert_data = request.get_json()
        
        if not alert_data:
            return jsonify({"error": "Invalid or empty JSON payload"}), 400

        # Extract core fields from standard Sentinel alert schema
        alert_name = alert_data.encapsulated_alert.get("AlertName", "Unknown Alert")
        alert_severity = alert_data.encapsulated_alert.get("Severity", "Unknown")
        tactics = alert_data.encapsulated_alert.get("Tactics", "N/A")
        raw_entities = alert_data.encapsulated_alert.get("Entities", [])
        alert_description = alert_data.encapsulated_alert.get("Description", "No description provided.")

        # Construct the user prompt for the LLM
        user_prompt = f"""
        Please triage the following Microsoft Sentinel Security Alert:
        
        - **Alert Name:** {alert_name}
        - **Severity:** {alert_severity}
        - **MITRE Tactics:** {tactics}
        - **Description:** {alert_description}
        - **Extracted Entities / Telemetry:** {json.dumps(raw_entities, indent=2)}
        """

        # Call OpenAI API (using gpt-4o or gpt-4-turbo for high-fidelity reasoning)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SOC_ANALYST_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1,  # Low temperature for analytical consistency
            max_tokens=800
        )

        triage_output = response.choices[0].message.content

        # Return structured triage response
        return jsonify({
            "status": "success",
            "alert_name": alert_name,
            "severity": alert_severity,
            "ai_triage_brief": triage_output
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    # Run locally on port 5000 for testing with ngrok or local webhooks
    app.run(host="0.0.0.0", port=5000, debug=False)
