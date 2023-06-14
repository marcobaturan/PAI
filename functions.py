"""Functions module.

    This module contains many functions for general purposes
    like configuration, language detection, count syllabus,etc.
    In this module we place non classifiable functions.

    Resources:
        https://pyphen.org/
        https://github.com/aboSamoor/pycld2

"""
import math
import py_avataaars as pa
from langdetect import detect
import pyphen
from PIL import Image, ImageDraw


def face_generator(emotion):
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
    img.save(f'{emotion}.png')


def detect_language(text):
    """Detect language

        Function for detect the language output
        and config the count of syllables.
        :src https://pypi.org/project/langdetect/ :
        :params text:
        :return language:

    """
    detector = detect(text)
    return detector


def count_syllable(text):
    """Count Syllable

        This function get the number of syllables from a word or from a phrase.
        The number conditioning the movement of the mouth in the avatar's face.

    """
    dictionary = pyphen.Pyphen(lang='es')
    result = dictionary.inserted(text)
    syllables = len(result.split('-'))
    syllables = syllables + 1
    return syllables


def read_file(start_line, end_line, file_path):
    """Read the file configuration.

       Start in line 15 and end in line 19,
       these places are the data configuration of the voice.

       Resources:
       https://jnjsite.com/python-haciendo-hablar-a-un-programa/
       https://github.com/nateshmbhat/pyttsx3
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines[start_line - 1:end_line]


def face_generator(Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr,
                   clothe_expr, eye_expr, eyebrow_expr, face_expression, graphic, hatcolor):
    """face generator.

        Received parameters to generate a new face or modify an existent face.
        In the first case It's will be used in configuration module.
        In the second case It'll be use in face module for modify eye and mouth expression.

    """
    avatar = pa.PyAvataaar(
        style=Style,
        skin_color=Skin_color,
        hair_color=Hair_color,
        facial_hair_type=Facial_hair_type,
        facial_hair_color=Facial_hair_color,
        top_type=Top,
        hat_color=hatcolor,
        mouth_type=face_expression,
        eye_type=eye_expr,
        eyebrow_type=eyebrow_expr,
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=accessories_expr,
        clothe_type=clothe_expr,
        clothe_color=hatcolor,
        clothe_graphic_type=graphic)
    # generate
    avatar.render_png_file('The_Face.png')


def rate_mouth(texto):
    """Rate mouth.

        This function in functions calculate the rate of movement's mouth
        and give the number of movements in a rounded measure of time
        based in ratio of voice, words per phrase, and syllables per
        word.

        Return a tuple with a list and a numeric variable.
        You access by two assigned vars.

        :params string:
        :params list:
        :params int:

    """
    # read rate voice
    words_per_minute = read_file(15, 16, 'configuration.mem')
    # get syllables from phrase
    syllables_in_a_phrase = count_syllable(texto)
    rate = math.ceil(syllables_in_a_phrase / int(words_per_minute[0]))/2
    # number of syllables in a phrase to run the loop for
    cycles = syllables_in_a_phrase
    return cycles, rate


def set_variables_configuration():
    """Set variables configuration.

        I put the set of variables for initial configuration and on the fly emotional reconfiguration.
        Because it's too many variables, it's necessary to put in the module functions for the best
        refactor.
        :return variables:

    """
    # variables
    circle = ['CIRCLE', 'TRANSPARENT']
    skin_tones = ['BLACK', 'BROWN', 'DARK_BROWN', 'LIGHT', 'PALE', 'TANNED', 'YELLOW']
    hair_colors = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PASTEL_PINK', 'PLATINUM',
                   'RED', 'SILVER_GRAY']
    beard_styles = ['BEARD_LIGHT', 'BEARD_MAJESTIC', 'BEARD_MEDIUM', 'DEFAULT', 'MOUSTACHE_FANCY', 'MOUSTACHE_MAGNUM']
    facial_hair_colors = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PASTEL_PINK',
                          'PLATINUM', 'RED', 'SILVER_GRAY']
    top_types = ['EYE_PATCH', 'HAT', 'HIJAB', 'LONG_HAIR_BIG_HAIR', 'LONG_HAIR_BOB', 'LONG_HAIR_BUN', 'LONG_HAIR_CURLY',
                 'LONG_HAIR_CURVY', 'LONG_HAIR_DREADS', 'LONG_HAIR_FRIDA', 'LONG_HAIR_FRO', 'LONG_HAIR_FRO_BAND',
                 'LONG_HAIR_MIA_WALLACE', 'LONG_HAIR_NOT_TOO_LONG', 'LONG_HAIR_SHAVED_SIDES', 'LONG_HAIR_STRAIGHT',
                 'LONG_HAIR_STRAIGHT2', 'LONG_HAIR_STRAIGHT_STRAND', 'NO_HAIR', 'SHORT_HAIR_DREADS_01',
                 'SHORT_HAIR_DREADS_02',
                 'SHORT_HAIR_FRIZZLE', 'SHORT_HAIR_SHAGGY_MULLET', 'SHORT_HAIR_SHORT_CURLY', 'SHORT_HAIR_SHORT_FLAT',
                 'SHORT_HAIR_SHORT_ROUND', 'SHORT_HAIR_SHORT_WAVED', 'SHORT_HAIR_SIDES', 'SHORT_HAIR_THE_CAESAR',
                 'SHORT_HAIR_THE_CAESAR_SIDE_PART', 'TURBAN', 'WINTER_HAT1', 'WINTER_HAT2', 'WINTER_HAT3',
                 'WINTER_HAT4']
    colors = ['BLACK', 'BLUE_01', 'BLUE_02', 'BLUE_03', 'GRAY_01', 'GRAY_02', 'HEATHER', 'PASTEL_BLUE', 'PASTEL_GREEN',
              'PASTEL_ORANGE', 'PASTEL_RED', 'PASTEL_YELLOW', 'PINK', 'RED', 'WHITE']
    expressions = ['CONCERNED', 'DEFAULT', 'DISBELIEF', 'EATING', 'GRIMACE', 'SAD', 'SCREAM_OPEN', 'SERIOUS', 'SMILE',
                   'TONGUE',
                   'TWINKLE', 'VOMIT']
    eye_types = ['CLOSE', 'CRY', 'DEFAULT', 'DIZZY', 'EYE_ROLL', 'HAPPY', 'HEARTS', 'SIDE', 'SQUINT', 'SURPRISED',
                 'WINK',
                 'WINK_WACKY']
    eyebrow_types = ['ANGRY', 'ANGRY_NATURAL', 'DEFAULT', 'DEFAULT_NATURAL', 'FLAT_NATURAL', 'FROWN_NATURAL',
                     'RAISED_EXCITED',
                     'RAISED_EXCITED_NATURAL', 'SAD_CONCERNED', 'SAD_CONCERNED_NATURAL', 'UNI_BROW_NATURAL', 'UP_DOWN',
                     'UP_DOWN_NATURAL']
    accessories_types = ['DEFAULT', 'KURT', 'PRESCRIPTION_01', 'PRESCRIPTION_02', 'ROUND', 'SUNGLASSES', 'WAYFARERS']
    clothing_types = ['BLAZER_SHIRT', 'BLAZER_SWEATER', 'COLLAR_SWEATER', 'GRAPHIC_SHIRT', 'HOODIE', 'OVERALL',
                      'SHIRT_CREW_NECK',
                      'SHIRT_SCOOP_NECK', 'SHIRT_V_NECK']
    graphic = ['BAT', 'BEAR', 'CUMBIA', 'DEER', 'DIAMOND', 'HOLA', 'PIZZA', 'RESIST', 'SELENA', 'SKULL',
               'SKULL_OUTLINE']
    rate = ['25', '50', '75', '100', '125', '150']
    volume = ['0.25', '0.50', '0.75', '1.0']
    sex = ['0', '1']
    language = ['es', 'en', 'eo']
    return accessories_types, beard_styles, circle, clothing_types, colors, expressions, eye_types, eyebrow_types, facial_hair_colors, graphic, hair_colors, language, rate, sex, skin_tones, top_types, volume


def params_on_the_fly(values):
    """Parameters on-the-fly.

        This function manage the parameters from values get from configuration and
        output speak of the chatbot. And detect the I/O stream for sentimental
        analysis for generate mouth movement and emotional expression.

        :param values:
        :return values:

    """
    graphic_expr = None
    # parameters on-the-fly
    if values[0] == 'CIRCLE':
        Style = pa.AvatarStyle.CIRCLE
    else:
        Style = pa.AvatarStyle.TRANSPARENT
    # SkinColor
    if values[1] == 'BLACK':
        Skin_color = pa.SkinColor.BLACK
    elif values[1] == 'BROWN':
        Skin_color = pa.SkinColor.BROWN
    elif values[1] == 'DARK_BROWN':
        Skin_color = pa.SkinColor.DARK_BROWN
    elif values[1] == 'LIGHT':
        Skin_color = pa.SkinColor.LIGHT
    elif values[1] == 'PALE':
        Skin_color = pa.SkinColor.PALE
    elif values[1] == 'TANNED':
        Skin_color = pa.SkinColor.TANNED
    elif values[1] == 'YELLOW':
        Skin_color = pa.SkinColor.YELLOW
    else:
        print("Invalid skin tone.")
    # hair_colors
    if values[2] == 'AUBURN':
        Hair_color = pa.HairColor.AUBURN
    elif values[2] == 'BLACK':
        Hair_color = pa.HairColor.BLACK
    elif values[2] == 'BLONDE':
        Hair_color = pa.HairColor.BLONDE
    elif values[2] == 'BLONDE_GOLDEN':
        Hair_color = pa.HairColor.BLONDE_GOLDEN
    elif values[2] == 'BROWN':
        Hair_color = pa.HairColor.BROWN
    elif values[2] == 'BROWN_DARK':
        Hair_color = pa.HairColor.BROWN_DARK
    elif values[2] == 'PASTEL_PINK':
        Hair_color = pa.HairColor.PASTEL_PINK
    elif values[2] == 'PLATINUM':
        Hair_color = pa.HairColor.PLATINUM
    elif values[2] == 'RED':
        Hair_color = pa.HairColor.RED
    elif values[2] == 'SILVER_GRAY':
        Hair_color = pa.HairColor.SILVER_GRAY
    else:
        print("Invalid hair color.")
    # BEARD
    if values[3] == 'BEARD_LIGHT':
        Facial_hair_type = pa.FacialHairType.BEARD_LIGHT
    elif values[3] == 'BEARD_MAJESTIC':
        Facial_hair_type = pa.FacialHairType.BEARD_MAJESTIC
    elif values[3] == 'BEARD_MEDIUM':
        Facial_hair_type = pa.FacialHairType.BEARD_MEDIUM
    elif values[3] == 'DEFAULT':
        Facial_hair_type = pa.FacialHairType.DEFAULT
    elif values[3] == 'MOUSTACHE_FANCY':
        Facial_hair_type = pa.FacialHairType.MOUSTACHE_FANCY
    elif values[3] == 'MOUSTACHE_MAGNUM':
        Facial_hair_type = pa.FacialHairType.MOUSTACHE_MAGNUM
    else:
        print("Invalid beard style.")
    # facial hair color
    if values[4] == 'AUBURN':
        Facial_hair_color = pa.HairColor.AUBURN
    elif values[4] == 'BLACK':
        Facial_hair_color = pa.HairColor.BLACK
    elif values[4] == 'BLONDE':
        Facial_hair_color = pa.HairColor.BLONDE
    elif values[4] == 'BLONDE_GOLDEN':
        Facial_hair_color = pa.HairColor.BLONDE_GOLDEN
    elif values[4] == 'BROWN':
        Facial_hair_color = pa.HairColor.BROWN
    elif values[4] == 'BROWN_DARK':
        Facial_hair_color = pa.HairColor.BROWN_DARK
    elif values[4] == 'PASTEL_PINK':
        Facial_hair_color = pa.HairColor.PASTEL_PINK
    elif values[4] == 'PLATINUM':
        Facial_hair_color = pa.HairColor.PLATINUM
    elif values[4] == 'RED':
        Facial_hair_color = pa.HairColor.RED
    elif values[4] == 'SILVER_GRAY':
        Facial_hair_color = pa.HairColor.SILVER_GRAY
    else:
        print("Invalid facial hair color.")
    # TopType
    if values[5] == 'EYE_PATCH':
        Top = pa.TopType.EYE_PATCH
    elif values[5] == 'HAT':
        Top = pa.TopType.HAT
    elif values[5] == 'HIJAB':
        Top = pa.TopType.HIJAB
    elif values[5] == 'LONG_HAIR_BIG_HAIR':
        Top = pa.TopType.LONG_HAIR_BIG_HAIR
    elif values[5] == 'LONG_HAIR_BOB':
        Top = pa.TopType.LONG_HAIR_BOB
    elif values[5] == 'LONG_HAIR_BUN':
        Top = pa.TopType.LONG_HAIR_BUN
    elif values[5] == 'LONG_HAIR_CURLY':
        Top = pa.TopType.LONG_HAIR_CURLY
    elif values[5] == 'LONG_HAIR_CURVY':
        Top = pa.TopType.LONG_HAIR_CURVY
    elif values[5] == 'LONG_HAIR_DREADS':
        Top = pa.TopType.LONG_HAIR_DREADS
    elif values[5] == 'LONG_HAIR_FRIDA':
        Top = pa.TopType.LONG_HAIR_FRIDA
    elif values[5] == 'LONG_HAIR_FRO':
        Top = pa.TopType.LONG_HAIR_FRO
    elif values[5] == 'LONG_HAIR_FRO_BAND':
        Top = pa.TopType.LONG_HAIR_FRO_BAND
    elif values[5] == 'LONG_HAIR_MIA_WALLACE':
        Top = pa.TopType.LONG_HAIR_MIA_WALLACE
    elif values[5] == 'LONG_HAIR_NOT_TOO_LONG':
        Top = pa.TopType.LONG_HAIR_NOT_TOO_LONG
    elif values[5] == 'LONG_HAIR_SHAVED_SIDES':
        Top = pa.TopType.LONG_HAIR_SHAVED_SIDES
    elif values[5] == 'LONG_HAIR_STRAIGHT':
        Top = pa.TopType.LONG_HAIR_STRAIGHT
    elif values[5] == 'LONG_HAIR_STRAIGHT2':
        Top = pa.TopType.LONG_HAIR_STRAIGHT2
    elif values[5] == 'LONG_HAIR_STRAIGHT_STRAND':
        Top = pa.TopType.LONG_HAIR_STRAIGHT_STRAND
    elif values[5] == 'NO_HAIR':
        Top = pa.TopType.NO_HAIR
    elif values[5] == 'SHORT_HAIR_DREADS_01':
        Top = pa.TopType.SHORT_HAIR_DREADS_01
    elif values[5] == 'SHORT_HAIR_DREADS_02':
        Top = pa.TopType.SHORT_HAIR_DREADS_02
    elif values[5] == 'SHORT_HAIR_FRIZZLE':
        Top = pa.TopType.SHORT_HAIR_FRIZZLE
    elif values[5] == 'SHORT_HAIR_SHAGGY_MULLET':
        Top = pa.TopType.SHORT_HAIR_SHAGGY_MULLET
    elif values[5] == 'SHORT_HAIR_SHORT_CURLY':
        Top = pa.TopType.SHORT_HAIR_SHORT_CURLY
    elif values[5] == 'SHORT_HAIR_SHORT_FLAT':
        Top = pa.TopType.SHORT_HAIR_SHORT_FLAT
    elif values[5] == 'SHORT_HAIR_SHORT_ROUND':
        Top = pa.TopType.SHORT_HAIR_SHORT_ROUND
    elif values[5] == 'SHORT_HAIR_SHORT_WAVED':
        Top = pa.TopType.SHORT_HAIR_SHORT_WAVED
    elif values[5] == 'SHORT_HAIR_SIDES':
        Top = pa.TopType.SHORT_HAIR_SIDES
    elif values[5] == 'SHORT_HAIR_THE_CAESAR':
        Top = pa.TopType.SHORT_HAIR_THE_CAESAR
    elif values[5] == 'SHORT_HAIR_THE_CAESAR_SIDE_PART':
        Top = pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART
    elif values[5] == 'TURBAN':
        Top = pa.TopType.TURBAN
    elif values[5] == 'WINTER_HAT1':
        Top = pa.TopType.WINTER_HAT1
    elif values[5] == 'WINTER_HAT2':
        Top = pa.TopType.WINTER_HAT2
    elif values[5] == 'WINTER_HAT3':
        Top = pa.TopType.WINTER_HAT3
    elif values[5] == 'WINTER_HAT4':
        Top = pa.TopType.WINTER_HAT4
    else:
        print("Invalid top type.")
    # color hat
    if values[6] == 'BLACK':
        hatcolor = pa.Color.BLACK
    elif values[6] == 'BLUE_01':
        hatcolor = pa.Color.BLUE_01
    elif values[6] == 'BLUE_02':
        hatcolor = pa.Color.BLUE_02
    elif values[6] == 'BLUE_03':
        hatcolor = pa.Color.BLUE_03
    elif values[6] == 'GRAY_01':
        hatcolor = pa.Color.GRAY_01
    elif values[6] == 'GRAY_02':
        hatcolor = pa.Color.GRAY_02
    elif values[6] == 'HEATHER':
        hatcolor = pa.Color.HEATHER
    elif values[6] == 'PASTEL_BLUE':
        hatcolor = pa.Color.PASTEL_BLUE
    elif values[6] == 'PASTEL_GREEN':
        hatcolor = pa.Color.PASTEL_GREEN
    elif values[6] == 'PASTEL_ORANGE':
        hatcolor = pa.Color.PASTEL_ORANGE
    elif values[6] == 'PASTEL_RED':
        hatcolor = pa.Color.PASTEL_RED
    elif values[6] == 'PASTEL_YELLOW':
        hatcolor = pa.Color.PASTEL_YELLOW
    elif values[6] == 'PINK':
        hatcolor = pa.Color.PINK
    elif values[6] == 'RED':
        hatcolor = pa.Color.RED
    elif values[6] == 'WHITE':
        hatcolor = pa.Color.WHITE
    else:
        print("Invalid color.")
    # Mouth Expressions
    if values[7] == 'CONCERNED':
        face_expression = pa.MouthType.CONCERNED
    elif values[7] == 'DEFAULT':
        face_expression = pa.MouthType.DEFAULT
    elif values[7] == 'DISBELIEF':
        face_expression = pa.MouthType.DISBELIEF
    elif values[7] == 'EATING':
        face_expression = pa.MouthType.EATING
    elif values[7] == 'GRIMACE':
        face_expression = pa.MouthType.GRIMACE
    elif values[7] == 'SAD':
        face_expression = pa.MouthType.SAD
    elif values[7] == 'SCREAM_OPEN':
        face_expression = pa.MouthType.SCREAM_OPEN
    elif values[7] == 'SERIOUS':
        face_expression = pa.MouthType.SERIOUS
    elif values[7] == 'SMILE':
        face_expression = pa.MouthType.SMILE
    elif values[7] == 'TONGUE':
        face_expression = pa.MouthType.TONGUE
    elif values[7] == 'TWINKLE':
        face_expression = pa.MouthType.TWINKLE
    elif values[7] == 'VOMIT':
        face_expression = pa.MouthType.VOMIT
    else:
        print("Invalid expression.")
    # eye express
    if values[8] == 'CLOSE':
        eye_expr = pa.EyesType.CLOSE
    elif values[8] == 'CRY':
        eye_expr = pa.EyesType.CRY
    elif values[8] == 'DEFAULT':
        eye_expr = pa.EyesType.DEFAULT
    elif values[8] == 'DIZZY':
        eye_expr = pa.EyesType.DIZZY
    elif values[8] == 'EYE_ROLL':
        eye_expr = pa.EyesType.EYE_ROLL
    elif values[8] == 'HAPPY':
        eye_expr = pa.EyesType.HAPPY
    elif values[8] == 'HEARTS':
        eye_expr = pa.EyesType.HEARTS
    elif values[8] == 'SIDE':
        eye_expr = pa.EyesType.SIDE
    elif values[8] == 'SQUINT':
        eye_expr = pa.EyesType.SQUINT
    elif values[8] == 'SURPRISED':
        eye_expr = pa.EyesType.SURPRISED
    elif values[8] == 'WINK':
        eye_expr = pa.EyesType.WINK
    elif values[8] == 'WINK_WACKY':
        eye_expr = pa.EyesType.WINK_WACKY
    else:
        print(f"Invalid eye type: {values[8]}")
    # Eyebrow types
    if values[9] == 'ANGRY':
        eyebrow_expr = pa.EyebrowType.ANGRY
    elif values[9] == 'ANGRY_NATURAL':
        eyebrow_expr = pa.EyebrowType.ANGRY_NATURAL
    elif values[9] == 'DEFAULT':
        eyebrow_expr = pa.EyebrowType.DEFAULT
    elif values[9] == 'DEFAULT_NATURAL':
        eyebrow_expr = pa.EyebrowType.DEFAULT_NATURAL
    elif values[9] == 'FLAT_NATURAL':
        eyebrow_expr = pa.EyebrowType.FLAT_NATURAL
    elif values[9] == 'FROWN_NATURAL':
        eyebrow_expr = pa.EyebrowType.FROWN_NATURAL
    elif values[9] == 'RAISED_EXCITED':
        eyebrow_expr = pa.EyebrowType.RAISED_EXCITED
    elif values[9] == 'RAISED_EXCITED_NATURAL':
        eyebrow_expr = pa.EyebrowType.RAISED_EXCITED_NATURAL
    elif values[9] == 'SAD_CONCERNED':
        eyebrow_expr = pa.EyebrowType.SAD_CONCERNED
    elif values[9] == 'SAD_CONCERNED_NATURAL':
        eyebrow_expr = pa.EyebrowType.SAD_CONCERNED_NATURAL
    elif values[9] == 'UNI_BROW_NATURAL':
        eyebrow_expr = pa.EyebrowType.UNI_BROW_NATURAL
    elif values[9] == 'UP_DOWN':
        eyebrow_expr = pa.EyebrowType.UP_DOWN
    elif values[9] == 'UP_DOWN_NATURAL':
        eyebrow_expr = pa.EyebrowType.UP_DOWN_NATURAL
    else:
        print(f"Invalid eye type: {values[9]}")
    # accessories type
    if values[10] == 'DEFAULT':
        accessories_expr = pa.AccessoriesType.DEFAULT
    elif values[10] == 'KURT':
        accessories_expr = pa.AccessoriesType.KURT
    elif values[10] == 'PRESCRIPTION_01':
        accessories_expr = pa.AccessoriesType.PRESCRIPTION_01
    elif values[10] == 'PRESCRIPTION_02':
        accessories_expr = pa.AccessoriesType.PRESCRIPTION_02
    elif values[10] == 'ROUND':
        accessories_expr = pa.AccessoriesType.ROUND
    elif values[10] == 'SUNGLASSES':
        accessories_expr = pa.AccessoriesType.SUNGLASSES
    elif values[10] == 'WAYFARERS':
        accessories_expr = pa.AccessoriesType.WAYFARERS
    else:
        print(f"Invalid accessories type: {values[10]}")
    # clothing_types
    if values[11] == 'BLAZER_SHIRT':
        clothe_expr = pa.ClotheType.BLAZER_SHIRT
    elif values[11] == 'BLAZER_SWEATER':
        clothe_expr = pa.ClotheType.BLAZER_SWEATER
    elif values[11] == 'COLLAR_SWEATER':
        clothe_expr = pa.ClotheType.COLLAR_SWEATER
    elif values[11] == 'GRAPHIC_SHIRT':
        clothe_expr = pa.ClotheType.GRAPHIC_SHIRT
    elif values[11] == 'HOODIE':
        clothe_expr = pa.ClotheType.HOODIE
    elif values[11] == 'OVERALL':
        clothe_expr = pa.ClotheType.OVERALL
    elif values[11] == 'SHIRT_CREW_NECK':
        clothe_expr = pa.ClotheType.SHIRT_CREW_NECK
    elif values[11] == 'SHIRT_SCOOP_NECK':
        clothe_expr = pa.ClotheType.SHIRT_SCOOP_NECK
    elif values[11] == 'SHIRT_V_NECK':
        clothe_expr = pa.ClotheType.SHIRT_V_NECK
    else:
        print(f"Invalid clothing type: {values[11]}")
    # clothe graphic
    if values[12] == 'BAT':
        graphic_expr = pa.ClotheGraphicType.BAT
    elif values[12] == 'BEAR':
        graphic_expr = pa.ClotheGraphicType.BEAR
    elif values[12] == 'CUMBIA':
        graphic_expr = pa.ClotheGraphicType.CUMBIA
    elif values[12] == 'DEER':
        graphic_expr = pa.ClotheGraphicType.DEER
    elif values[12] == 'DIAMOND':
        graphic_expr = pa.ClotheGraphicType.DIAMOND
    elif values[12] == 'HOLA':
        graphic_expr = pa.ClotheGraphicType.HOLA
    elif values[12] == 'PIZZA':
        graphic_expr = pa.ClotheGraphicType.PIZZA
    elif values[12] == 'RESIST':
        graphic_expr = pa.ClotheGraphicType.RESIST
    elif values[12] == 'SELENA':
        graphic_expr = pa.ClotheGraphicType.SELENA
    elif values[12] == 'SKULL':
        graphic_expr = pa.ClotheGraphicType.SKULL
    elif values[12] == 'SKULL_OUTLINE':
        graphic_expr = pa.ClotheGraphicType.SKULL_OUTLINE
    else:
        print(f"Invalid graphic type: {values[12]}")

    return Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr, clothe_expr, eye_expr, eyebrow_expr, face_expression, graphic_expr,hatcolor
