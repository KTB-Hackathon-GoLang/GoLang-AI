from langchain_core.output_parsers import StrOutputParser
from aiModel import llm
from prompts import summary_prompt
from services import context

def summary(user_id, relation, message):
    history = context.get_user_memory(user_id)
    formatted_messages = summary_prompt.make_summary_prompt(relation, message, history)
    
    response = llm.AI_model.invoke(formatted_messages)

    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    return parsed_output.content