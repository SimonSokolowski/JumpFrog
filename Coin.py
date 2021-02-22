import Initialise

class Coin:
    def __init__(self, x, y):
        self.IMGS = Initialise.COIN_IMGS
        self.Imgs = self.IMGS[0]
        self.animationTime = 10
        self.img_count = 0

        self.collidingWithFrog = False
        self.x = x
        self.y = y

        self.left = self.x
        self.right = self.x + 32
        self.top = self.y
        self.bot = self.y + 32

    def initiate(self):
        self.processImageAnimation()
        self.animateRotation()

    def move(self):
        self.y += 3.5

    def processImageAnimation(self):
        self.img_count += 1

    def checkIfCollidingWithFrog(self, frogRight, frogLeft,
                        frogBot, frogTop):
        coinRight = self.x + 32
        coinLeft = self.x
        coinBot = self.y + 32
        coinTop = self.y

        if (frogLeft <= coinLeft <= frogRight or frogLeft <= coinRight <= frogRight)\
                and (frogTop <= coinTop <= frogBot or frogTop <= coinBot <= frogBot):
            self.collidingWithFrog = True
        else:
            self.collidingWithFrog = False

    def animateRotation(self):
        if self.img_count < self.animationTime:
            self.Imgs = self.IMGS[0]
        elif self.img_count < self.animationTime*2:
            self.Imgs = self.IMGS[1]
        elif self.img_count < self.animationTime*3:
            self.Imgs = self.IMGS[2]
        elif self.img_count < self.animationTime*4:
            self.Imgs = self.IMGS[1]
        elif self.img_count < self.animationTime*5:
            self.Imgs = self.IMGS[0]
            self.img_count = 0

    def draw(self, win):
        win.blit(self.Imgs, (self.x, self.y))