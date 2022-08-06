from calculator_gui import *


def main() -> None:
    """
    Main function that opens the calculator gui
    :return: None
    """
    window = Tk()
    window.title('CALCULATOR')
    window.geometry('200x190')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()