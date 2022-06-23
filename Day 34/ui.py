THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *
import html


class QuizInterface:
    def __init__(self, quizBrain: QuizBrain) -> None:
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=50)
        self.window.config(bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.false_img_location = (
            "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 34/false.png"
        )
        self.true_img_location = (
            "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 34/true.png"
        )
        self.true_image = PhotoImage(file=self.true_img_location)
        self.false_image = PhotoImage(file=self.false_img_location)
        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}", bg=THEME_COLOR, fg="white"
        )
        self.score_label.grid(row=0, column=1)
        self.true_button = Button(
            image=self.true_image, highlightthickness=0, command=self.check_answer_true
        )
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.check_answer_false,
        )
        self.false_button.grid(row=2, column=1)
        self.true_button.grid(row=2, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz!"
            )
        q_text = self.quiz.next_question()
        fixedtext = html.escape(q_text)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        print(fixedtext)
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, isRight):
        if isRight:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
