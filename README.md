# GoLang-AI
고랭 AI 레포지토리입니다 🐳

## 사용 기술 스택
- Python
- FastAPI
- OpenAI API
  - gpt-4o-mini
  - `Temperature: 0.75, Max Token: 1024`
- LangChain
- Naver Cloud API

## Endpoint 별 기능
1. 언어 순화: `POST /ai/purify`
   - 주어진 문장을 순화한 표현 3가지를 반환

2. 내용 요약: `POST /ai/summarize`
   - 주어진 문장을 요약한 표현 2가지를 반환

3. 가상 인물과의 대화: `POST /ai/chat`
   - 인공지능이 실제 상대 역할을 하여 대화 주도

4. 채팅 종료: `POST /ai/end-chat`
   - 채팅방 내용을 요약하여 DB에 저장
   - 주어진 채팅방에 참여한 사람의 감정 상태를 긍정/중립/부정 로 DB에 저장

- Request Body
   - ```json
     {
       "username": "Userc8657928",
       "relation": "친구",
       "chatroom_uuid": "a045fd27-1ba7-46e2-99ad-9e7088990034",
       "chat_message": "메시지 내용",
       "chat_type": "CHAT_FILTER"
     }
     ```

- Response Body
    - ```json
      {
        "success": true,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": {} // 응답 데이터
      }
      ```