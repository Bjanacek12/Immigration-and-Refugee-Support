#pull data from speech to text to analyze the data and save to text file
from TextSpeech import Text_Speech
from openai import OpenAI


def analyze(SpeechText):
    client = OpenAI()
    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Use "system" role for assistant behavior
                {"role": "user", "content": SpeechText}  # Use "user" role for the input
            ]
        )

    print(completion.choices[0].message.content)
    Text_Speech(completion.choices[0].message.content)

