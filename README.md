# MINI-LAB - Server Setup

Follow these steps to set up and run the MINI-LAB server locally

---

## 1. Clone the repository

```bash
git clone https://github.com/pedromf3/mini-lab.git
cd mini-lab
```

## 2. Create a virtual environment

```bash
python3 -m venv venv
```

#### Activate it!
On Linux/Mac:

```bash
source venv/bin/activate
```

On Windows (PowerShell):

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Add your API key
The server requires an API key to fetch weather data. Create a file named api_key.txt in the root directory of the project and paste your Visual Crossing Weather API key inside it.

## 5. Run the server

```bash
python app.py
```

## 6. Open in browser
http://127.0.0.1:5000/

