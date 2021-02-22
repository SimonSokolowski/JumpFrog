import random, pygame
import Initialise

class Lilies:
    def __init__(self, x, y):
        self.lily = Initialise.LILIES_IMG[0]
        self.oddsOfFakeLily = random.randint(1, 6)
        self.fakeLily = False
        self.frogDead = False

        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 3.5

        self.tick_count = 0
        self.rotatedNum = 0
        self.SpawnRange = -140
        self.setRot = False
        self.right = False
        self.wetLily = False

        self.collidingWithFrog = False
        self.passedStartingHeight = False
        self.addPoint = True
        self.remove = False

        self.alreadyCheckedForCoin = False
        self.drawCoin = False

    def set_if_right_or_left(self):
        if self.x <= Initialise.WIN_WIDTH/2:
            self.right = False
        if self.x >= Initialise.WIN_WIDTH/2:
            self.right = True

    def check_if_colliding_with_frog(self, frogRight, frogLeft,
                        frogBot, frogTop, frogVel):
        lilyRight = self.x + 90
        lilyLeft = self.x
        lilyBot = self.y + 115
        lilyTop = self.y

        if frogVel == 0:
            if lilyLeft <= frogLeft and frogRight <= lilyRight \
                and lilyTop <= frogTop and frogBot <= lilyBot:
                    self.collidingWithFrog = True
        else:
            self.collidingWithFrog = False

    def if_colliding_with_frog(self):
        self.tick_count += 1

        collidedSpeedY = 0.1*self.tick_count
        collidedSpeedX = 1.2 - 0.1*self.tick_count

        if collidedSpeedY >= 4:
            collidedSpeedY = 4
        if collidedSpeedX <= 0:
            collidedSpeedX = 0

        self.y += collidedSpeedY

        if self.right:
            self.x += collidedSpeedX
        else:
            self.x -= collidedSpeedX

    def changeImgForFakeLily(self):
        if self.oddsOfFakeLily == 1:
            if not self.wetLily:
                self.lily = Initialise.LILIES_IMG[1]
            else:
                self.lily = Initialise.LILIES_IMG[2]
            self.fakeLily = True
        else:
            self.lily = Initialise.LILIES_IMG[0]
            self.fakeLily = False

    def checkIfAddCoin(self):
        if random.randint(1, 10) == 1 and not self.drawCoin \
                and not self.alreadyCheckedForCoin:
            self.drawCoin = True
        self.alreadyCheckedForCoin = True

    def setSpawnRange(self, score):
        if score <= 20:
            self.SpawnRange = random.randint(-145, -135)

    def removeLily(self, lilyToRemove):
        if self.y >= Initialise.WIN_HEIGHT:
            lilyToRemove.append(self)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def setRotation(self):
        self.rotatedNum = random.randint(0, 360)
        self.setRot = True

    def draw(self, win):
        rotatedImage = pygame.transform.rotate(self.lily, self.rotatedNum)
        win.blit(rotatedImage, (self.x, self.y))