import streamlit as st
from ai_llm import ask_with_reference

st.set_page_config(page_title="소득세법 챗봇", page_icon="🧠")
st.title("소득세법 챗봇")
st.caption("소득세 관련된 질문을 답변 드립니다")

print("-----------------시작")

if user_question := st.chat_input(placeholder ="소득세 관련무엇이 궁금하신가요?"):
  with st.chat_message('user'):
    st.write(user_question)
  with st.spinner('질문을 처리하는 중입니다...'):
    answer = ask_with_reference(user_question)
    with st.chat_message('ai'):
      st.write(answer)
      print('답변완료')