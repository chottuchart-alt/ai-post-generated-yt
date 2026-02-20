import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame
from PIL import Image as PILImage
import tempfile
import os

st.set_page_config(page_title="Resume Builder PRO", page_icon="📄")

st.title("📄 Professional Resume Builder PRO")

# ---------------- THEME ----------------
theme = st.selectbox("Choose Resume Theme", 
                     ["Modern Blue", "Elegant Gray", "Minimal Black"])

if theme == "Modern Blue":
    primary_color = colors.HexColor("#1D4ED8")
elif theme == "Elegant Gray":
    primary_color = colors.HexColor("#374151")
else:
    primary_color = colors.black

# ---------------- INPUT ----------------
name = st.text_input("Full Name")
role = st.text_input("Professional Title")
location = st.text_input("Location")
phone = st.text_input("Phone")
email = st.text_input("Email")

summary = st.text_area("Professional Summary")
skills = st.text_input("Skills (comma separated)")
experience = st.text_area("Experience")
education = st.text_area("Education")
achievements = st.text_area("Achievements")

photo = st.file_uploader("Upload Photo", type=["png","jpg","jpeg"])

# ---------------- PDF FUNCTION ----------------
def create_resume_pdf(path):

    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    # Sidebar
    c.setFillColor(primary_color)
    c.rect(0, 0, 160, height, fill=1)

    # White background
    c.setFillColor(colors.white)
    c.rect(160, 0, width-160, height, fill=1)

    # Photo
    if photo:
        img = PILImage.open(photo)
        img_path = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name
        img.save(img_path)
        c.drawImage(img_path, 30, height-200, width=100, height=100, mask='auto')

    # Name
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(180, height-60, name)

    c.setFont("Helvetica", 14)
    c.drawString(180, height-85, role)

    # Contact
    c.setFont("Helvetica", 10)
    c.drawString(180, height-105, location)
    c.drawString(180, height-120, phone)
    c.drawString(180, height-135, email)

    y = height - 170

    # Section Function
    def draw_section(title, content):
        nonlocal y
        c.setFillColor(primary_color)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(180, y, title)
        y -= 15

        c.setFillColor(colors.black)
        c.setFont("Helvetica", 11)

        text_obj = c.beginText(180, y)
        text_obj.setLeading(14)
        text_obj.textLines(content)
        c.drawText(text_obj)

        y -= (14 * (len(content.split("\n")) + 1)) + 10

    if summary:
        draw_section("Professional Summary", summary)

    if experience:
        draw_section("Experience", experience)

    if education:
        draw_section("Education", education)

    if achievements:
        draw_section("Achievements", achievements)

    # Skills in sidebar
    if skills:
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(30, height-250, "Skills")

        y_skill = height-270
        c.setFont("Helvetica", 10)
        for skill in skills.split(","):
            c.drawString(30, y_skill, f"- {skill.strip()}")
            y_skill -= 15

    c.save()

# ---------------- PREVIEW ----------------
st.subheader("Preview (Theme Applied)")
st.write("Theme:", theme)
st.write("Name:", name)
st.write("Role:", role)

# ---------------- DOWNLOAD ----------------
if st.button("📥 Generate Resume PDF"):
    pdf_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    create_resume_pdf(pdf_file.name)

    with open(pdf_file.name, "rb") as f:
        st.download_button("Download Resume", f, file_name="Professional_Resume.pdf")
