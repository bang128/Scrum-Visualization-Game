import pygame
import sys
from pygame.locals import *
from message import Message

class ScrumMasterMessage(Message):
    def __init__(self, screen, index):
        super().__init__(screen, 100, 200, 700, 300)
        self.index = index
        # Check team process
        message1 = ["Our team are working very well. We have done many stories.",
                    "Let's try our best to complete all stories by the end of this sprint!"]

        # Assign tasks
        message2 = ["Product Owner will be responsible for communicating with stakeholders",
                    "and customers to get their feedback and updated requirement. ",
                    "Teammate will be responsible for developing, testing and debugging ",
                    "the program. I will keep track of our project and be willing to help ",
                    "if you have any issues."]

        # Host Scrum meeting
        message3 = ["Scrum meeting replenishes team morale and put the team", "back on track!"]

        # Increase Salary
        message4 = ["With more salary, scrum master is more passionate to ",
                    "facilitate team dynamics and work efficiency!"]
        self.messages = [message1, message2, message3, message4]
        # self.action(self.messages[index])

    def do_action(self):
        self.action(self.messages[self.index])

class ProductOwnerMessage(Message):
    def __init__(self, screen, index):
        super().__init__(screen, 100, 200, 700, 300)
        self.index = index
        # Present customer requirements
        message1 = ["The customer is very satisfied with our program's operation.",
                    "However, they still want us to change background and text's ",
                    "colors to make them more visible."]

        # Develop user stories
        message2 = ["I think to meet the customers' requirements, we need to break",
                    "down story 5 and story 6 into smaller ones, and add more ",
                    "acceptance criteria."]

        # Give feedback
        message3 = ["Our team are working very well to meet initial requirements, ",
                    "but the requirements are frequently updated, so we need to",
                    "work harder and try to get the customer's feedback to fix ",
                    "our program."]

        message4 = ["With more salary, product owner can increase customer ",
                    "satisfaction and improve sprint demo"]

        self.messages = [message1, message2, message3, message4]
        # self.action(self.messages[index])

    def do_action(self):
        self.action(self.messages[self.index])

class TeammateMessage(Message):
    def __init__(self, screen, index):
        super().__init__(screen, 100, 200, 700, 300)
        self.index = index
        self.stats = []
        self.salary = ""
        self.efficiency = ""
        self.work_status = ""
        self.tasks_completed = ""
        message1 = [self.salary,self.efficiency, self.work_status, self.tasks_completed]
        message2 = ["This teammate wants to do more work at the cost of $10", "increase in salaries!"]
        message3 = ["This teammate complies with the scrum master for attending!"]

        self.messages = [message1, message2, message3]
        # self.action(self.messages[index])

    def set_stats(self, stats):
        self.stats = stats
        self.salary = "Salary: " + str(self.stats[0])
        self.efficiency = "Efficiency: " + str(self.stats[1])
        self.work_status = "Working: " + str(self.stats[2])
        self.tasks_completed = "Tasks completed: " + str(self.stats[3])
        self.messages[0] = [self.salary,self.efficiency, self.work_status, self.tasks_completed]

    def set_upgrade_message(self):
        message2 = ["This teammate wants to do more work at the cost of $10", "increase in salaries!", "Salary: $"+ str(self.stats[0] - 10) + " -> $" + str(self.stats[0]),
                    "Efficiency: "+ str(self.stats[1] - 25) + " -> " + str(self.stats[1])]
        self.messages[1] = message2

    def not_enough_message(self):
        message2 = ["Not enough money for upgrade"]
        self.messages[1] = message2

    def max_level_reached(self):
        message2 = ["Teammate is at the maximum salary!"]
        self.messages[1] = message2

    def do_action(self):
        self.action(self.messages[self.index])

class TeammateLock(Message):
    def __init__(self, screen):
        super().__init__(screen, 200, 230, 500, 200)
        self.request = ["To unlock, you need to pay $20.", "Do you want to unlock this teammate?"]
        self.unlock = False
        # create unlock button
        self.unlockButton = pygame.Rect(self.xPos + 300, self.yPos + 155, 70, 25)
        pygame.draw.rect(screen, (51, 153, 255), self.unlockButton)
        font = pygame.font.SysFont('Arial', 15, bold=True)
        self.draw_text('Unlock', font, self.textColor, self.screen, self.xPos + 310, self.yPos + 158)
        # self.action(self.request)

    def action(self):
        while self.running:
            self.writeMessage(self.request)
            self.handleCloseButton()

            mouseX, mouseY = pygame.mouse.get_pos()
            if self.unlockButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    print("Unlock")
                    self.unlock = True
                    self.running = False

            self.handleClick()

            pygame.display.update()
            self.clock.tick(60)

    def getUnLock(self):
        return self.unlock