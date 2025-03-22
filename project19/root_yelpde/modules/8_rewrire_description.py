# import openai
from openai import OpenAI
from load_django import *
from parser_app.models import *

# Set your OpenAI API key

client = OpenAI(
    api_key="",
)
def rewrite_text(text, tone="neutral"):
    """
    Rewrite the input text using OpenAI's ChatGPT.

    Args:
        text (str): The text to be rewritten.
        tone (str): The desired tone for the rewritten text (e.g., "formal", "casual", "professional").

    Returns:
        str: The rewritten text.
    """
    try:
        # Make the API request
        # response = openai.ChatCompletion.create(
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can also use gpt-4 if available
            # model="gpt-4",
            messages=[
                # {"role": "system", "content": f"Sie sind ein hilfreicher Assistent, der Texte so umschreibt, dass sie einen {tone} Tonhaben."},
                {"role": "user", "content": f"Schreiben Sie den Text, den ich Ihnen gebe, in maximal 500 Zeichen um. {text}"}
            ]
        )

        # Extract and return the rewritten text
        # rewritten_text = response["choices"][0]["message"]["content"]
        rewritten_text = response.choices[0].message.content.strip()
        return rewritten_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
items = Business.objects.filter(status='FullDescription').order_by('id')
for item in items:
    if not item.description:
        continue
    description = item.description
    rewritten = rewrite_text(description, tone="formal")
    if rewritten:
        item.rewritten_description = rewritten
        item.status = 'DoneRewriteDescription'
        item.save()
        print(item, 'Done')   
