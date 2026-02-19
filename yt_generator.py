import streamlit as st
import random
from PIL import Image, ImageDraw, ImageFont
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI YouTube Growth Tool FREE", page_icon="🎬", layout="centered")

st.title("🎬 AI YouTube Title & Thumbnail Generator (FREE)")
st.write("Generate viral YouTube content instantly 🚀")

# ---------------- INPUT ----------------
topic = st.text_input("📌 Enter Video Topic")
audience = st.selectbox("🎯 Target Audience", ["Students", "Developers", "Beginners", "General Public"])
tone = st.selectbox("🔥 Tone", ["Viral", "Educational", "Shocking", "Funny", "Professional"])

# ---------------- TITLE GENERATOR ----------------
def generate_titles(topic, tone):
    templates = [
        f"{topic} Explained in 5 Minutes!",
        f"You Won't Believe This About {topic}",
        f"The Truth About {topic}",
        f"Master {topic} Fast!",
        f"Stop Doing This in {topic}",
        f"{topic} Secrets Nobody Tells You",
        f"How I Learned {topic} Quickly",
        f"Big Mistakes in {topic}",
        f"{topic} Made Simple",
        f"Ultimate Guide to {topic}"
    ]
    random.shuffle(templates)
    return templates[:10]

# ---------------- DESCRIPTION ----------------
def generate_description(topic, audience):
    return f"""
This video explains {topic} in a simple and practical way specially for {audience}.

You will learn:
- Core concepts
- Common mistakes
- Practical applications
- Smart tips for faster growth

Watch till the end for maximum value 🚀
"""

# ---------------- HASHTAGS ----------------
def generate_hashtags(topic):
    base = topic.replace(" ", "")
    return [f"#{base}", "#YouTubeGrowth", "#ViralVideo", "#ContentCreator",
            "#Trending", "#LearnFast", "#Success", "#DigitalGrowth",
            "#CreatorTips", "#OnlineIncome"]

# ---------------- THUMBNAIL GENERATOR ----------------
def generate_thumbnail(text):
    img = Image.new("RGB", (1280, 720), color=(20, 20, 30))
    draw = ImageDraw.Draw(img)

    # Big text
    draw.text((200, 300), text[:20], fill="yellow")

    return img

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Content"):

    if topic:

        st.subheader("📈 Viral Titles")
        titles = generate_titles(topic, tone)
        for t in titles:
            st.write("🔥", t)

        st.subheader("💬 Thumbnail Hook Text")
        hooks = [
            "SHOCKING!",
            "DON'T MISS",
            "MUST WATCH",
            "SECRET REVEALED",
            "BIG UPDATE"
        ]
        for h in hooks[:3]:
            st.write("👉", h)

        st.subheader("📝 Description")
        st.write(generate_description(topic, audience))

        st.subheader("🏷 Hashtags")
        hashtags = generate_hashtags(topic)
        st.write(" ".join(hashtags))

        # Thumbnail
        st.subheader("🎨 Thumbnail Preview")
        thumb = generate_thumbnail(topic.upper())
        st.image(thumb)

        # Download button
        buf = io.BytesIO()
        thumb.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="⬇️ Download Thumbnail",
            data=byte_im,
            file_name=f"{topic}_thumbnail.png",
            mime="image/png"
        )

    else:
        st.warning("Please enter topic.")
