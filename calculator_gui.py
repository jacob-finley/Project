from tkinter import *
import gui_commands


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
        self.window.config(bg='light grey')

        # Setting up the entry
        self.frame_entry = Frame(self.window)
        self.user_entry1 = Label(self.frame_entry, fg='BLACK', text='0')
        self.user_entry1.config(bg='light grey', state=DISABLED, justify=CENTER)
        self.frame_entry.pack(padx=5, pady=5)
        self.user_entry1.pack(side='top', padx=0, pady=0)

        # first row: C / -/+ / % / /
        self.first_row = Frame(self.window)
        self.first_row.pack()
        # creates the buttons for the first row
        self.clear_button = Button(self.first_row, text=' C ', command=self.clear)
        self.negative_switch_button = Button(self.first_row, text='-/+', command=self.negative_switch)
        self.percent_button = Button(self.first_row, text=' % ', command=self.percent)
        self.divide_button = Button(self.first_row, text=' / ', command=self.divide)
        # places the buttons for the first row
        self.clear_button.pack(side='left')
        self.negative_switch_button.pack(side='left')
        self.percent_button.pack(side='left')
        self.divide_button.pack(side='left')

        # second row: 7 / 8 / 9 / multiply
        self.second_row = Frame(self.window)
        self.second_row.pack()
        # creates buttons for the second row
        self.seven_button = Button(self.second_row, text=' 7 ', command=self.seven)
        self.eight_button = Button(self.second_row, text=' 8 ', command=self.eight)
        self.nine_button = Button(self.second_row, text=' 9 ', command=self.nine)
        self.multiply_button = Button(self.second_row, text=' x ', command=self.multiply)
        # places the buttons for the second row
        self.seven_button.pack(side='left')
        self.eight_button.pack(side='left')
        self.nine_button.pack(side='left')
        self.multiply_button.pack(side='left')

        # third row: 4 / 5 / 6 / subtract
        self.third_row = Frame(self.window)
        self.third_row.pack()
        # creates buttons for the third row
        self.four_button = Button(self.third_row, text=' 4 ', command=self.four)
        self.five_button = Button(self.third_row, text=' 5 ', command=self.five)
        self.six_button = Button(self.third_row, text=' 6 ', command=self.six)
        self.subtract_button = Button(self.third_row, text=' - ', command=self.subtract)
        # places buttons for the third row
        self.four_button.pack(side='left')
        self.five_button.pack(side='left')
        self.six_button.pack(side='left')
        self.subtract_button.pack(side='left')

        # fourth row: 1 / 2 / 3 / add
        self.fourth_row = Frame(self.window)
        self.fourth_row.pack()
        # creates buttons for the fourth row
        self.one_button = Button(self.fourth_row, text=' 1 ', command=self.one)
        self.two_button = Button(self.fourth_row, text=' 2 ', command=self.two)
        self.three_button = Button(self.fourth_row, text=' 3 ', command=self.three)
        self.add_button = Button(self.fourth_row, text=' + ', command=self.add)
        # places buttons for the fourth row
        self.one_button.pack(side='left')
        self.two_button.pack(side='left')
        self.three_button.pack(side='left')
        self.add_button.pack(side='left')

        # fifth row: 0      / . / equal
        self.fifth_row = Frame(self.window)
        self.fifth_row.pack()
        # creates buttons for the fifth row
        self.zero_button = Button(self.fifth_row, text='        0        ', command=self.zero)
        self.period_button = Button(self.fifth_row, text=' . ', command=self.period)
        self.equal_button = Button(self.fifth_row, text=' = ', command=self.equals)
        # places buttons for the fifth row
        self.zero_button.pack(side='left', fill=X, pady=6)
        self.period_button.pack(side='left')
        self.equal_button.pack(side='left')

    def clear(self):
        gui_commands.clear(self.user_entry1)

    def negative_switch(self):
        gui_commands.negative_switch(self.user_entry1)

    def percent(self):
        gui_commands.percent(self.user_entry1)

    def divide(self):
        gui_commands.divide(self.user_entry1)

    def seven(self):
        gui_commands.seven(self.user_entry1)

    def eight(self):
        gui_commands.eight(self.user_entry1)

    def nine(self):
        gui_commands.nine(self.user_entry1)

    def multiply(self):
        gui_commands.multiply(self.user_entry1)

    def four(self):
        gui_commands.four(self.user_entry1)

    def five(self):
        gui_commands.five(self.user_entry1)

    def six(self):
        gui_commands.six(self.user_entry1)

    def subtract(self):
        gui_commands.subtract(self.user_entry1)

    def one(self):
        gui_commands.one(self.user_entry1)

    def two(self):
        gui_commands.two(self.user_entry1)

    def three(self):
        gui_commands.three(self.user_entry1)

    def add(self):
        gui_commands.add(self.user_entry1)

    def zero(self):
        gui_commands.zero(self.user_entry1)

    def period(self):
        gui_commands.period(self.user_entry1)

    def equals(self):
        gui_commands.equals(self.user_entry1)