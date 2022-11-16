class QuizBrain:
    def __init__(self, question_data):
        self.question_number = 0
        self.question_list = question_data
        self.score = 0
        self.question_amount = 0

    def still_has_questions(self):
        return self.question_number + 1 <= self.question_amount

    def quiz_amount_choice(self):
        try:
            self.question_amount = int(input("How many questions would you like? "
                                             "[N.B: Maximum amount of question is 50]: "))
        except ValueError:
            print("You should enter the amount in number eg: 10 or 45")

    def next_question(self):
        while self.question_number < self.question_amount:
            question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").upper()
            self.check_answer(user_answer, question.answer)
            print()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong.")
            print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
