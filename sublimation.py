from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,  HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import secret

# 프롬프트
chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("{user}가 {target}에게 보내는 대화 내용을 순화하여 표현해 보세요. 욕설이 있으면 제외하고 격한 표현이 있으면 돌려 표현하세요. 단, 담고 있는 의미는 누락되어서는 안 됩니다."),
        HumanMessagePromptTemplate.from_template("{user_input}"),
    ]
)

# LLM 
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.1, 
    openai_api_key = secret.openai_api_key
)

USER="아버지"
TARGET="아들"
USER_INPUT="너를 자식이라고 낳은 게 한심하다. 수능 8등급이 뭐냐!!? 학원비 1000억 들여 가며 공부시켰으면 이 이상은 해내야 사람이라고 할 수 있을 것 아니냐!! 한번만 더 이런 점수를 점수라고 받아온다면 그날부로 호적에서 파버릴 줄 알아라!!"

# 메시지 포맷팅
formatted_messages = chat_prompt.format(user=USER, target=TARGET, user_input=USER_INPUT)

example_list = []
for example in range(3):
  # LLM 메시지 전달
  response = llm.invoke(formatted_messages)
  # 문자열로 변환
  parser = StrOutputParser()
  parsed_output = parser.parse(response)
  example_list.append(parsed_output.content)

print(USER_INPUT)
for example in range(3):
  print( f"{example+1}번째 순화 후보 : \n {example_list[example]}")
