from openai import OpenAI
from src import config as C
from src import prompt as P 
import json

def get_from_llm(userMessage):
    try:
        client = OpenAI()
        completion = client.chat.completions.create(
            model=C.LLM_MODEL,
            response_format={'type': 'json_object'},
            messages=[
                {
                    "role": "system", 
                    "content": P.GRADER_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": userMessage
                }
            ]
        )
        # Extract and clean the response
        response_content = completion.choices[0].message.content
        response_content = '\n'.join(line for line in response_content.split('\n') if not line.strip().startswith('```'))
        
        # Attempt to load the cleaned response as JSON
        try:
            response_json = json.loads(response_content)
            return response_json
        except json.JSONDecodeError:
            print(f"Failed to decode JSON from response: {response_content}")
            return {"current_score": 0, "reason": "Failed to decode JSON"}
    except Exception as e:
        print(f"An error occurred in get_from_llm: {e}")
        return {"current_score": 0, "reason": f"An error occurred: {e}"}