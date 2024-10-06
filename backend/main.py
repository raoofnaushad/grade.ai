from openai import OpenAI

from src import config as C


client = OpenAI()

completion = client.chat.completions.create(
    model=C.LLM_MODEL,
    messages=[
        {
            "role": "system", 
            "content": "Consider yourself as a 20-year experienced Muslim marriage broker who is very good in digital platforms to find the perfect match for the perfect woman in the world."},
        {
            "role": "user",
            "content": "My name is Rehana Rasooluddin. My father's name is Rasooluddin. I have a sister called Ammuz. I have a brother called Mohammed. My mother's name is Serina Rasat. I am really beautiful. I am cute. I am the best woman who is ready to get married. I am looking... I never had a boyfriend other than a boyfriend who used to... who took my book which was given to him by my brother itself. And he was kind of a psycho. He was very serious about it. Other than that, I am always nice and better. I know how to dress well. I know how to act to people. I know cooking. I know everything. And I am awesome. Can you please create a marriage bio for me which looks really cool? Thank you."
        }
    ]
)
# print(response)
response=str(completion.choices[0].message.content)
print(response)

