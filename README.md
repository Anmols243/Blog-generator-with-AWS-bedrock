### 📝 AI Blog Generator (AWS Bedrock + Lambda + Streamlit)

Generate high-quality blogs using Meta Llama (Amazon Bedrock) — powered by a fully-serverless backend and a simple Streamlit UI.

This project demonstrates how to combine Gen-AI + AWS serverless architecture to build a real, production-ready AI application.

---

### 🚀 Demo

- 👉 Live App: https://blog-generator-with-aws-bedrock.streamlit.app/  
- 👉 Backend: AWS Lambda + API Gateway  
- 👉 Model: Meta Llama (Amazon Bedrock)

---

### 🧠 Features

- ✔ Generate AI-written blogs  
- ✔ Serverless backend  
- ✔ Secure integration  
- ✔ Stored in S3  
- ✔ Streamlit UI  
- ✔ Deployed  

---

### 🏗 Architecture

```
Streamlit UI  →  API Gateway  →  AWS Lambda  →  Amazon Bedrock (Llama)
                             ↓
                           S3 (blog storage)
```

---

### 🛠 Tech Stack

- Cloud: AWS (Lambda, API Gateway, S3, Bedrock)  
- Backend: Python + boto3  
- Frontend: Streamlit  
- Model: Meta Llama (Bedrock)  

---

### 🔌 API Endpoint (Backend)

**POST /blog-generation**

#### Request

```json
{
  "blog_topic": "black holes"
}
```

#### Response

```json
{
  "message": "Blog generated successfully",
  "blog": "Your generated blog content here..."
}
```

---

### 🖥 Running Frontend Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

### 🔐 Configure API URL (Streamlit Secrets)

Create or edit:

`.streamlit/secrets.toml`

```toml
API_URL = "https://your-api-url.amazonaws.com/dev/blog-generation"
```

Streamlit automatically loads it — **clean & secure** 🎯

---

### ⚙ Lambda Handler Workflow

- 1️⃣ Receive topic via API Gateway  
- 2️⃣ Call Bedrock model via boto3  
- 3️⃣ Generate blog text  
- 4️⃣ Save result in S3  
- 5️⃣ Return response to UI  
