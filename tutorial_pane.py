from window import Window
from panel import Sprite
import pygame
import scrum_message
from teammate import Teammate

class Tutorial(Window):
    def __init__(self):
        super().__init__("Tutorial")
        self.panelFont = pygame.font.SysFont('Arial', 15, bold=True)
        self.panelFont2 = pygame.font.SysFont('Arial', 20, bold=False)
        self.panelColor = (250, 0, 0)
        self.textColor = (255, 255, 255)
        self.playing_sfx = True
        # ScrumMaster panel
        self.scrumMasterShown = False
        self.scrumMasterButton = None
        # ProductOwner panel
        self.productOwnerShown = False
        self.productOwnerButton = None
        # Team mate panel
        self.teamMemberShown = False
        self.teamMemberButton = None

    def tutorial(self):
        running = True
        while running:
            self.screen.fill((42, 131, 247))
            background = pygame.image.load("images/office.jpg")
            #background = pygame.transform.scale(background, (600, 450))
            self.screen.blit(background, (140, 200))

            mouseX, mouseY = pygame.mouse.get_pos()
            self.createReturnButton()

            productOwner = self.createGameButton(600, 230, 110, 25, 'Product Owner', 600, 233)
            scrumMaster = self.createGameButton(680, 420, 110, 25, 'Scrum Master', 685, 423)
            teamMember = self.createGameButton(210, 310, 110, 25, 'Teammate', 230, 313)

            self.draw_text('Tutorial', self.font, (0, 0, 0), self.screen, 390, 20)
            self.draw_text('Objective:', self.font,(0 ,0 ,0), self.screen, 50, 70)
            self.draw_text(' Complete the set number of stories before the Scrum session is completed.', self.panelFont2, (0, 0, 0), self.screen, 180, 73)
            self.draw_text(' Players will be given resources that could be spent on team morale and', self.panelFont2, (0, 0, 0), self.screen, 180, 98)
            self.draw_text(' additional team members. Unlocking more team members will help increase', self.panelFont2, (0, 0, 0), self.screen, 180, 123)
            self.draw_text(' user productivity.', self.panelFont2, (0, 0, 0), self.screen, 180, 148)
            self.draw_text('More:', self.font, (0, 0, 0), self.screen, 50, 175)
            self.draw_text(' Click on the character titles down below to get more information on what', self.panelFont2, (0, 0, 0), self.screen, 180, 178)
            self.draw_text(' each character does and their objectives.', self.panelFont2, (0, 0, 0), self.screen, 180, 198)

            if self.returnButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("Return(tutorial)")
                    running = False
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
            # clicking on team member
            elif teamMember.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("teamMate\n")
                    if not self.teamMemberShown:
                        self.teamMemberShown = True
                    else:
                        self.teamMemberShown = False
            # scrum master info
            if self.scrumMasterShown:
                text1 = "Scrum Master checks the team"
                text2 = "progress, assigns tasks, and"
                text3 = "hosts scrum meetings."
                self.scrumMasterButton = self.drawPanel([text1, text2, text3], 688, 450, True, 150)
                if self.scrumMasterButton:
                    for i in range(len(self.scrumMasterButton)):
                        if self.scrumMasterButton[i].collidepoint((mouseX, mouseY)):
                            if self.click:
                                scrum_message.ScrumMasterMessage(self.screen, i)
            # product owner info
            if self.productOwnerShown:
                text1 = "Product owner presents customer"
                text2 = "requirements, suggests any "
                text3 = "changes or additions to user"
                text4 = "stories, and gives feedback to"
                text5 = "the player."
                self.productOwnerButton = self.drawPanel([text1, text2, text3, text4, text5], 675, 264, True, 220)
                if self.productOwnerButton:
                    for i in range(len(self.productOwnerButton)):
                        if self.productOwnerButton[i].collidepoint((mouseX, mouseY)):
                            if self.click:
                                scrum_message.ProductOwnerMessage(self.screen, i)
            # team member info
            if self.teamMemberShown:
                text1 = "Team members work on"
                text2 = "completing the stories. Users"
                text3 = "can view the team mate details and"
                text4 = "can increase the team mate salaries."
                self.teamMemberButton = self.drawPanel([text1, text2, text3, text4], 5, 285, True, 150)
                if self.teamMemberButton:
                    for i in range(len(self.teamMemberButton)):
                        if self.teamMemberButton[i].collidepoint((mouseX, mouseY)):
                            if self.click:
                                scrum_message.TeammateMessage(self.screen, i)

            self.handle_click()

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

        return arrButton

    def createGameButton(self, rectX, rectY, rectW, rectH, text, textX, textY):
        button = pygame.Rect(rectX, rectY, rectW, rectH)
        pygame.draw.rect(self.screen, self.panelColor, button)
        self.draw_text(text, self.panelFont, self.textColor, self.screen, textX, textY)
        return button

    def set_sfx(self, isPlaying):
        self.playing_sfx = isPlaying
