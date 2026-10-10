import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

res = model.invoke("Hi, I am Rehan, How are you dear?")
print(res.content[0]["text"])

