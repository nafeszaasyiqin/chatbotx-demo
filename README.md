
# Chatbotx

Chatbotx is a rule-based chatbot built with FastAPI that recognizes basic user intents such as greetings, operating hours, outlet inquiries, and simple calculations. It also maintains short-term conversation memory for contextual replies.

## Setup & Run Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/nafeszaasyiqin/chatbotx-demo.git
   cd chatbotx-demo

2. Create a virtual environment and install dependencies:
 ```bash
   python -m venv venv
   source venv/bin/activate  # (Windows: venv\Scripts\activate)
   pip install -r requirements.txt

3. Run the app locally:
  ```bash
   uvicorn main:app --reload

