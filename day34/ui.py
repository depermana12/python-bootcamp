import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = tk.Label(text=f"Score: {0}", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.label.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text_holder = self.canvas.create_text(
            150,
            125,
            width=280,
            text="hello this is example",
            fill="black",
            font=("Arial", 10, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        check_image = tk.PhotoImage(file="images/true.png")
        self.button_correct = tk.Button(image=check_image, highlightthickness=0, command=self.true_button)
        self.button_correct.grid(row=2, column=0)
        cross_image = tk.PhotoImage(file="images/false.png")
        self.button_wrong = tk.Button(image=cross_image, highlightthickness=0, command=self.wrong_button)
        self.button_wrong.grid(row=2, column=1)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        self.label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text_holder, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text_holder, text="You've reached the end of the questions")
            self.button_correct.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def true_button(self):
        self.answer_feedback(self.quiz.check_answer("True"))

    def wrong_button(self):
        self.answer_feedback(self.quiz.check_answer("False"))

    def answer_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
