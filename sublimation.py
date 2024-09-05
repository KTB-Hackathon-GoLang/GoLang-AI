from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import secret

import os
import sys
sys.path.append(os.path.abspath('prompt/'))
import prompt

# LLM 
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.1, 
    openai_api_key = secret.openai_api_key
)


USER="팀장"
TARGET="팀원"
USER_INPUT="미안하다. 너희들을 과대평가해서 미안하다. 너희들로도 이 간단한 프로젝트 정도는 진행할 수 있을 줄 알았다."

# 메시지 포맷팅
formatted_messages = prompt.chat_prompt.format(user=USER, target=TARGET, user_input=USER_INPUT)

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
