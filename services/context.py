from langchain.memory import ConversationSummaryBufferMemory

from aiModel import llm

memory_store = {}

def get_user_memory(username):
    if username not in memory_store:
        memory_store[username] = ConversationSummaryBufferMemory(llm=llm.AI_model)
        return "nothing"
    return memory_store[username]

def add_message(username, chat_message, output):
    memory_store[username].save_context({"inputs": chat_message}, {"outputs": output})
