from openai import AzureOpenAI
endpoint = "https://25695a3201-2301-resource.services.ai.azure.com/api/projects/25695a3201-2301"
api_key = "C46Hj82fsbco8MyWQvIBjr4jWRGiRONzslwAjNpUCfYcz0UimZ8nJQQJ99CKACE1PydXJ3w3AAAAACOGw0Bl"
deployment_name = "gpt-5-mini"
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are name entity AI assistant which does only entity extraction from the user content separated by commas"},
        {"role": "user", "content": "My name is akhila and i love India"}
        
    ],
)

print(response.choices[0].message.content)
