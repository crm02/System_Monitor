# System Monitor

A real-time system monitoring dashboard built with Flask and Chart.js.

## Features
- Live CPU usage tracking
- RAM usage monitoring
- Disk activity monitoring
- Network upload/download speeds
- Interactive charts 

## Installation

1. Clone the repository:
```bash
git clone https://github.com/crm02/system-monitor.git
cd system-monitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The dashboard will automatically open in your browser at `http://127.0.0.1:5000`

## Requirements
- Python 3.7+
- Flask
- psutil

## License
MIT
```

**3. .gitignore** - Don't commit unnecessary files:
```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv
*.egg-info/
dist/
build/
.DS_Store
*.log
```

**4. Project structure** should look like:
```
system-monitor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    └── index.html