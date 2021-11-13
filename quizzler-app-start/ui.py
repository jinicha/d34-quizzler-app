from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create a label
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        # create canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="question goes here", width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # create two buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.next_question()
        self.answer_true()
        self.answer_false()

        self.window.mainloop()

    def next_question(self):
        self.score.config(text=f'Score: {self.quiz.score}')
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question, text=self.quiz.next_question())

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)
