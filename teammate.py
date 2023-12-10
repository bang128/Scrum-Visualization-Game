import pygame
import random

class Teammate():
    def __init__(self, unlocked, button, screen):
        self.screen = screen
        self.unlocked = unlocked
        self.button = button
        self.salary = 10
        self.efficiency = 25
        self.work_status = "Active"
        self.level = 0
        self.white = (255,255,255)
        self.green = (50,205,50)
        self.red = (255,0,0)
        self.max_bar_length = 110
        self.bar_height = 10
        self.progress = 0
        self.bar_ratio = 110 * (self.progress*0.01)
        self.work_speed = [0.5, 1, 2, 2.5]
        self.tasks_completed = 0
        self.max_distraction = 25
        self.current_distraction = 0
        self.attentive = True
        self.percentage_chance = [0.10, 0.05, 0.01, 0]

    def setUnlocked(self, unlocked):
        self.unlocked = unlocked

    def setButton(self, button):
        self.button = button

    def getUnlocked(self):
        return self.unlocked

    def getButton(self):
        return self.button

    def increase_salary(self):
        if self.level < 3:
            self.salary += 10
            self.efficiency += 25
            self.level += 1

    def get_salary(self):
        return self.salary

    def get_efficiency(self):
        return self.efficiency

    def get_work_status(self):
        return self.work_status

    def get_stats(self):
        temp = [self.salary, self.efficiency, self.attentive, self.tasks_completed]
        return temp

    def is_upgradable(self):
        if self.level < 3:
            return True
        return False

    def make_bar(self):
        if self.attentive:
            bar = pygame.Rect(self.button.x, self.button.y - 10, self.bar_ratio, self.bar_height)
            pygame.draw.rect(self.screen, self.green, bar)
            bar_frame = pygame.Rect(self.button.x, self.button.y - 10, self.max_bar_length, self.bar_height)
            pygame.draw.rect(self.screen, self.white, bar_frame, 1)
        else:
            bar = pygame.Rect(self.button.x, self.button.y - 10, self.bar_ratio, self.bar_height)
            pygame.draw.rect(self.screen, self.red, bar)
            bar_frame = pygame.Rect(self.button.x, self.button.y - 10, self.max_bar_length, self.bar_height)
            pygame.draw.rect(self.screen, self.white, bar_frame, 1)

    # def set_progress(self, value):
    #     if value <= 100:
    #         self.progress = value
    #         self.bar_ratio = 110 * (self.progress*0.01)
    #     else:
    #         self.progress = 0

    def action(self, score):
        if self.attentive:
            return self.do_work(score)
        else:
            self.do_distraction()

        return score

    def do_work(self, score):
        if self.progress + self.work_speed[self.level] <= 100:
            self.progress += self.work_speed[self.level]
            self.bar_ratio = 110 * (self.progress*0.01)
            if random.random() < self.percentage_chance[self.level]:
                self.attentive = False
        else:
            self.progress = 0
            self.tasks_completed += 1
            return score + 1

        return score

    def do_distraction(self):
        if self.current_distraction + self.work_speed[self.level] <= self.max_distraction:
            self.current_distraction += self.work_speed[self.level]
        else:
            self.current_distraction = 0
            self.attentive = True

    def get_projects_completed(self):
        return self.tasks_completed

