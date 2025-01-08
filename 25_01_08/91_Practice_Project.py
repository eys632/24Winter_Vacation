import os
import mimetypes
import openai

# 1. 파일 형식 판별 함수
def detect_file_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type

# 2. 로더 선택 함수
def select_loader(file_type):
    if 'pdf' in file_type:
        return ["PDFLoader1", "PDFLoader2", "PDFLoader3"]
    elif 'text' in file_type:
        return ["txtLoader"]
    elif 'json' in file_type:
        return ["JsonLoader"]
    # 추가 파일 형식 로더
    else:
        return []

# 3. 스플리터 정의
def get_splitters():
    return [
        "CharacterTextSplitter",
        "TokenTextSplitter",
        "RecursiveCharacterTextSplitter"
        # 다른 스플리터 추가
    ]

# 4. OpenAI API 활용 함수
def evaluate_splits(api_key, loader, splitter, data):
    openai.api_key = api_key
    prompt = f"Loader: {loader}\nSplitter: {splitter}\nData: {data}"
    response = openai.Completion.create(
        engine="gpt-4",  # GPT-4 mini 사용
        prompt=prompt,
        max_tokens=100
    )
    return response

# 5. 메인 함수
def main():
    file_path = input("파일 경로를 입력하세요: ")
    file_type = detect_file_type(file_path)
    loaders = select_loader(file_type)
    splitters = get_splitters()

    # 환경 변수에서 OpenAI API 키 불러오기
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: 환경 변수 OPENAI_API_KEY가 설정되지 않았습니다.")
        return

    results = []
    for loader in loaders:
        for splitter in splitters:
            # 로더와 스플리터 조합 처리
            data = f"Simulated data using {loader}"  # 로더에서 데이터 가져오기
            result = evaluate_splits(api_key, loader, splitter, data)
            results.append({
                "loader": loader,
                "splitter": splitter,
                "result": result
            })
    
    # 최적 조합 선택 (예: 최고 점수)
    best_combination = max(results, key=lambda x: x['result']['choices'][0]['text'])
    print(f"최적 조합: {best_combination}")

if __name__ == "__main__":
    main()
