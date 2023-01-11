import os
import openai
from django.conf import settings

openai.api_key = settings.OPEN_API_KEY

def open_ai_completion(text="resignation letter"):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response