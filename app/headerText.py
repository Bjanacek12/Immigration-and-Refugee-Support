from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def header(text):
    try:
        # First, detect the language of the input text
        language_detection = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a language detection assistant. Respond only with the language name of the text and nothing else."},
                {"role": "user", "content": text}
            ]
        )
        detected_language = language_detection.choices[0].message.content.strip()

        # Then, generate a short header title for the context
        title_generation = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Give me a short header title for this context: {text}"}
            ]
        )
        header_title = title_generation.choices[0].message.content.strip()

        return {
            "title": header_title,
            "language": detected_language
        }

    except Exception as e:
        print(f"Error in header: {str(e)}")
        raise