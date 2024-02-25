# app/routes.py
from fastapi import Query, Depends
from starlette.requests import Request
import redis
import ast
from app import PROMPT, app, llm
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def get_client_ip(request: Request):
    return request.client.host

r = redis.Redis(
    host='redis',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

Memory = ConversationBufferMemory(ai_prefix="InteraktBot", human_prefix="client")

conversation = ConversationChain(
    prompt=PROMPT,
    llm=llm,
    verbose=False
)

@app.get("/predict/", name="predict_endpoint")
async def predict(input_text: str = Query(..., title="Input Text"), client_ip: str = Depends(get_client_ip)):
    Memory.clear()
    conversation_data = r.get(client_ip)
    if conversation_data:
        mydict = ast.literal_eval(conversation_data)

        history = mydict.get('history', '')
        messages = history.split('\n')

        for message in messages:
            if message.startswith('client:'):
                Memory.chat_memory.add_user_message(message[len('client:'):].strip())
            elif message.startswith('InteraktBot:'):
                Memory.chat_memory.add_ai_message(message[len('InteraktBot:'):].strip())
    else :
        Memory.chat_memory.add_ai_message("Bienvenue ! Je suis Interakt Bot. Comment puis-je vous aider ? Puis-je connaître votre nom ? 😊")
                
    conversation.memory=Memory
    result = conversation.predict(input=input_text)

    string_representation = str(Memory.load_memory_variables({}))
    
    r.set(client_ip, string_representation)

    return {"result": result}