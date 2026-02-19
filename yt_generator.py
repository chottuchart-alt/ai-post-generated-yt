import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io

st.set_page_config(page_title="🔥 Marketing Poster PRO", layout="centered")
st.title("🔥 Ultimate Marketing Poster Generator PRO")

topic = st.text_input("📌 Enter Topic (Trading, Crypto, Baby, Motivation)")
platform = st.selectbox("📱 Platform", ["Instagram (1:1)", "YouTube (16:9)", "LinkedIn (4:5)"])
style = st.selectbox("🎨 Style", ["Money / Forex", "Luxury Gold", "Soft Baby", "Dark Business"])

if st.button("🚀 Generate Poster"):

    if topic:

        # -------- SIZE --------
        if platform == "Instagram (1:1)":
            width, height = 1080, 1080
        elif platform == "YouTube (16:9)":
            width, height = 1280, 720
        else:
            width, height = 1080, 1350

        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

        # -------- PREMIUM GRADIENT BACKGROUND --------
        for y in range(height):
            if style == "Money / Forex":
                color = (10, 30 + int(y/8), 40 + int(y/5))
            elif style == "Luxury Gold":
                color = (40 + int(y/4), 25 + int(y/6), 0)
            elif style == "Soft Baby":
                color = (255, 200 - int(y/10), 220)
            else:
                color = (20, 20 + int(y/6), 60)
            draw.line([(0, y), (width, y)], fill=color)

        # -------- FONTS --------
        try:
            font_big = ImageFont.truetype("arial.ttf", int(width/6))
            font_medium = ImageFont.truetype("arial.ttf", int(width/15))
            font_small = ImageFont.truetype("arial.ttf", int(width/25))
        except:
            font_big = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()

        headline = topic.upper()

        # -------- GLOW EFFECT --------
        glow_layer = Image.new("RGB", (width, height), (0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_layer)

        bbox = glow_draw.textbbox((0, 0), headline, font=font_big)
        text_width = bbox[2] - bbox[0]

        text_x = (width - text_width) / 2
        text_y = height / 4

        glow_draw.text((text_x, text_y), headline, font=font_big, fill=(255, 215, 0))
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))

        image = Image.blend(image, glow_layer, alpha=0.4)
        draw = ImageDraw.Draw(image)

        draw.text((text_x, text_y), headline, font=font_big, fill=(255, 255, 255))

        # -------- SUBTITLE --------
        subtitle = "🔥 Premium Marketing Content 🔥"
        draw.text((width/2, height/2),
                  subtitle,
                  font=font_medium,
                  fill=(255, 255, 0),
                  anchor="mm")

        # -------- PRO BADGE --------
        badge_text = "PRO"
        badge_w, badge_h = draw.textbbox((0,0), badge_text, font=font_small)[2:]
        badge_x = width - badge_w - 40
        badge_y = 40

        draw.rectangle(
            [badge_x-20, badge_y-10, badge_x+badge_w+20, badge_y+badge_h+10],
            fill=(0, 0, 0)
        )

        draw.text((badge_x, badge_y),
                  badge_text,
                  font=font_small,
                  fill=(255, 215, 0))

        # -------- CTA BUTTON --------
        button_text = "BUY NOW >>"
        btn_w, btn_h = draw.textbbox((0,0), button_text, font=font_medium)[2:]
        btn_x = (width - btn_w) / 2
        btn_y = height - height/4

        draw.rectangle(
            [btn_x-40, btn_y-20, btn_x+btn_w+40, btn_y+btn_h+20],
            fill=(40, 180, 75)
        )

        draw.text((btn_x, btn_y),
                  button_text,
                  font=font_medium,
                  fill=(255, 255, 255))

        # -------- SHOW --------
        st.image(image, use_column_width=True)

        # -------- DOWNLOAD --------
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")

        st.download_button(
            "📥 Download Poster",
            img_bytes.getvalue(),
            file_name="marketing_poster_pro.png",
            mime="image/png"
        )

        # -------- DESCRIPTION --------
        st.subheader("📝 Caption")

        caption = f"""
🔥 {topic} Special Offer!

Level up your {topic} game with powerful strategies.

Consistency + Smart Action = Growth 🚀

#Trending #{topic.replace(" ","")} #Success
"""
        st.write(caption)

    else:
        st.warning("Please enter topic.")
