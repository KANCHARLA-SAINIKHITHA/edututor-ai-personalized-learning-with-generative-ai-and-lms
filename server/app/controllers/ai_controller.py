import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_content(data):
    topic = data.get("topic", "math")
    level = data.get("level", "beginner")
    prompt = f"Generate a {level}-level quiz on {topic}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"content": response.choices[0].message['content']}
    except Exception as e:
        return {"error": str(e)}
