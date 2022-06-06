class Quizbrain:
    def __init__(self, input_list) -> None:
        self.question_number = 0
        self.question_list = input_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_answer = input(
            f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: "
        )
        correct_answer = self.question_list[self.question_number].answer
        self.check_answer(user_answer, correct_answer)
        self.question_number += 1

    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            print("You got it right")
            self.score += 1
        else:
            print(f"That is wrong")
        print(f"The correct answer was {correct}")
        print(f"Your current score is {self.score}/{self.question_number}")
