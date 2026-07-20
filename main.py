import streamlit as st

from pokemon_data import MBTI_POKEMON, COMPATIBLE_MBTI, get_sprite_url

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
    sprite_url = get_sprite_url(result["dex"])

    # 채팅방 페이지에서 프로필 사진으로 쓸 수 있도록 세션에 저장
    st.session_state["my_mbti"] = selected_mbti
    st.session_state["my_pokemon"] = result

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

    compat = COMPATIBLE_MBTI[selected_mbti]
    st.subheader(f"💞 {selected_mbti}와 궁합이 좋은 MBTI는 {compat['partner']}!")
    st.write(compat["reason"])

    partner_pokemon = MBTI_POKEMON[compat["partner"]]
    partner_sprite_url = get_sprite_url(partner_pokemon["dex"])

    col3, col4 = st.columns([1, 2])
    with col3:
        st.image(partner_sprite_url, width=140)
    with col4:
        st.markdown(f"**{compat['partner']}의 포켓몬:** {partner_pokemon['name']} ({partner_pokemon['type']})")

    st.divider()
    st.success("이제 왼쪽 사이드바에서 '공유 채팅방'으로 이동해 이 포켓몬을 프로필로 대화해보세요!")
    st.page_link("pages/00_공유채팅방.py", label="💬 공유 채팅방으로 이동", icon="💬")

st.divider()
st.caption("Made with Streamlit 🐍 · 16가지 MBTI 유형별 포켓몬 매칭")
