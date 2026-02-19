import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import io
import random
import datetime

st.set_page_config(page_title="🔥 Ultimate Poster Generator PRO MAX", layout="centered")

st.title("🔥 Ultimate Poster + Content Generator PRO MAX")

topic = st.text_input("📌 Enter Topic")
platform = st.selectbox("📱 Platform Size", ["YouTube (1280x720)", "Instagram (1080x1080)"])
template = st.selectbox("🎨 Choose Template", [
    "Luxury Gold",
    "Crypto Coins",
    "Forex Candles",
    "Baby Soft",
    "Auto Daily Generator"
])

# -------- SIZE --------
if "YouTube" in platform:
    width, height = 1280, 720
else:
    width, height = 1080, 1080

# -------- AUTO DAILY --------
if template == "Auto Daily Generator":
    today = datetime.datetime.now().strftime("%A")
    daily_topics = [
        "Motivation Boost",
        "Crypto Profits",
        "Trading Strategy",
        "Business Growth",
        "Baby Care Tips"
    ]
    topic = random.choice(daily_topics) + " - " + today

if st.button("🚀 Generate PRO Poster"):

    if not topic:
        st.warning("Enter topic")
        st.stop()

    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # =====================================================
    # TEMPLATE: LUXURY GOLD
    # =====================================================
    if template == "Luxury Gold":

        for i in range(height):
            r = int(10 + (120 * (i/height)))
            g = int(20 + (80 * (i/height)))
            b = int(5)
            draw.line([(0, i), (width, i)], fill=(r, g, b))

        for _ in range(500):
            x = np.random.randint(0, width)
            y = np.random.randint(0, height)
            draw.ellipse((x, y, x+3, y+3), fill=(255,215,0))

        text_color = (255,215,0)

    # =====================================================
    # TEMPLATE: CRYPTO
    # =====================================================
    elif template == "Crypto Coins":

        img.paste((10, 20, 40), [0,0,width,height])

        for _ in range(10):
            x = random.randint(100, width-200)
            y = random.randint(100, height-200)
            draw.ellipse((x, y, x+120, y+120), fill=(255, 200, 0), outline="black", width=5)
            draw.text((x+40, y+35), "₿", fill="black")

        text_color = (0,255,180)

    # =====================================================
    # TEMPLATE: FOREX
    # =====================================================
    elif template == "Forex Candles":

        img.paste((5, 25, 50), [0,0,width,height])

        candle_width = 20
        gap = 15
        x = 50

        for _ in range(30):
            open_price = random.randint(200, height-200)
            close_price = random.randint(200, height-200)
            high = min(open_price, close_price) - random.randint(20,60)
            low = max(open_price, close_price) + random.randint(20,60)

            color = (0,255,120) if close_price < open_price else (255,60,60)

            draw.line((x+10, high, x+10, low), fill=color, width=3)
            draw.rectangle((x, open_price, x+candle_width, close_price), fill=color)

            x += candle_width + gap

        text_color = (0,255,180)

    # =====================================================
    # TEMPLATE: BABY
    # =====================================================
    elif template == "Baby Soft":

        for i in range(height):
            r = 255
            g = int(200 + (50 * (i/height)))
            b = int(220 + (30 * (i/height)))
            draw.line([(0, i), (width, i)], fill=(r, g, b))

        draw.ellipse((width/4, height/3, width/1.5, height/1.2), fill=(255,240,250))

        text_color = (255,105,180)

    # =====================================================
    # TEXT STYLING (3D GOLD EFFECT)
    # =====================================================
    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", int(width/10))
    except:
        font_big = ImageFont.load_default()

    text = topic.upper()
    bbox = draw.textbbox((0, 0), text, font=font_big)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = height / 3

    # 3D shadow layers
    for offset in range(8,0,-1):
        draw.text((x+offset, y+offset), text, font=font_big, fill=(0,0,0))

    draw.text((x, y), text, font=font_big, fill=text_color)

    # =====================================================
    # SHOW IMAGE
    # =====================================================
    st.image(img, use_column_width=True)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")

    st.download_button("⬇ Download Poster",
                       img_bytes.getvalue(),
                       file_name="poster.png",
                       mime="image/png")

    # =====================================================
    # AUTO CONTENT GENERATOR
    # =====================================================

    caption = f"🔥 Master {topic} today and level up your game!"
    description = f"""
If you want better results in {topic},
you must understand the fundamentals and apply them consistently.

This post gives powerful insight to help you grow faster.
Start today. Stay consistent. Win big.
"""
    hashtags = f"""
#{topic.lower().replace(" ","")}
#success
#growth
#money
#motivation
#business
#crypto
#trading
#viral
#reels
#contentcreator
"""

    st.subheader("📢 Caption")
    st.write(caption)

    st.subheader("📝 Description")
    st.write(description)

    st.subheader("🏷 Hashtags")
    st.code(hashtags)
