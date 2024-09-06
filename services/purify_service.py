from openai import OpenAI

client = OpenAI()

def purify(prompt, message):
    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'system', 'content': prompt
            }, {
                'role': 'user', 'content': message
            }
        ]
    )

    return completion.choices[0].message.content