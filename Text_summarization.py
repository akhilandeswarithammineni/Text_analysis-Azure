from openai import AzureOpenAI
endpoint = "https://25695a3201-2301-resource.services.ai.azure.com/api/projects/25695a3201-2301"
api_key = "C46Hj82fsbco8MyWQvIBjr4jWRGiRONzslwAjNpUCfYcz0UimZ8nJQQJ99CKACE1PydXJ3w3AAAAACOGw0Bl"
deployment_name = "gpt-5-mini"
text="""On a rocky island far from the shore, an old lighthouse keeper named Arthur lived with his loyal dog, Barnaby. Every evening, Arthur climbed the winding stairs to light the giant lamp, guiding ships safely past the sharp cliffs.
One stormy night, the wind howled and the waves crashed violently against the tower. Suddenly, Arthur slipped on the wet stone steps and hurt his ankle, unable to reach the top.
Seeing his master in trouble, Barnaby barked loudly and raced up the spiral staircase alone. The clever dog nudged the heavy brass lever with his nose until the bright beam flared to life across the dark ocean.
A passing fishing boat saw the light just in time and steered clear of the dangerous rocks. From that night on, the sailors didn't just thank Arthur—they always brought a juicy bone for the brave little dog who saved them.."""


response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are text summarization  AI assistant  which gives summary for the content provided by user senetence by sentence "},
        {"role": "user", "content":  text}
        
    ],
)

print(response.choices[0].message.content)
