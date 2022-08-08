def clear(user_entry1) -> str:
    """
    clears the label

    :param user_entry1: the text inside the label
    :return: str
    """
    return user_entry1.config(text='0')


def negative_switch(user_entry1) -> str:
    """
    switches the sign of the last inputted number

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        display = text.split()
        if display[-1].isdigit():
            display[-1] = str(-1 * int(display[-1]))
            text = ''
            for items in display:
                text += f'{items} '
            return user_entry1.config(text=f'{text}')
        elif display[-1].startswith('-'):
            if display[-1][1:].isdigit():
                display[-1] = str(-1 * int(display[-1]))
                text = ''
                for items in display:
                    text += f'{items} '
                return user_entry1.config(text=f'{text}')
            else:
                return user_entry1.config(text='SYNTAX ERROR')
        else:
            return user_entry1.config(text='SYNTAX ERROR')
    
    
def percent(user_entry1) -> str:
    """
    divides the last inputted number by 100 to
    easily convert it into a percent

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        display = text.split()
        if display[-1].isdigit() or '.' in display[-1] or 'e-' in display[-1]:
            display[-1] = str(float(display[-1]) / 100)
            text = ''
            for items in display:
                text += f'{items} '
            return user_entry1.config(text=f'{text}')
        else:
            return user_entry1.config(text='SYNTAX ERROR')


def divide(user_entry1) -> str:
    """
    divides the numbers to the immediate left and right
    of the division sign

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == 'SYNTAX ERROR':
            return user_entry1.config(text='0')
        else:
            return user_entry1.config(text=f'{text} / ')


def seven(user_entry1) -> str:
    """
    either starts the label with a 7 or creates a 7
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '7'
            return user_entry1.config(text=f'{text}')
        else:
            text += '7'
            return user_entry1.config(text=f'{text}')


def eight(user_entry1) -> str:
    """
    either starts the label with an 8 or creates an 8
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '8'
            return user_entry1.config(text=f'{text}')
        else:
            text += '8'
            return user_entry1.config(text=f'{text}')


def nine(user_entry1) -> str:
    """
    either starts the label with a 9 or creates a 9
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '9'
            return user_entry1.config(text=f'{text}')
        else:
            text += '9'
            return user_entry1.config(text=f'{text}')


def multiply(user_entry1) -> str:
    """
    takes the numbers to the immediate left and right
    of the multiplication symbol and multiplies them

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == 'SYNTAX ERROR':
            return user_entry1.config(text='0')
        else:
            return user_entry1.config(text=f'{text} x ')


def four(user_entry1) -> str:
    """
        either starts the label with a 4 or creates a 4
        in the label

        :param user_entry1: the text inside the label
        :return: str
        """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '4'
            return user_entry1.config(text=f'{text}')
        else:
            text += '4'
            return user_entry1.config(text=f'{text}')


def five(user_entry1) -> str:
    """
        either starts the label with a 5 or creates a 5
        in the label

        :param user_entry1: the text inside the label
        :return: str
        """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '5'
            return user_entry1.config(text=f'{text}')
        else:
            text += '5'
            return user_entry1.config(text=f'{text}')


def six(user_entry1) -> str:
    """
    either starts the label with a 6 or creates a 6
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '6'
            return user_entry1.config(text=f'{text}')
        else:
            text += '6'
            return user_entry1.config(text=f'{text}')


def subtract(user_entry1) -> str:
    """
    takes the two numbers to the immediate left and right
    of the subtraction sign and subtracts them

    :param user_entry1: the text inside the label
    :return: str
        """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == 'SYNTAX ERROR':
            return user_entry1.config(text='0')
        else:
            return user_entry1.config(text=f'{text} - ')


def one(user_entry1) -> str:
    """
    either starts the label with a 1 or creates a 1
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '1'
            return user_entry1.config(text=f'{text}')
        else:
            text += '1'
            return user_entry1.config(text=f'{text}')


def two(user_entry1) -> str:
    """
    either starts the label with a 2 or creates a 2
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '2'
            return user_entry1.config(text=f'{text}')
        else:
            text += '2'
            return user_entry1.config(text=f'{text}')


def three(user_entry1) -> str:
    """
    either starts the label with a 3 or creates a 3
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '3'
            return user_entry1.config(text=f'{text}')
        else:
            text += '3'
            return user_entry1.config(text=f'{text}')


def add(user_entry1) -> str:
    """
    takes the two numbers to the immediate left and right
    of the addition sign and adds them

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == 'SYNTAX ERROR':
            return user_entry1.config(text='0')
        else:
            return user_entry1.config(text=f'{text} + ')


def zero(user_entry1) -> str:
    """
    either starts the label with a 0 or creates a 0
    in the label

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':
            text = '0'
            return user_entry1.config(text=f'{text}')
        else:
            text += '0'
            return user_entry1.config(text=f'{text}')


def period(user_entry1) -> str:
    """
    adds a period to the number or if no number exists
    will create a 0. in instead

    :param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 20:
        pass
    else:
        if text == 'SYNTAX ERROR':
            return user_entry1.config(text='0')
        else:
            if text[-1].isspace():
                return user_entry1.config(text=f'{text}0.')
            else:
                return user_entry1.config(text=f'{text}.')
    
    
def equals(user_entry1) -> str:
    """
    will perform the equation in the label

    :param user_entry1: the text in the label
    :return: str
    """
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
        return user_entry1.config(text='SYNTAX ERROR')
    except ValueError:
        return user_entry1.config(text='0')
    except IndexError:
        return user_entry1.config(text=f'{text}')
    else:
        return user_entry1.config(text=result)