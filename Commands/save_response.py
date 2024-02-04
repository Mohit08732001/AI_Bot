import os
from openai import OpenAI
from config import apikey

client = OpenAI(api_key=apikey)


def ai(content):
    text = f"OpenAI response for prompt: {content} \n ****************************\n\n"

    response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                  {
                    "role": "user",
                    "content": content
                  }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
              )
    print(response.choices[0].message.content)
    text += response.choices[0].message.content

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    file_name = str(content).replace("artificial intelligence", "")
    with open(f"Openai/{file_name}.txt", "w") as f:
        f.write(text)
