"""GUI Inteface"""
from tkinter import Tk, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_QUESTION = ("Arial", 20, "italic")
FONT_OTHERS = ("Arial", 15, " italic")


class QuizGUI:
    """GUI Class developed on Tkinter for the Quiz App"""

    def __init__(self, engine: QuizBrain) -> None:
        self.engine = engine

        self.window = Tk()
        self.window.title("Quiz Game App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text=f"Score: {self.engine.score}",
            font=FONT_OTHERS,
            bg=THEME_COLOR,
            fg="white",
        )
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(
            width=300,
            height=350,
            bg="white",
        )
        self.question_text = self.question_canvas.create_text(
            150,
            175,
            width=290,
            text="",
            font=FONT_QUESTION,
            fill=THEME_COLOR,
        )
        self.question_canvas.grid(column=0, columnspan=2, row=1, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            borderwidth=0,
            bg=THEME_COLOR,
            command=self._true,
        )
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            borderwidth=0,
            bg=THEME_COLOR,
            command=self._false,
        )
        self.false_button.grid(column=1, row=2)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        q_text = self.engine.next_question()
        self.question_canvas.config(bg="white")
        self.question_canvas.itemconfig(self.question_text, text=f"{q_text}")

    def finish(self):
        self.question_canvas.config(bg="white")
        self.question_canvas.itemconfig(
            self.question_text,
            text="You've completed the quiz\n"
            f"Your final score is {self.engine.score}/{self.engine.question_number}",
        )
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def feedback(self, answer: bool):
        if answer:
            self.question_canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.engine.score}")
        else:
            self.question_canvas.config(bg="red")

        if self.engine.still_has_questions():
            self.window.after(1000, func=self.get_question)
        else:
            self.window.after(1000, func=self.finish)

    def _true(self):
        answer = self.engine.check_answer("True")
        self.feedback(answer)

    def _false(self):
        answer = self.engine.check_answer("False")
        self.feedback(answer)
