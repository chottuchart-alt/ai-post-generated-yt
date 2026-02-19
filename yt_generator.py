import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Poster Generator PRO", page_icon="🔥", layout="centered")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.big-title {
    font-size: 34px;
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
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🔥 AI Poster + Content Generator PRO</p>', unsafe_allow_html=True)
st.write("Create Attractive Posters + Post Content + Hashtags Instantly 🚀")

# ---------------- INPUT ----------------
topic = st.text_input("📌 Enter Topic (Example: Trading Strategy, AI Business, Motivation)")
platform = st.selectbox("📱 Platform", ["Instagram Post (1:1)", "YouTube Thumbnail (16:9)", "LinkedIn Post (4:5)"])
tone = st.selectbox("🔥 Tone", ["Professional", "Motivational", "Bold", "Luxury", "Modern"])

# ---------------- GENERATE ----------------
if st.button("🚀 Generate Poster & Content"):

    if topic:

        # -------- PLATFORM SIZE --------
        if platform == "Instagram Post (1:1)":
            width, height = 1080, 1080
        elif platform == "YouTube Thumbnail (16:9)":
            width, height = 1280, 720
        else:
            width, height = 1080, 1350

        # -------- CREATE IMAGE --------
        image = Image.new("RGB", (width, height), (10, 15, 30))
        draw = ImageDraw.Draw(image)

        # -------- FONTS --------
        try:
            font_big = ImageFont.truetype("arial.ttf", int(width/12))
            font_small = ImageFont.truetype("arial.ttf", int(width/20))
        except:
            font_big = ImageFont.load_default()
            font_small = ImageFont.load_default()

        hook_words = [
            "SECRET STRATEGY",
            "STOP LOSING MONEY",
            "LEVEL UP NOW",
            "THIS CHANGES EVERYTHING",
            "MASTER THIS TODAY"
        ]

        hook = random.choice(hook_words)

        # -------- TEXT SIZE FIX --------
        bbox = draw.textbbox((0, 0), hook, font=font_big)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        draw.text(
            ((width - text_width) / 2, height / 3),
            hook,
            font=font_big,
            fill=(255, 75, 75)
        )

        draw.text(
            (width / 2, height / 2),
            topic,
            font=font_small,
            fill=(255, 255, 255),
            anchor="mm"
        )

        # -------- SHOW IMAGE --------
        st.image(image, use_column_width=True)

        # -------- DOWNLOAD --------
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        st.download_button(
            label="📥 Download Poster",
            data=img_bytes.getvalue(),
            file_name="poster.png",
            mime="image/png"
        )

        # -------- CONTENT --------
        st.markdown('<div class="result-box">', unsafe_allow_html=True)

        st.subheader("📝 Post Content")
        st.write(f"""
🔥 {hook}  

If you want to master **{topic}**, this is your time.

Start learning.
Start improving.
Start winning.

Don't miss this opportunity 🚀
""")

        st.subheader("🏷 Hashtags")
        st.write(f"# {topic.replace(' ', '')} #Success #Growth #Mindset #Business #Motivation")

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("Please enter a topic.")
