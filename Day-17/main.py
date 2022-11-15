from question_model import Question
from data import question_data

question_bank = []

for items in question_data:
    question_bank_data = Question(items["text"], items["answer"])
    question_bank.append(question_bank_data)
print(question_bank[0].answer)