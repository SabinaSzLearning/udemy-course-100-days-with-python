THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text='Score 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Test",
                                                     font=("Ariel", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image_right = PhotoImage(file=".\images\\true.png")
        self.button_right = Button(image=image_right, highlightthickness=0, command=self.true_pressed)
        self.button_right.grid(row=2, column=0)

        image_wrong = PhotoImage(file=".\images\\false.png")
        self.button_wrong = Button(image=image_wrong, highlightthickness=0,command=self.false_pressed)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.score.config(text=f"Score = {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="All questions completed")
            self.button_right.config(state='disabled')
            self.button_wrong.config(state='disabled')

    def true_pressed(self):
        answer = self.quiz.check_answer('True')
        self.get_feedback(answer)

    def false_pressed(self):
        answer = self.quiz.check_answer('False')
        self.get_feedback(answer)

    def get_feedback(self, answer):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


