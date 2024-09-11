from langchain_core.output_parsers import StrOutputParser

from aiModel import llm
from prompts import purify_prompt
from services import context, rag_service


def purify(username, chatroom_id, relation, explain_situation, chat_message, file_path=None):
    history = context.get_user_memory(username)
    
    if file_path:
        # file_path = f"/home/ubuntu/files/{file_path}"
        retriever = rag_service.make_rag_file(file_path, chatroom_id)
        # 메시지와 관련된 문서 검색
        related_documents = retriever.get_relevant_documents(chat_message)
    else:
        related_documents = "none"

    formatted_messages = purify_prompt.make_purify_prompt(relation, explain_situation, chat_message, history, related_documents)
    response = llm.AI_model.invoke(formatted_messages)
        
    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    context.add_message(username, chat_message, parsed_output.content)
    
    return parsed_output.content
