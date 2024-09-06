from langchain_core.output_parsers import StrOutputParser
from LLM import llm
from prompts import purify_prompt
from services import context


def purify(user_id, relation, message):
    history = context.get_user_memory(user_id)
    formatted_messages = purify_prompt.make_purify_prompt(relation, message, history)
    
    response = llm.AI_model.invoke(formatted_messages)

    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    return parsed_output.content