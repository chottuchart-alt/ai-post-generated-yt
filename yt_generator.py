import streamlit as st
from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont
import requests
import io

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Real Image Post Generator", page_icon="🔥")
st.title("🔥 AI Real Image Post Generator")

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # <-- Add your key

# ---------------- INPUT ----------------
topic = st.text_input("📌 Enter Topic (Example: ADX Trading Strategy, Baby Care Tips)")
platform = st.selectbox("📱 Platform", ["Instagram (1:1)", "YouTube (16:9)", "LinkedIn (4:5)"])
tone = st.selectbox("🔥 Tone", ["Professional", "Cinematic", "Luxury", "Bold"])

# ---------------- SIZE ----------------
if platform == "Instagram (1:1)":
    size = "1024x1024"
elif platform == "YouTube (16:9)":
    size = "1792x1024"
else:
    size = "1024x1792"

# ---------------- GENERATE ----------------
if st.button("🚀 Generate Real Post"):

    if not topic:
        st.warning("Enter topic first")
        st.stop()

    with st.spinner("Generating real AI image..."):

        prompt = f"""
        Create a high quality realistic social media post background about {topic}.
        Style: {tone}.
        Professional photography, ultra realistic, cinematic lighting,
        social media marketing style, no text.
        """

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size
        )

        image_url = response.data[0].url
        img_response = requests.get(image_url)
        image = Image.open(io.BytesIO(img_response.content))

        # -------- TEXT OVERLAY --------
        draw = ImageDraw.Draw(image)

        try:
            font_big = ImageFont.truetype("arial.ttf", 80)
        except:
            font_big = ImageFont.load_default()

        text = topic.upper()

        bbox = draw.textbbox((0, 0), text, font=font_big)
        text_width = bbox[2] - bbox[0]

        draw.text(
            ((image.width - text_width) / 2, image.height * 0.75),
            text,
            font=font_big,
            fill="white"
        )

        # -------- SHOW --------
        st.image(image, use_container_width=True)

        # -------- DOWNLOAD --------
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")

        st.download_button(
            "📥 Download Image",
            img_bytes.getvalue(),
            file_name="ai_post.png",
            mime="image/png"
        )

        st.success("Post Generated Successfully 🔥")
