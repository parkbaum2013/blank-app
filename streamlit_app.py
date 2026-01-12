import streamlit as st

st.title("🎈 숩숩이 앱 따라한 앱")
st.write(
    "안영하세요 코딩을 배우고 있습니다."
)
# st.markdown(): 마크다운 문법지월
st.markdown("**굵은 텍스트**, *기울입 텍스트*")
st.markdown("-첫 번째 항목")

# 정보성 메시지 막스
st.info("정보 에시지 입니다")

import streamlit as st

import pandas as pd

 

st.title("  공개 Google Sheet 읽기")

st.info(" 누구나 볼 수 있도록 공개된 시트를 Pandas로 직접 불러오는 가장 간단한 방법입니다.\n 링크는 반드시 `export?format=csv` 형태로 설정하세요.")

 

csv_url1 = "https://docs.google.com/spreadsheets/d/1VC_q8HJfIufjGVR2zGRcJjBgkefIbp6Pv01rQ1uvoXI/export?format=csv"

df1 = pd.read_csv(csv_url1)

st.dataframe(df1)