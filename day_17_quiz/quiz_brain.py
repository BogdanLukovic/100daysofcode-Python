from question_model import Question
# ask question
# check if answer was correct
# check if end of quiz


class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):

        selected_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input("Q.{}: {} (True/False)? ".format(self.question_number, selected_question.text))
        self.check_answer(answer, selected_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}.")

        print(f"Your score is {self.score} / {self.question_number}.\n")
