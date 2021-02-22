import random
import Initialise

class Crocodile:
    def __init__(self, x, y):
        self.IMGS = Initialise.CROC_IMGS
        self.Imgs = self.IMGS[0]
        self.img_count = 0
        self.count = 0

        self.x = x
        self.y = y
        self.vel = 3.5
        self.ANIMATION_TIME = 60

        self.drawCoin = False
        self.alreadyCheckedForCoin = False
        self.frogDead = False

        self.passedStartingHeight = False
        self.collidingWithFrog = False
        self.closedEyes = False
        self.drawCroc = False
        self.beingDrawn = False

    def initiate(self):
        self.blinking_animation()
        self.checkIfDrawCroc()

    def move(self):
        self.y += self.vel
        self.img_count += 1

    def check_if_colliding_with_frog(self, frogRight, frogLeft,
                        frogBot, frogTop, frogVel):
        crocRight = self.x + 135
        crocLeft = self.x
        crocBot = self.y + 168
        crocTop = self.y + 50

        if frogVel == 0:
            if crocLeft <= frogLeft and frogRight <= crocRight \
                and crocTop <= frogTop and frogBot <= crocBot:
                    self.collidingWithFrog = True
        else:
            self.collidingWithFrog = False

    def checkIfAddCoin(self):
        if random.randint(1, 2) == 1 and not self.drawCoin \
            and not self.alreadyCheckedForCoin:
            self.drawCoin = True
        self.alreadyCheckedForCoin = True

    def if_colliding_with_frog(self):
        if not self.closedEyes:
            self.frogDead = True

    def checkIfDrawCroc(self):
        if random.randint(1, 5) == 1:
            self.drawCroc = True
        else:
            self.drawCroc = False

        if self.y >= Initialise.WIN_HEIGHT:
            self.beingDrawn = False
            return self.beingDrawn

    def blinking_animation(self):
        if self.img_count < self.ANIMATION_TIME:
            self.Imgs = self.IMGS[2]
            self.closedEyes = True
        elif self.img_count < self.ANIMATION_TIME*2:
            self.Imgs = self.IMGS[1]
            self.closedEyes = False
        elif self.img_count < self.ANIMATION_TIME*3:
            self.Imgs = self.IMGS[2]
            self.closedEyes = True

    def draw(self, win):
        win.blit(self.Imgs, (self.x, self.y))