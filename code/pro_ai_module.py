import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_gemini_ending(progress, health, energy, first_ending_text):
    prompt = (
        f"這是一段遊戲結局：「{first_ending_text}、角色課業完成度 {progress}%，健康度 {health}%，精力度 {energy}%。」請幫我延伸後續發展，再寫出第二段結局收尾，大約 50~80 字。"
        "請保持與第一段相同的風格（如感性、幽默、崩潰等）中文故事性結局，內容可以是內心轉折、後來的狀況、或一個小總結，但重要的是要用台灣大學生的語氣與口吻。"
    )
    model = genai.GenerativeModel(model_name="gemini-1.5-flash") 
    response = model.generate_content(prompt)
    return response.text.strip()
