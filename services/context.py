from langchain.memory import ConversationSummaryBufferMemory
import llm

memory_store = {}

def get_user_memory(user_id):

    if user_id not in memory_store:
        memory_store[user_id] = ConversationSummaryBufferMemory(llm.AI_model)
    return memory_store[user_id]


