import streamlit as st
from openai import OpenAI
import os
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI YouTube Growth Tool", page_icon="🎬", layout="centered")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    color: #FF4B4B;
}
.result-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #FF4B4B;
}
.download-btn {
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🎬 AI YouTube Title & Thumbnail Generator PRO</p>', unsafe_allow_html=True)
st.write("Generate viral titles, hooks, description & AI thumbnails instantly 🚀")

# ---------------- OPENAI SETUP ----------------
OPENAI_KEY = st.secrets["OPENAI_KEY"]
client = OpenAI(api_key=OPENAI_KEY)

if not OPENAI_KEY:
    st.error("⚠️ OPENAI_KEY not found. Add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=OPENAI_KEY)

# ---------------- USER INPUT ----------------
topic = st.text_input("📌 Enter Video Topic")
audience = st.selectbox("🎯 Target Audience", ["Students", "Developers", "Beginners", "General Public"])
tone = st.selectbox("🔥 Tone", ["Viral", "Educational", "Shocking", "Funny", "Professional"])

generate_thumbs = st.checkbox("🎨 Generate 3 Thumbnail Variations")

# ---------------- GENERATE BUTTON ----------------
if st.button("🚀 Generate Content"):

    if topic:

        # -------- CONTENT GENERATION --------
        with st.spinner("Generating viral content..."):

            prompt = f"""
            You are a professional YouTube growth expert.

            Topic: {topic}
            Audience: {audience}
            Tone: {tone}

            Generate clearly formatted sections:

            1) 10 Viral YouTube Titles
            2) 3 Powerful Thumbnail Hook Texts (max 4 words)
            3) Thumbnail Visual Concept Idea
            4) SEO Optimized Description (150 words)
            5) 15 Trending Hashtags
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.choices[0].message.content

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("📈 Generated YouTube Content")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

        # -------- IMAGE GENERATION --------
        st.subheader("🎨 AI Thumbnail Images")

        num_images = 3 if generate_thumbs else 1

        for i in range(num_images):

            with st.spinner(f"Creating thumbnail {i+1}..."):

                image = client.images.generate(
                    model="gpt-image-1",
                    prompt=f"""
                    Create a high CTR YouTube thumbnail for topic: {topic}.
                    Style: Bold, dramatic lighting, high contrast,
                    expressive face, big readable text,
                    modern YouTube style, 16:9 ratio.
                    Variation number: {i+1}
                    """,
                    size="1024x576"
                )

                image_base64 = image.data[0].b64_json
                image_bytes = base64.b64decode(image_base64)

                st.image(image_bytes, use_column_width=True)

                st.download_button(
                    label=f"⬇️ Download Thumbnail {i+1}",
                    data=image_bytes,
                    file_name=f"{topic}_thumbnail_{i+1}.png",
                    mime="image/png"
                )

    else:
        st.warning("Please enter a video topic.")
