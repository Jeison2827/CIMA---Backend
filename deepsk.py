

from openai import OpenAI   

client = OpenAI(api_key="sk-c34fadaee63e4fbebad108e270f97cc4", base_url="https://api.deepseek.com")
API_KEY = "sk-c34fadaee63e4fbebad108e270f97cc4"
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "brindame algo novedoso podria usarte para que hagas analisis de archivos de excel con demaciados registros?"},
    ],
    stream=False
)

print(response.choices[0].message.content)