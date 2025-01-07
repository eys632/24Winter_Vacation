#!pip install -U langchain_upstage
#!pip install -qU langchain-teddynote

from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
upstage_api_key = os.getenv("UPSTAGE_API_KEY")

from langchain_upstage import UpstageLayoutAnalysisLoader

# 파일 경로
file_path = r"C:\Users\eys63\Desktop\기타활동\2024\겨울방학\24Winter_Vacation\data\Linear Algebra and Its Applications, chapter1.pdf"

# 문서 로더 설정
loader = UpstageLayoutAnalysisLoader(
    file_path,
    output_type="html",
    split="page",
    use_ocr=True,
    exclude=["header", "footer"],
    api_key=UPSTAGE_API_KEY,
)

# 문서 로드
docs = loader.load()

# 결과 출력
for doc in docs[:]:
    print(doc)
