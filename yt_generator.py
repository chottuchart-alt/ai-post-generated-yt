import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import io
import random

st.set_page_config(page_title="🔥 Poster + Content Generator PRO", layout="centered")

st.title("🔥 AI Poster + Content Generator PRO (FREE)")

topic = st.text_input("📌 Enter Topic (Example: Trading Strategy, Motivation, Crypto, Baby Care)")
platform = st.selectbox("📱 Platform Size", ["YouTube (1280x720)", "Instagram (1080x1080)"])
tone = st.selectbox("🔥 Tone", ["Professional", "Aggressive", "Motivational", "Luxury", "Educational"])

if st.button("🚀 Generate Complete Post"):

    if not topic:
        st.warning("Enter topic")
        st.stop()

    # -------- SIZE --------
    if "YouTube" in platform:
        width, height = 1280, 720
    else:
        width, height = 1080, 1080

    # -------- BACKGROUND --------
    bg = Image.new("RGB", (width, height), "#0f2027")
    draw = ImageDraw.Draw(bg)

    for i in range(height):
        r = int(20 + (180 * (i/height)))
        g = int(30 + (140 * (i/height)))
        b = int(40 + (80 * (i/height)))
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    # Gold particles
    for _ in range(400):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        draw.ellipse((x, y, x+3, y+3), fill=(255,215,0))

    bg = bg.filter(ImageFilter.GaussianBlur(0.4))
    draw = ImageDraw.Draw(bg)

    # -------- FONT --------
    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", int(width/9))
        font_small = ImageFont.truetype("DejaVuSans-Bold.ttf", int(width/28))
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    text = topic.upper()

    bbox = draw.textbbox((0, 0), text, font=font_big)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = height / 3

    draw.text((x+6, y+6), text, font=font_big, fill=(0,0,0))
    draw.text((x, y), text, font=font_big, fill=(255,215,0), stroke_width=4, stroke_fill=(0,0,0))

    draw.text((width/2, height*0.65),
              "🔥 Powerful Insights Inside 🔥",
              font=font_small,
              fill="white",
              anchor="mm")

    # -------- SHOW IMAGE --------
    st.image(bg, use_column_width=True)

    img_bytes = io.BytesIO()
    bg.save(img_bytes, format="PNG")

    st.download_button("⬇ Download Poster",
                       img_bytes.getvalue(),
                       file_name="poster.png",
                       mime="image/png")

    # =====================================================
    # ================= CONTENT GENERATOR =================
    # =====================================================

    hooks = [
        f"🚀 Ready to master {topic}?",
        f"🔥 The ultimate guide to {topic}!",
        f"💰 Unlock the secrets of {topic} today!",
        f"⚡ Stop missing out on {topic}!"
    ]

    captions = [
        f"{topic} can completely change your results if done correctly.",
        f"Most people fail at {topic} because they don't know the fundamentals.",
        f"If you want real success in {topic}, consistency is key.",
        f"Understanding {topic} gives you a competitive edge."
    ]

    description = f"""
If you're serious about {topic}, this is for you.

In this post, we break down practical strategies, proven concepts,
and real-world insights that help you get better results.

Whether you're a beginner or experienced, mastering {topic}
can unlock new opportunities and growth.

Start applying these principles today and see the difference.
"""

    hashtag_base = topic.lower().replace(" ", "")
    hashtags = f"""
#{hashtag_base}
#{hashtag_base}tips
#{hashtag_base}strategy
#success
#growth
#business
#entrepreneur
#motivation
#digitalmarketing
#learning
#mindset
#viralcontent
#contentcreator
#socialmedia
#trending
"""

    # -------- DISPLAY TEXT CONTENT --------
    st.subheader("📢 Post Caption")
    st.write(random.choice(hooks))
    st.write(random.choice(captions))

    st.subheader("📝 Description")
    st.write(description)

    st.subheader("🏷 Hashtags")
    st.code(hashtags)

    # Download text file
    full_text = f"""
CAPTION:
{random.choice(hooks)}
{random.choice(captions)}

DESCRIPTION:
{description}

HASHTAGS:
{hashtags}
"""

    st.download_button("⬇ Download Content (TXT)",
                       full_text,
                       file_name="post_content.txt")
