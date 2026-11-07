# Flask Calculator Web Application & API

A lightweight Flask-based calculator web application and REST API created for the Programming Language Lab (PL-Lab). This repository demonstrates building interactive web forms with Jinja2 templates and handling query-based RESTful API endpoints in Python.

---

## 📁 Repository Structure

```text
calculator/
│
├── app.py              # Main Flask application (Interactive Web UI + REST API)
├── hello.py            # Practice/starter Flask API endpoints and routing
├── requirements.txt    # Project dependencies
└── templates/
    └── index.html      # HTML template with Jinja2 for calculator interface
```

---

## 🛠️ Prerequisites

Ensure you have **Python 3.8 or higher** installed on your system. You can verify your installation by running:

```bash
python --version
# or on macOS/Linux
python3 --version
```

---

## 🚀 Setup Instructions (Virtual Environment & Dependencies)

Follow these steps to set up and run the project using a Python virtual environment (`venv`).

### 1. Open Terminal / Command Prompt

Navigate to the project root directory:

```bash
cd path/to/calculator
```

### 2. Create a Virtual Environment

Run the following command to create a virtual environment named `venv`:

- **Windows:**
  ```cmd
  python -m venv venv
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  ```

---

### 3. Activate the Virtual Environment

Activate the environment based on your operating system and shell:

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(If you get a script execution policy error, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then try again).*

- **Windows (Command Prompt - cmd.exe):**
  ```cmd
  venv\Scripts\activate.bat
  ```

- **Windows (Git Bash) / macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

> **Note:** Once activated, your terminal prompt will show `(venv)` at the beginning of the line.

---

### 4. Install Dependencies

With the virtual environment active, install all required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

*(Optional) You can ensure `pip` is up to date before installing:*
```bash
python -m pip install --upgrade pip
```

---

## ▶️ Running the Applications

### Option 1: Run the Full Calculator App (`app.py`)

`app.py` serves an interactive browser interface along with structured API endpoints and maintains calculation history.

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```text
   http://127.0.0.1:5000/
   ```

#### Features:
- **Web Interface (`/`)**: Input two numbers, select an operation (`add`, `subtract`, `multiply`, `divide`), submit to compute results, and view calculation history.
- **REST API Endpoint (`/api/<operation>`)**:
  - Example: `http://127.0.0.1:5000/api/add?a=15&b=25`
  - Response:
    ```json
    {
      "operation": "add",
      "result": 40.0
    }
    ```
  - Available operations: `add`, `subtract`, `multiply`, `divide`.

---

### Option 2: Run the Starter API App (`hello.py`)

`hello.py` demonstrates route parameters, greetings, and dedicated operation endpoints.

1. Start the server:
   ```bash
   python hello.py
   ```

2. Access endpoints in your browser or via curl:
   - **Greeting**: `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/YourName`
   - **Addition**: `http://127.0.0.1:5000/add?a=10&b=20`
   - **Subtraction**: `http://127.0.0.1:5000/subtract?a=50&b=15`
   - **Multiplication**: `http://127.0.0.1:5000/multiply?a=6&b=7`
   - **Division**: `http://127.0.0.1:5000/divide?a=100&b=4`

---

## 🛑 Stopping the Server & Deactivating venv

- **Stop the Flask server**: Press `Ctrl + C` in the terminal.
- **Deactivate virtual environment**: Run the command:
  ```bash
  deactivate
  ```

---

## ❓ Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **`Activate.ps1 cannot be loaded because running scripts is disabled`** | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in PowerShell before running the activation script. |
| **`Address already in use` / Port 5000 conflict** | Ensure no other Flask instance or service is running on port 5000, or edit `app.run(debug=True, port=5001)` to use another port. |
| **`ModuleNotFoundError: No module named 'flask'`** | Verify your virtual environment is active (terminal should display `(venv)`), then run `pip install -r requirements.txt`. |

