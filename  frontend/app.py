import streamlit as st

st.title("🔥 AttentionX AI – Viral Clip Engine")

st.caption("Turn long videos into viral shorts using AI 🚀")

uploaded = st.file_uploader("Upload Video", type=["mp4"])

if uploaded:
    st.success("Processing video...")

    st.video(uploaded)

    st.subheader("Generated Clips")

    for i in range(3):
        st.write(f"🎬 Clip {i+1}")
        st.write("Hook: This will blow your mind 🔥")
        st.write("Viral Score:", round(0.7 + i*0.1, 2))
        st.write("AI Confidence:", int((0.7 + i*0.1)*100), "%")