from random import randint


class Controller:
    def __init__(self, repository):
        """
        :param repository: Repository
        """
        self.__repo = repository

    @staticmethod
    def __random():
        """
        :return random int from 1 to 100: int
        """
        return randint(1, 100)

    def __computer_choice(self):
        """
        :return 1: if the choice is between 0 and 33
        :return 2: if the choice is between 34 and 66
        :return 3: if the choice is between 67 and 100
        """
        choice = self.__random()
        if choice <= 33:
            return 1
        elif choice <= 66:
            return 2
        else:
            return 3

    def decision(self, choice):
        """
        :param choice: int
        :return -1: if the computer win
        :return 0: if is tie
        :return 1: if the player win
        """
        pc_choice = self.__computer_choice()
        # Tie
        if pc_choice == choice:
            return 0
        # pc_choice is rock
        elif pc_choice == 1:
            if choice == 3:
                return -1
            else:
                return 1
        # pc_choice is paper
        elif pc_choice == 2:
            if choice == 1:
                return -1
            else:
                return 1
        # pc_choice is scissors
        elif pc_choice == 3:
            if choice == 2:
                return -1
            else:
                return 1

    def get_param(self):
        """
        :return list with parameters: list
        """
        return self.__repo.get_param()

    def save(self, attr):
        """
        :param attr: String
        """
        self.__repo.save(attr)
