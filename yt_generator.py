import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import io

# ---------------- PAGE ----------------
st.set_page_config(page_title="Smart AI Poster FREE", page_icon="🔥")
st.title("🔥 Smart Real Style Post Generator (FREE)")

topic = st.text_input("📌 Enter Topic")
platform = st.selectbox("📱 Platform", ["Instagram (1:1)", "YouTube (16:9)", "LinkedIn (4:5)"])
style = st.selectbox("🎨 Style", ["Corporate", "Dark Luxury", "Motivation", "Crypto", "Soft Baby"])

# -------- SIZE --------
if platform == "Instagram (1:1)":
    width, height = 1080, 1080
elif platform == "YouTube (16:9)":
    width, height = 1280, 720
else:
    width, height = 1080, 1350

# ---------------- GENERATE ----------------
if st.button("🚀 Generate Post"):

    if not topic:
        st.warning("Enter topic first")
        st.stop()

    # -------- BASE IMAGE --------
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # -------- REALISTIC GRADIENT BACKGROUND --------
    for y in range(height):

        if style == "Corporate":
            color = (20, 30 + y//8, 60 + y//5)

        elif style == "Dark Luxury":
            color = (10, 10, 10 + y//6)

        elif style == "Motivation":
            color = (80 + y//5, 40, 120)

        elif style == "Crypto":
            color = (15, 25 + y//6, 80 + y//4)

        else:  # Soft Baby
            color = (255, 200 + y//10, 230)

        draw.line([(0, y), (width, y)], fill=color)

    # -------- LIGHT EFFECT --------
    overlay = Image.new("RGBA", (width, height))
    overlay_draw = ImageDraw.Draw(overlay)

    for i in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(100, 300)
        overlay_draw.ellipse((x, y, x+size, y+size), fill=(255,255,255,20))

    image = Image.alpha_composite(image.convert("RGBA"), overlay)
    image = image.convert("RGB")
    image = image.filter(ImageFilter.GaussianBlur(0.5))

    draw = ImageDraw.Draw(image)

    # -------- TEXT --------
    try:
        font_big = ImageFont.truetype("arial.ttf", int(width/10))
        font_small = ImageFont.truetype("arial.ttf", int(width/25))
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    hook = "LEVEL UP YOUR GAME"

    bbox = draw.textbbox((0,0), hook, font=font_big)
    text_width = bbox[2] - bbox[0]

    # Shadow
    draw.text(((width-text_width)/2+5, height/6+5), hook, font=font_big, fill="black")

    # Main Hook
    draw.text(((width-text_width)/2, height/6), hook, font=font_big, fill="white")

    # Topic Text
    draw.text((width/2, height/2), topic.upper(), font=font_small, fill="white", anchor="mm")

    # -------- SHOW --------
    st.image(image, use_container_width=True)

    # -------- DOWNLOAD --------
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")

    st.download_button(
        "📥 Download Post",
        img_bytes.getvalue(),
        file_name="real_style_post.png",
        mime="image/png"
    )

    # -------- CONTENT --------
    st.subheader("📝 Caption")
    caption = f"""
🔥 {hook}

{topic} can transform your growth journey.

Stay consistent. Stay focused. Achieve success.
"""
    st.write(caption)

    st.subheader("📢 Hashtags")
    st.write(f"#{topic.replace(' ','')} #Growth #Success #Branding #Trending #Digital")
