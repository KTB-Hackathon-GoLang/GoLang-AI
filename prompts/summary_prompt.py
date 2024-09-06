from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,  HumanMessagePromptTemplate

summary_system_message = '''### 지시 ###
주어지는 문장은 두서없이 작성한 문장이다. 내용을 요약하고 정리하라. 단, 원본 문장의 말투는 변경하지 마시오.
총 2가지 다른 방식으로 요약하라.
정리할 내용이 아무것도 없다면 그대로 출력해도 된다.

### 출력 형식 ###
json 형식으로 출력하되 아래 형식으로 출력하라.
{{
    "summary": [
        // 요약한 메시지 2개, 이는 겹치면 안 된다.
    ]
}}'''

def make_summary_prompt(relation, user_input, history) :
    summary_prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template("다음은 '{RELATION}' 간의 대화이며 그들은 이전에 '{HISTORY}'라는 대화를 나누었다." + summary_system_message),
            HumanMessagePromptTemplate.from_template("{USER_INPUT}"),
        ]
    ).format(RELATION=relation, USER_INPUT=user_input, HISTORY= history)
    return summary_prompt