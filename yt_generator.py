import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import io
import datetime

st.set_page_config(page_title="🔥 AutoBuy EA Thumbnail Generator", layout="centered")

st.title("🔥 YouTube Profit Thumbnail Generator")

topic = st.text_input("📌 Enter EA Name", value="AUTOBUY EA")
profit = st.text_input("💰 Enter Profit Amount", value="+$57,489")
date_text = st.text_input("📅 Enter Date Range", value="JAN - FEB 2026")

width, height = 1280, 720


# -------------------------------
# BACKGROUND GENERATOR
# -------------------------------
def generate_background(width, height):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    c1 = (10, 20, 40)
    c2 = (0, 150, 90)

    for i in range(height):
        r = int(c1[0] + (c2[0]-c1[0])*(i/height))
        g = int(c1[1] + (c2[1]-c1[1])*(i/height))
        b = int(c1[2] + (c2[2]-c1[2])*(i/height))
        draw.line([(0, i), (width, i)], fill=(r,g,b))

    return img


# -------------------------------
# GENERATE BUTTON
# -------------------------------
if st.button("🚀 Generate Thumbnail"):

    img = generate_background(width, height)
    draw = ImageDraw.Draw(img)

    # Fonts
    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", 120)
        font_mid = ImageFont.truetype("DejaVuSans-Bold.ttf", 70)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 40)
    except:
        font_big = ImageFont.load_default()
        font_mid = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # -------------------------------
    # TITLE
    # -------------------------------
    title_w = draw.textlength(topic, font=font_big)
    draw.text(((width-title_w)/2, 120), topic, font=font_big, fill="yellow")

    # DATE
    date_w = draw.textlength(date_text, font=font_mid)
    draw.text(((width-date_w)/2, 260), date_text, font=font_mid, fill="white")

    # PROFIT RESULTS TEXT
    pr_text = "PROFIT RESULTS"
    pr_w = draw.textlength(pr_text, font=font_mid)
    draw.text(((width-pr_w)/2, 360), pr_text, font=font_mid, fill="lime")

    # PROFIT BOX
    profit_w = draw.textlength(profit, font=font_big)

    box_x1 = (width-profit_w)/2 - 60
    box_y1 = 470
    box_x2 = (width+profit_w)/2 + 60
    box_y2 = 600

    draw.rounded_rectangle(
        [box_x1, box_y1, box_x2, box_y2],
        radius=30,
        fill=(0, 0, 0)
    )

    draw.text(
        ((width-profit_w)/2, 490),
        profit,
        font=font_big,
        fill="lime"
    )

    # DISCLAIMER
    disclaimer = "⚠ Past Results ≠ Future Profits"
    disc_w = draw.textlength(disclaimer, font=font_small)

    draw.text(
        ((width-disc_w)/2, 650),
        disclaimer,
        font=font_small,
        fill="white"
    )

    # BORDER
    draw.rectangle(
        [(20,20),(width-20,height-20)],
        outline="white",
        width=5
    )

    st.image(img, use_column_width=True)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")

    st.download_button(
        "⬇ Download Thumbnail",
        img_bytes.getvalue(),
        file_name="autobuy_ea_thumbnail.png",
        mime="image/png"
    )
