import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

# ---------------- PAGE ----------------
st.set_page_config(page_title="Trading Poster PRO", page_icon="📈", layout="centered")
st.title("🔥 Trading Poster + Content Generator PRO")

topic = st.text_input("📌 Enter Topic (Example: ADX EA Strategy)")
platform = st.selectbox("📱 Platform", ["Instagram (1:1)", "YouTube (16:9)", "LinkedIn (4:5)"])
tone = st.selectbox("🔥 Tone", ["Professional", "Bold", "Aggressive"])

if st.button("🚀 Generate Poster"):

    if topic:

        # -------- SIZE --------
        if platform == "Instagram (1:1)":
            width, height = 1080, 1080
        elif platform == "YouTube (16:9)":
            width, height = 1280, 720
        else:
            width, height = 1080, 1350

        # -------- GRADIENT BACKGROUND --------
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

        for y in range(height):
            r = 10
            g = int(20 + (y / height) * 40)
            b = int(40 + (y / height) * 80)
            draw.line([(0, y), (width, y)], fill=(r, g, b))

        # -------- GRID --------
        for x in range(0, width, 120):
            draw.line((x, 0, x, height), fill=(30, 50, 80))
        for y in range(0, height, 120):
            draw.line((0, y, width, y), fill=(30, 50, 80))

        # -------- CANDLE CHART --------
        candle_width = 18
        x_pos = 100
        base_line = height - 250

        for i in range(35):

            open_p = random.randint(-120, 120)
            close_p = random.randint(-120, 120)

            high = max(open_p, close_p) + random.randint(20, 50)
            low = min(open_p, close_p) - random.randint(20, 50)

            color = (0, 255, 140) if close_p > open_p else (255, 70, 70)

            top = base_line - max(open_p, close_p)
            bottom = base_line - min(open_p, close_p)

            # Wick
            draw.line(
                (x_pos, base_line - high, x_pos, base_line - low),
                fill=color,
                width=2
            )

            # Body (fixed coordinates to avoid error)
            draw.rectangle(
                [x_pos - candle_width//2, top,
                 x_pos + candle_width//2, bottom],
                fill=color
            )

            x_pos += 28

        # -------- TEXT --------
        try:
            font_big = ImageFont.truetype("arial.ttf", int(width/9))
            font_small = ImageFont.truetype("arial.ttf", int(width/22))
        except:
            font_big = ImageFont.load_default()
            font_small = ImageFont.load_default()

        hook = "PROFIT MODE"

        bbox = draw.textbbox((0, 0), hook, font=font_big)
        text_width = bbox[2] - bbox[0]

        draw.text(
            ((width - text_width)/2, height/8),
            hook,
            font=font_big,
            fill=(0, 255, 150)
        )

        draw.text(
            (width/2, height/4),
            topic,
            font=font_small,
            fill=(255, 255, 255),
            anchor="mm"
        )

        # -------- SHOW --------
        st.image(image, use_column_width=True)

        # -------- DOWNLOAD --------
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        st.download_button(
            "📥 Download Poster",
            img_bytes.getvalue(),
            file_name="trading_poster.png",
            mime="image/png"
        )

        # -------- CONTENT --------
        st.subheader("📝 Post Description")

        description = f"""
🔥 {hook} Activated!

Learn {topic} and improve your trading performance.

Consistency + Risk Management + Strategy = Long Term Profit 💰

Start your journey today.
"""

        st.write(description)

        st.subheader("📢 Hashtags")
        st.write(f"#Trading #Forex #StockMarket #Crypto #{topic.replace(' ','')} #TraderLife #Investment")

    else:
        st.warning("Please enter a topic.")
