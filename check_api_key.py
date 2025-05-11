from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("XAI_API_KEY")
print(api_key)  # 取得したキーが表示されるはず