from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,  HumanMessagePromptTemplate

purify_system_message = '''### 지시 ### 
역할과 상황에 몰입하여 대답하여라. 필요하다면 질문도 가능하다.
'''

def make_ai_chating_prompt(relation,  explain_situation,user_input, history, related_documents) :
    if related_documents != "none":
        related_documents = "\n".join([doc.page_content for doc in related_documents])

    putify_prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template("다음은 '{RELATION}' 간의 대화이며 '{EXPLAIN_SITUATION}'인 상황에 처해 있다. 당신과 상대는 직전에 '{HISTORY}'라는 대화를 나누었다. 이와 관련된 자료 내용으로는 '{RELATED_DOCUMENTS}'가 있다. 자료 내용을 참고하여 다음 주어지는 문장에 대한 답변을 보내라." + purify_system_message),
            HumanMessagePromptTemplate.from_template("{USER_INPUT}"),
        ]
    ).format(RELATION=relation, EXPLAIN_SITUATION= explain_situation, USER_INPUT=user_input, HISTORY=history,RELATED_DOCUMENTS =related_documents)
    return putify_prompt
