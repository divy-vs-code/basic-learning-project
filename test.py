import ollama as ol

while True:
    n = input("Enter a message : ")

    response = ol.chat(
        model="gpt-oss:120b-cloud",
        messages=[{'role': 'user', 'content': n}],
        stream=True,
        options={"temperature": 0.3, "max_tokens": 50}
    )

    for chunk in response:
        print(chunk["message"]["content"], end="", flush=True)