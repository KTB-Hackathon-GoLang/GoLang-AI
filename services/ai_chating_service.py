from langchain_core.output_parsers import StrOutputParser

from aiModel import llm
from prompts import ai_chat_prompt
from services import context
from services import rag_service


def ai_chating(user_id, chating_room_id, relation, explain_situation, message, file_path=None): 
    history = context.get_user_memory(user_id)
    
    if file_path:
        file_path = f"/home/ubuntu/files/{file_path}"
        retriever = rag_service.make_rag_file(file_path,chating_room_id)
        related_documents = retriever.get_relevant_documents(message)
    else:
        related_documents = "none"

    formatted_messages = ai_chat_prompt.make_ai_chating_prompt(relation,  explain_situation,message, history, related_documents)
    response = llm.AI_model.invoke(formatted_messages)
        
    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    context.add_message(user_id, message, parsed_output.content)
    
    return parsed_output.content
