If you are struggling where to start, you can follow these general guidelines to set up the lab and get data flowing. 

There is obviously room to customize this set up to your needs or interests, but this is how I set up mine. I will document the steps I took and problems I ran into. 

My VMs are all set up to ingest logs into Microsoft Sentinel via the AMA agent and data collection rules. My detections are created in Sigma and translated to Sentinel KQL. You can use the Sigma in the tactics folder of this repo as your basis for your detection rule in whatever language you want; just pump it into a translation tool and select the language you want for your specific SIEM (YARA for Google SecOps, Splunk QL for Splunk, EQL for Elastic, so on so forth)

First, set up the VMs
  I used Oracle VirtualBox because it is free and I am pretty used to the interface, but any virtualization software should work, honestly. 
  I downloaded VirtuaBox and set up separate directories on my PC for the VMs, the ISO files I will be creating the VMs with, and each VM's shared folder. 
  I would recommend some variety. I set up a Windows 2022 Server VM, a Windows 10 VM, and an Ubuntu 22 VM. The installation and setup of each is generally the same: 
    
    1. Download the ISOs.
        a. For the Windows 10 VM, I created an installation media based on my PC using this doc (https://support.microsoft.com/en-us/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d
        b. For the Windows 2022 Server, I used the Evaluation version for this because it is free. Yeah, it expires after 180 days, but the set up is really fast so it's not much of a hassle.
        c. Download the Ubuntu 22 ISO from Ubuntu's previous releases download page. Since I am using Microsoft Sentinel, the most recen release I can use (as of writing this June 2026) is Ubuntu 24
    2. Create a new VM in VirtualBox and select the ISO you downloaded. The deafult specs are usually alright he re. The only thing I changed was upping the RAM spec a bit so the VMs aren't as squishy. 
    3. Start the VMs and follow the basic user set ups. Once you have a login, you should make sure you have the VirtualBox shared folders set up. You'll need that for the next part. 

Next, get the VMs ready for log ingestion
  Since I am using Microsoft Sentinel here, there are about 4 general steps you'll have to follow: 

  1. Onboard the VMs to Azure Arc. The reason you need to do this is to essentially make the VM an Azure resource that can be monitored. If you were to create the VMs in Azure, you wouldn't need to onboard the VMs into Azure Arc. 
      a. You can follow the MSFT docs to do this. The only note I would give to save you a bit of time is to use a service principal to authenticate rather than enter your creds each time. The service principal will need the Azure Arc Machine Onboarding role assigned to it. When you create it, it will give you a txt file with the ID and secret. You will need to plug this into the onboarding script you download
      b. Fill out the onboarding script with the service principal. You will need one script for linux (give you a bash script) and one for Windows (gives you a powershell script). Upload the filled-out scripts to your VM Shared Folders you created in the previous section. 
      c. Sign in and run your scripts to onboard your VMs to Azure Arc. Note: this doc is super handy for any script error codes you may get -> https://learn.microsoft.com/en-us/azure/azure-arc/servers/troubleshoot-agent-onboard
  2. In your Sentinel instance, go to Content Management then Content Hub. From here, download the Windows Security Events, Syslog, and Custom Logs via AMA solutions. This will give you parsers, some general analytic rules, and workbooks. You mostly need the data connectors. 
  3. Once the data connectors are downloaded, go to Configuration then Data Connectors page in Sentinel. Click on each data connector you downloaded, then "View connector page", then "+Create a data collection rule". Follow the wizard to set them up
      a. Windows Security Events: I chose the Common log level here. You will have the option to filter out specfic EventIDs at any time to save some ingestion costs. I'll document those in a separate note sheet. 
      b. Syslog via AMA: I set all log facilities to the LOG_NOTICE level so I am kinda collecting it all. This can also be changed at any time and there are plenty of transforms you can write to filter logs as you wish. 
