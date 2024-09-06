from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,  HumanMessagePromptTemplate

SUMMARY_PROMPT = '''### 지시 ###
주어지는 문장은 두서없이 작성한 문장이다. 내용을 요약하고 정리하라. 단, 원본 문장의 말투는 변경하지 마시오.
총 2가지 다른 방식으로 요약하라.

### 출력 형식 ###
json 형식으로 출력하되 아래 형식으로 출력하라.
{{
    "summary": [
        // 요약한 메시지 2개, 이는 겹치면 안 된다.
    ]
}}'''

def make_summary_prompt(user,target,user_input) :
    summary_prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template("다음은 {USER}가 {TARGET}에게 보내는 대화 내용이다." + SUMMARY_PROMPT),
            HumanMessagePromptTemplate.from_template("{USER_INPUT}"),
        ]
    ).format(USER=user, TARGET=target, USER_INPUT=user_input)
    return summary_prompt