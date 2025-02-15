# RAG_Chatbot

## Project Setup
1. **Clone this repository**
```bash
git clone https://github.com/pdobariya1/RAG_Chatbot.git
```

2. **Change directory**
```bash
cd RAG_Chatbot
```

3. **Create virtual environment**
```bash
conda create -p {env_name} python=3.10.16 -y
```

4. **Activate Environment**
```bash
conda activate ./{env_name}
```

5. **Install dependencies**
```bash
pip install -r requirements.txt --use-pep517
```

6. **Run the Streamlit App**
```bash
streamlit run app.py
```


## Environment Variables

Set up a .env file in root directory with the following:
```bash
MYSQL_HOST=your_host
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_database_name
GOOGLE_GEMINI_API=your_gemini_api
HUGGINGFACE_API=your_huggingface_Api
```

## Testing the API
1. "/chat" Route Endpoint
```bash
import requests
url = "http://127.0.0.1:5000/chat"
data = {"query": "What are the treatment methods for managing laminitis in animals?"}
response = requests.post(url, json=data)
print(response.json())
```

2. "/history" Route Endpoint
```bash
import requests
url = "http://127.0.0.1:5000/history"
response = requests.get(url)
print(response.json())
```