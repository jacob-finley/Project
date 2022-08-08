from tkinter import *

#FIXME: ADD CHARACTER LIMIT OF LEN(26) TO ALL CODE


def clear(user_entry1):
    user_entry1.config(text='0')


def negative_switch(user_entry1):
    text = user_entry1.cget('text')
    display = text.split()
    if display[-1].isdigit():
        display[-1] = str(-1 * int(display[-1]))
        text = ''
        for items in display:
            text += f'{items} '
        user_entry1.config(text=f'{text}')
    elif display[-1].startswith('-'):
        if display[-1][1:].isdigit():
            display[-1] = str(-1 * int(display[-1]))
            text = ''
            for items in display:
                text += f'{items} '
            user_entry1.config(text=f'{text}')
        else:
            user_entry1.config(text='SYNTAX ERROR')
    else:
        user_entry1.config(text='SYNTAX ERROR')
    
    
def percent(user_entry1):
    text = user_entry1.cget('text')
    display = text.split()
    if display[-1].isdigit() or '.' in display[-1]:
        display[-1] = str(float(display[-1]) / 100)
        text = ''
        for items in display:
            text += f'{items} '
        user_entry1.config(text=f'{text}')
    else:
        user_entry1.config(text='SYNTAX ERROR')
    # FIXME: prevent exponential error (ex: 8e-6:: throws SYNTAX ERROR)


def divide(user_entry1):
    text = user_entry1.cget('text')
    if text == 'SYNTAX ERROR':
        user_entry1.config(text='0')
    else:
        user_entry1.config(text=f'{text} / ')


def seven(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '7'
        user_entry1.config(text=f'{text}')
    else:
        text += '7'
        user_entry1.config(text=f'{text}')


def eight(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '8'
        user_entry1.config(text=f'{text}')
    else:
        text += '8'
        user_entry1.config(text=f'{text}')


def nine(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '9'
        user_entry1.config(text=f'{text}')
    else:
        text += '9'
        user_entry1.config(text=f'{text}')


def multiply(user_entry1):
    text = user_entry1.cget('text')
    if text == 'SYNTAX ERROR':
        user_entry1.config(text='0')
    else:
        user_entry1.config(text=f'{text} x ')


def four(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '4'
        user_entry1.config(text=f'{text}')
    else:
        text += '4'
        user_entry1.config(text=f'{text}')


def five(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '5'
        user_entry1.config(text=f'{text}')
    else:
        text += '5'
        user_entry1.config(text=f'{text}')


def six(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '6'
        user_entry1.config(text=f'{text}')
    else:
        text += '6'
        user_entry1.config(text=f'{text}')


def subtract(user_entry1):
    text = user_entry1.cget('text')
    if text == 'SYNTAX ERROR':
        user_entry1.config(text='0')
    else:
        user_entry1.config(text=f'{text} - ')


def one(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '1'
        user_entry1.config(text=f'{text}')
    else:
        text += '1'
        user_entry1.config(text=f'{text}')


def two(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '2'
        user_entry1.config(text=f'{text}')
    else:
        text += '2'
        user_entry1.config(text=f'{text}')


def three(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '3'
        user_entry1.config(text=f'{text}')
    else:
        text += '3'
        user_entry1.config(text=f'{text}')


def add(user_entry1):
    text = user_entry1.cget('text')
    if text == 'SYNTAX ERROR':
        user_entry1.config(text='0')
    else:
        user_entry1.config(text=f'{text} + ')


def zero(user_entry1):
    text = user_entry1.cget('text')
    if text == '0' or text == 'SYNTAX ERROR':
        text = '0'
        user_entry1.config(text=f'{text}')
    else:
        text += '0'
        user_entry1.config(text=f'{text}')


def period(user_entry1):
    text = user_entry1.cget('text')
    if text == 'SYNTAX ERROR':
        user_entry1.config(text='0')
    else:
        user_entry1.config(text=f'{text}.')
    
    
def equals(user_entry1):
    text = user_entry1.cget('text')
    equation = text.split()
    try:
        if text == 'SYNTAX ERROR':
            raise ValueError
        elif len(equation) == 1:
            raise IndexError
        else:
            while len(equation) > 1:
                m_d_index = []
                a_s_index = []
                for i in range(len(equation)):
                    if equation[i] == 'x' or equation[1] == '/':
                        m_d_index.append(i)
                    elif equation[i] == '+' or equation[i] == '-':
                        a_s_index.append(i)

                if 'x' in equation or '/' in equation:
                    for char in equation:
                        if char == 'x':
                            mul_position = equation.index(char)
                            result = str(float(equation[mul_position - 1]) * float(equation[mul_position + 1]))
                            equation[mul_position] = result
                            del equation[mul_position - 1]
                            del equation[mul_position]
                        elif char == '/':
                            div_position = equation.index(char)
                            if equation[div_position + 1] == '0':
                                raise ZeroDivisionError
                            else:
                                result = str(float(equation[div_position - 1]) / float(equation[div_position + 1]))
                                equation[div_position] = result
                                del equation[div_position - 1]
                                del equation[div_position]
                if '+' in equation or '-' in equation:
                    for char in equation:
                        if char == '+':
                            add_position = equation.index(char)
                            result = str(float(equation[add_position - 1]) + float(equation[add_position + 1]))
                            equation[add_position] = result
                            del equation[add_position - 1]
                            del equation[add_position]
                        elif char == '-':
                            sub_position = equation.index(char)
                            result = str(float(equation[sub_position - 1]) - float(equation[sub_position + 1]))
                            equation[sub_position] = result
                            del equation[sub_position - 1]
                            del equation[sub_position]
    except ZeroDivisionError:
        user_entry1.config(text='SYNTAX ERROR')
    except ValueError:
        user_entry1.config(text='0')
    except IndexError:
        user_entry1.config(text=f'{text}')
    else:
        user_entry1.config(text=result)