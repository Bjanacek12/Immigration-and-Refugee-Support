#pull data from speech to text to analyze the data and save to text file
from TextSpeech import Text_Speech
from openai import OpenAI


def analyze():
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    )

    print(completion.choices[0].message)

