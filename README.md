🚗 AI Automotive Testing Assistant

An AI-enhanced automotive CAN log analysis tool built with Python, Streamlit, and LLM-based engineering analysis.

This project demonstrates how traditional automotive ECU validation workflows can be integrated with AI-assisted diagnostics to accelerate CAN log analysis, abnormal frame detection, and root-cause investigation.

✨ Features
    📂 Upload Vector .blf CAN logs
    🔄 Automatically convert BLF → Pandas DataFrame → CSV
    ⚠️ Detect abnormal CAN frames
    Invalid payloads (7F ...)
    Message timeout gaps
    Timing violations
    📊 Interactive Streamlit dashboard
    🤖 AI-powered engineering analysis using GitHub Copilot SDK / LLM
    📥 Download converted CSV logs
    🧩 Modular architecture for future DBC, UDS, and DTC decoding
    🏗️ Project Architecture
    
Vector CANoe / CANalyzer
          │
          ▼
      .blf file
          │
          ▼
   python-can BLFReader
          │
          ▼
   Pandas DataFrame
          │
   ┌──────┴────────┐
   ▼               ▼
Abnormal       CSV Export
Detection
   │
   ▼
AI Engineering Analysis--->Stores in .txt file
   │
   ▼
Streamlit Dashboard

Project Structure

AI-Automotive-Assistant/
│
├
│
├── src/
│   ├── app.py               # Streamlit UI
│   ├── analyzer.py          # CAN abnormal frame detection
│   ├── blf_parser.py        # BLF → DataFrame conversion
│   ├── ai_helper.py         # AI / Copilot SDK integration
│   └── __init__.py
│
├── reports/
│   ├── abnormal_frames_xxx.csv
│   └── converted_can_log.csv
│    └──ai_analysis_xxxxxx.txt
│   
│── data/
│   ├── sample_can_log.csv
│   └── CAN-Trace.blf     # ".bf" file contains CAN traces
│
│
├
└── README.md

Installation.
1. Clone the repository
    git clone https://github.com/your-username/AI-Automotive-Assistant.git 
    cd AI-Automotive-Assistant
    
2.Create a virtual environment.

3.Install dependencies

    Dependencies
        streamlit
        pandas
        python-can
        python-dotenv
        copilot-sdk
        
4.Please Install Pycharm community latest edition.

🚀Running the Application

From the project root:

    streamlit run src/app.py

Open the browser at:

    http://localhost:8501

📂 Using the Tool
Step 1 — Upload a BLF file

    Upload a Vector CANoe / CANalyzer .blf log.

Step 2 — Automatic Parsing

    The tool converts the BLF into a structured DataFrame:

    Time	ID	DLC	Data
    12.345	0x120	8	7F 00 00 00 00 00 00 0A
    12.445	0x100	8	10 22 45 00 00 00 00 00
    
Step 3 — Abnormal Frame Detection

    Detected issues include:

    Invalid Payload
    Message Timeout
    Timing Gap Violations
    
Step 4 — AI Analysis

    The application generates an engineering summary such as:

    Failure Summary
    - Invalid payloads detected on CAN ID 0x120
    - Communication timeout detected on CAN ID 0x100

    Probable Root Causes
    - ECU watchdog reset
    - CAN Bus-Off recovery
    - Sensor communication failure
    - Power supply interruption

    Recommended Tests
    - Ignition cycle test
    - Voltage drop robustness test
    - High bus-load stress test
    - Temperature chamber validation
    
🧠 AI Integration

The project uses an LLM-based engineering assistant through the GitHub Copilot SDK.

Instead of sending thousands of raw CAN frames directly to the model, the tool first builds a condensed statistical summary:
Then find unique abnormal frames(deleting repeated abnormal frames)
Total abnormal frames: 28463
Most affected CAN IDs:
  - 0x120: 18002 frames
  - 0x100: 10461 frames

Issue distribution:
  - Invalid Payload: 18002
  - Message Timeout: 10461

This approach improves:

    ⚡ Performance
    💰 Token efficiency
    🎯 Diagnostic relevance
    🤖 LLM response quality
    
🔍 Example Abnormal Frame Detection
Input
    Time      ID      Data
    12.345    0x120  7F FF FF FF FF FF FF FF
    12.445    0x120  7F FF FF FF FF FF FF FF
    15.800    0x100  10 22 45 00 00 00 00 00
Output
    Time	ID	Issue
    12.345	0x120	Invalid Payload
    12.445	0x120	Invalid Payload
    15.800	0x100	Message Timeout

📊 Dashboard Preview

The Streamlit UI provides:

    📈 CAN log summary metrics
    📄 Parsed frame viewer
    ⚠️ Abnormal event table
    🤖 AI engineering report
    📥 CSV download button
    
    
🛠️ Future Enhancements

    DBC signal decoding using cantools

    UDS diagnostic decoder (ISO 14229)

    DTC extraction and interpretation

    CAN-FD support

    PDF validation report generation

    Trend charts and timing graphs

    Machine-learning-based anomaly detection

    RAG knowledge base for AUTOSAR / ISO standards

🎯 Automotive Use Cases

This project is relevant for:

    Automotive Test Automation Engineer
    CANoe / CANalyzer Validation Engineer
    ECU Integration Test Engineer
    ADAS Validation Engineer
    AUTOSAR Software Validation Engineer
    HIL / SIL Test Automation Engineer
    
🧪 Tested With
    Tool	Version
    Python	3.11+
    Streamlit	1.48+
    pandas	2.x
    python-can	4.x
    Vector BLF	CANoe / CANalyzer generated logs
    
🤝 Contributing

Contributions are welcome!

If you’d like to add:

    DBC decoding
    UDS services
    Additional anomaly detectors
    Better AI prompts
    Report generation templates

please open an issue or pull request.

📜 License

This project is released under the MIT License.

👨‍💻 Author

Pradeep Jayarama
email:itzmepradeep238@gmail.com

Automotive Testing & Validation Engineer
CAN / UDS / ECU Integration

AI-assisted Automotive Test Automation

GitHub: https://github.com/your-username

⭐ Why This Project Matters

Traditional automotive validation tools are excellent at capturing and filtering CAN traffic, but engineers still spend significant time interpreting failures, correlating abnormal events, and planning follow-up tests.

This project demonstrates how AI can augment automotive testing workflows by combining:

    Vector BLF log processing
    Automated anomaly detection
    Statistical summarization
    LLM-based engineering reasoning
    Interactive visualization

The result is a practical prototype of an AI-powered automotive validation assistant capable of accelerating CAN log triage, root-cause investigation, and regression analysis in modern ECU development environments.