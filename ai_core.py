import openai

openai.api_key = "your_openai_api_key"

def generate_code_from_prompt(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a code generator for dApps."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"generated_code": response['choices'][0]['message']['content']}
