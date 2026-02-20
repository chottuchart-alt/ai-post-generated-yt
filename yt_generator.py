import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import io
import datetime

st.set_page_config(page_title="🔥 Ultimate Viral Poster AI", layout="centered")

st.title("🔥 Ultimate AI Viral Poster Generator")

topic = st.text_input("📌 Enter Topic")
platform = st.selectbox("📱 Platform Size", ["YouTube (1280x720)", "Instagram (1080x1080)"])

if "YouTube" in platform:
    width, height = 1280, 720
else:
    width, height = 1080, 1080


# -------------------------------
# SMART HOOK GENERATOR
# -------------------------------
def generate_hook(topic):
    hooks = [
        "STOP SCROLLING",
        "DON'T MISS",
        "MASTER",
        "SECRETS OF",
        "BREAKTHROUGH IN",
        "HOW TO WIN IN",
        "ULTIMATE GUIDE TO",
        "THIS WILL CHANGE"
    ]
    return random.choice(hooks) + " " + topic.upper()


# -------------------------------
# SMART CAPTION
# -------------------------------
def smart_caption(topic):
    hooks = [
        "🔥 This will change your game in",
        "🚀 Stop scrolling if you care about",
        "💎 Master the art of",
        "⚡ Unlock the secrets of"
    ]
    return f"{random.choice(hooks)} {topic}!"


def smart_description(topic):
    return f"""
If you truly want success in {topic},
you must focus on consistency and smart execution.

Most people talk.
Winners take action.

Start today.
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


# -------------------------------
# MULTI LINE CENTER TEXT
# -------------------------------
def draw_multiline_center(draw, text, font, img_width, y_start, max_width):
    words = text.split()
    lines = []
    while words:
        line = ''
        while words:
            test_line = line + words[0] + ' '
            w = draw.textlength(test_line, font=font)
            if w <= max_width:
                line = test_line
                words.pop(0)
            else:
                break
        lines.append(line.strip())

    y = y_start
    for line in lines:
        w = draw.textlength(line, font=font)
        x = (img_width - w) / 2
        draw.text((x, y), line, font=font, fill="white")
        y += font.size + 20

    return y


# -------------------------------
# BACKGROUND GENERATOR
# -------------------------------
def generate_background(width, height):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    c1 = (random.randint(0,120), random.randint(0,120), random.randint(0,120))
    c2 = (random.randint(150,255), random.randint(150,255), random.randint(150,255))

    for i in range(height):
        r = int(c1[0] + (c2[0]-c1[0])*(i/height))
        g = int(c1[1] + (c2[1]-c1[1])*(i/height))
        b = int(c1[2] + (c2[2]-c1[2])*(i/height))
        draw.line([(0, i), (width, i)], fill=(r,g,b))

    # Soft light circles (depth effect)
    for _ in range(20):
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

    img = img.filter(ImageFilter.GaussianBlur(2))
    return img


# -------------------------------
# GENERATE BUTTON
# -------------------------------
if st.button("🚀 Generate Viral Poster"):

    if not topic:
        st.warning("Enter topic")
        st.stop()

    img = generate_background(width, height)
    draw = ImageDraw.Draw(img)

    hook_text = generate_hook(topic)

    safe_margin = 100
    max_width = width - safe_margin * 2

    # AUTO FONT RESIZE
    font_size = int(width / 9)
    while font_size > 40:
        try:
            font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
        except:
            font_big = ImageFont.load_default()

        if draw.textlength(hook_text, font=font_big) <= max_width:
            break
        font_size -= 5

    # GLOW EFFECT
    for blur in range(20, 0, -4):
        glow = Image.new("RGB", (width, height))
        glow_draw = ImageDraw.Draw(glow)
        glow_draw.text((safe_margin, height/3), hook_text, font=font_big, fill="white")
        glow = glow.filter(ImageFilter.GaussianBlur(blur))
        img = Image.blend(img, glow, 0.12)

    draw = ImageDraw.Draw(img)

    y_end = draw_multiline_center(
        draw,
        hook_text,
        font_big,
        width,
        height/3,
        max_width
    )

    # CTA BUTTON STYLE
    font_small = ImageFont.truetype("DejaVuSans.ttf", int(width/25))
    cta_text = "START TODAY 🚀"

    text_w = draw.textlength(cta_text, font=font_small)
    btn_x1 = (width - text_w)/2 - 40
    btn_y1 = y_end + 40
    btn_x2 = (width + text_w)/2 + 40
    btn_y2 = btn_y1 + 70

    draw.rounded_rectangle(
        [btn_x1, btn_y1, btn_x2, btn_y2],
        radius=20,
        fill=(0,0,0)
    )

    draw.text(
        ((width-text_w)/2, btn_y1+20),
        cta_text,
        font=font_small,
        fill="white"
    )

    # BORDER FRAME
    draw.rectangle(
        [(25,25),(width-25,height-25)],
        outline=(255,255,255),
        width=5
    )

    st.image(img, use_column_width=True)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")

    st.download_button(
        "⬇ Download Poster",
        img_bytes.getvalue(),
        file_name="viral_poster.png",
        mime="image/png"
    )

    # CONTENT
    caption = smart_caption(topic)
    description = smart_description(topic)
    hashtags = smart_hashtags(topic)

    st.subheader("📢 Caption")
    st.write(caption)

    st.subheader("📝 Description")
    st.write(description)

    st.subheader("🏷 Hashtags")
    st.code(hashtags)
