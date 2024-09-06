import os
from langchain_core.output_parsers import StrOutputParser
from aiModel import llm
from prompts import purify_prompt
from services import context
from langchain.vectorstores import Chroma
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from aiModel import embedding_model

def purify(user_id, chat_room_id, relation, message): 
    history = context.get_user_memory(user_id)
    
    cache_dir_path = f"../.cache/{chat_room_id}"
    
    # 캐시 경로가 있으면 retriever 로드
    if os.path.exists(cache_dir_path):
        cache_dir = LocalFileStore(cache_dir_path)
        cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embedding_model, cache_dir)
        vectorstore = Chroma(persist_directory=cache_dir_path, embedding_function=cached_embeddings)
        retriever = vectorstore.as_retriever()
        
        # 메시지와 관련된 문서 검색
        related_documents = retriever.get_relevant_documents(message)
    else:
        related_documents = "none"

    # 메시지와 관련된 프롬프트 생성
    formatted_messages = purify_prompt.make_purify_prompt(relation, message, history, related_documents)

    # AI 모델 응답 생성
    response = llm.AI_model.invoke(formatted_messages)

    # 응답 파싱
    parser = StrOutputParser()
    parsed_output = parser.parse(response)

    # 히스토리 업데이트
    context.add_message(user_id, message, parsed_output.content)

    return parsed_output.content
