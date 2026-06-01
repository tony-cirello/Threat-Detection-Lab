# Threat-Detection-Lab
 
This is a lab environment that can be used to teach the front-to-back process of Detection and Response. It is primarily meant to be used as a teaching tool. 

The topics covered are: 
  - Log Ingestion to SIEMs
  - SIEM alert creation
  - Automated responses to alerts

Pre-requisites: 
1. Multiple VMs: I spun up a Windows 10, Windows Server 2022, and an Ubuntu 22 VM using VirtualBox.
2. Connection to SIEM: In my lab, I am ingesting these logs to Microsoft Sentinel. There are a few steps to accomplish this:
   - Install and connect Azure Arc: Since we are using VirtualBox in this case, you need to connect the VMs to Azure with Azure Arc. If you are also using Microsoft Sentinel and don't want to bother with Azure Arc, you would have to create Azure-hosted VMs.
3. Log Ingestion: Create Data Collection Rules (DCRs) in Azure for the related logging. This will differ slightly on each endpoint, but generally you will need the following DCRs
   - A Windows Security Event DCR: Installed from Sentinel Content Hub (it's free, don't worry). You should only need the basic events covered; no need for verbose log collection. You will assign the Windows 10 and Windows 2022 machines to this DCR once you've gotten them connected to Azure Arc.
   - A Syslog via AMA DCR: Another free data connector installed from Sentinel Content Hub. This will be the event collection for your Linux server. You may have to do some tweaking on your local syslog config so it collects everything you need, but the ingestion from the server to Sentinel will be handled by the AMA agent. I would recommend setting this to listen on all log facilities.
   
     You can find some general Microsoft docs to help with steps 2 and 3 above here:
     - https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-connected-machine-agent?tabs=WindowsScript
     - https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview
     
     Once you create and assign the DCRs accordingly, the AMA and its configs will push to the VMs automatically. 
