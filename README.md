# 📘 AI Tutor – MEAN Region Project Submission

An interactive **AI Tutor application** built with **Python, Gradio, and OpenAI/GitHub Models API**.
The app allows users to ask any question and get explanations at different depth levels (from *like I’m 5 years old* to *PhD-level detail*).

This project demonstrates **API integration, rate limiting, error handling, modular code design, and UI development**.

---

## 🚀 Features

* **Multiple Explanation Levels** – Choose from 6 levels of depth in explanations.
* **Streaming Responses** – Answers stream progressively for a smoother user experience.
* **Rate Limiting** – Built-in safeguard to respect API usage policies.
* **Error Handling** – Handles authentication, forbidden access, and rate-limit errors gracefully.
* **Persistent Storage** – Logs questions, responses, and Q\&A pairs to local files.
* **Gradio UI** – Simple and shareable web interface for interaction.
* **Modular Design** – Clean separation of API, UI, storage, and configuration.

---

## 🏗️ Project Structure

```
ai_tutor/
│── app.py              # Entry point (Gradio UI + app launch)
│── tutor_client.py     # Handles OpenAI/GitHub API requests
│── rate_limiter.py     # Manages request throttling
│── storage.py          # Handles saving Questions & Responses
│── config.py           # Environment & configuration management
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/IsmailMohamed010/ai_tutor.git
cd AI_Tutor
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
GITHUB_TOKEN=your_github_models_token_here
```

### 5. Run the App

```bash
python app.py
```

Gradio will start the web interface at:

```
http://127.0.0.1:7860
```

---

## 🧩 Example Usage

* Open the web UI.
* Type: *"Explain Machine Learning"*
* Choose level **2 (like I’m 10 years old)**.
* Get a friendly, step-by-step explanation.

---

## 📂 Data Logging

The app automatically saves:

* **Questions.txt** → All user questions
* **Responses.txt** → All model responses
* **QnA.txt** → Paired Q\&A history

---

## 🔐 Security Notes

* Never hardcode API tokens.
* Use `.env` file with `dotenv` to load secrets.
* Add `.env` to `.gitignore` before pushing code.

---

## 🏅 Evaluation Notes (for Hiring Managers)

This project demonstrates:

* ✅ Knowledge of **Python API integration**
* ✅ Awareness of **rate limiting**
* ✅ Ability to build **interactive AI apps**
* ✅ Basic **error handling & persistence**
* ✅ Code structured for **team collaboration**

Potential Improvements:

* Replace file storage with **database logging**.
* Implement **dynamic rate-limit backoff** using API headers.
* Add **unit tests** for modular components.

---
