from langchain_core.output_parsers import StrOutputParser
from LLM import llm
from prompt import summary_prompt
import context

def summary(user_id, user, target, message):
    history = context.get_user_memory(user_id)
    formatted_messages = summary_prompt.make_summary_prompt(user,target,message, history)
    
    response = llm.AI_model.invoke(formatted_messages)

    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    return parsed_output.content