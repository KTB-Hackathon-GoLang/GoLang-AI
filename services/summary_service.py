from langchain_core.output_parsers import StrOutputParser
from aiModel import llm
from prompts import summary_prompt
from services import context,rag_service

def summary(user_id, chating_room_id, relation,  explain_situation,message,file_path=None): 
    history = context.get_user_memory(user_id)
    
    if file_path:
        retriever = rag_service.make_rag_file(file_path,chating_room_id)
        # 메시지와 관련된 문서 검색
        related_documents = retriever.get_relevant_documents(message)
    else:
        related_documents = "none"

    # 메시지와 관련된 프롬프트 생성
    formatted_messages = summary_prompt.make_summary_prompt(relation,  explain_situation,message, history, related_documents)

    # AI 모델 응답 생성
    response = llm.AI_model.invoke(formatted_messages)

    # 응답 파싱
    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    # 히스토리 업데이트
    context.add_message(user_id, message, parsed_output.content)

    return parsed_output.content