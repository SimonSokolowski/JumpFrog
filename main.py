import pygame, os

WIN_WIDTH = 500
WIN_HEIGHT = 800
STARTING_HEIGHT = 0

FrogPic1 = pygame.image.load("C:/Users/Simon/Desktop/frog imgs/frog.png")
FrogPic2 = pygame.image.load("C:/Users/Simon/Desktop/frog imgs/frog1.png")
FROG_IMGS = [pygame.transform.scale(FrogPic1, (64, 52)),
             pygame.transform.scale(FrogPic2, (64, 52))]

BG_IMG = pygame.image.load(os.path.join("C:/Users/Simon/Desktop/frog imgs/bg.png"))

LilyPic1 = pygame.image.load(os.path.join("C:/Users/Simon/Desktop/frog imgs/lilypad.png"))
LILIES_IMG = pygame.transform.scale(LilyPic1, (90, 90))

class Frog:
    IMGS = FROG_IMGS
    ANIMATION_TIME = 30

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0

        self.collidingWithLily = False

        self.tick_count = 0
        self.count = 0

        self.img_count = 0
        self.img = self.IMGS[0]
        self.right = False

        self.jumping = False

    def inc_count(self):
        self.count += 1

    def process_jump(self):
        self.collidingWithLily = False
        self.jumping = True
        self.vel_x = 10
        self.vel_y = 11

    def jump(self):
        if self.count > 0 and self.jumping:
            if self.right:
                self.x -= self.vel_x
            else:
                self.x += self.vel_x

            self.tick_count += 1
            jumpYSpeed = self.vel_y - self.tick_count

            self.y -= jumpYSpeed

            if self.x < 120 or self.x > 320:
                self.jumping = False
                self.vel_x = 0
                self.vel_y = 0
                self.count = 0
                self.tick_count = 0

        self.collidingWithLily = False

    def set_direction_to_face(self):
        if self.x <= WIN_WIDTH/2 and self.vel_x == 0:
            self.right = False
        if self.x >= WIN_WIDTH/2 and self.vel_x == 0:
            self.right = True

    def if_colliding_with_lily(self, lilyx, lilyy):
        if self.vel_y == 0:
            self.x = lilyx + 20
            self.y = lilyy + 20
            self.collidingWithLily = True

    def breathing(self):
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.jumping:
            self.img = self.IMGS[0]

    def draw(self, win):
        mirrored_frog = pygame.transform.flip(self.img, True, False)

        if self.right:
            win.blit(self.img, (self.x, self.y))
        else:
            win.blit(mirrored_frog, (self.x, self.y))

        self.img_count += 1

class Lilies:
    VEL_X = 0
    VEL_Y = 4
    LILIES = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.passed = False
        self.right = False
        self.lily = LILIES_IMG
        self.collidingWithFrog = False

    def set_if_right_or_left(self):
        if self.x <= WIN_WIDTH/2:
            self.right = False
        if self.x >= WIN_WIDTH/2:
            self.right = True

    def check_if_colliding_with_frog(self, frogXPos, frogYPos, frogVel):
        frogRight = frogXPos + 60
        frogLeft = frogXPos
        frogBot = frogYPos + 45
        frogTop = frogYPos + 20

        lilyRight = self.x + 90
        lilyLeft = self.x
        lilyBot = self.y + 89
        lilyTop = self.y + 3

        if frogVel == 0:
            if lilyLeft <= frogLeft and frogRight <= lilyRight:
                if lilyTop <= frogTop and frogBot <= lilyBot:
                    self.collidingWithFrog = True
            else:
                self.collidingWithFrog = False
                self.tick_count = 0

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

    def move(self):
        self.x += self.VEL_X
        self.y += self.VEL_Y

    def draw(self, win):
        win.blit(self.lily, (self.x, self.y))

def draw_window(win, frog, lilies):
    win.blit(BG_IMG, (0,0))
    for lily in lilies:
        lily.draw(win)
    frog.draw(win)
    pygame.display.update()

def main():
    frog = Frog(320, 325)
    lilies = [Lilies(300, 300), Lilies(100, 200), Lilies(300, 100), Lilies(100, 0)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    lilyRight = False
    start = False
    letFrogJump = False

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        frog.breathing()
        frog.set_direction_to_face()

        lilyToRemove = []
        add_lily = False

        for lily in lilies:
            if lily.y >= WIN_HEIGHT:
                lilyToRemove.append(lily)

            lily.set_if_right_or_left()

            if not lily.passed and lily.y >= STARTING_HEIGHT:
                add_lily = True
                lily.passed = True

            if start:
                lily.check_if_colliding_with_frog(frog.x, frog.y, frog.vel_x)

                if lily.collidingWithFrog:
                    frog.collidingWithLily = True

                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and start:
                    frog.inc_count()
                    letFrogJump = True
                if not keys[pygame.K_UP] and letFrogJump:
                    frog.process_jump()
                    letFrogJump = False
                    lily.collidingWithFrog = False

                if lily.collidingWithFrog:
                    lily.if_colliding_with_frog()
                    frog.if_colliding_with_lily(lily.x, lily.y)
                else:
                    lily.move()

        frog.jump()
        if add_lily:
            if lilyRight:
                lilies.append(Lilies(110, -120))
                lilyRight = False
            else:
                lilies.append(Lilies(300, -120))
                lilyRight = True
        for r in lilyToRemove:
            lilies.remove(r)

        draw_window(win, frog, lilies)

        keys = pygame.key.get_pressed()
        if not start and keys[pygame.K_UP]:
            start = True


    pygame.quit()
    quit()

main()
