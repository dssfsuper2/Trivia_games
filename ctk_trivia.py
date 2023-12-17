from random import randint
import customtkinter
import threading

global answer
global question
global questions
global right_counter
global wrong_counter
global sound


def main():
    global right_counter
    global wrong_counter
    global question
    global questions
    global answer
    import playsound
    global sound

    li = [0, 0, 0, 0]
    right_counter = 0
    wrong_counter = 0
    sound = 0

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    app = customtkinter.CTk()
    app.geometry("950x250")

    font = customtkinter.CTkFont("Calibri", 25, "bold")

    right_counter_label = customtkinter.CTkLabel(app,
                                                 font=customtkinter.CTkFont("Calibri", 22, "bold"),
                                                 text=f'{right_counter} right answers')
    wrong_counter_label = customtkinter.CTkLabel(app,
                                                 font=customtkinter.CTkFont("Calibri", 23, "bold"),
                                                 text=f'{wrong_counter} wrong answers')

    def reset():
        global right_counter
        global wrong_counter
        right_counter = 0
        wrong_counter = 0
        right_counter_label.configure(text=f'0 right answers')
        wrong_counter_label.configure(text=f'0 wrong answers')

    def do_questions():
        global questions
        questions = []
        if li.count(1) == 0:
            with open('assets/question') as file:
                for line in file.readlines():
                    questions.append(list(line.split(';')))
        if li[0] == 1:
            with open('assets/questions/chemie') as file:
                for line in file.readlines():
                    questions.append(list(line.split(';')))
        if li[1] == 1:
            with open('assets/questions/geo') as file:
                for line in file.readlines():
                    questions.append(list(line.split(';')))
        if li[2] == 1:
            with open('assets/questions/history') as file:
                for line in file.readlines():
                    questions.append(list(line.split(';')))
        if li[3] == 1:
            with open('assets/questions/math') as file:
                for line in file.readlines():
                    questions.append(list(line.split(';')))

    def sw(n):
        if li[n] == 1:
            li[n] = 0
        else:
            li[n] = 1
        do_questions()
        global question
        global answer
        num_questio = randint(0, len(questions) - 1)
        question = questions[num_questio][0]
        answer = questions[num_questio][1]
        questionlabel.configure(text=question)
        entry.delete(0, customtkinter.END)
        app.update()

    def skip():
        global question
        global answer
        num_questio = randint(0, len(questions) - 1)
        question = questions[num_questio][0]
        answer = questions[num_questio][1]
        questionlabel.configure(text=question)
        entry.delete(0, customtkinter.END)
        app.update()

    def allah():
        playsound.playsound("assets/sounds/allah.mp3")
        # this is just a joke, it does not have the purpose to insult anyone or to insult anyone's religion

    def yes():
        playsound.playsound("assets/sounds/yeah.mp3")

    def switch_sound():
        global sound

        if sound:
            sound = 0
        else:
            sound = 1

    do_questions()

    num_question = randint(0, len(questions) - 1)
    question = questions[num_question][0]
    answer = questions[num_question][1]
    app.resizable(True, False)

    switch0 = customtkinter.CTkSwitch(
        master=app,
        text="chemie",
        command=lambda: sw(0),
        font=customtkinter.CTkFont('Calibri', 17)
    )
    switch1 = customtkinter.CTkSwitch(
        master=app,
        text="geography",
        command=lambda: sw(1),
        font=customtkinter.CTkFont('Calibri', 17)
    )
    switch2 = customtkinter.CTkSwitch(
        master=app,
        text="history",
        command=lambda: sw(2),
        font=customtkinter.CTkFont('Calibri', 17)
    )
    switch3 = customtkinter.CTkSwitch(
        master=app,
        text="math",
        command=lambda: sw(3),
        font=customtkinter.CTkFont('Calibri', 17)
    )
    sound_switch = customtkinter.CTkSwitch(
        master=app,
        text="sounds",
        command=switch_sound,
        font=customtkinter.CTkFont('Arial', 15, "bold")
    )
    switch0.place(x=20, y=20)
    switch1.place(x=20, y=70)
    switch2.place(x=20, y=120)
    switch3.place(x=20, y=170)
    questionlabel = customtkinter.CTkLabel(app, font=font, text=question)
    entry = customtkinter.CTkEntry(app, 200, 30)
    skip_button = customtkinter.CTkButton(app,
                                          text="skip question",
                                          font=customtkinter.CTkFont("Calibri", 21, "bold"),
                                          command=skip)
    reset_button = customtkinter.CTkButton(app,
                                           text="reset the score",
                                           font=font,
                                           command=reset)
    skip_button.place(x=350, y=100)
    reset_button.place(x=630, y=210)

    def submit():
        global right_counter
        global wrong_counter
        global question
        global answer
        global sound

        if answer.strip().lower() == entry.get().strip().lower():
            if sound:
                thread = threading.Thread(target=yes)
                thread.start()
            right_counter += 1
        else:
            if sound:
                thread = threading.Thread(target=allah)
                thread.start()
            wrong_counter += 1
        num_questio = randint(0, len(questions) - 1)
        question = questions[num_questio][0]
        answer = questions[num_questio][1]
        right_counter_label.configure(text=f'{right_counter} right answers')
        wrong_counter_label.configure(text=f'{wrong_counter} wrong answers')
        questionlabel.configure(text=question)
        entry.delete(0, customtkinter.END)
        app.update()

    entry.bind('<Return>', lambda event: submit())
    right_counter_label.place(x=150, y=215)
    wrong_counter_label.place(x=400, y=215)
    questionlabel.place(y=50, x=150)
    entry.place(y=100, x=150)
    sound_switch.place(y=220, x=20)
    app.mainloop()


if __name__ == '__main__':
    main()
