from langchain.memory import ConversationSummaryBufferMemory
from aiModel import llm

memory_store = {}

def get_user_memory(user_id):

    if user_id not in memory_store:
        memory_store[user_id] = ConversationSummaryBufferMemory(llm=llm.AI_model)
        return "nothing"
<<<<<<< HEAD

=======
>>>>>>> upstream/dev
    return memory_store[user_id]


def add_message(user_id,input,output):
    memory_store[user_id].save_context({"inputs": input}, {"outputs": output})
