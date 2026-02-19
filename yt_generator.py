import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# ---------------- PAGE ----------------
st.set_page_config(page_title="Marketing Poster PRO", page_icon="🔥")
st.title("🔥 Big Text Marketing Poster Generator")

topic = st.text_input("📌 Main Product Name (Example: GOLD TRADING EA)")
price = st.text_input("💰 Price (Example: $250)")
platform = st.selectbox("📱 Platform", ["Instagram (1:1)", "YouTube (16:9)"])

# -------- SIZE --------
if platform == "Instagram (1:1)":
    width, height = 1080, 1080
else:
    width, height = 1280, 720

if st.button("🚀 Generate Poster"):

    if not topic:
        st.warning("Enter product name")
        st.stop()

    # -------- BACKGROUND --------
    image = Image.new("RGB", (width, height), (5, 25, 20))
    draw = ImageDraw.Draw(image)

    # Gradient
    for y in range(height):
        color = (5, 40 + y//10, 30 + y//8)
        draw.line([(0, y), (width, y)], fill=color)

    # -------- FONTS --------
    try:
        font_big = ImageFont.truetype("arial.ttf", int(width/7))
        font_medium = ImageFont.truetype("arial.ttf", int(width/15))
        font_small = ImageFont.truetype("arial.ttf", int(width/22))
    except:
        font_big = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # -------- BIG TITLE --------
    title_text = topic.upper()

    bbox = draw.textbbox((0,0), title_text, font=font_big)
    text_width = bbox[2] - bbox[0]

    draw.text(
        ((width-text_width)/2, height/5),
        title_text,
        font=font_big,
        fill=(255,215,0)
    )

    # -------- PRICE BADGE --------
    if price:
        badge_text = f"FOR SALE {price}"
        badge_width = width * 0.6
        badge_height = 90
        badge_x = (width - badge_width)/2
        badge_y = height/2.3

        draw.rectangle(
            [badge_x, badge_y, badge_x+badge_width, badge_y+badge_height],
            fill=(255, 200, 0)
        )

        draw.text(
            (width/2, badge_y+badge_height/2),
            badge_text,
            font=font_medium,
            fill="black",
            anchor="mm"
        )

    # -------- BULLET POINTS --------
    points = [
        "✔ Automated Trading System",
        "✔ MT5 Compatible",
        "✔ Simple & Profitable"
    ]

    y_start = height/1.8
    for p in points:
        draw.text((width/6, y_start), p, font=font_small, fill="white")
        y_start += 60

    # -------- BUY NOW BUTTON --------
    button_width = width * 0.5
    button_height = 100
    btn_x = (width - button_width)/2
    btn_y = height - 180

    draw.rectangle(
        [btn_x, btn_y, btn_x+button_width, btn_y+button_height],
        fill=(0, 180, 0)
    )

    draw.text(
        (width/2, btn_y+button_height/2),
        "BUY NOW >>",
        font=font_medium,
        fill="white",
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
        file_name="marketing_poster.png",
        mime="image/png"
    )
