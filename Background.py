import Initialise

class Background:
    def __init__(self, x):
        self.height = Initialise.BG_IMG.get_height()
        self.IMG = Initialise.BG_IMG
        self.vel = 4.5
        self.x = x
        self.y1 = 0
        self.y2 = self.height

    def move(self):
        self.y1 += self.vel
        self.y2 += self.vel

        if self.y1 + self.height > Initialise.WIN_HEIGHT:
            self.y2 = self.y1 - self.height

        if self.y2 + self.height > Initialise.WIN_HEIGHT:
            self.y1 = self.y2 - self.height

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y1))
        win.blit(self.IMG, (self.x, self.y2))