# 1단계: 빌드 단계
FROM python:3.12-slim AS builder

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치 및 타임존 설정 (tzdata 포함)
RUN apt-get update && \
    apt-get install -y python3-pip tzdata libmagic-dev libmariadb-dev-compat libmariadb-dev && \
    apt-get clean

# 타임존 설정 (Asia/Seoul)
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 가상환경 설정
RUN python3 -m venv /app/golang

# 가상환경 활성화 및 필요한 패키지 설치
RUN /app/golang/bin/pip install --upgrade pip && \
    /app/golang/bin/pip install openai fastapi[standard] langchain langchain_openai \
    unstructured \
    langchain-community \
    langchain_chroma \
    langchain_unstructured \
    mariadb \
    pymongo

# 2단계: 실제 실행 환경
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 타임존 설정 (Asia/Seoul)
ENV TZ=Asia/Seoul
RUN apt-get update && \
    apt-get install -y tzdata libmagic-dev libmariadb-dev-compat libmariadb-dev && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get clean

# 빌드 단계에서 생성된 가상 환경 복사
COPY --from=builder /app/golang /app/golang

# 앱 파일 복사
COPY secret.py /app/
COPY main.py /app/
COPY models /app/models
COPY services /app/services
COPY aiModel /app/aiModel
COPY prompts /app/prompts
COPY repository /app/repository

# FastAPI 앱 실행
CMD ["/app/golang/bin/fastapi", "run"]