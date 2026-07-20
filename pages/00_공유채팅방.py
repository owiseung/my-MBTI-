import sqlite3
import datetime

import streamlit as st

from pokemon_data import MBTI_POKEMON, get_sprite_url

st.set_page_config(page_title="공유 채팅방", page_icon="💬", layout="centered")

DB_PATH = "chat_room.db"


# ------------------------------
# SQLite 저장소 (모든 방문자가 같은 파일을 읽고 씀 → 공유 채팅방)
# ------------------------------
def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT NOT NULL,
            mbti TEXT NOT NULL,
            pokemon_name TEXT NOT NULL,
            dex INTEGER NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def add_message(nickname, mbti, pokemon_name, dex, message):
    conn = get_connection()
    conn.execute(
        """INSERT INTO messages (nickname, mbti, pokemon_name, dex, message, created_at)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (nickname, mbti, pokemon_name, dex, message, datetime.datetime.now().strftime("%H:%M")),
    )
    conn.commit()
    conn.close()


def fetch_messages():
    conn = get_connection()
    rows = conn.execute(
        "SELECT nickname, mbti, pokemon_name, dex, message, created_at FROM messages ORDER BY id ASC"
    ).fetchall()
    conn.close()
    return rows


st.title("💬 공유 채팅방")
st.caption("이 채팅방은 모든 방문자가 함께 봅니다. 추천받은 포켓몬이 내 프로필 사진으로 쓰여요.")

# ------------------------------
# 내 프로필(닉네임 + MBTI/포켓몬) 설정
# ------------------------------
with st.expander("👤 내 프로필 설정", expanded=("my_pokemon" not in st.session_state)):
    nickname = st.text_input(
        "닉네임",
        value=st.session_state.get("chat_nickname", ""),
        placeholder="채팅방에서 사용할 닉네임을 입력하세요",
    )
    st.session_state["chat_nickname"] = nickname

    if "my_mbti" in st.session_state and "my_pokemon" in st.session_state:
        my_pokemon = st.session_state["my_pokemon"]
        col_p1, col_p2 = st.columns([1, 4])
        with col_p1:
            st.image(get_sprite_url(my_pokemon["dex"]), width=70)
        with col_p2:
            st.write(f"**{st.session_state['my_mbti']} · {my_pokemon['name']}**을(를) 프로필로 사용해요.")
        if st.button("다른 MBTI로 바꾸기"):
            del st.session_state["my_mbti"]
            del st.session_state["my_pokemon"]
            st.rerun()
    else:
        st.write("아직 추천을 안 받으셨네요! 여기서 바로 MBTI를 골라도 돼요.")
        picked_mbti = st.selectbox("MBTI 선택", list(MBTI_POKEMON.keys()))
        if st.button("이 포켓몬으로 프로필 설정하기"):
            st.session_state["my_mbti"] = picked_mbti
            st.session_state["my_pokemon"] = MBTI_POKEMON[picked_mbti]
            st.rerun()

is_ready = bool(st.session_state.get("chat_nickname")) and "my_pokemon" in st.session_state

st.divider()

# ------------------------------
# 채팅 내역 표시
# ------------------------------
_, col_refresh = st.columns([5, 1])
with col_refresh:
    if st.button("🔄 새로고침"):
        st.rerun()

messages = fetch_messages()

if not messages:
    st.write("아직 대화가 없어요. 첫 메시지를 남겨보세요!")
else:
    for nickname_, mbti_, pokemon_name_, dex_, message_, created_at_ in messages:
        avatar_url = get_sprite_url(dex_)
        with st.chat_message(name=nickname_, avatar=avatar_url):
            st.markdown(f"**{nickname_}** · {mbti_} · {pokemon_name_}")
            st.write(message_)
            st.caption(created_at_)

# ------------------------------
# 메시지 입력
# ------------------------------
if not is_ready:
    st.warning("닉네임을 입력하고 프로필(MBTI/포켓몬)을 설정해야 채팅에 참여할 수 있어요.")
else:
    new_message = st.chat_input("메시지를 입력하세요")
    if new_message:
        my_pokemon = st.session_state["my_pokemon"]
        add_message(
            nickname=st.session_state["chat_nickname"],
            mbti=st.session_state["my_mbti"],
            pokemon_name=my_pokemon["name"],
            dex=my_pokemon["dex"],
            message=new_message,
        )
        st.rerun()
