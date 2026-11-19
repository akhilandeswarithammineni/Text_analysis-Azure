response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are Sentiment analysis  AI assistant which does which does sentiment analysis from the user content "},
        {"role": "user", "content": "i am very happy"}
        
    ],
)

print(response.choices[0].message.content)