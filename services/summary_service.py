from langchain_core.output_parsers import StrOutputParser
import os
import sys
sys.path.append(os.path.abspath('LLM/'))
sys.path.append(os.path.abspath('prompt/'))
import llm, summary_prompt


def summary(user,target,message):
    formatted_messages = summary_prompt.make_summary_prompt(user,target,message)
    
    response = llm.AI_model.invoke(formatted_messages)

    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    return parsed_output.content