import pygame
import scrum_message
from statistics import Stats
from statistics import Salary
from message import Message
from window import Window
from panel import Sprite
from game_over_pane import GameOver
from teammate import Teammate


class Game(Window):
    def __init__(self):
        super().__init__("Game")

        self.panelFont = pygame.font.SysFont('Arial', 15, bold=True)
        self.panelColor = (250, 0, 0)
        self.textColor = (255, 255, 255)

        # Resource panel
        self.stats = Stats()
        self.resourceShown = False
        self.morale = self.stats.get_morale()
        self.money = self.stats.get_money()
        self.velocity = self.stats.get_velocity()

        # Day and Time panel
        self.timeShown = False
        self.totalSprints = 2
        self.curSprint = 2
        self.totalDays = 3
        self.curDay = 3
        self.curTime = [0, 0]  #[hour, min]

        # Score panel
        self.scoreShown = False
        # self.totalStories = 100
        self.doneProject = 0
        self.customerSatisfaction = 50
        self.score = 0


        # ScrumMaster panel
        self.scrumMasterShown = False
        self.scrumMasterButton = None
        self.scrumMasterSalary = Salary("ScrumMaster", 100)

        # ProductOwner panel
        self.productOwnerShown = False
        self.productOwnerButton = None
        self.productOwnerSalary = Salary("ProductOwner", 100)

        # Teammates panel
        self.teammateShown = [False, False, False, False, False]
        self.teammateOptions = None
        # self.teammateButton = None

        # Teammate
        self.teammates = [Teammate(True, None, self.screen), Teammate(True, None, self.screen),
                          Teammate(False, None, self.screen), Teammate(False, None, self.screen), Teammate(False, None,self.screen)]

        # Locked Teammate
        lock1 = pygame.Rect(140, 480, 110, 25)
        lock2 = pygame.Rect(420, 650, 110, 25)
        lock3 = pygame.Rect(550, 600, 110, 25)

        self.locks = [lock1, lock2, lock3]

        self.playing_sfx = True
        self.progress = 0
        # self.game()

    def game(self):

        #functions for score
        def getScore():
            return self.score
        def getProjectDone():
            return self.doneProject
        def getCustomerSatisfaction():
            return self.customerSatisfaction
        def updateProjectDone():
            self.doneProject += 1
        def updateCustomerSatisfaction(newCustSat):
            self.customerSatisfaction = (self.customerSatisfaction+newCustSat)/2
        def updateScore():
            self.score=self.doneProject*self.customerSatisfaction

        running = True
        while running:
            self.screen.fill((42, 131, 247))
            background = pygame.image.load("images/office.jpg")
            self.screen.blit(background, (150, 200))

            mouseX, mouseY = pygame.mouse.get_pos()
            self.createReturnButton()

            quitButton = self.createGameButton(120, 700, 100, 25, 'QUIT', 150, 703)
            temp_gameoverButton = self.createGameButton(230, 700, 100, 25, 'Gameover', 244, 703)
            productOwner = self.createGameButton(600, 230, 110, 25, 'Product Owner', 600, 233)
            scrumMaster = self.createGameButton(680, 420, 110, 25, 'Scrum Master', 685, 423)
            teammate1 = self.createGameButton(320, 250, 110, 25, 'Teammate', 340, 253)
            teammate2 = self.createGameButton(210, 310, 110, 25, 'Teammate', 230, 313)
            resourceButton = self.createGameButton(245, 20, 100, 30, 'Resource', 260, 26)
            timeButton = self.createGameButton(405, 20, 100, 30, 'Day & Time', 415, 26)
            scoreButton = self.createGameButton(565, 20, 100, 30, 'Score', 595, 26)

            if self.locks[0]:
                self.createGameButton(self.locks[0].x, self.locks[0].y, self.locks[0].w, self.locks[0].h, 'Lock', 180,
                                      483)
            if self.locks[1]:
                self.createGameButton(self.locks[1].x, self.locks[1].y, self.locks[1].w, self.locks[1].h, 'Lock', 460,
                                      653)
            if self.locks[2]:
                self.createGameButton(self.locks[2].x, self.locks[2].y, self.locks[2].w, self.locks[2].h, 'Lock', 590,
                                      603)

            self.teammates[0].setButton(teammate1)
            self.teammates[1].setButton(teammate2)
            self.teammates[0].make_bar()
            self.teammates[1].make_bar()
            self.score = self.teammates[0].action(self.score)
            self.score = self.teammates[1].action(self.score)

            for i in range(2, 5):
                if self.teammates[i].getUnlocked():
                    if self.locks[i - 2]:
                        button = self.createGameButton(self.locks[i - 2].x, self.locks[i - 2].y, 110, 25, 'Teammate',
                                                       self.locks[i - 2].x + 20, self.locks[i - 2].y + 3)
                        self.locks[i - 2] = None
                    else:
                        temp = self.teammates[i].getButton()
                        button = self.createGameButton(temp.x, self.teammates[i].getButton().y, 110, 25, 'Teammate',
                                                       temp.x + 20, temp.y + 3)
                    self.teammates[i].setButton(button)
                    self.teammates[i].make_bar()
                    self.score = self.teammates[i].action(self.score)
                    #self.score += self.teammates[i].get_projects_completed()

            # clicking on return
            if self.returnButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("Menu")
                    # main_menu.Menu(True)
                    running = False

            # clicking on quit
            if quitButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("Quit\n")
                    exit()
            # clicking on gameover
            if temp_gameoverButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("Gameover\n")
                    Message(self.screen, 350, 230, 225, 150).action(["GAME OVER"])
                    GameOver(self.score, self.customerSatisfaction, self.doneProject)
            # clicking on productOwner
            elif productOwner.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("ProductOwner\n")
                    if not self.productOwnerShown:
                        self.productOwnerShown = True
                    else:
                        self.productOwnerShown = False

            # clicking on scrumMaster
            elif scrumMaster.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("scrumMaster\n")
                    if not self.scrumMasterShown:
                        self.scrumMasterShown = True
                    else:
                        self.scrumMasterShown = False

            elif resourceButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("resource\n")
                    if not self.resourceShown:
                        self.resourceShown = True
                    else:
                        self.resourceShown = False

            # clicking on day&time
            elif timeButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("time\n")
                    if not self.timeShown:
                        self.timeShown = True
                    else:
                        self.timeShown = False

            # clicking on score
            elif scoreButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("score\n")
                    if not self.scoreShown:
                        self.scoreShown = True
                    else:
                        self.scoreShown = False

            # clicking on resource

            # check if clicking on teammate
            for i in range(len(self.teammates)):
                if self.teammates[i].getButton():
                    if self.teammates[i].getButton().collidepoint((mouseX, mouseY)) and self.click:
                        print("teammate\n")
                        self.sound.play_ui_click(self.playing_sfx)
                        if not self.teammateShown[i]:
                            self.teammateShown[i] = True
                        else:
                            self.teammateShown[i] = False

            # check if clicking on lock
            for i in range(len(self.locks)):
                if self.locks[i] and self.locks[i].collidepoint((mouseX, mouseY)):
                    if self.click:
                        self.sound.play_ui_click(self.playing_sfx)
                        temp = scrum_message.TeammateLock(self.screen)
                        temp.set_sfx(self.playing_sfx)
                        temp.action()
                        if temp.getUnLock():
                            self.sound.play_ui_click(self.playing_sfx)
                            self.stats.subtract_money(20)
                            self.teammates[i + 2].setUnlocked(True)

            # Show panel content
            if self.resourceShown:
                text1 = "Team morale: " + str(self.stats.get_morale())
                text2 = "Money: $" + str(self.stats.get_money())
                text3 = "Velocity: " + str(self.stats.get_velocity())
                self.drawPanel([text1, text2, text3], 240, 60, False, 0)

            if self.timeShown:
                text1 = "Current sprint: " + str(self.curSprint) + "/" + str(self.totalSprints)
                text2 = "Current day: " + str(self.curDay) + "/" + str(self.totalDays)
                text3 = "Current time: " + str(self.curTime[0]) + ":" + str(self.curTime[1])
                self.drawPanel([text1, text2, text3], 400, 60, False, 0)

            if self.scoreShown:
                text1 = "Done Project: " + str(self.doneProject)
                text2 = "Customer Satisfaction: " + str(self.customerSatisfaction) +"%"
                text3 = "Score: " + str(self.score)
                self.drawPanel([text1, text2, text3], 560, 60, False, 0)

            if self.scrumMasterShown:
                text1 = "Check team process"
                text2 = "Assign tasks"
                text3 = "Host scrum meetings"
                text4 = "Increase salary"
                self.scrumMasterButton = self.drawPanel([text1, text2, text3, text4], 700, 450, True, 150)
                if self.scrumMasterButton:
                    for i in range(len(self.scrumMasterButton)):
                        if self.scrumMasterButton[i].collidepoint((mouseX, mouseY)):
                            if self.click:
                                self.sound.play_ui_click(self.playing_sfx)
                                temp = scrum_message.ScrumMasterMessage(self.screen, i)
                                if i == 3:
                                    salary = self.scrumMasterSalary.getSalary()
                                    if self.stats.subtract_money(20):
                                        temp.setSalaryMessage([salary, salary + 20])
                                        self.scrumMasterSalary.setSalary(salary + 20)
                                    else: temp.setSalaryMessage([salary, 0])
                                temp.set_sfx(self.playing_sfx)
                                temp.do_action()

            if self.productOwnerShown:
                text1 = "Present customer requirements"
                text2 = "Develop user stories"
                text3 = "Give feedback"
                text4 = "Increase salary"
                self.productOwnerButton = self.drawPanel([text1, text2, text3, text4], 650, 120, True, 220)
                if self.productOwnerButton:
                    for i in range(len(self.productOwnerButton)):
                        if self.productOwnerButton[i].collidepoint((mouseX, mouseY)):
                            if self.click:
                                self.sound.play_ui_click(self.playing_sfx)
                                temp = scrum_message.ProductOwnerMessage(self.screen, i)
                                if i == 3:
                                    salary = self.productOwnerSalary.getSalary()
                                    if self.stats.subtract_money(20):
                                        temp.setSalaryMessage([salary, salary + 20])
                                        self.productOwnerSalary.setSalary(salary + 20)
                                        if self.customerSatisfaction < 100:
                                            self.customerSatisfaction += 10
                                    else: temp.setSalaryMessage([salary, 0])
                                temp.set_sfx(self.playing_sfx)
                                temp.do_action()
                                # scrum_message.ProductOwnerMessage(self.screen, i)

            for i in range(len(self.teammateShown)):
                if self.teammateShown[i]:
                    text1 = "My Details"
                    text2 = "Increase salary"
                    text3 = "Attend Scrum meeting"
                    pos = None
                    if i == 0: pos = [250, 150]
                    elif i == 1: pos = [10, 270]
                    elif i == 2: pos = [20, 520]
                    elif i == 3: pos = [550, 670]
                    elif i == 4: pos = [670, 580]
                    self.teammateOptions = self.drawPanel([text1, text2, text3], pos[0], pos[1], True, 170)
                    if self.teammateOptions:
                        for j in range(len(self.teammateOptions)):
                            if self.teammateOptions[j].collidepoint((mouseX, mouseY)):
                                if self.click:
                                    self.sound.play_ui_click(self.playing_sfx)
                                    temp = scrum_message.TeammateMessage(self.screen, j)
                                    if j == 0:
                                        temp.set_stats(self.teammates[i].get_stats())
                                    if j == 1:
                                        if self.teammates[i].is_upgradable():
                                            if self.stats.subtract_money(10):
                                                self.teammates[i].increase_salary()
                                                temp.set_stats(self.teammates[i].get_stats())
                                                temp.set_upgrade_message()
                                            else:
                                                temp.not_enough_message()
                                        else:
                                            temp.max_level_reached()

                                    temp.set_sfx(self.playing_sfx)
                                    temp.do_action()


            self.handle_click()
            self.curTime[1] += 1
            if self.curTime[1] == 60:
                self.curTime[0] += 1
                self.curTime[1] = 0

            if self.curTime[0] == 24:
                self.curTime[0] = 0
                self.curDay += 1

            if self.curDay > self.totalDays:
                self.curDay = 1
                self.curSprint += 1

            if self.curSprint > self.totalSprints:
                Message(self.screen, 350, 230, 225, 150).action(["GAME OVER"])
                GameOver(self.score, self.customerSatisfaction, self.doneProject)

    def drawPanel(self, arrText, xPos, yPos, needButton, distance):
        i = 0
        all_sprites_list = pygame.sprite.Group()
        arrButton = None
        for text in arrText:
            object = Sprite(text, self.screen, xPos, yPos + i * 25)
            all_sprites_list.add(object)
            i += 1
            all_sprites_list.update()
            all_sprites_list.draw(self.screen)

        if needButton:
            arrButton = []
            for i in range(len(arrText)):
                button = pygame.Rect(xPos + distance, yPos + 5 + i * 25, 10, 10)
                arrButton.append(button)
                pygame.draw.rect(self.screen, (255, 128, 128), button)

        return arrButton

    def createGameButton(self, rectX, rectY, rectW, rectH, text, textX, textY):
        button = pygame.Rect(rectX, rectY, rectW, rectH)
        pygame.draw.rect(self.screen, self.panelColor, button)
        self.draw_text(text, self.panelFont, self.textColor, self.screen, textX, textY)
        return button

    def set_sfx(self, isPlaying):
        self.playing_sfx = isPlaying

    def getTeammates(self):
        return self.teammates
