class Stats:
    def __init__(self):
        self.money = 100
        self.morale = 100
        self.velocity = 100

    def add_money(self, value):
        self.money += value

    def subtract_money(self, value):
        if self.money - value >= 0:
            self.money -= value
            print("Subtracted", value)
            return True
        else:
            print("Not enough money!")
            return False

    def add_morale(self, value):
        if self.morale + value > 100:
            self.morale = 100
        else:
            self.morale += value

    def subtract_morale(self, value):
        if self.morale - value >= 0:
            self.morale -= value
        else:
            self.morale = 0

    def add_velocity(self, value):
        self.velocity += value

    def subtract_velocity(self, value):
        if self.velocity - value >= 0:
            self.velocity -= value
        else:
            self.velocity = 0

    def get_money(self):
        return self.money

    def get_morale(self):
        return self.morale

    def get_velocity(self):
        return self.velocity

class Salary:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

