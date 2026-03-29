import ollama as ol 

text_recognize = input
response = ol.chat(
        model='gpt-oss:120b-cloud',
        messages=[{'role': 'user', 'content': 'What is water?'}],
    )
response_text = response.message.content
print(response_text)

