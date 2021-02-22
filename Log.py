import random, pygame
import Initialise

class Log:
    def __init__(self, x, y):
        self.IMG = Initialise.Log_IMGS
        self.Img = self.IMG

        self.x = x
        self.y = y
        self.vel = 3.5
        self.count = 0

        self.drawCoin = False
        self.alreadyCheckedForCoin = False

        self.chanceOfSpawning = 0
        self.spawn = False
        self.collidingWithFrog = False

    def checkIfSpawnLog(self):
        self.chanceOfSpawning = random.randint(1, 6)

        if self.chanceOfSpawning == 1:
            self.spawn = True

    def checkIfRemove(self, logs):
        if self.y >= Initialise.WIN_HEIGHT:
            logs.remove(self)

    def check_if_colliding_with_frog(self, frogRight, frogLeft,
                        frogBot, frogTop, frogVel):
        logRight = self.x + 100
        logLeft = self.x
        logBot = self.y + 100
        logTop = self.y

        if frogVel == 0:
            if logLeft <= frogLeft and frogRight <= logRight \
                and logTop <= frogTop and frogBot <= logBot:
                    self.collidingWithFrog = True
        else:
            self.collidingWithFrog = False
            self.count = 0

    def checkIfAddCoin(self):
        if random.randint(1, 3) == 1 and not self.drawCoin \
            and not self.alreadyCheckedForCoin:
            self.drawCoin = True
        self.alreadyCheckedForCoin = True

    def if_colliding_with_frog(self):
        self.count += 1

        if self.count <= 10:
            self.y += 1
        if 11 <= self.count <= 20:
            self.y -= 1

    def move(self):
        self.y += self.vel

    def draw(self, win):
        rotatedImage = pygame.transform.rotate(self.Img, 350)
        win.blit(rotatedImage, (self.x, self.y))