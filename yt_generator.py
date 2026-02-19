import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

st.set_page_config(page_title="AI Poster Generator FREE", page_icon="🔥", layout="centered")

# ---------- STYLING ----------
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
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🔥 AI Poster + Content Generator (FREE)</p>', unsafe_allow_html=True)
st.write("Create Attractive Posters + Caption + Hashtags Instantly 🚀")

# ---------- INPUT ----------
topic = st.text_input("📌 Enter Topic (Example: Trading Strategy, AI Business, Motivation)")
platform = st.selectbox("📱 Platform", [
    "Instagram Post (1:1)",
    "YouTube Thumbnail (16:9)",
    "LinkedIn Post (4:5)"
])
tone = st.selectbox("🔥 Tone", ["Professional", "Motivational", "Bold", "Modern"])

# ---------- GENERATE ----------
if st.button("🚀 Generate Poster"):

    if not topic:
        st.warning("Enter topic first")
        st.stop()

    # --------- AUTO CONTENT GENERATION ---------
    hooks = [
        f"Master {topic} Today!",
        f"Why {topic} Is Game Changer",
        f"Stop Ignoring {topic}",
        f"{topic} Explained Simply",
        f"Secrets Behind {topic}"
    ]

    caption_templates = [
        f"🚀 Want to dominate in {topic}? Start learning smart strategies today.",
        f"🔥 {topic} is changing the future. Are you ready?",
        f"💡 If you're serious about {topic}, this is your sign to start now.",
        f"📈 Grow faster using powerful {topic} techniques."
    ]

    hashtags = [
        f"#{topic.replace(' ', '')}",
        "#Success",
        "#Growth",
        "#Business",
        "#Motivation",
        "#Entrepreneur",
        "#DigitalMarketing",
        "#AI",
        "#Learning"
    ]

    hook = random.choice(hooks)
    caption = random.choice(caption_templates)
    hashtag_text = " ".join(hashtags[:6])

    # --------- IMAGE SIZE BASED ON PLATFORM ---------
    if "1:1" in platform:
        width, height = 1080, 1080
    elif "16:9" in platform:
        width, height = 1280, 720
    else:
        width, height = 1080, 1350

    # --------- CREATE IMAGE ---------
    img = Image.new("RGB", (width, height), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    try:
        font_big = ImageFont.truetype("arial.ttf", int(height/10))
        font_small = ImageFont.truetype("arial.ttf", int(height/20))
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Center Text
    # Get text size (NEW Pillow Method)
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


    # --------- DISPLAY CONTENT ---------
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("📝 Caption")
    st.write(caption)

    st.subheader("🔖 Hashtags")
    st.write(hashtag_text)
    st.markdown('</div>', unsafe_allow_html=True)

    st.subheader("🎨 Generated Poster")
    st.image(img, use_column_width=True)

    # --------- DOWNLOAD BUTTON ---------
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    st.download_button(
        label="⬇ Download Poster",
        data=buffer.getvalue(),
        file_name="poster.png",
        mime="image/png"
    )
