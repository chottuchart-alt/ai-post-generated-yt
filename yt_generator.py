import streamlit as st
from openai import OpenAI
import os
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Social Media Poster Generator", page_icon="🔥", layout="centered")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    color: #ff4b4b;
}
.result-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ff4b4b;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🔥 AI Poster + Content Generator PRO</p>', unsafe_allow_html=True)
st.write("Create Attractive Posters + Post Content + Hashtags Instantly 🚀")

# ---------------- OPENAI ----------------
OPENAI_KEY = os.getenv("OPENAI_KEY")

if not OPENAI_KEY:
    st.error("Add OPENAI_KEY in Streamlit secrets")
    st.stop()

client = OpenAI(api_key=OPENAI_KEY)

# ---------------- INPUTS ----------------
topic = st.text_input("📌 Enter Topic (Example: Trading Strategy, AI Business, Motivation)")

platform = st.selectbox("📱 Platform",
                        ["Instagram Post (1:1)",
                         "Instagram Story (9:16)",
                         "LinkedIn Post (1:1)",
                         "YouTube Thumbnail (16:9)"])

tone = st.selectbox("🔥 Tone",
                    ["Professional", "Viral", "Motivational", "Luxury", "Bold"])

# ---------------- SIZE LOGIC ----------------
size_map = {
    "Instagram Post (1:1)": "1024x1024",
    "Instagram Story (9:16)": "1024x1792",
    "LinkedIn Post (1:1)": "1024x1024",
    "YouTube Thumbnail (16:9)": "1792x1024"
}

# ---------------- GENERATE ----------------
if st.button("🚀 Generate Poster & Content"):

    if topic:

        with st.spinner("Generating AI content..."):

            prompt = f"""
            Create attractive social media content.

            Topic: {topic}
            Tone: {tone}

            Provide clearly separated sections:

            1) Powerful Hook Line
            2) Short Engaging Post Content (100 words)
            3) 15 Trending Hashtags
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            text_result = response.choices[0].message.content

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("📢 Generated Post Content")
        st.write(text_result)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- IMAGE GENERATION ----------------
        st.subheader("🎨 AI Poster Image")

        with st.spinner("Creating Attractive Poster..."):

            image = client.images.generate(
                model="gpt-image-1",
                prompt=f"""
                Create a high quality {platform} poster.

                Topic: {topic}
                Style: {tone}
                Bold typography, dramatic lighting,
                modern social media style,
                eye-catching,
                high contrast,
                professional design.
                """,
                size=size_map[platform]
            )

            image_url = image.data[0].url
            st.image(image_url, use_column_width=True)

            # DOWNLOAD BUTTON
            st.markdown("### ⬇ Download Poster")
            st.markdown(f"[Click Here To Download]({image_url})")

    else:
        st.warning("Enter topic first.")
