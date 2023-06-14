from PIL import Image, ImageDraw

# Define emotions
emotions = {
    "happy": {
        "brows": "relaxed",
        "mouth": "smiling",
    },
    "sad": {
        "brows": "angled",
        "mouth": "frowning",
    },
    "angry": {
        "brows": "angled",
        "mouth": "straight",
    },
    "surprised": {
        "brows": "raised",
        "mouth": "open",
    },
    "neutral": {
        "brows": "relaxed",
        "mouth": "straight",
    }
}

# Choose emotion
emotion = "surprised"  # change this to choose a different emotion

# Create a new image with white background
img = Image.new('RGB', (500, 500), 'white')
d = ImageDraw.Draw(img)

# Draw a circle for the face
face_color = (255, 219, 172)  # Some skin color
d.ellipse([(100, 100), (400, 400)], fill=face_color)

# Draw two circles for the eyes
eye_color = (0, 0, 0)  # Black
d.ellipse([(175, 200), (225, 250)], fill=eye_color)
d.ellipse([(275, 200), (325, 250)], fill=eye_color)

# Draw two lines for the brows
brow_color = (165, 42, 42)  # Brown

if emotions[emotion]["brows"] == "relaxed":
    # Draw lines for relaxed brows
    d.line([(170, 180), (230, 180)], fill=brow_color, width=10)
    d.line([(270, 180), (330, 180)], fill=brow_color, width=10)
elif emotions[emotion]["brows"] == "angled":
    # Draw angled brows for angry or sad
    d.line([(170, 160), (230, 180)], fill=brow_color, width=10)
    d.line([(270, 180), (330, 160)], fill=brow_color, width=10)
elif emotions[emotion]["brows"] == "raised":
    # Draw raised brows for surprised
    d.line([(170, 160), (230, 160)], fill=brow_color, width=10)
    d.line([(270, 160), (330, 160)], fill=brow_color, width=10)

# Draw a triangle for the nose
d.polygon([(250, 250), (225, 300), (275, 300)], fill=eye_color)

# Draw a line for the mouth
if emotions[emotion]["mouth"] == "smiling":
    # Draw an arc for a smiling mouth
    d.arc([(200, 350), (300, 400)], start=10, end=170, fill=eye_color, width=10)
elif emotions[emotion]["mouth"] == "frowning":
    # Draw an arc upside down for a frowning mouth
    d.arc([(200, 350), (300, 400)], start=190, end=350, fill=eye_color, width=10)
elif emotions[emotion]["mouth"] == "straight":
    # Draw a straight line for a neutral or angry mouth
    d.line([(200, 375), (300, 375)], fill=eye_color, width=10)
elif emotions[emotion]["mouth"] == "open":
    # Draw an ellipse for a surprised open mouth
    d.ellipse([(200, 350), (300, 400)], fill=eye_color)

# Save the image
img.save('face.png')