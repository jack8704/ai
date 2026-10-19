# 실행 : streamlit run 2_streamlit.py
import streamlit as st
st.set_page_config(page_title="ai요약", page_icon="🧠", layout="wide")
st.title("나의 첫 streamlit 웹 애플리케이션") # h1 태그
st.header("요약 시스템") #h2 태그
st.subheader("요약 시스템을 사용하여 내용을 요약합니다.") # h3
st.text("tex함수를 이용한 텍스트 입니다") # p태그
st.write("write 함수를 이용한 텍스트 표시입니다.")
st.caption("caption 함수를 이용한 텍스트 캡션입니다.")
st.markdown("---")
st.markdown("# 요약 시스템")
message = st.text_area("요약할 내용을 입력하세요 : ")

if st.button("요약"):
  st.info('버튼클릭했음')
  st.write(message)

if prompt := st.chat_input("요약할 내용을 입력하세요 : "):
  st.chat_message("assistant").write(prompt)
  st.chat_message("ai").write(prompt)
  st.chat_message("user").write(prompt)
  st.chat_message("홍길동").write(prompt)

