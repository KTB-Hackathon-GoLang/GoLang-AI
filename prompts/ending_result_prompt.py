def make_chat_title_prompt(relation, explain_situation):
    prompt = f"""
    아래는 두 사람 사이의 대화입니다. 두 사람의 관계는 "{relation}"이고, 상황은 "{explain_situation}"입니다.
    이 대화를 적절히 설명하는 짧은 제목을 만들어 주세요.
    제목 형식은 < '관계' 사이 '상황'에서의 대화 > 입니다.
    
    대화 제목:
    """
    
    return prompt

def make_chat_summary_prompt(relation, explain_situation, whole_message):
    message_log = ""
    for message in whole_message:
        message_log += f"{message['username']}: {message['message']}\n"
    
    # 프롬프트 구성
    prompt = f"""
    아래는 두 사람의 대화입니다. 두 사람의 관계는 "{relation}"이고, 상황은 "{explain_situation}"입니다.
    대화를 100자 내외로 간결하게 요약해 주세요.
    
    대화 내용:
    {message_log}

    대화 요약:
    """
    
    return prompt
