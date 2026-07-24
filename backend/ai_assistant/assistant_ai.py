import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


MODEL_NAME = os.environ.get(
    "HF_MODEL",
    "Qwen/Qwen2.5-7B-Instruct"
)


HF_TOKEN = (
    os.environ.get("HF_TOKEN")
    or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
)


client = InferenceClient(
    model=MODEL_NAME,
    token=HF_TOKEN
)



SYSTEM_PROMPT = """

You are an expert IPL cricket analyst.

Rules:
- Explain only the provided statistics.
- Do not invent numbers.
- Do not perform incorrect comparisons.
- Keep answers concise and insightful.
- Mention that data is based on IPL statistics.

"""



def generate_answer(question, data):

    user_prompt = f"""
User Question:
{question}

Available IPL Analysis:
{data}

Explain this analysis in a cricket expert style.
"""

    print("=" * 80)
    print(user_prompt)
    print("=" * 80)

    response = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        max_tokens=500,
        temperature=0.3
    )

    return response.choices[0].message.content