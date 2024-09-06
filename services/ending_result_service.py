from langchain_core.output_parsers import StrOutputParser
from aiModel import llm
from prompts import ending_result_prompt

# DB [{username: 'A', message: '안녕}, {'username: 'B', message: 반가워 }] whole_message가 생긴 모양 
def ending_result_chat_title(relation, explain_situation): 
    formatted_messages = ending_result_prompt.make_chat_title_prompt(relation, explain_situation)
    
    response = llm.AI_model.invoke(formatted_messages)
        
    parser = StrOutputParser()
    parsed_output = parser.parse(response)
    
    return parsed_output.content
    

def ending_result_chat_summary(relation, explain_situation, whole_message): 
    formatted_messages = ending_result_prompt.make_chat_summary_prompt(relation, explain_situation, whole_message)
    
    response = llm.AI_model.invoke(formatted_messages)
        
    parser = StrOutputParser()
    parsed_output = parser.parse(response)
    
    return parsed_output.content