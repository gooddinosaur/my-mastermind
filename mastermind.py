import copy
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
        checker = ""
        guess_list = []
        for i in self.guess:
            guess_list.append(i)
        if guess_list == self.ans:
            for x in range(len(guess_list)):
                checker += "*"
            return checker
        count_all_correct = 0
        count_half_correct = 0
        for x in range(len(guess_list)):
            if guess_list[x] == self.ans[x]:
                count_all_correct += 1

            elif guess_list[x] in self.ans and guess_list[x] != self.ans[x]:
                count_half_correct += 1
        checker += "*"*count_all_correct
        checker += "o"*count_half_correct
        return checker

    def hint(self, index):
        if index == 0:
            return f"First color is {self.ans[index]}"
        elif index == 1:
            return f"Second color is {self.ans[index]}"
        elif index == 2:
            return f"Third color is {self.ans[index]}"
        elif index == 3:
            return f"Fourth color is {self.ans[index]}"








color = int(input("Enter number of color: "))
position = int(input("Enter number of postion: "))
duplicate = input("Do you want duplicate?(yes/no): ")
setup = Setup_game(position, color, duplicate)
count = 1
answer = Setup_game.create_answer(setup)
guess_num = ""
answer_str = ""
for i in answer:
    answer_str += i
while guess_num != answer_str:
    guess_num = input("What is your guess?: ")
    g = Play_game(answer, guess_num)
    checker = Play_game.checker(g)
    print(f"Your guess is {guess_num}")
    print(checker)
    if guess_num == answer_str:
        break
    count += 1
    if count > 3:
        hint = input("Do you  want a hint ?(y/n): ")
        if hint == "y":
            index = random.randint(0,4)
            print(Play_game.hint(g, index))
        elif hint == "n":
            pass

print()
print(f"You solve it after {count} rounds")
