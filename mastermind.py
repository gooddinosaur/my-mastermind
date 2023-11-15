import random


class Setup_game:
    def __init__(self, num_position, num_color, _duplicate):
        self.num_position = num_position
        self.num_color = num_color
        self.answer = []
        self.du = _duplicate

    def create_answer(self):
        if self.du == "yes":
            for i in range(self.num_position):
                n = random.randint(1, self.num_color)
                self.answer.append(str(n))
        elif self.du == "no":
            _list = []
            while len(_list) != self.num_position:
                n = random.randint(1, self.num_color)
                if n not in _list:
                    _list.append(n)
            for k in _list:
                self.answer.append(str(k))
        return self.answer


class Play_game:
    def __init__(self, answer_list, guess_number):
        self.ans = answer_list
        self.guess = guess_number

    def checker(self):





color = int(input("Enter number of color: "))
position = int(input("Enter number of postion: "))
duplicate = input("Do you want duplicate?(yes/no): ")
setup = Setup_game(position, color, duplicate)
answer = Setup_game.create_answer(setup)

