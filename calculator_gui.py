from tkinter import *
import calculator


class GUI:
    def __init__(self, window):
        """
        initializing the layout of the GUI

        NOTES: -HAVE THE PROGRAM LOOP UNTIL THE USER PRESSES
                THE EQUAL BUTTON

               -HAVE THE COMMAND BUTTONS GO A DARKER GREY WHILE
                THEY ARE BEING USED TO SHOW WHAT BUTTON WAS PRESSED

               -HAVE THE NUMBER BUTTONS SLEEP FOR HALF A SECOND TO A
                DARKER GREY TO SHOW THE USER WHAT BUTTON THEY PRESSED

        :param window: comes from the main.py file to initialize the window
        """
        #TODO: -MAKE THE BUTTONS ABLE TO PRINT TO THE USER ENTRY LABEL
        #TODO: -MAKE THE BUTTONS COMMUNICATE WITH CALCULATOR.PY

        self.window = window

        # Setting up the entry
        self.frame_entry = Frame(self.window)
        self.user_entry = Label(self.frame_entry, fg='Red', text=' '*52)  # 48 spaces
        self.user_entry.config(bg='light grey')
        self.frame_entry.pack()
        self.user_entry.pack(side='top', padx=10, pady=10)

        # first row: C / -/+ / % / /
        self.first_row = Frame(self.window)
        self.first_row.pack()
        # creates the buttons for the first row
        self.clear_button = Button(self.first_row, text='C')
        self.negative_switch_button = Button(self.first_row, text='-/+')
        self.percent_button = Button(self.first_row, text='%')
        self.divide_button = Button(self.first_row, text='/')
        # places the buttons for the first row
        self.clear_button.pack(side='left')
        self.negative_switch_button.pack(side='left')
        self.percent_button.pack(side='left')
        self.divide_button.pack(side='left')

        # second row: 7 / 8 / 9 / multiply
        self.second_row = Frame(self.window)
        self.second_row.pack()
        # creates buttons for the second row
        self.seven_button = Button(self.second_row, text='7')
        self.eight_button = Button(self.second_row, text='8')
        self.nine_button = Button(self.second_row, text='9')
        self.multiply_button = Button(self.second_row, text='*')
        # places the buttons for the second row
        self.seven_button.pack(side='left')
        self.eight_button.pack(side='left')
        self.nine_button.pack(side='left')
        self.multiply_button.pack(side='left')

        # third row: 4 / 5 / 6 / subtract
        self.third_row = Frame(self.window)
        self.third_row.pack()
        # creates buttons for the third row
        self.four_button = Button(self.third_row, text='4')
        self.five_button = Button(self.third_row, text='5')
        self.six_button = Button(self.third_row, text='6')
        self.subtract_button = Button(self.third_row, text='-')
        # places buttons for the third row
        self.four_button.pack(side='left')
        self.five_button.pack(side='left')
        self.six_button.pack(side='left')
        self.subtract_button.pack(side='left')

        # fourth row: 1 / 2 / 3 / add
        self.fourth_row = Frame(self.window)
        self.fourth_row.pack()
        # creates buttons for the fourth row
        self.one_button = Button(self.fourth_row, text='1')
        self.two_button = Button(self.fourth_row, text='2')
        self.three_button = Button(self.fourth_row, text='3')
        self.add_button = Button(self.fourth_row, text='+')
        # places buttons for the fourth row
        self.one_button.pack(side='left')
        self.two_button.pack(side='left')
        self.three_button.pack(side='left')
        self.add_button.pack(side='left')

        # fifth row: 0      / . / equal
        self.fifth_row = Frame(self.window)
        self.fifth_row.pack()
        # creates buttons for the fifth row
        self.zero_button = Button(self.fifth_row, text='0')
        self.period_button = Button(self.fifth_row, text='.')
        self.equal_button = Button(self.fifth_row, text='=')
        # places buttons for the fifth row
        self.zero_button.pack(side='left', fill=X)
        self.period_button.pack(side='left')
        self.equal_button.pack(side='left')

    def clear(self):
        pass

    def clicked(self):
        pass