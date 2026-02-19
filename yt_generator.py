import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

st.set_page_config(page_title="AI Smart Poster PRO", layout="centered")
st.title("🔥 AI Smart Poster + Content Generator PRO")

topic = st.text_input("📌 Enter Any Topic (Baby, Trading, Motivation, Business)")
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

        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

        topic_lower = topic.lower()

        # -------- BACKGROUND AUTO SWITCH --------
        if "trade" in topic_lower or "forex" in topic_lower or "stock" in topic_lower:
            # Trading background
            for y in range(height):
                draw.line([(0,y),(width,y)], fill=(10,20+int(y/10),40+int(y/5)))

            for x in range(0, width, 100):
                draw.line((x, 0, x, height), fill=(30, 60, 90))
            for y in range(0, height, 100):
                draw.line((0, y, width, y), fill=(30, 60, 90))

        elif "baby" in topic_lower or "kids" in topic_lower:
            # Soft baby background
            for y in range(height):
                draw.line([(0,y),(width,y)], fill=(255,200-int(y/10),220))

        elif "motivation" in topic_lower or "success" in topic_lower:
            # Gold motivation theme
            for y in range(height):
                draw.line([(0,y),(width,y)], fill=(40+int(y/5),20,0))

        else:
            # Default modern gradient
            for y in range(height):
                draw.line([(0,y),(width,y)], fill=(20,20+int(y/6),60))

        # -------- BIG TEXT --------
        try:
            font_big = ImageFont.truetype("arial.ttf", int(width/7))
            font_small = ImageFont.truetype("arial.ttf", int(width/20))
        except:
            font_big = ImageFont.load_default()
            font_small = ImageFont.load_default()

        hook = topic.upper()

        bbox = draw.textbbox((0,0), hook, font=font_big)
        text_width = bbox[2] - bbox[0]

        draw.text(
            ((width - text_width)/2, height/5),
            hook,
            font=font_big,
            fill=(255,255,255)
        )

        draw.text(
            (width/2, height/2),
            "🔥 Powerful Content Inside 🔥",
            font=font_small,
            fill=(255,255,0),
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
            file_name="smart_poster.png",
            mime="image/png"
        )

        # -------- CONTENT --------
        st.subheader("📝 Description")

        description = f"""
🔥 {topic} Special Post!

If you're interested in {topic}, this content will help you grow.

Consistency + Smart Action = Success 🚀

Follow for more powerful updates!
"""
        st.write(description)

        st.subheader("📢 Hashtags")

        base_tags = "#Viral #Trending #Growth #Success"

        st.write(f"{base_tags} #{topic.replace(' ','')} #ContentCreator")

    else:
        st.warning("Please enter topic.")
