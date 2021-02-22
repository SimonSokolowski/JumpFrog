import pygame
import Initialise

class Menu:
    def __init__(self):
        self.Imgs = Initialise.MENU_IMGS
        self.skinsMenu = self.Imgs[0]
        self.skinsWaterMenu = self.Imgs[1]
        self.skinsWaterMenu = self.Imgs[1]
        self.height = Initialise.BG_IMG.get_height()

        self.clickingSkins = False
        self.allowClickingSkins = False
        self.clickingShop = False
        self.allowClickingShop = False
        self.clickingSettings = False
        self.allowClickingSettings = False
        self.clickingMenu = False

        self.drawSkinsMenu = False
        self.drawShopMenu = False
        self.drawPlayOption = False

        self.pauseXpos = 0
        self.pauseYpos = 0
        self.skinsXpos = 20
        self.skinsYpos = 600
        self.shopXpos = 20
        self.shopYpos = 645
        self.settingsXpos = 20
        self.settingsYpos = 690
        self.playXpos = 20
        self.playYpos = 735

        self.highscore = 0
        self.drawMenu = False
        self.drawMenuItems = False
        self.drawSkinsAndShopMenu = False

        self.vel = 4.5
        self.y1 = 0
        self.y2 = self.height

    def checkIfDrawMenu(self, allowInitiateStart, highscore):
        if not allowInitiateStart:
            self.drawMenuItems = True
            self.drawMenu = True
        else:
            self.drawMenu = False
            self.drawMenuItems = False

        self.highscore = highscore

    def checkIfClickingMenuButton(self, clicking):
        if clicking:
            if self.skinsXpos <= pygame.mouse.get_pos()[0] <= self.skinsXpos + 144 \
                and self.skinsYpos <= pygame.mouse.get_pos()[1] <= self.skinsYpos + 60:
                self.clickingMenu = True
                self.allowClickingSkins = True
        elif self.allowClickingSkins:
            self.clickingSkins = True
            self.allowClickingSkins = False
        else:
            self.clickingMenu = False
            self.clickingSkins = False

        if clicking:
            if self.shopXpos <= pygame.mouse.get_pos()[0] <= self.shopXpos + 132 \
                and self.shopYpos <= pygame.mouse.get_pos()[1] <= self.shopYpos + 60:
                self.clickingMenu = True
                self.allowClickingShop = True
        elif self.allowClickingShop:
            self.clickingShop = True
            self.allowClickingShop = False
        else:
            self.clickingMenu = False

        if clicking:
            if self.settingsXpos <= pygame.mouse.get_pos()[0] <= self.settingsXpos + 250 \
                and self.settingsYpos <= pygame.mouse.get_pos()[1] <= self.settingsYpos + 65:
                self.clickingMenu = True
                self.allowClickingSettings = True
        elif self.allowClickingSettings:
            self.clickingSettings = True
            self.allowClickingSettings = False
        else:
            self.clickingMenu = False

    def ifClickingMenuItemEnableBackButton(self):
        if self.drawShopMenu or self.drawSkinsMenu:
            self.drawPlayOption = True
        else:
            self.drawPlayOption = False

    def moveSkinsAndShopMenu(self):
        self.y1 += self.vel
        self.y2 += self.vel

        if self.y1 + self.height > Initialise.WIN_HEIGHT:
            self.y2 = self.y1 - self.height

        if self.y2 + self.height > Initialise.WIN_HEIGHT:
            self.y1 = self.y2 - self.height

    def ifClickingSkins(self):
        if self.clickingSkins:
            self.drawSkinsMenu = True
            self.drawSkinsAndShopMenu = True

    def ifClickingShop(self):
        if self.clickingShop:
            self.drawShopMenu = True
            self.drawSkinsAndShopMenu = True

    def draw(self, win):
        if self.drawMenu:
            TapToPlayShadowText = Initialise.FONT3.render("Tap To Play!", True, (25, 25, 25))
            win.blit(TapToPlayShadowText, (Initialise.WIN_WIDTH/2 - TapToPlayShadowText.get_width()/2 - 7, 210))
            TapToPlayText = Initialise.FONT3.render("Tap To Play!", True, (255, 255, 255))
            win.blit(TapToPlayText, (Initialise.WIN_WIDTH/2 - TapToPlayText.get_width()/2, 200))
            frogShadowText = Initialise.FONT4.render("Frog", True, (25, 25, 25))
            win.blit(frogShadowText, (Initialise.WIN_WIDTH/2 - frogShadowText.get_width()/2 - 7, 160))
            frogText = Initialise.FONT4.render("Frog", True, (255, 255, 255))
            win.blit(frogText, (Initialise.WIN_WIDTH/2 - frogText.get_width()/2, 155))
            highscoreBest = Initialise.FONT4.render("Highscore", True, (255, 255, 255))
            win.blit(highscoreBest, (Initialise.WIN_WIDTH/2 - highscoreBest.get_width()/2, 290))
            highscoreText = Initialise.FONT.render(str(self.highscore), True, (255, 255, 255))
            win.blit(highscoreText, (Initialise.WIN_WIDTH/2 - highscoreText.get_width()/2, 340))

        if self.drawSkinsAndShopMenu:
            win.blit(self.skinsWaterMenu, (0, self.y1))
            win.blit(self.skinsWaterMenu, (0, self.y2))
            win.blit(self.skinsMenu, (150,0))

        if self.drawMenuItems:
            skinsText = Initialise.FONT4.render("Skins", True, (255, 255, 255))
            win.blit(skinsText, (self.skinsXpos, self.skinsYpos))
            shopText = Initialise.FONT4.render("Shop", True, (255, 255, 255))
            win.blit(shopText, (self.shopXpos, self.shopYpos))
            settingsText = Initialise.FONT4.render("Settings", True, (255, 255, 255))
            win.blit(settingsText, (self.settingsXpos, self.settingsYpos))

            if self.drawPlayOption:
                playText = Initialise.FONT4.render("-Play", True, (255, 255, 255))
                win.blit(playText, (self.playXpos, self.playYpos))
