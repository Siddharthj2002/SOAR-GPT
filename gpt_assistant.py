import json
import openai

# Load an alert
with open("alerts/alert1.json") as f:
    alert = json.load(f)

# Compose prompt
prompt = f"""
Given the following security event log:

{alert}

Classify the type of threat (e.g., brute force, phishing, insider threat).
Assign a severity (Low, Medium, High).
Summarize in 1 line for an analyst.

Return JSON:
{{
  "threat_type": ...,
  "severity": ...,
  "summary": ...
}}
"""

# Send to GPT (mocked here for safety)
print("=== Prompt ===")
print(prompt)
print("\n=== Response (sample) ===")
print(json.dumps({
    "threat_type": "Brute Force Login Attempt",
    "severity": "Medium",
    "summary": "Multiple failed login attempts from the same IP address."
}, indent=2))
