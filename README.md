
# 🛡️ SOAR-GPT: AI-Powered Security Alert Triage Assistant

This micro-project simulates a lightweight **SOAR (Security Orchestration, Automation, and Response)** system using **GPT-3.5** to assist in **cybersecurity alert classification** and triage. It demonstrates how language models can interpret security event logs, assign threat types and severities, and generate analyst-ready summaries.

---

## 🚀 Features

- Accepts structured JSON logs (e.g., from SIEM tools like Splunk, Elastic, or CrowdStrike)
- Uses prompt-based classification with LLMs to:
  - Identify **threat type** (e.g., brute force, phishing, insider threat)
  - Assign **severity** (Low / Medium / High)
  - Generate a **1-line summary** for analysts
- Designed as a beginner-friendly simulation for SOAR-LLM integration

---

## 📂 Project Structure

```
soar-gpt/
├── alerts/
│   └── alert1.json        # Sample input alert
├── gpt_assistant.py       # Core script for triage logic and GPT interaction
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

---

## 📄 Example Alert Input

`alerts/alert1.json`:
```json
{
  "timestamp": "2024-06-28T10:32:00Z",
  "source_ip": "192.168.1.54",
  "destination_ip": "10.0.0.9",
  "event_type": "user_login_failed",
  "details": "5 failed login attempts within 3 minutes from same IP"
}
```

---

## 🧠 GPT Prompt Logic

The alert is fed into a prompt like:

```
Given the following security event log:

{alert}

Classify the type of threat (e.g., brute force, phishing, insider threat).
Assign a severity (Low, Medium, High).
Summarize in 1 line for an analyst.

Return JSON:
{
  "threat_type": ...,
  "severity": ...,
  "summary": ...
}
```

---

## 💡 Sample Output (Mocked)

```json
{
  "threat_type": "Brute Force Login Attempt",
  "severity": "Medium",
  "summary": "Multiple failed login attempts from the same IP address."
}
```

---

## 🛠️ Requirements

- Python 3.7+
- [OpenAI Python SDK](https://pypi.org/project/openai/)

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Script

```bash
python gpt_assistant.py
```

> 📝 This version simulates GPT output. To use real OpenAI API calls, replace the mock section with:
```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": prompt}]
)
```

---

## 🧰 Possible Extensions

- 🌀 Batch processing multiple alerts
- 📊 Compare GPT classification vs rule-based logic
- 🌐 Deploy with Streamlit for analyst-facing UI
- 🎯 Map alerts to MITRE ATT&CK tactics

---

## 🧠 Why This Matters

LLMs can help reduce alert fatigue, enrich raw logs, and assist human analysts by providing natural-language summaries and prioritization — especially useful in low-signal or ambiguous cases.

---

## 📜 License

This project is for **educational and demonstration purposes only**. Not intended for production use.
