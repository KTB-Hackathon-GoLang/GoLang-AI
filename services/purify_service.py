from langchain_core.output_parsers import StrOutputParser
import os
import sys
sys.path.append(os.path.abspath('LLM/'))
sys.path.append(os.path.abspath('prompt/'))
import llm, putify_prompt



def purify(user,target,message):
    formatted_messages = putify_prompt.make_putify_prompt(user,target,message)
    
    response = llm.AI_model.invoke(formatted_messages)

    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    return parsed_output.content