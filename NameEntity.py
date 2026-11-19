response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are name entity AI assistant which does only entity extraction from the user content separated by commas"},
        {"role": "user", "content": "My name is akhila and i love India"}
        
    ],
)

print(response.choices[0].message.content)