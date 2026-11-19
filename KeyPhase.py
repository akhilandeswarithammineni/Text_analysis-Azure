from openai import AzureOpenAI
endpoint = "https://25695a3201-2301-resource.services.ai.azure.com/api/projects/25695a3201-2301"
api_key = "C46Hj82fsbco8MyWQvIBjr4jWRGiRONzslwAjNpUCfYcz0UimZ8nJQQJ99CKACE1PydXJ3w3AAAAACOGw0Bl"
deployment_name = "gpt-5-mini"
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are AI assistant which does only key phrase extraction from the user content separated by commas"},
        {"role": "user", "content": "India is a beautiful country filled with nature and good culture"}
        
    ],
)

print(response.choices[0].message.content)
