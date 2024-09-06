from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,  HumanMessagePromptTemplate

purify_system_message = '''### 지시 ### 
주어지는 문장을 순화하라. 욕설이 있으면 제외하라. 격한 표현이 있으면 돌려 표현하라. 조롱조가 있으면 표현을 긍정적으로 바꿔 표현하라. 단, 담고 있는 의미는 누락되어서는 안 된다. 
순화할 표현이 아무것도 없다면 그대로 출력해도 된다.
### 실행 순서 ###
1. 비속어를 순화한 문장을 3가지 만들어라.
이때 먼저 상대방의 감정에 공감, 나의 감정 전달, 나의 의도를 전달하면서 순화하면 좋다. 
2. 1차로 순화한 문장을 한 번 더 순화하라. 

### 출력 형식 ###
json 형식으로 출력하되 아래 형식으로 출력하라.
{{
    "messages_1": [
        // 1차적으로 순화한 메시지 3개, 모두 겹치면 안 된다.
    ],
    "messages_2": [
        // 2차적으로 순화한 메시지 3개, 모두 겹치면 안 된다.
    ]
}}'''

def make_purify_prompt(relation,  explain_situation,user_input, history, related_documents) :
    if related_documents != "none":
        related_documents = "\n".join([doc.page_content for doc in related_documents])

    putify_prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template("다음은 '{RELATION}' 간의 대화이며 '{EXPLAIN_SITUATION}'인 상황에 처해 있다. 그들은 직전에 '{HISTORY}'라는 대화를 나누었다. 이와 관련된 자료 내용으로는 '{RELATED_DOCUMENTS}'가 있다. 자료 내용을 참고하여 다음 주어지는 문장을 보완하여라." + purify_system_message),
            HumanMessagePromptTemplate.from_template("{USER_INPUT}"),
        ]
    ).format(RELATION=relation, EXPLAIN_SITUATION= explain_situation, USER_INPUT=user_input, HISTORY=history,RELATED_DOCUMENTS =related_documents)
    return putify_prompt