from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,  HumanMessagePromptTemplate

summary_system_message = '''### 지시 ###
주어지는 문장은 두서없이 작성한 문장이다. 상대방이 정확하게 이해할 수 있도록 내용을 요약하고 정리하라. 단, 원본 문장의 말투는(주로 대화체) 변경하지 마시오.
총 2가지 다른 방식으로 요약하라.
정리할 내용이 아무것도 없다면 그대로 출력해도 된다.

### 출력 형식 ###
json 형식으로 출력하되 아래 형식으로 출력하라.
{{
    "messages": [
        // 요약한 메시지 2개, 이는 겹치면 안 된다.
    ]
}}'''

def make_summary_prompt(relation,  explain_situation,user_input, history, related_documents) :
    if related_documents != "none":
        related_documents = "\n".join([doc.page_content for doc in related_documents])

    summary_prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template("다음은 '{RELATION}' 간의 대화이며 '{EXPLAIN_SITUATION}'인 상황에 처해 있다. 그들은 직전에 '{HISTORY}'라는 대화를 나누었다. 이와 관련된 자료 내용으로는 '{RELATED_DOCUMENTS}'가 있다. 자료 내용을 참고하여 다음 주어지는 문장을 보완하여라." + summary_system_message),
            HumanMessagePromptTemplate.from_template("{USER_INPUT}"),
        ]
    ).format(RELATION=relation,  EXPLAIN_SITUATION= explain_situation,USER_INPUT=user_input, HISTORY= history, RELATED_DOCUMENTS= related_documents)
    return summary_prompt
