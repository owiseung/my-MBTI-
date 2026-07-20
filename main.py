import streamlit as st
st.title (오위승의 첫 웹앱)

# ------------------------------
# MBTI별 추천 포켓몬 데이터
# ------------------------------
MBTI_POKEMON = {
    "INTJ": {"name": "메타그로스", "dex": 376, "type": "강철/에스퍼",
             "reason": "치밀한 계산과 전략으로 목표를 달성하는 완벽주의자. INTJ의 냉철한 통찰력과 닮았어요."},
    "INTP": {"name": "폴리곤",   "dex": 137, "type": "노말",
             "reason": "논리와 데이터로 세상을 분석하는 디지털 생명체. 이론 탐구를 좋아하는 INTP와 잘 맞아요."},
    "ENTJ": {"name": "리자몽",   "dex": 6,   "type": "불꽃/비행",
             "reason": "타고난 카리스마로 무리를 이끄는 강력한 리더. ENTJ의 추진력과 통솔력을 상징해요."},
    "ENTP": {"name": "조로아크", "dex": 571, "type": "악",
             "reason": "재치와 임기응변으로 상대를 놀라게 하는 전략가. 토론을 즐기는 ENTP와 통해요."},
    "INFJ": {"name": "가디안",   "dex": 282, "type": "에스퍼",
             "reason": "신비로운 직관으로 소중한 존재를 지키는 수호자. INFJ의 깊은 통찰과 이상주의를 닮았어요."},
    "INFP": {"name": "이브이",   "dex": 133, "type": "노말",
             "reason": "무한한 가능성을 품고 자신만의 길을 찾는 존재. 순수한 이상을 좇는 INFP와 잘 어울려요."},
    "ENFJ": {"name": "루카리오", "dex": 448, "type": "격투/강철",
             "reason": "타인의 감정(파동)을 읽고 이끌어주는 조언자. ENFJ의 공감 능력과 리더십을 상징해요."},
    "ENFP": {"name": "피카츄",   "dex": 25,  "type": "전기",
             "reason": "활발하고 사교적이며 주변에 에너지를 전파하는 존재. ENFP의 밝은 매력 그 자체예요."},
    "ISTJ": {"name": "골렘",     "dex": 76,  "type": "바위/땅",
             "reason": "묵묵하고 우직하게 원칙을 지키는 든든한 존재. 성실하고 신뢰감 있는 ISTJ와 닮았어요."},
    "ISFJ": {"name": "해피너스", "dex": 113, "type": "노말",
             "reason": "따뜻한 마음으로 주변을 세심하게 보살피는 존재. 헌신적인 ISFJ와 잘 맞아요."},
    "ESTJ": {"name": "괴력몬",   "dex": 68,  "type": "격투",
             "reason": "체계적으로 계획을 세우고 강한 실행력으로 밀어붙이는 타입. ESTJ의 관리 능력을 닮았어요."},
    "ESFJ": {"name": "럭키",     "dex": 242, "type": "노말",
             "reason": "사람들과 어울리며 행복을 나눠주는 다정한 존재. 사교적인 ESFJ와 잘 어울려요."},
    "ISTP": {"name": "핫삼",     "dex": 212, "type": "벌레/강철",
             "reason": "군더더기 없이 실용적이고 손재주가 뛰어난 장인 타입. 문제 해결에 강한 ISTP와 닮았어요."},
    "ISFP": {"name": "샤미드",   "dex": 134, "type": "물",
             "reason": "감성적이고 자유로운 흐름을 따르는 예술가 기질. 자유로운 영혼 ISFP와 잘 맞아요."},
    "ESTP": {"name": "초염몽",   "dex": 392, "type": "불꽃/격투",
             "reason": "생각보다 몸이 먼저 움직이는 대담한 행동파. 모험을 즐기는 ESTP를 꼭 닮았어요."},
    "ESFP": {"name": "누오",     "dex": 272, "type": "물/풀",
             "reason": "흥이 넘치고 분위기를 즐겁게 만드는 무드메이커. 사람들의 시선을 즐기는 ESFP와 잘 어울려요."},
}

# ------------------------------
# 페이지 기본 설정
# ------------------------------
st.set_page_config(page_title="MBTI 포켓몬 추천기", page_icon="⚡", layout="centered")

st.title("⚡ MBTI 포켓몬 추천기")
st.write("당신의 MBTI에 딱 맞는 포켓몬 파트너를 찾아드릴게요!")

# ------------------------------
# MBTI 선택
# ------------------------------
mbti_list = list(MBTI_POKEMON.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기 🔍"):
    result = MBTI_POKEMON[selected_mbti]
    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{result['dex']}.png"

    st.balloons()
    st.subheader(f"{selected_mbti} 유형에게 어울리는 포켓몬은...")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(sprite_url, width=180)
    with col2:
        st.markdown(f"### {result['name']}")
        st.markdown(f"**타입:** {result['type']}")
        st.write(result["reason"])

st.divider()
st.caption("Made with Streamlit 🐍 · 16가지 MBTI 유형별 포켓몬 매칭")
