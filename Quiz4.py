class word:
    def __init__(self, word, ex1, ex2, answer):
        self.word = word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer


    def show_question(self):
        print(f"\" {self.word}\"의 뜻은?")
        print("1." + self.ex1)
        print("2." + self.ex2)

    def check_answer(self):
        if user_input == self.answer:
            print("정답")
        else:
            print("오답")

word = word("애빼시", "애교 빼면 시체", "애들은 빼빼로 시시해")
word.show_question()
word.check_answer(int(input("=> ")))