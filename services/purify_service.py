from langchain_core.output_parsers import StrOutputParser
import llm, putify_prompt,context



def purify(user_id, user, target, message):
    history = context.get_user_memory(user_id)
    formatted_messages = putify_prompt.make_putify_prompt(user,target,message, history)
    
    response = llm.AI_model.invoke(formatted_messages)

    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    return parsed_output.content