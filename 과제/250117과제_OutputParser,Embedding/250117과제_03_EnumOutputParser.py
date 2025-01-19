from langchain.output_parsers.enum import EnumOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT")
LANGCHAIN_PROJECT_ID = os.getenv("LANGCHAIN_PROJECT_ID")

class Colors(Enum):
    RED = "빨간색"
    GREEN = "초록색"
    BLUE = "파란색"
    WHITE = "흰색"
    BLACK = "검은색"
    GRAY = "회색"
    SILVER = "은색"
    MAROON = "적갈색"
    OLIVE = "올리브색"
    LIME = "라임색"
    NAVY = "남색"
    TEAL = "청록색"
    PURPLE = "보라색"
    FUCHSIA = "핫핑크"
    AQUA = "물색"
    YELLOW = "노란색"
    ORANGE = "주황색"
    BROWN = "갈색"
    BEIGE = "베이지색"
    IVORY = "아이보리색"
    KHAKI = "카키색"
    CORAL = "산호색"
    CRIMSON = "심홍색"
    INDIGO = "남보라색"
    VIOLET = "보라빛"
    PLUM = "자두색"
    MAGENTA = "마젠타"
    GOLD = "금색"
    HOTPINK = "핫핑크"
    DEEPPINK = "딥핑크"
    LIGHTPINK = "연분홍색"
    PALEVIOLETRED = "연보라빛빨강"
    SALMON = "연어색"
    TOMATO = "토마토색"
    ORANGERED = "오렌지레드"
    CHOCOLATE = "초콜릿색"
    SADDLEBROWN = "진한 갈색"
    SIENNA = "시엔나색"
    PERU = "페루색"
    BISQUE = "비스킷색"
    MOCCASIN = "모카신색"
    WHEAT = "밀색"
    TAN = "황갈색"
    LAVENDER = "라벤더색"
    THISTLE = "엉겅퀴색"
    SEASHELL = "조개껍데기색"
    SNOW = "눈색"
    HONEYDEW = "허니듀색"
    MINTCREAM = "민트크림색"
    AZURE = "담청색"
    ALICEBLUE = "앨리스블루"
    GHOSTWHITE = "유령흰색"
    FLORALWHITE = "플로럴화이트"
    LINEN = "리넨색"
    OLDLACE = "올드레이스색"
    PAPAYAWHIP = "파파야휘핑색"
    BLANCHEDALMOND = "블랜치드아몬드색"
    CORNSILK = "콘실크색"
    LEMONCHIFFON = "레몬시폰색"
    LIGHTGOLDENRODYELLOW = "연한 골든로드 노랑"
    LIGHTYELLOW = "연노랑"
    IVORY2 = "아이보리색(2)"
    BEIGE2 = "베이지색(2)"
    CORNFLOWERBLUE = "수레국화파랑"
    CADETBLUE = "군청록"
    STEELBLUE = "강철파랑"
    ROYALBLUE = "로열블루"
    MEDIUMBLUE = "중간파랑"
    DODGERBLUE = "도저블루"
    DEEPSKYBLUE = "깊은하늘색"
    LIGHTSKYBLUE = "연하늘색"
    SKYBLUE = "하늘색"
    LIGHTBLUE = "연파랑"
    POWDERBLUE = "파우더블루"
    PALETURQUOISE = "연한 청록색"
    DARKTURQUOISE = "진청록"
    MEDIUMTURQUOISE = "중청록"
    TURQUOISE = "청록색"
    CYAN = "시안"
    DARKCYAN = "진시안색"
    LIGHTCYAN = "연한 시안색"
    CADETBLUE2 = "군청록(2)"
    LIGHTSEAGREEN = "연한 바다초록"
    DARKSEAGREEN = "진한 바다초록"
    SEAGREEN = "바다초록"
    MEDIUMSEAGREEN = "중간 바다초록"
    MEDIUMAQUAMARINE = "중간 아콰마린"
    AQUAMARINE = "아콰마린색"
    MEDIUMSPRINGGREEN = "중간 봄초록"
    SPRINGGREEN = "봄초록"
    MEDIUMMINT = "중간 민트색"
    LIMEGREEN = "라임그린"
    FORESTGREEN = "숲초록"
    DARKGREEN = "진초록"
    CHARTREUSE = "샤르트뢰즈"
    LAWNGREEN = "잔디초록"
    GREENYELLOW = "초록노랑"
    PALEGREEN = "연초록"
    LIGHTGREEN = "연한 초록"
    DARKOLIVEGREEN = "진올리브초록"
    OLIVEDRAB = "올리브드랍"
    YELLOWGREEN = "노랑초록"
    DARKKHAKI = "진카키색"
    KHAKI2 = "카키색(2)"
    GOLDENROD = "골든로드색"
    DARKGOLDENROD = "진한 골든로드"
    LIGHTGOLDENROD = "연한 골든로드"
    ROSYBROWN = "로지브라운"
    INDIANRED = "인디안레드"
    FIREBRICK = "벽돌빨강"
    BROWN2 = "갈색(2)"
    DARKRED = "진빨강"
    LIGHTSALMON = "연연어색"
    DARKSALMON = "진연어색"
    LIGHTCORAL = "연산호색"
    DARKORANGE = "진주황색"
    ORANGE2 = "주황색(2)"
    LIGHTORANGE = "연주황색"
    GOLD2 = "금색(2)"
    LIGHTGOLD = "연한 금색"
    LEMON = "레몬색"
    SEPIA = "세피아색"
    LIGHTMAROON = "연적갈색"
    DIMGRAY = "어두운 회색"
    DARKGRAY = "진회색"
    GAINSBORO = "게인즈보로색"
    LIGHTGREY = "연회색"
    SLATEGRAY = "슬레이트색"
    LIGHTSLATEGRAY = "연슬레이트색"
    MIDNIGHTBLUE = "미드나잇블루"
    MEDIUMPURPLE = "중간보라"
    BLUEVIOLET = "파랑보라"
    DARKVIOLET = "진보라"
    DARKORCHID = "진난초색"
    MEDIUMORCHID = "중간 난초색"
    ORCHID = "난초색"
    MEDIUMPURPLE2 = "중간보라(2)"
    REBECCAPURPLE = "레베카퍼플"
    LAVENDERBLUSH = "라벤더블러쉬"
    MEDIUMSLATEBLUE = "중간슬레이트블루"
    SLATEBLUE = "슬레이트블루"
    DARKSLATEBLUE = "진슬레이트블루"
    LIGHTSLATEBLUE = "연슬레이트블루"
    MEDIUMBLUE2 = "중간파랑(2)"
    COBALTBLUE = "코발트블루"
    PEACHPUFF = "피치퍼프색"
    LAVENDER2 = "라벤더색(2)"
    LAVENDER3 = "라벤더색(3)"
    LIGHTSTEELBLUE = "연한 강철파랑"
    LIGHTSTEELBLUE2 = "연한 강철파랑(2)"
    LIGHTSTEELBLUE3 = "연한 강철파랑(3)"
    CORNFLOWERBLUE2 = "수레국화파랑(2)"
    MEDIUMSPRINGGREEN2 = "중간 봄초록(2)"
    SPRINGGREEN2 = "봄초록(2)"
    EMERALD = "에메랄드"
    JADE = "비취색"
    MINT = "민트색"
    LIGHTYELLOW2 = "연노랑(2)"
    CANARYYELLOW = "카나리아노랑"
    MUSTARD = "머스타드색"
    LEMONLIME = "레몬라임색"
    TEAL2 = "청록색(2)"
    MINTCREAM2 = "민트크림색(2)"
    AZURE2 = "담청색(2)"
    SKYBLUE2 = "하늘색(2)"
    LIGHTBLUE2 = "연파랑(2)"
    POWDERBLUE2 = "파우더블루(2)"
    TURQUOISE2 = "청록색(2)"
    CYAN2 = "시안(2)"
    SEAFOAM = "바다거품색"
    LIGHTSEAFOAM = "연한 바다거품색"
    SEAFOAMGREEN = "바다거품 초록"
    LIGHTTEAL = "연한 청록"
    MEDIUMTEAL = "중간 청록"
    DEEPTEAL = "깊은 청록"
    LIME2 = "라임색(2)"
    LIME3 = "라임색(3)"
    CHLOROPHYLL = "엽록소색"
    HUNTERGREEN = "헌터그린"
    PISTACHIO = "피스타치오색"
    PASTELGREEN = "파스텔초록"
    PASTELYELLOW = "파스텔노랑"
    PASTELBLUE = "파스텔파랑"
    PASTELPINK = "파스텔분홍"
    PASTELPURPLE = "파스텔보라"
    PASTELORANGE = "파스텔주황"
    PASTELRED = "파스텔빨강"
    PASTELBROWN = "파스텔갈색"
    PASTELGRAY = "파스텔회색"
    PASTELTEAL = "파스텔청록"
    MISTYROSE = "미스티로즈"
    GAINSBORO2 = "게인즈보로색(2)"
    LIGHTCORAL2 = "연산호색(2)"
    SALMON2 = "연어색(2)"
    CORAL2 = "산호색(2)"
    DARKSALMON2 = "진연어색(2)"
    LIGHTSALMON2 = "연연어색(2)"
    PINK = "분홍색"
    LIGHTPINK2 = "연분홍색(2)"
    HOTPINK2 = "핫핑크(2)"
    FUCHSIA2 = "핫핑크(2)"
    VIOLET2 = "보라빛(2)"
    LIGHTVIOLET = "연보라빛"
    PURPLE2 = "보라색(2)"
    MEDIUMPURPLE3 = "중간보라(3)"
    MEDIUMORCHID2 = "중간 난초색(2)"
    ORCHID2 = "난초색(2)"
    THISTLE2 = "엉겅퀴색(2)"
    PLUM2 = "자두색(2)"
    LAVENDERBLUSH2 = "라벤더블러쉬(2)"
    CRIMSON2 = "심홍색(2)"
    MAROON2 = "적갈색(2)"
    DEEPMAROON = "깊은 적갈색"
    BERRY = "베리색"
    DEEPBERRY = "깊은 베리색"
    BURGUNDY = "버건디색"
    WINE = "와인색"
    VERMILION = "주홍색"
    SCARLET = "스칼렛색"
    ROSE = "장미색"
    ROSETTE = "로제트색"
    DARKMAGENTA = "진마젠타"
    MEDIUMMAGENTA = "중간마젠타"
    LIGHTMAGENTA = "연마젠타"
    ALIZARINCRIMSON = "알리자린크림슨"
    CARMINE = "카민색"
    RUBY = "루비색"
    DEEPRUBY = "깊은 루비색"
    ULTRAMARINE = "울트라마린"
    COBALT = "코발트색"
    PRUSSIANBLUE = "프로이센블루"
    DENIM = "데님색"
    CERULEAN = "세룰리안"
    TOPAZ = "토파즈색"
    SAPPHIRE = "사파이어색"
    TIFFANYBLUE = "티파니블루"
    DARKBLUE = "진파랑"
    DARKTEAL = "진한 청록"
    DARKNAVY = "진한 남색"
    EBONY = "에보니색"
    CHARCOAL = "차콜색"
    SLATE = "슬레이트색"
    ONYX = "오닉스색"
    GREY2 = "회색(2)"
    COOLGREY = "쿨그레이"
    WARMGREY = "웜그레이"
    TAUPE = "토프색"
    NUDE = "누드톤"
    PARCHMENT = "파치먼트색"
    DRAB = "드랩색"
    FAWN = "폰색"
    SEPIA2 = "세피아(2)"
    SMOKE = "스모크색"
    SMOKEWHITE = "스모크화이트"
    LIGHTSMOKE = "연스모크색"
    DARKSMOKE = "진스모크색"
    MIDGRAY = "중간회색"
    DARKCHARCOAL = "진차콜색"
    COOLBLACK = "쿨블랙"
    WARMBLACK = "웜블랙"
    JET = "제트블랙"
    EBONY2 = "에보니색(2)"
    MIDGREEN = "중간초록"
    MIDORANGE = "중간주황"
    MIDBLUE = "중간파랑"
    MIDPURPLE = "중간보라"
    MIDRED = "중간빨강"
    MIDYELLOW = "중간노랑"
    MIDBROWN = "중간갈색"
    MIDGRAY2 = "중간회색(2)"
    MIDNAVY = "중간남색"
    MIDTEAL = "중간청록"
    MIDMAROON = "중간적갈색"
    MIDMAGENTA = "중간마젠타"
    MIDCYAN = "중간시안"
    MIDLIME = "중간라임"
    MIDPINK = "중간분홍"
    MIDGOLD = "중간금색"
    MIDOLIVE = "중간올리브"
    MIDKHAKI = "중간카키"
    MIDBEIGE = "중간베이지"
    MIDIVORY = "중간아이보리"
    MIDCORAL = "중간산호색"
    MIDCRIMSON = "중간심홍색"
    MIDINDIGO = "중간남보라"
    MIDVIOLET = "중간보라빛"
    MIDPLUM = "중간자두색"
    MIDFUCHSIA = "중간핫핑크"
    MIDAQUA = "중간물색"
    MIDYELLOW2 = "중간노랑(2)"
    MIDORANGE2 = "중간주황(2)"
    MIDBROWN2 = "중간갈색(2)"
    LIGHTMAROON2 = "연적갈색(2)"
    LIGHTINDIGO = "연남보라"
    LIGHTPLUM = "연자두색"
    LIGHTOLIVE = "연올리브색"
    LIGHTKHAKI = "연카키색"
    LIGHTTEAL2 = "연청록색(2)"
    LIGHTNAVY = "연남색"
    LIGHTMAGENTA2 = "연마젠타(2)"
    LIGHTCYAN2 = "연시안(2)"
    LIGHTLIME = "연라임색"
    LIGHTPINK3 = "연분홍색(3)"
    LIGHTGOLD2 = "연금색(2)"
    LIGHTOLIVE2 = "연올리브색(2)"
    LIGHTKHAKI2 = "연카키색(2)"
    LIGHTBEIGE = "연베이지색"
    LIGHTCORAL3 = "연산호색(3)"
    LIGHTCRIMSON = "연심홍색"
    LIGHTINDIGO2 = "연남보라(2)"
    LIGHTVIOLET2 = "연보라빛(2)"
    ULTRALIGHTGRAY = "초연회색"
    ULTRALIGHTBLUE = "초연파랑"
    ULTRALIGHTPINK = "초연분홍"
    ULTRALIGHTYELLOW = "초연노랑"
    ULTRALIGHTGREEN = "초연초록"
    ULTRALIGHTORANGE = "초연주황"
    ULTRALIGHTPURPLE = "초연보라"
    ULTRALIGHTRED = "초연빨강"

parser = EnumOutputParser(enum=Colors)

# 프롬프트 템플릿을 생성합니다.
prompt = PromptTemplate.from_template(
    """다음의 물체는 어떤 색깔인가요? 색깔만 출력해주세요.

    Object: {object}

    Instructions: {instructions}"""
    # 파서에서 지시사항 형식을 가져와 부분적으로 적용합니다.
).partial(instructions=parser.get_format_instructions())

chain = prompt|ChatOpenAI(temperature=0, model='gpt-4o')|parser

response = chain.invoke({"object": "책상"})

print(response)