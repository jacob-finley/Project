def clear(user_entry1) -> str:
    """
    clears the label

    param user_entry1: the text inside the label
    :return: str
    """
    return user_entry1.config(text='0')


def negative_switch(user_entry1) -> str:
    """
    switches the sign of the last inputted number

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:     # character limit
        pass
    else:
        display = text.split()
        if display[-1].isdigit() or '.' in display[-1] or 'e-' in display[-1] or 'e+' in display[-1]:          # checks the last inputted character to see if it is a number
            display[-1] = str(-1 * float(display[-1]))
            text = ''
            for items in display:
                text += f'{items} '
            return user_entry1.config(text=f'{text}')     # places text back onto the label
        elif display[-1].startswith('-'):                 # checks to see if the number is already negative to turn positive
            if display[-1][1:].isdigit():
                display[-1] = str(-1 * float(display[-1]))
                text = ''
                for items in display:
                    text += f'{items} '
                return user_entry1.config(text=f'{text}')     # places text back onto the label
            else:
                return user_entry1.config(text='SYNTAX ERROR')      # throws error if sign is subtraction
        else:
            return user_entry1.config(text='SYNTAX ERROR')          # throws error if not a number
    
    
def percent(user_entry1) -> str:
    """
    divides the last inputted number by 100 to
    easily convert it into a percent

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:          # checks character length
        pass
    else:
        display = text.split()
        if display[-1].isdigit() or '.' in display[-1] or 'e-' in display[-1] or 'e+' in display[-1]:      # checks to see if a valid character is being "percented"
            display[-1] = str(float(display[-1]) / 100)
            text = ''
            for items in display:
                text += f'{items} '
            return user_entry1.config(text=f'{text}')       # returns the "percented" number
        else:                                               # throws error if a non number is put through
            return user_entry1.config(text='SYNTAX ERROR')


def divide(user_entry1) -> str:
    """
    divides the numbers to the immediate left and right
    of the division sign

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == 'SYNTAX ERROR':      # resets if error is displayed
            return user_entry1.config(text='0')
        else:                           # adds division symbol to display
            return user_entry1.config(text=f'{text} / ')


def seven(user_entry1) -> str:
    """
    either starts the label with a 7 or creates a 7
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':   # replaces error or zero screen
            return user_entry1.config(text=f'7')
        else:                                       # adds 7 to display
            return user_entry1.config(text=f'{text + "7"}')


def eight(user_entry1) -> str:
    """
    either starts the label with an 8 or creates an 8
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':   # replaces error or zero screen
            return user_entry1.config(text=f'8')
        else:                                       # adds 8 to display
            return user_entry1.config(text=f'{text + "8"}')


def nine(user_entry1) -> str:
    """
    either starts the label with a 9 or creates a 9
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':   # replaces zero or error screen
            return user_entry1.config(text=f'9')
        else:                                       # adds 9 to display
            return user_entry1.config(text=f'{text + "9"}')


def multiply(user_entry1) -> str:
    """
    takes the numbers to the immediate left and right
    of the multiplication symbol and multiplies them

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == 'SYNTAX ERROR':      # replaces error screen with zero screen
            return user_entry1.config(text='0')
        else:                           # adds x to display
            return user_entry1.config(text=f'{text} x ')


def four(user_entry1) -> str:
    """
        either starts the label with a 4 or creates a 4
        in the label

        param user_entry1: the text inside the label
        :return: str
        """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':       # replaces error or zero screen
            return user_entry1.config(text=f'4')
        else:                                           # adds 4 to display
            return user_entry1.config(text=f'{text + "4"}')


def five(user_entry1) -> str:
    """
        either starts the label with a 5 or creates a 5
        in the label

        param user_entry1: the text inside the label
        :return: str
        """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':       # replaces zero or error screen
            return user_entry1.config(text=f'5')
        else:                                           # adds 5 to display
            return user_entry1.config(text=f'{text + "5"}')


def six(user_entry1) -> str:
    """
    either starts the label with a 6 or creates a 6
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':       # replaces zero or error screen
            return user_entry1.config(text=f'6')
        else:                                           # adds 6 to display
            return user_entry1.config(text=f'{text + "6"}')


def subtract(user_entry1) -> str:
    """
    takes the two numbers to the immediate left and right
    of the subtraction sign and subtracts them

    param user_entry1: the text inside the label
    :return: str
        """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == 'SYNTAX ERROR':      # replaces error screen with zero screen
            return user_entry1.config(text='0')
        else:                           # adds subtraction to display
            return user_entry1.config(text=f'{text} - ')


def one(user_entry1) -> str:
    """
    either starts the label with a 1 or creates a 1
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':       # replaces error or zero screen
            return user_entry1.config(text=f'1')
        else:                                           # adds 1 to the display
            return user_entry1.config(text=f'{text +"1"}')


def two(user_entry1) -> str:
    """
    either starts the label with a 2 or creates a 2
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':   # replaces error or zero screen
            return user_entry1.config(text=f'2')
        else:                                       # adds 2 to display
            return user_entry1.config(text=f'{text + "2"}')


def three(user_entry1) -> str:
    """
    either starts the label with a 3 or creates a 3
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == '0' or text == 'SYNTAX ERROR':   # replaces zero or error screen
            return user_entry1.config(text=f'3')
        else:                                       # adds 3 to display
            return user_entry1.config(text=f'{text + "3"}')


def add(user_entry1) -> str:
    """
    takes the two numbers to the immediate left and right
    of the addition sign and adds them

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == 'SYNTAX ERROR':              # replaces error screen with 0 screen
            return user_entry1.config(text='0')
        else:                                   # adds 0 to display
            return user_entry1.config(text=f'{text} + ')


def zero(user_entry1) -> str:
    """
    either starts the label with a 0 or creates a 0
    in the label

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:          # checks char length
        pass
    else:
        if text == 'SYNTAX ERROR':   # replaces error screen
            return user_entry1.config(text=f'0')
        else:                        # adds 0 to display
            return user_entry1.config(text=f'{text + "0"}')


def period(user_entry1) -> str:
    """
    adds a period to the number or if no number exists
    will create a 0. in instead

    param user_entry1: the text inside the label
    :return: str
    """
    text = user_entry1.cget('text')
    if len(text) > 22:      # checks char length
        pass
    else:
        if text == 'SYNTAX ERROR':      # replaces error screen with zero screen
            return user_entry1.config(text='0')
        else:
            if text[-1].isspace():      # if char is a space, adds a zero with period
                return user_entry1.config(text=f'{text}0.')
            else:                       # adds zero to number
                return user_entry1.config(text=f'{text}.')
    
    
def equals(user_entry1) -> str:
    """
    will perform the equation in the label

    param user_entry1: the text in the label
    :return: str
    """
    text = user_entry1.cget('text')
    equation = text.split()             # turns display into ordered list
    try:
        if text == 'SYNTAX ERROR':      # checks to see if text is an error
            raise ValueError
        elif len(equation) == 1:        # checks to see if only one character is passed
            raise IndexError
        else:                           # run through equation
            while len(equation) > 1:
                m_d_index = []          # list for the 'x' and '/' positions
                a_s_index = []          # list for the '+' and '-' positions
                for i in range(len(equation)):
                    if equation[i] == 'x' or equation[i] == '/':
                        m_d_index.append(i)         # find the 'x' and '/' positions
                    elif equation[i] == '+' or equation[i] == '-':
                        a_s_index.append(i)         # find the '+' and '-' positions
                if 'x' in equation or '/' in equation:      # runs through multiplication and division first
                    for char in equation:
                        if char == 'x':
                            mul_position = equation.index(char)
                            result = str(float(equation[mul_position - 1]) * float(equation[mul_position + 1]))
                            equation[mul_position] = result     # replaces result with the 'x'
                            del equation[mul_position - 1]      # deletes the first num
                            del equation[mul_position]          # deletes the second num
                        elif char == '/':
                            div_position = equation.index(char)
                            if equation[div_position + 1] == '0':
                                raise ZeroDivisionError
                            else:
                                result = str(float(equation[div_position - 1]) / float(equation[div_position + 1]))
                                equation[div_position] = result     # replaces result with the '/'
                                del equation[div_position - 1]      # deletes the first num
                                del equation[div_position]          # deletes the second num
                if '+' in equation or '-' in equation:      # runs through '+' and '-' after 'x' and '/'
                    for char in equation:
                        if char == '+':
                            add_position = equation.index(char)
                            result = str(float(equation[add_position - 1]) + float(equation[add_position + 1]))
                            equation[add_position] = result     # replaces result with the '+'
                            del equation[add_position - 1]      # deletes the first num
                            del equation[add_position]          # deletes the second num
                        elif char == '-':
                            sub_position = equation.index(char)
                            result = str(float(equation[sub_position - 1]) - float(equation[sub_position + 1]))
                            equation[sub_position] = result     # replaces result with the '-'
                            del equation[sub_position - 1]      # deletes the first num
                            del equation[sub_position]          # deletes the second num
    except ZeroDivisionError:       # checks x / 0 in display
        return user_entry1.config(text='SYNTAX ERROR')
    except ValueError:              # replaces error screen with zero screen
        return user_entry1.config(text='0')
    except IndexError:              # if only one number is passed, have the number run through
        return user_entry1.config(text=f'{text}')
    else:                           # returns answer if no errors occurred
        return user_entry1.config(text=result)