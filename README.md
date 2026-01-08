# SecureMesh

SecureMesh is an educational defensive cybersecurity project that simulates a distributed network security system.

The system combines client-side monitoring (IDS / IPS / Firewall concepts) with a central server for event correlation and analysis.

## Project Goals
- Detect suspicious network behavior on endpoints
- Enforce basic security rules on the client side
- Correlate events from multiple clients on a central server
- Provide a foundation for GUI-based monitoring and control

## Structure

src/securemesh/ # Core project code
tests/ # Automated tests


## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt

Run
python -m securemesh

Notes
    This project is for learning purposes
