"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-inheritance/problem
"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def __get_avg(self):
        avg = self.scores[0]
        score_size = len(self.scores)

        if score_size > 1:
            count = 1
            while count < score_size:
                avg += self.scores[count]
                count += 1

            avg /= count

        return avg

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = self.__get_avg()

        score_map = {
            'O': (90, 100),
            'E': (80, 89),
            'A': (70, 79),
            'P': (55, 69),
            'D': (40, 54)
        }

        for k, v in score_map.items():
            if avg >= v[0] and avg <= v[1]:
                return k
        else:
            return 'T'