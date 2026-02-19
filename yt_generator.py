import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Ultimate Poster Generator PRO", page_icon="🎨", layout="centered")

st.title("🚀 Ultimate AI Poster + Content Generator PRO")

# ---------------- INPUTS ----------------
topic = st.text_input("📌 Enter Topic (Example: Trading Strategy, Baby Care, Motivation)")
platform = st.selectbox("📱 Platform", ["Instagram (1:1)", "YouTube (16:9)", "LinkedIn (4:5)"])
style = st.selectbox("🎨 Poster Style", ["Trading", "Motivational", "Business", "Crypto", "Baby", "Dark Luxury"])
tone = st.selectbox("🔥 Tone", ["Professional", "Bold", "Aggressive", "Elegant"])

# ---------------- GENERATE BUTTON ----------------
if st.button("🚀 Generate Poster"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    # -------- SIZE --------
    if platform == "Instagram (1:1)":
        width, height = 1080, 1080
    elif platform == "YouTube (16:9)":
        width, height = 1280, 720
    else:
        width, height = 1080, 1350

    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # -------- BACKGROUND THEMES --------
    for y in range(height):

        if style == "Trading":
            color = (10, 20 + y//20, 40 + y//10)

        elif style == "Motivational":
            color = (80 + y//5, 30, 120)

        elif style == "Business":
            color = (20, 20, 20 + y//8)

        elif style == "Crypto":
            color = (25, 10 + y//15, 60 + y//6)

        elif style == "Baby":
            color = (255, 200 + y//10, 220)

        else:  # Dark Luxury
            color = (15, 15, 15 + y//12)

        draw.line([(0, y), (width, y)], fill=color)

    # -------- STYLE ELEMENTS --------
    if style == "Trading" or style == "Crypto":

        x_pos = 80
        base_line = height - 200

        for i in range(35):
            open_p = random.randint(-120, 120)
            close_p = random.randint(-120, 120)
            high = max(open_p, close_p) + random.randint(20, 50)
            low = min(open_p, close_p) - random.randint(20, 50)

            color = (0, 255, 140) if close_p > open_p else (255, 70, 70)

            draw.line((x_pos, base_line-high, x_pos, base_line-low), fill=color, width=2)

            draw.rectangle(
                [x_pos-8, base_line-max(open_p, close_p),
                 x_pos+8, base_line-min(open_p, close_p)],
                fill=color
            )
            x_pos += 28

    elif style == "Motivational":
        for i in range(50):
            draw.ellipse(
                (random.randint(0,width),
                 random.randint(0,height),
                 random.randint(0,width),
                 random.randint(0,height)),
                outline=(255,255,255)
            )

    elif style == "Business":
        for i in range(15):
            draw.rectangle(
                (random.randint(0,width),
                 random.randint(0,height),
                 random.randint(0,width),
                 random.randint(0,height)),
                outline=(0,255,255)
            )

    elif style == "Baby":
        for i in range(60):
            draw.ellipse(
                (random.randint(0,width),
                 random.randint(0,height),
                 random.randint(0,width),
                 random.randint(0,height)),
                fill=(255,255,255)
            )

    # -------- FONTS --------
    try:
        font_big = ImageFont.truetype("arial.ttf", int(width/10))
        font_small = ImageFont.truetype("arial.ttf", int(width/25))
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # -------- HOOK BASED ON TONE --------
    if tone == "Aggressive":
        hook = "DOMINATE NOW!"
    elif tone == "Bold":
        hook = "TAKE ACTION!"
    elif tone == "Elegant":
        hook = "Refined Excellence"
    else:
        hook = "Professional Growth"

    # -------- TEXT DRAW --------
    bbox = draw.textbbox((0,0), hook, font=font_big)
    text_width = bbox[2] - bbox[0]

    draw.text(
        ((width-text_width)/2, height/8),
        hook,
        font=font_big,
        fill=(255,215,0)
    )

    draw.text(
        (width/2, height/3),
        topic,
        font=font_small,
        fill=(255,255,255),
        anchor="mm"
    )

    # -------- SHOW --------
    st.image(image, use_container_width=True)

    # -------- DOWNLOAD --------
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")

    st.download_button(
        "📥 Download Poster",
        img_bytes.getvalue(),
        file_name="ultimate_poster.png",
        mime="image/png"
    )

    # -------- CONTENT --------
    st.subheader("📝 Post Description")

    description = f"""
🔥 {hook}

Discover the power of {topic}.

Smart Strategy + Consistency + Execution = Real Growth 🚀

Start today and level up.
"""

    st.write(description)

    st.subheader("📢 Hashtags")
    st.write(f"#{topic.replace(' ','')} #Growth #Success #DigitalBrand #Trending #Business #ContentCreator")
