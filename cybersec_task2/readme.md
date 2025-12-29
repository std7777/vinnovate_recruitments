# Vulnerable E-Commerce API

A simple backend e-commerce API provided for a **security audit exercise**.

---

## 🛡️ Security Audit Task

This project is being evaluated for potential **production deployment**.

Your task is to perform a **security review** of the codebase and assess its security posture.

This is a **defensive security task** — no exploitation is required.

---

## 🎯 Objective

Identify and explain:
- Security vulnerabilities
- Potential impact and likelihood
- Practical mitigation strategies

Think like an **Application Security Engineer**, not a penetration tester.

---

## 🧩 Scope

Review the following:
- Application code
- Authentication & authorization logic
- JWT usage
- Dependencies
- Configuration and secrets
- Attack surface and trust boundaries

---

## 🚫 What Not To Do

- Do not exploit vulnerabilities
- Do not run automated attack tools
- Do not modify the code to demonstrate attacks

---

## 📄 Deliverable

Submit a **Security Audit Report** (Markdown or PDF) including:
- Brief project overview
- Identified issues with severity (Low / Medium / High)
- Evidence (file names / code references)
- Mitigation recommendations
- Final assessment (production-ready or not)

---

## 🛠️ Running the Application (Optional)

### Requirements
- Python 3.9+
- pip

### Setup
In your terminal
```bash
git clone https://github.com/vinnovateit/cybersec_task2.git
cd vuln-ecommerce-api
python -m venv venv
venv\Scripts\activate # For Linux or Mac source venv/bin/activate
pip install -r requirements.txt
```

#### Create a Database for testing your API endpoints
Enter this in your terminal
```bash
python
```
Then copy paste the next code directly into python
```python
import sqlite3

conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

cur.execute("CREATE TABLE users (username TEXT, password TEXT, role TEXT)")
cur.execute("CREATE TABLE orders (user TEXT, product TEXT)")

cur.execute("INSERT INTO users VALUES ('admin','admin123','admin')")
cur.execute("INSERT INTO users VALUES ('user1','password','user')")

conn.commit()
conn.close()
exit()
```

### Run Server
```bash
python app.py
```

Your server will start at
```
http://127.0.0.1:5000
```

### For Sumbission of the task
Use the provided submission_template.md for your report.
