# Monitoring-for-Suspicious-HTTP-Requests
Python Script: Monitoring for Suspicious HTTP Requests

To address the Cisco Secure Firewall Management Center (FMC) vulnerability (CVE-2024-20424), it's important to emphasize that ethical hacking and responsible disclosure are key principles in dealing with vulnerabilities. Writing scripts to exploit vulnerabilities without explicit permission is illegal and unethical. Instead, you should focus on developing solutions or mitigation scripts that help detect, block, or patch such vulnerabilities.

Given the context of this vulnerability, let's develop a Python script to monitor and detect potential exploitation attempts by analyzing web request logs and looking for suspicious inputs. The script will alert you if any HTTP requests contain patterns that might suggest an attacker is trying to inject commands through the FMC's management interface.

How It Works:
Log Monitoring: The script reads from the web server’s log file in real-time, monitoring for any HTTP requests that contain suspicious characters often used in command injection attacks (e.g., ;, &&, |, etc.).

Pattern Matching: The script uses regular expressions to find potentially malicious input in HTTP requests.

Alert Logging: If a suspicious request is found, it is logged into a separate suspicious_activity.log file for further investigation.

How to Use:
Run the Script: Place this Python script on the server where your Cisco FMC management interface is hosted (or where logs are accessible). Ensure the path to the log file is correct.

Monitor Logs: The script will run indefinitely, watching for potential command injection attempts and alerting you if suspicious patterns are detected.

Take Action: If you detect suspicious activity, it’s critical to patch the system immediately (apply the latest updates from Cisco) and review logs for further compromise.

Important:
Always follow best practices for network security and apply patches issued by Cisco as soon as they become available.
This script is for defensive purposes only. Use it to detect potential attacks and secure your environment responsibly.
