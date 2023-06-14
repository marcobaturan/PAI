'''The Face
    
    Programing for generate event-state-driven avatar
    from chatbot interaction. This module is for
    configuration the entire agent in the computer.
    
    Resources;
    https://www.pysimplegui.org/
    
'''
# imports
import PySimpleGUI as psg
from face import show_the_face
from functions import face_generator, set_variables_configuration, params_on_the_fly


def configuration():
    # set variables for face generation
    accessories_types, beard_styles, circle, clothing_types, colors, expressions, eye_types, eyebrow_types, facial_hair_colors, graphic, hair_colors, language, rate, sex, skin_tones, top_types, volume = set_variables_configuration()
    # Format window.
    psg.theme('GreenTan')
    psg.set_options(text_justification='right')
    # nested structured list for the format of configuration window.
    layout = [
        [psg.Text('Select params and generate the face', font=('Helvetica', 16))],
        [psg.Text('Style window'), psg.Drop(values=(circle), expand_x=True)],
        [psg.Text('Skin color'), psg.Drop(values=(skin_tones), expand_x=True)],
        [psg.Text('Hair color'), psg.Drop(values=(hair_colors), expand_x=True)],
        [psg.Text('facial hair type'), psg.Drop(values=(beard_styles), expand_x=True)],
        [psg.Text('facial hair color'), psg.Drop(values=(facial_hair_colors), expand_x=True)],
        [psg.Text('top type'), psg.Drop(values=(top_types), expand_x=True)],
        [psg.Text('top colors'), psg.Drop(values=(colors), expand_x=True)],
        [psg.Text('mouth type'), psg.Drop(values=(expressions), expand_x=True)],
        [psg.Text('eye type'), psg.Drop(values=(eye_types), expand_x=True)],
        [psg.Text('eyebrow type'), psg.Drop(values=(eyebrow_types), expand_x=True)],
        [psg.Text('accessories type'), psg.Drop(values=(accessories_types), expand_x=True)],
        [psg.Text('clothing type'), psg.Drop(values=(clothing_types), expand_x=True)],
        [psg.Text('clothing colors'), psg.Drop(values=(colors), expand_x=True)],
        [psg.Text('clothing graphic type'), psg.Drop(values=(graphic), expand_x=True)],
        [psg.Text('Select params for voice')],
        [psg.Text('rate'), psg.Drop(values=(rate), expand_x=True)],
        [psg.Text('volume'), psg.Drop(values=(volume), expand_x=True)],
        [psg.Text('Sex (male:0, female:1)'), psg.Drop(values=(sex), expand_x=True)],
        [psg.Text('Language'), psg.Drop(values=(language), expand_x=True)],
        [psg.Text('Name'), psg.InputText('', expand_x=True)],
        [psg.Submit(), psg.Cancel()]]
    window = psg.Window('Configurarion', layout, font=("Helvetica", 12))
    event, values = window.read()
    window.close()
    # Write and save configuration of the face.
    with open('configuration.mem', 'wt') as file:
        for value in range(len(values)):
            file.write(values[value] + '\n')
    # Parameters on the fly
    Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr, clothe_expr, eye_expr, eyebrow_expr, face_expression, hatcolor, graphic_expr = params_on_the_fly(
        values)
    '''happy = ['HAPPY','HAPPY','DEFAULT_NATURAL', 'happy']
    sad = ['SAD','CRY','SAD_CONCERNED', 'sad']
    fear = ['SCREAM_OPEN','SURPRISED','SAD_CONCERNED_NATURAL', 'fear']
    anger = ['SAD','DEFAULT','ANGRY', 'anger']
    neutral_close = ['SERIOUS','DEFAULT','DEFAULT', 'close']
    neutral_open = ['SCREAM_OPEN','DEFAULT','DEFAULT', 'open']
    faces = [happy,sad,fear,anger,neutral_open,neutral_close]
    # instance & config for generate png file by SVG,
    for iteration in range(len(faces)):

        face_generator(Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr,
                       clothe_expr, faces[iteration-1][1], faces[iteration-1][2], faces[iteration-1][0], graphic_expr,
                       hatcolor,faces[iteration-1][3])'''
    face_generator(Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr,
                   clothe_expr, eye_expr, eyebrow_expr, face_expression, graphic, hatcolor)
    show_the_face()


