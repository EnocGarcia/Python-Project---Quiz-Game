"""Game Engine"""
import html
from question_model import Question


class QuizBrain:
    """Game Engine Class"""

    def __init__(self, q_list: list[Question]):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[0]

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            #     print("You got it right!")
            return True
        else:
            #     print("That's wrong.")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
