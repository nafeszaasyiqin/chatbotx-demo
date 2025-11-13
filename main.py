
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import re

app = FastAPI(title="Chatbotx")

app.mount("/static", StaticFiles(directory="static"),name="static")

@app.get("/")

def home():
    return FileResponse("templates/index.html")


#store memory for conversation
conversation_memori={}

class ChatRequest (BaseModel):
    user_id:str
    mesej:str

def planner (mesej,memory):
    mesej_lower=mesej.lower()

    if any(word in mesej_lower for word in ["calculate","+","-","*","/" ] ):
        return "calc"

    if "outlet" in mesej_lower:
        return "ask_outlet"

    if any(word in mesej_lower for word in ["operating","hours","open"] ):
        return "operating_hours"

    if any(word in mesej_lower for word in ["thank you","tq","thanks","okay","ok" ] ):
        return "closure"

    if any(word in mesej_lower for word in ["hi","hey","hello","hai"] ):
        return "greet"

    return "fallback"



@app.post("/chat")
def chat(request:ChatRequest):
    user_id= request.user_id
    mesej=request.mesej

    #initialize memory if 1st message
    if user_id not in conversation_memori:
        conversation_memori[user_id]={}

    memory = conversation_memori[user_id]

    #Decide action
    action = planner(mesej,memory)

    #Execute action
    if action == "calc":
        try:
            expression = re.findall(r"[\d\.\+\-\*\/\(\)\s]+", mesej)
            expression = "".join(expression).strip()

            result = eval(expression)
            return {"response":f"Calculation result:{result}"}
        except Exception:
            return {"response":"Invalid expression for calculation"}

    elif action == "ask_outlet":
        memory["asked_outlet"]=True
        return {"response":"Yes! Which outlet are you referring to?"}

    elif memory.get("asked_outlet"):
        memory["outlet"]=mesej
        memory.pop("asked_outlet")#resetting
        return {"response":f"Ah yes, the {mesej} outlet open at 9am" }

    elif action == "greet":
        return {"response":f"Hi! How i may help you?"}

    elif action == "closure":
        return {"response":f"You're welcome! Happy to help"}

    elif action == "operating_hours":
        return {"response":f"We are open from Monday to Saturday 10:00 a.m. to 10:00 p.m."}

    else:
        return {"response":f"Sorry, i didnt understand. Can you clarify?" }








