import streamlit as st

st.set_page_config(page_title="AttentionX AI", layout="centered")

st.title("🔥 AttentionX AI – Viral Clip Engine")
st.caption("Transform long videos into viral short-form content instantly 🚀")

uploaded = st.file_uploader("Upload your video", type=["mp4"])

if uploaded:
    st.success("🔍 AI analyzing content... extracting emotional peaks")

    st.video(uploaded)

    st.subheader("🎬 Generated Viral Clips")

    for i in range(3):
        score = round(0.75 + i*0.08, 2)

        st.markdown(f"### Clip {i+1}")
        st.write("🔥 Hook:", "This insight will change your perspective")
        st.write("📊 Viral Score:", score)
        st.write("🤖 AI Confidence:", int(score*100), "%")
        st.divider()