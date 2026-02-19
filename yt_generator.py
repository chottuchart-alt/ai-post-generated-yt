import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import io

st.set_page_config(page_title="Cinematic Poster Generator", layout="centered")

st.title("🔥 Ultimate Poster Generator PRO")

topic = st.text_input("Enter Topic")

platform = st.selectbox("Platform Size", ["YouTube (1280x720)", "Instagram (1080x1080)"])

if st.button("🚀 Generate Cinematic Poster"):

    if not topic:
        st.warning("Enter topic")
        st.stop()

    # -------- SIZE --------
    if "YouTube" in platform:
        width, height = 1280, 720
    else:
        width, height = 1080, 1080

    # -------- GOLD GRADIENT BACKGROUND --------
    bg = Image.new("RGB", (width, height), "#0f2027")
    draw = ImageDraw.Draw(bg)

    for i in range(height):
        r = int(15 + (200 * (i/height)))
        g = int(32 + (150 * (i/height)))
        b = int(39 + (50 * (i/height)))
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    # Glow particles effect
    for _ in range(300):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        draw.ellipse((x, y, x+3, y+3), fill=(255,215,0))

    bg = bg.filter(ImageFilter.GaussianBlur(0.5))
    draw = ImageDraw.Draw(bg)

    # -------- FONT --------
    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", int(width/10))
        font_small = ImageFont.truetype("DejaVuSans-Bold.ttf", int(width/25))
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    text = topic.upper()

    bbox = draw.textbbox((0, 0), text, font=font_big)
    text_width = bbox[2] - bbox[0]

    x = (width - text_width) / 2
    y = height / 3

    # Shadow
    draw.text((x+6, y+6), text, font=font_big, fill=(0,0,0))

    # Main text
    draw.text(
        (x, y),
        text,
        font=font_big,
        fill=(255,215,0),
        stroke_width=4,
        stroke_fill=(0,0,0)
    )

    # Sub text
    draw.text(
        (width/2, height*0.65),
        "🔥 Powerful Content Inside 🔥",
        font=font_small,
        fill=(255,255,255),
        anchor="mm"
    )

    # -------- BUTTON STYLE BOX --------
    btn_w, btn_h = 400, 80
    btn_x = (width - btn_w) // 2
    btn_y = int(height * 0.8)

    draw.rounded_rectangle(
        (btn_x, btn_y, btn_x+btn_w, btn_y+btn_h),
        radius=20,
        fill=(34,197,94)
    )

    draw.text(
        (width/2, btn_y+btn_h/2),
        "🚀 GENERATE NOW",
        font=font_small,
        fill="white",
        anchor="mm"
    )

    # -------- SHOW --------
    st.image(bg, use_column_width=True)

    # -------- DOWNLOAD --------
    img_bytes = io.BytesIO()
    bg.save(img_bytes, format="PNG")
    st.download_button(
        label="⬇ Download Poster",
        data=img_bytes.getvalue(),
        file_name="poster.png",
        mime="image/png"
    )
