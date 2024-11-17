token = "8G0JP4D39348WYKF4G6VKALT7644LHCRMK58MTY350RKK9TDTQJVNSQF4CXEZQ4H"
from openai import OpenAI
client = OpenAI(api_key=token, base_url="https://jamsapi.hackclub.dev/openai")

response = client.chat.completions.create(
    messages=[{
        "role":"user",
        "content": "Create an english sentence with incorrect homophones. Minimize accuracy and show only final output.?"
    }],
    model="gpt-4o-mini",
)
print(response.choices[0].message.content)
userfixed=input("Enter your modified version of this phrase!")
response = client.chat.completions.create(
    messages=[{
        "role":"user",
        "content": "Say thank you. The correct answer is the user input."
    }],
    model="gpt-4o-mini",
)
print(response.choices[0].message.content)
