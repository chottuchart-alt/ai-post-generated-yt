import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import random
import math

st.set_page_config(page_title="🔥 PRO MAX Thumbnail Generator", layout="centered")

st.title("🔥 YouTube Profit Thumbnail PRO MAX")

topic = st.text_input("📌 Enter EA Name", value="AUTOBUY EA")
profit = st.text_input("💰 Enter Profit Amount", value="+$57,489")
date_text = st.text_input("📅 Enter Date Range", value="JAN - FEB 2026")

width, height = 1280, 720
safe_margin = 120
max_width = width - (safe_margin * 2)


# -------------------------------
# MULTI LINE TEXT
# -------------------------------
def draw_multiline_center(draw, text, font, y_start):
    words = text.split()
    lines = []
    line = ""

    for word in words:
        test = line + word + " "
        if draw.textlength(test, font=font) <= max_width:
            line = test
        else:
            lines.append(line.strip())
            line = word + " "
    lines.append(line.strip())

    y = y_start
    for line in lines:
        w = draw.textlength(line, font=font)
        x = (width - w) / 2
        draw.text((x, y), line, font=font, fill="white")
        y += font.size + 20
    return y


# -------------------------------
# GRADIENT TEXT
# -------------------------------
def draw_gradient_text(img, position, text, font, color1, color2):
    txt = Image.new("RGBA", img.size, (255,255,255,0))
    d = ImageDraw.Draw(txt)

    x, y = position
    w = d.textlength(text, font=font)
    h = font.size

    for i in range(h):
        ratio = i / h
        r = int(color1[0] + (color2[0]-color1[0]) * ratio)
        g = int(color1[1] + (color2[1]-color1[1]) * ratio)
        b = int(color1[2] + (color2[2]-color1[2]) * ratio)
        d.text((x, y+i), text, font=font, fill=(r,g,b,255))

    img.alpha_composite(txt)


# -------------------------------
# GLOW EFFECT
# -------------------------------
def draw_glow(draw, img, text, font, position):
    glow_layer = Image.new("RGBA", img.size, (0,0,0,0))
    glow_draw = ImageDraw.Draw(glow_layer)
    glow_draw.text(position, text, font=font, fill="white")
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(15))
    img.alpha_composite(glow_layer)


# -------------------------------
# BACKGROUND + CHART
# -------------------------------
def generate_background():
    img = Image.new("RGB", (width, height), (10,20,40))
    draw = ImageDraw.Draw(img)

    # Chart lines
    for i in range(30):
        x1 = random.randint(0,width)
        y1 = random.randint(height//2,height)
        x2 = x1 + random.randint(50,200)
        y2 = y1 - random.randint(50,200)
        draw.line((x1,y1,x2,y2), fill=(0,255,100), width=3)

    # Up arrow
    draw.line((100,600,500,300), fill="red", width=12)
    draw.polygon([(500,300),(470,330),(530,330)], fill="red")

    return img.convert("RGBA")


# -------------------------------
# ROBOT DRAW
# -------------------------------
def draw_robot(draw):
    draw.ellipse((100,150,300,350), fill=(200,200,220))
    draw.rectangle((150,350,250,550), fill=(180,180,200))
    draw.ellipse((170,200,230,260), fill="cyan")
    draw.ellipse((240,200,300,260), fill="cyan")


# -------------------------------
# GENERATE BUTTON
# -------------------------------
if st.button("🚀 Generate PRO Thumbnail"):

    img = generate_background()
    draw = ImageDraw.Draw(img)

    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", 120)
        font_mid = ImageFont.truetype("DejaVuSans-Bold.ttf", 70)
        font_profit = ImageFont.truetype("DejaVuSans-Bold.ttf", 110)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 35)
    except:
        font_big = ImageFont.load_default()
        font_mid = ImageFont.load_default()
        font_profit = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # ROBOT
    draw_robot(draw)

    # TITLE with glow + gradient
    title_w = draw.textlength(topic, font=font_big)
    title_x = (width-title_w)/2
    draw_glow(draw, img, topic, font_big, (title_x,100))
    draw_gradient_text(img, (title_x,100), topic, font_big, (255,200,0), (255,0,0))

    # DATE
    date_w = draw.textlength(date_text, font=font_mid)
    draw.text(((width-date_w)/2, 250), date_text, font=font_mid, fill="white")

    # PROFIT TEXT
    pr = "PROFIT RESULTS"
    pr_w = draw.textlength(pr, font=font_mid)
    draw.text(((width-pr_w)/2, 340), pr, font=font_mid, fill="lime")

    # PROFIT BOX
    profit_w = draw.textlength(profit, font=font_profit)

    box_x1 = (width-profit_w)/2 - 60
    box_y1 = 430
    box_x2 = (width+profit_w)/2 + 60
    box_y2 = 580

    draw.rounded_rectangle(
        [box_x1, box_y1, box_x2, box_y2],
        radius=30,
        fill=(0,0,0)
    )

    draw_glow(draw, img, profit, font_profit, ((width-profit_w)/2,450))
    draw.text(((width-profit_w)/2,450), profit, font=font_profit, fill="lime")

    # DISCLAIMER
    disclaimer = "⚠ Past Results ≠ Future Profits"
    disc_w = draw.textlength(disclaimer, font=font_small)
    draw.text(((width-disc_w)/2,650), disclaimer, font=font_small, fill="white")

    st.image(img, use_column_width=True)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")

    st.download_button(
        "⬇ Download Thumbnail",
        img_bytes.getvalue(),
        file_name="pro_thumbnail.png",
        mime="image/png"
    )
