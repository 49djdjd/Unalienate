from flask import Flask
app = Flask(__name__)
@app.router("http://127.0.0.1:5500/l.html")

token = "8G0JP4D39348WYKF4G6VKALT7644LHCRMK58MTY350RKK9TDTQJVNSQF4CXEZQ4H"
from openai import OpenAI
client = OpenAI(api_key=token, base_url="https://jamsapi.hackclub.dev/openai")
#Functions
def InputResponse():
    response = client.chat.completions.create(
        messages=[{
            "role":"user",
            "content": "Create an english sentence with 5 incorrect homophones, do not name the errors, make it space theme"
        }],
        model="gpt-4o-mini"
    )
    print(response.choices[0].message.content)


def Response():
    response = client.chat.completions.create(
        messages=[{
            "role":"user",
            "content": "Say thank you and nothing else"
        }],
        model="gpt-4o-mini",
    )
    print(response.choices[0].message.content)

def NextResponse():
    response = client.chat.completions.create(
        messages=[{
            "role":"user",
            "content": "Create an english sentence with incorrect homophones however some of issues that were addressed in the user's past input. do not name the errors made by the human, if any."
        }],
        model="gpt-4o-mini",
    )
    print(response.choices[0].message.content)

def RepeatEverything():
    response = client.chat.completions.create(
    messages=[{
            "role":"user",
            "content": "Give us a new, not repeating phrase that is an english setnecne with incorrect homophones about space "
        }],
        model="gpt-4o-mini",
    )
    print(response.choices[0].message.content)


InputResponse()
for i in range(5):
    userinput=input("Fix this sentence!")
    Response()
    NextResponse()
    RepeatEverything()

