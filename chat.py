import openai


#Open AI Key
openai.api_key = "" #Enter yours here, you will need to sign up for an Open.ai account to get one
model_engine = "text-davinci-003"


def chatGPT(prompt):

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=5,
        stop=None,
        temperature=0.9,
    )

    return completion.choices[0].text