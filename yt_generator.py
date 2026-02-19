import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io

st.set_page_config(page_title="🔥 Universal Poster AI", layout="centered")
st.title("🔥 Universal Smart Marketing Poster Generator")

topic = st.text_input("📌 Enter ANY Topic")
platform = st.selectbox("📱 Platform", ["Instagram (1:1)", "YouTube (16:9)", "LinkedIn (4:5)"])

if st.button("🚀 Generate Poster"):

    if not topic:
        st.warning("Please enter topic")
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

    topic_lower = topic.lower()

    # -------- AUTO CATEGORY DETECTION --------
    if any(word in topic_lower for word in ["trade", "forex", "stock", "crypto", "bitcoin"]):
        theme = "finance"
    elif any(word in topic_lower for word in ["baby", "kids", "sleep"]):
        theme = "baby"
    elif any(word in topic_lower for word in ["motivation", "success", "mindset"]):
        theme = "motivation"
    elif any(word in topic_lower for word in ["business", "growth", "marketing"]):
        theme = "business"
    elif any(word in topic_lower for word in ["fitness", "gym", "workout"]):
        theme = "fitness"
    elif any(word in topic_lower for word in ["house", "real estate", "property"]):
        theme = "realestate"
    elif any(word in topic_lower for word in ["study", "education", "exam"]):
        theme = "education"
    else:
        theme = "default"

    # -------- BACKGROUND THEMES --------
    for y in range(height):
        if theme == "finance":
            color = (10, 30 + int(y/8), 40 + int(y/5))
        elif theme == "baby":
            color = (255, 200 - int(y/10), 230)
        elif theme == "motivation":
            color = (50 + int(y/4), 20, 0)
        elif theme == "business":
            color = (20, 20 + int(y/6), 60)
        elif theme == "fitness":
            color = (40 + int(y/5), 0, 0)
        elif theme == "realestate":
            color = (0, 40 + int(y/6), 50)
        elif theme == "education":
            color = (30, 30, 70 + int(y/6))
        else:
            color = (20, 20 + int(y/6), 60)

        draw.line([(0, y), (width, y)], fill=color)

    # -------- FONTS --------
    try:
        font_big = ImageFont.truetype("arial.ttf", int(width/7))
        font_medium = ImageFont.truetype("arial.ttf", int(width/15))
        font_small = ImageFont.truetype("arial.ttf", int(width/25))
    except:
        font_big = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # -------- HEADLINE --------
    headline = topic.upper()

    bbox = draw.textbbox((0,0), headline, font=font_big)
    text_width = bbox[2] - bbox[0]

    x = (width - text_width) / 2
    y = height / 4

    draw.text((x, y), headline, font=font_big, fill=(255,255,255))

    # -------- SUB TEXT --------
    draw.text((width/2, height/2),
              "🔥 Premium Marketing Post 🔥",
              font=font_medium,
              fill=(255,215,0),
              anchor="mm")

    # -------- CTA BUTTON --------
    btn_text = "LEARN MORE >>"
    btn_w = draw.textbbox((0,0), btn_text, font=font_medium)[2]
    btn_h = draw.textbbox((0,0), btn_text, font=font_medium)[3]

    btn_x = (width - btn_w) / 2
    btn_y = height - height/4

    draw.rectangle(
        [btn_x-40, btn_y-20, btn_x+btn_w+40, btn_y+btn_h+20],
        fill=(0, 180, 90)
    )

    draw.text((btn_x, btn_y),
              btn_text,
              font=font_medium,
              fill=(255,255,255))

    # -------- DISPLAY --------
    st.image(image, use_column_width=True)

    # -------- DOWNLOAD --------
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")

    st.download_button(
        "📥 Download Poster",
        img_bytes.getvalue(),
        file_name="universal_marketing_post.png",
        mime="image/png"
    )

    # -------- CAPTION --------
    st.subheader("📝 Caption")

    caption = f"""
🔥 {topic} Special Post!

If you're serious about {topic}, this content is for you.

Consistency + Smart Action = Success 🚀

Follow for more updates!
"""

    st.write(caption)

    # -------- HASHTAGS --------
    st.subheader("📢 Hashtags")

    hashtags = f"#Trending #{topic.replace(' ','')} #Growth #Success #Viral"

    st.write(hashtags)
