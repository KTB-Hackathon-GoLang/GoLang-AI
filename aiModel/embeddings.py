from langchain.embeddings import OpenAIEmbeddings
import secret

embedding_model = OpenAIEmbeddings(openai_api_key = secret.openai_api_key)