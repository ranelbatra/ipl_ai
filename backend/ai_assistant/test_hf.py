from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="hf-inference",      # or remove this line if you weren't using it
    api_key=os.getenv("HF_TOKEN")
)

response = client.chat_completion(
    model="Qwen/Qwen2.5-7B-Instruct",   # your model
    messages=[
        {
            "role": "user",
            "content": "Who is Virat Kohli?"
        }
    ],
    max_tokens=200
)

print(response.choices[0].message.content)