import time
import tkinter

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR)
        # self.window.geometry("340x500")

        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, font=("Ariel", 13, "bold"), fg="white")
        self.score_label.grid(column=1, row=0, pady=(20, 0))

        self.question_canvas = tkinter.Canvas(width=300, height=250, bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125, width=300, justify="center",  text="question", font=FONT)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        image_correct = tkinter.PhotoImage(file="images/true.png")
        self.button_correct = tkinter.Button(image=image_correct,
                                             highlightthickness=0,
                                             borderwidth=0,
                                             command=self.answer_true)
        self.button_correct.grid(column=0, row=2, pady=20)

        image_wrong = tkinter.PhotoImage(file="images/false.png")
        self.button_wrong = tkinter.Button(image=image_wrong,
                                           highlightthickness=0,
                                           borderwidth=0,
                                           command=self.answer_false)
        self.button_wrong.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def make_canvas_white(self):
        self.question_canvas.config(bg="white")

    def get_next_question(self):
        self.make_canvas_white()
        self.enable_buttons()

        if self.quiz.still_has_questions():
            question = self.quiz.next_question()

            self.question_canvas.itemconfig(self.question_text, text=question)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"Game Over\nYour score is {self.quiz.score}/10")
            self.disable_buttons()

    def answer_false(self):
        answer_is_correct = self.quiz.check_answer(user_answer="False")

        self.update_scoreboard()
        self.flash_screen(answer_is_correct)
        self.disable_buttons()

        self.window.after(1000, self.get_next_question)

    def answer_true(self):
        answer_is_correct = self.quiz.check_answer(user_answer="True")

        self.update_scoreboard()
        self.flash_screen(answer_is_correct)
        self.disable_buttons()

        self.window.after(1000, self.get_next_question)

    def update_scoreboard(self):
        new_score = self.quiz.score
        self.score_label.config(text=f"Score: {new_score}")

    def flash_screen(self, answer_is_correct: bool):
        if answer_is_correct:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        # self.window.after(1000, self.make_canvas_white)

    def disable_buttons(self):
        self.button_wrong.config(state="disabled")
        self.button_correct.config(state="disabled")

    def enable_buttons(self):
        self.button_wrong.config(state="active")
        self.button_correct.config(state="active")
