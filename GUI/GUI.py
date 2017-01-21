from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self, master, controller):
        """
        :param master: tkinter window
        :param controller: Controller
        """
        self.__master = master
        self.__master.resizable(width=FALSE, height=FALSE)
        self.__master.wm_title("Rock Paper Scissors")
        self.__ctrl = controller
        self.__create_variable()
        self.__create_widgets()

    def __create_variable(self):
        attr = self.__ctrl.get_param()
        self.__wins = int(attr[0])
        self.__draws = int(attr[1])
        self.__loses = int(attr[2])

    def __create_widgets(self):
        # Title
        Label(self.__master, text='~ Rock Paper Scissors ~', font=20).grid(row=0, column=0, columnspan=3)
        Frame(self.__master, height=2, bg='black').grid(row=2, columnspan=3, sticky=EW)
        # The game
        Button(self.__master, text='Rock', command=self.__set_rock, width=7).grid(row=1, column=0, sticky=EW)
        Button(self.__master, text='Paper', command=self.__set_paper, width=7).grid(row=1, column=1, sticky=EW)
        Button(self.__master, text='Scissors', command=self.__set_scissors, width=7).grid(row=1, column=2, sticky=EW)
        # Score
        self.__reload_score()
        # Menu
        Frame(self.__master, height=2, bg='black').grid(row=4, columnspan=3, sticky='WE')
        Button(self.__master, text='Rules', command=self.__help).grid(row=5, column=0, sticky='WE')
        Button(self.__master, text='Reset', command=self.__restart).grid(row=5, column=1, sticky='WE')
        Button(self.__master, text='EXIT', command=self.__quit).grid(row=5, column=2, sticky='WE')
        Frame(self.__master, height=1, bg='black').grid(row=6, columnspan=3, sticky='WE')
        # Credits
        Label(self.__master, text='© 2016 Senciuc Serban - Vasile').grid(row=7, columnspan=3, sticky='EW')

    @staticmethod
    def __help():
        top_help = Toplevel()
        Label(top_help, text=' - Rules - ', font=('Arial Black', 20), fg='Blue').pack()
        photo = PhotoImage(file='Data/image.png')
        photo.subsample(50, 50)
        w = Label(top_help, image=photo)
        w.photo = photo
        w.pack()
        Button(top_help, text='Quit', command=top_help.destroy).pack(fill=X)

    def __set_rock(self):
        self.__run_app(1)

    def __set_paper(self):
        self.__run_app(2)

    def __set_scissors(self):
        self.__run_app(3)

    def __restart(self):
        if messagebox.askquestion('Reset', 'Are you sure to reset the score?\n') == 'yes':
            self.__wins = 0
            self.__draws = 0
            self.__loses = 0
            self.__reload_score()

    def __reload_score(self):
        Label(self.__master, text='Wins: %s | Draws: %s | Loses: %s' % (self.__wins, self.__draws, self.__loses)).grid(row=3, columnspan=3, sticky='WE')

    def __run_app(self, choice):
        if self.__ctrl.decision(choice) == 0:
            self.__draws += 1
            self.__reload_score()
            if messagebox.askquestion('Draw', 'It was draw!\nDo you want to play one more?') == 'no':
                self.__quit()
        elif self.__ctrl.decision(choice) == 1:
            self.__wins += 1
            self.__reload_score()
            if messagebox.askquestion('Congratulations', 'You win!\nDo you want to play one more?') == 'no':
                self.__quit()
        else:
            self.__loses += 1
            self.__reload_score()
            if messagebox.askquestion('I am sorry', 'The computer win!\nDo you want to play one more?') == 'no':
                self.__quit()

    def __quit(self):
        attr = str(self.__wins) + ';' + str(self.__draws) + ';' + str(self.__loses)
        self.__ctrl.save(attr)
        self.__master.destroy()
