from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = [
    Question(obj["question"], obj["correct_answer"]) for obj in question_data
]

quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score was: {quiz.score}/{len(question_bank)}")
