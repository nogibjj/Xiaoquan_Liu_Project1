import openai

#write a function that uses open ar to generate a question and answer 
def generate_question_answer(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Q:", " A:"]
    )
    return response