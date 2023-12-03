# backdoor
This script can be used maliciously as a backdoor on a target system, allowing an attacker to execute arbitrary commands on the victim's machine remotely. The script attempts to ensure persistence by copying itself to the Windows Startup folder, ensuring it runs every time the system starts. It communicates with a Command and Controlserver to receive commands and send output/results.
