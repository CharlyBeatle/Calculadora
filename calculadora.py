#librerias
from typing import Text

import PySimpleGUI as sg          #PySimpleGUI => Creación de interfaz gráfica

import pygame                     #pygame => Creación de videojuegos

pygame.init()                     #Inicializamos la libreria pygame

# Botones, fuentes
bw = {'size': (8, 3), 'font': ('arial', 20, 'bold'), 'button_color': ('cornsilk', 'black')}
bt = {'size': (8, 3), 'font': ('arial', 20, 'bold'), 'button_color': ('seagreen', 'black')}
bo = {'size': (16, 3), 'font': ('arial', 20, 'bold'), 'button_color': ('white', 'black')}


# Layout => organizar, diseñar
sg.theme('DarkTanBlue')
layout = [
    [sg.Txt(''  * 10)],                      
    [sg.Text('', size=(25, 2), justification= 'right', background_color='black',font=('Arial', 30, 'bold'), text_color='white', key='input')],
    [sg.Txt(''  * 10)],
    [sg.ReadFormButton('(', **bt), sg.ReadFormButton(')', **bt), sg.ReadFormButton('c', **bt), sg.ReadFormButton('«', **bt)],
    [sg.ReadFormButton('7', **bw), sg.ReadFormButton('8',**bw), sg.ReadFormButton('9',**bw), sg.ReadFormButton('÷', **bt)],
    [sg.ReadFormButton('4',**bw), sg.ReadFormButton('5',**bw), sg.ReadFormButton('6',**bw), sg.ReadFormButton('x', **bt)],
    [sg.ReadFormButton('1',**bw), sg.ReadFormButton('2',**bw), sg.ReadFormButton('3',**bw), sg.ReadFormButton('-', **bt)],
    [sg.ReadFormButton('.',**bt), sg.ReadFormButton('0',**bw), sg.ReadFormButton('=', **bt), sg.ReadFormButton('+', **bt)],
    ]


form = sg.FlexForm('CALCULADORA CON SONIDO', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)

form.Layout(layout)

# Funciones
def formato():
    return float (''.join(vars['front'])+'.'+''.join(vars['black']))

def sonido(n):
    s = pygame.mixer.Sound("Sonidos/" + n + ".ogg")
    s.play()


# Usabilidad
Equal = ''
List_Op_Error =  ['+','-','*','/','(']

while True:
    button, value = form.Read()                            
    
# Sonido de teclas
    if button == sg.WIN_CLOSED:
        break
    sonido(button)

# Teclas de borrado y operaciones
    if button is 'c':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif button is '«':
        Equal = Equal[:-1]
        form.FindElement('input').Update(Equal)
    elif len(Equal) == 16 :
        pass
    elif str(button) in '1234567890+-().':
        Equal += str(button)
        form.FindElement('input').Update(Equal) 
    elif button is 'x':
        Equal += '*'
        form.FindElement('input').Update(Equal)
    elif button is '÷':
        Equal += '/'
        form.FindElement('input').Update(Equal)
    
# Condiciones
    elif button is '=':
        # Error Case
        for i in List_Op_Error :  
            if '*' is Equal[0] or '/' is Equal[0] or ')' is Equal[0]  or i is Equal[-1]:   
                Answer = "Error de operación" 
                break
            elif Equal == '6001012630187':
                Answer = 'Apisit.Khomcharoen'
                break
            elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                Answer = "Error de operación" 
                break
            elif '(' in Equal :
                if ')' not in Equal :
                    Answer = "Error de operación" 
                    break   
            elif '(' not in Equal:
                if ')' in Equal:
                    Answer = "Error de operación" 
                    break
# Cálculos    
        else :
            Answer = str("%0.2f" %(eval(Equal)))                           
            if '.0' in Answer:
                Answer = str(int(float(Answer)))                         
        form.FindElement('input').Update(Answer)                         
        Equal = Answer

    elif button is 'Quit'  or button is None:                            
        break


