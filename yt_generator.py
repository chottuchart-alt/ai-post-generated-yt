import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import random
import io
import datetime

st.set_page_config(page_title="🔥 Ultimate Poster AI Generator", layout="centered")

st.title("🔥 Ultimate AI Poster + Content Generator")

topic = st.text_input("📌 Enter Topic")
platform = st.selectbox("📱 Platform Size", ["YouTube (1280x720)", "Instagram (1080x1080)"])

if "YouTube" in platform:
    width, height = 1280, 720
else:
    width, height = 1080, 1080


def generate_human_style_background(width, height):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Random premium gradient
    c1 = (random.randint(0,150), random.randint(0,150), random.randint(0,150))
    c2 = (random.randint(100,255), random.randint(100,255), random.randint(100,255))

    for i in range(height):
        r = int(c1[0] + (c2[0]-c1[0])*(i/height))
        g = int(c1[1] + (c2[1]-c1[1])*(i/height))
        b = int(c1[2] + (c2[2]-c1[2])*(i/height))
        draw.line([(0, i), (width, i)], fill=(r,g,b))

    # Soft lighting circles (human photo feel)
    for _ in range(25):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(200, 500)

        overlay = Image.new("RGBA", (width, height))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse(
            (x, y, x+size, y+size),
            fill=(255,255,255,30)
        )

        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    # Slight blur for depth
    img = img.filter(ImageFilter.GaussianBlur(2))

    return img


def smart_caption(topic):
    hooks = [
        "🔥 This will change your game in",
        "🚀 Stop scrolling if you care about",
        "💎 Master the art of",
        "⚡ Unlock the secrets of",
        "📈 If you’re serious about"
    ]
    return f"{random.choice(hooks)} {topic}!"


def smart_description(topic):
    return f"""
If you truly want success in {topic},
you must focus on consistency, strategy, and smart execution.

Most people talk.
Winners take action.

Start today.
Improve daily.
Dominate {topic}.
"""


def smart_hashtags(topic):
    base = topic.lower().replace(" ", "")
    tags = [
        base,
        "success",
        "growth",
        "mindset",
        "money",
        "entrepreneur",
        "viral",
        "contentcreator",
        "motivation",
        "business",
        "reels"
    ]
    return "\n".join(["#" + t for t in tags])


if st.button("🚀 Generate Ultra Poster"):

    if not topic:
        st.warning("Enter topic")
        st.stop()

    img = generate_human_style_background(width, height)
    draw = ImageDraw.Draw(img)

    # FONT
    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", int(width/9))
        font_small = ImageFont.truetype("DejaVuSans.ttf", int(width/25))
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    text = topic.upper()

    bbox = draw.textbbox((0,0), text, font=font_big)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = height / 3

    # Glow effect
    for blur in range(20, 0, -4):
        glow = Image.new("RGB", (width, height))
        glow_draw = ImageDraw.Draw(glow)
        glow_draw.text((x, y), text, font=font_big, fill=(255,255,255))
        glow = glow.filter(ImageFilter.GaussianBlur(blur))
        img = Image.blend(img, glow, 0.12)

    # Main text
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, font=font_big, fill=(255,255,255))

    # Subtitle
    subtitle = "LEVEL UP YOUR LIFE"
    sub_bbox = draw.textbbox((0,0), subtitle, font=font_small)
    sub_width = sub_bbox[2] - sub_bbox[0]

    draw.text(
        ((width-sub_width)/2, y+150),
        subtitle,
        font=font_small,
        fill=(255,255,255)
    )

    # Premium border
    draw.rectangle(
        [(25,25),(width-25,height-25)],
        outline=(255,255,255),
        width=5
    )

    st.image(img, use_column_width=True)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")

    st.download_button("⬇ Download Poster",
                       img_bytes.getvalue(),
                       file_name="ultimate_poster.png",
                       mime="image/png")

    # Content
    caption = smart_caption(topic)
    description = smart_description(topic)
    hashtags = smart_hashtags(topic)

    st.subheader("📢 Caption")
    st.write(caption)

    st.subheader("📝 Description")
    st.write(description)

    st.subheader("🏷 Hashtags")
    st.code(hashtags)
