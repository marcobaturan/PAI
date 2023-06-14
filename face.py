# Import.
import PySimpleGUI as psg
from functions import read_file, rate_mouth, params_on_the_fly, face_generator, set_variables_configuration
from voice import load_voice_configuration
import time
import py_avataaars as pa


def show_the_face():
    """Show the face.

        Function to generate the window with generate face,
        after configure. You can delete the config file in case
        of dissatisfaction.

    """
    # Read lines from X to Y from configuration and return the params.
    global avatar
    lines = read_file(start_line=19, end_line=20, file_path='configuration.mem')
    # nested structured list for the format of configuration window.
    psg.theme('GreenTan')
    layout = [
        [psg.Image('The_Face.png', expand_x=True, expand_y=True)],
        [psg.Text('Speak!'), psg.InputText('', expand_x=True)],
        [psg.Button('Submit')]
    ]
    window = psg.Window(f'{lines[0]}', layout, size=(300, 500), keep_on_top=True)
    while True:
        event, values = window.read()
        move, rate = rate_mouth(values.get(1))
        #   MAÑANA HAGO EL RESTO DEL PROGRAMA
        # Tiene que leer el ratio y el movimiento para sacar un calculo de mover la boca.
        # use get over values because submit method retrieval a dictionary
        if event in (None, 'Exit'):
            window.close()
        elif event == 'Submit':
            load_voice_configuration(values.get(1))


