from langchain.storage import LocalFileStore 
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings import CacheBackedEmbeddings
from aiModel import embedding_model
import os

def make_rag_file(file_path, chating_room_id):
    # 캐시 디렉토리 설정 및 생성
    cache_dir_path = f"../.cache/{chating_room_id}"
    os.makedirs(cache_dir_path, exist_ok=True)
    
    # 캐시 디렉토리 초기화
    cache_dir = LocalFileStore(cache_dir_path)

    # 문서 로드하고 쪼개기
    loader = UnstructuredFileLoader(file_path)
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    docs = loader.load_and_split(text_splitter=splitter)

    # 임베딩 저장 (캐시에 임베딩 저장만 수행)
    embeddings = embedding_model
    CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)