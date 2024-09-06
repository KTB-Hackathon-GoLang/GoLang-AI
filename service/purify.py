from openai import OpenAI

client = OpenAI()
with open('prompts/purify_prompt', 'r') as file:
    prompt = file.read()

def purify(message):
    completion = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {
                'role': 'system', 'content': prompt
            }, {
                'role': 'user', 'content': message
            }
        ]
    )

    return completion.choices[0].message.content