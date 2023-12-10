from claude_api import Client
from mongoQuery import get_result
import openai
import streamlit as st


openai.api_key = st.secrets["OPENAI_API_KEY"]


def get_llm_result(query):
    print("Start get llm result")
    
    res = get_result(query)
    user_query = query
    context1 = res[0]['Context']
    fileName1 = res[0]['Filename'].split('/')[-1]
    context2 = res[1]['Context']
    fileName2 = res[1]['Filename'].split('/')[-1]

    summary_prompt = [
        {"role": "system", "content": "You are a helpful doctor from MIT giving a helpful recommendation to your patient so that he can pick the best insurance."},
        {"role": "user", "content": f"The patient has the following question: {user_query}. Answer the question detailing a summary of each policy. First set of Relevant policies: {context1} from Policy {fileName1}, second set of relevant policies: {context2} from Policy {fileName2}. Include the policy name on each response. Finally, respond in a paragraph recommending your patient what to pick and consider. The response should be clean, cohesive, conscise and empathic."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=summary_prompt
    )
    
    response_res = response['choices'][0]['message']['content']
    print("LLM response OK")
    #print(f'LLM response:{response_res}')
    return response_res