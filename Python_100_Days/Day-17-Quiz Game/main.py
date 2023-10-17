from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
questions = question_data['results']

for question in questions:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

que = QuizBrain(question_bank)

while que.still_has_questions():
    que.next_question()

print('You have completed the quiz!')
print(f'Final score: {que.score}/{que.question_number}')