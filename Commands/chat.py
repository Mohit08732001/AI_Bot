from Commands.speaker import speak
from openai import OpenAI
from config import apikey

client = OpenAI(api_key=apikey)
chatStr = ""


def chat(query):
    global chatStr
    chatStr += f"User: {query}\n Siri: "
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speak(response.choices[0].message.content)
    chatStr += f"{response.choices[0].message.content}\n"
    return response.choices[0].message.content
