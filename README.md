# DawsHacks_Automation

At Script Benders, we’re passionate about building innovative solutions fast—turning ideas into impactful prototypes 
without the complexity. We thrive on collaboration, creativity, and problem-solving under pressure.

In this hackathon, we aim to accelerate development, tackle real-world challenges, and deliver seamless user 
experiences. By combining diverse skills in coding, design, and strategy, we track our progress collaboratively, 
iterate quickly, and stay agile. Our mission: bend the script, break boundaries, and build something awesome.

## How to run LeadPilot

```
git clone https://gitlab.com/Jaehyoonx/dawshacks_automation.git
cd git_repo
python -m venv .venv-leadpilot
. .venv-leadpilot/Scripts/activate
pip install -r requirements.txt'
python
import secrets
secrets.token_hex(24)
>>> copy secret_key
>>> exit python terminal
export SECRET_KEY='secret_key'
flask --app run.py run --debug
>>> open local host http://127.0.0.1:5000 on your browser
```
