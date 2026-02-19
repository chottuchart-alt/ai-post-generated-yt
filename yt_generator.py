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
def generate_trading_thumbnail(text):
    from PIL import Image, ImageDraw, ImageFont
    import random

    width, height = 1280, 720
    img = Image.new("RGB", (width, height), "#0f172a")
    draw = ImageDraw.Draw(img)

    # Background gradient
    for i in range(height):
        color = (15, 23, 42 + i // 8)
        draw.line([(0, i), (width, i)], fill=color)

    # Draw fake trading candles
    for i in range(30):
        x = random.randint(50, width-50)
        candle_height = random.randint(100, 400)
        color = random.choice(["#00ff88", "#ff2e63"])
        draw.rectangle([x, height-100-candle_height, x+20, height-100], fill=color)

    # Big Font
    try:
        font = ImageFont.truetype("arial.ttf", 140)
    except:
        font = ImageFont.load_default()

    text = text.upper()

    # Center Text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) / 2
    y = height / 4

    # Shadow
    draw.text((x+6, y+6), text, font=font, fill="black")

    # Main text
    draw.text((x, y), text, font=font, fill="#FFD700")

    # Up Arrow
    draw.polygon(
        [(width-250, height-250),
         (width-150, height-450),
         (width-100, height-400),
         (width-200, height-200)],
        fill="#00ff00"
    )

    return img


