import os

from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from aiModel import embedding_model


def make_rag_file(file_path, chatroom_id):
    # 저장소
    cache_dir_path = f".cache/{chatroom_id}"
    os.makedirs(cache_dir_path, exist_ok=True)
    cache_dir = LocalFileStore(cache_dir_path)

    # 문서 로드, 쪼개기
    file_path = f"/home/ubuntu/files/{file_path}"
    loader = UnstructuredFileLoader(file_path)
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
    )
    docs = loader.load_and_split(text_splitter=splitter)

    # 임베딩 
    embeddings = embedding_model
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)

    # Chroma  
    vectorstore = Chroma.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()

    return retriever
