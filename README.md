# jwt-key-generator

This script was typically written to automate creating .env variables for [Chronicler](https://github.com/mrdsx/chronicler) which needs security keys for JWT authentication. The result of running script is jwks-es.json and .env file. The second file is important step when setting environment variables for [Chronicler](https://github.com/mrdsx/chronicler) backend.

## Getting started

### Prerequisites

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)

### 1. Clone the Repository and go to project directory

```bash
git clone https://github.com/mrdsx/jwt-key-generator.git
cd jwt-key-generator
```

### 2. Setup virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run script

```bash
python run.py
```
