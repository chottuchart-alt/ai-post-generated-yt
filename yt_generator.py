import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Trading Poster PRO", page_icon="📈", layout="centered")

st.title("📈 Trading Chart Style Poster Generator")

topic = st.text_input("Enter Topic (Example: ADX EA Strategy)")
platform = st.selectbox("Platform", ["Instagram (1:1)", "YouTube (16:9)", "LinkedIn (4:5)"])

if st.button("Generate Trading Poster"):

    if topic:

        # -------- SIZE --------
        if platform == "Instagram (1:1)":
            width, height = 1080, 1080
        elif platform == "YouTube (16:9)":
            width, height = 1280, 720
        else:
            width, height = 1080, 1350

        # -------- DARK BACKGROUND --------
        image = Image.new("RGB", (width, height), (8, 12, 25))
        draw = ImageDraw.Draw(image)

        # -------- DRAW GRID --------
        for x in range(0, width, 100):
            draw.line((x, 0, x, height), fill=(25, 35, 60), width=1)

        for y in range(0, height, 100):
            draw.line((0, y, width, y), fill=(25, 35, 60), width=1)

        # -------- DRAW FAKE CANDLE CHART --------
        candle_width = 20
        x_pos = 100
        base_line = height - 200

        for i in range(40):

            open_price = random.randint(-150, 150)
            close_price = random.randint(-150, 150)

            high = max(open_price, close_price) + random.randint(20, 60)
            low = min(open_price, close_price) - random.randint(20, 60)

            color = (0, 255, 120) if close_price > open_price else (255, 60, 60)

            # Wick
            draw.line(
                (x_pos, base_line - high, x_pos, base_line - low),
                fill=color,
                width=2
            )

            # Body
            draw.rectangle(
                (
                    x_pos - candle_width//2,
                    base_line - open_price,
                    x_pos + candle_width//2,
                    base_line - close_price
                ),
                fill=color
            )

            x_pos += 25

        # -------- FONTS --------
        try:
            font_big = ImageFont.truetype("arial.ttf", int(width/10))
            font_small = ImageFont.truetype("arial.ttf", int(width/20))
        except:
            font_big = ImageFont.load_default()
            font_small = ImageFont.load_default()

        hook = "PROFIT MODE ON"

        # -------- CENTER TEXT --------
        bbox = draw.textbbox((0, 0), hook, font=font_big)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        draw.text(
            ((width - text_width)/2, height/6),
            hook,
            font=font_big,
            fill=(0, 255, 120)
        )

        draw.text(
            (width/2, height/3),
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
            label="📥 Download Trading Poster",
            data=img_bytes.getvalue(),
            file_name="trading_poster.png",
            mime="image/png"
        )

        # -------- CONTENT --------
        st.subheader("Post Content")
        st.write(f"""
📈 {hook}

Master {topic} and take your trading to the next level.

Consistency + Strategy = Profit 💰

Are you ready?
""")

        st.subheader("Hashtags")
        st.write(f"#Trading #Forex #Crypto #StockMarket #{topic.replace(' ', '')}")

    else:
        st.warning("Please enter a topic.")
