from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
print("Client ID:", client_id)
print("Client Secret:", client_secret)