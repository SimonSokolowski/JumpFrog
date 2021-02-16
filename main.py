import pygame, os, random

pygame.font.init()
FONT = pygame.font.Font("font/04B_19__.TTF", 40)

WIN_WIDTH = 500
WIN_HEIGHT = 800
STARTING_HEIGHT = 0

Frog1 = pygame.image.load("imgs/frog.png")
Frog2 = pygame.image.load("imgs/frog1.png")
Shadow = pygame.image.load("imgs/frogshadow.png")
FrogJump1 = pygame.image.load("imgs/frogjump.png")
FrogJumpShadow = pygame.image.load("imgs/frogjumpshadow.png")
FrogJumpMedium = pygame.image.load("imgs/frogJumpMedium.png")
FrogJumpPowerfull = pygame.image.load("imgs/frogJumpPowerfull.png")
FrogDrowned = pygame.image.load("imgs/frogDrowned.png")
FrogDrowned1 = pygame.image.load("imgs/frogDrowned1.png")
FROG_IMGS = [pygame.transform.scale(Frog1, (64, 52)),
             pygame.transform.scale(Frog2, (64, 52)),
             pygame.transform.scale(FrogJump1, (76, 64)),
             pygame.transform.scale(Shadow, (56, 20)),
             pygame.transform.scale(FrogJumpShadow, (56, 20)),
             pygame.transform.scale(FrogJumpMedium, (64, 52)),
             pygame.transform.scale(FrogJumpPowerfull, (64, 52)),
             pygame.transform.scale(FrogDrowned, (64, 52)),
             pygame.transform.scale(FrogDrowned1, (64, 52))]

LilyPic1 = pygame.image.load(os.path.join("imgs/lilypad.png"))
FakeLilyPic1 = pygame.image.load(os.path.join("imgs/fakelilypad.png"))
FakeLilyPic2 = pygame.image.load(os.path.join("imgs/fakelilypad2.png"))
LILIES_IMG = [pygame.transform.scale(LilyPic1, (90, 90),),
              pygame.transform.scale(FakeLilyPic1, (90, 90),),
              pygame.transform.scale(FakeLilyPic2, (90, 90),)]

CrocPic1 = pygame.image.load(os.path.join("imgs/crocodile.png"))
CrocOpenEyes = pygame.image.load(os.path.join("imgs/crocOpenEyes.png"))
CrocClosedEyes = pygame.image.load(os.path.join("imgs/crocClosedEyes.png"))
CrocEating = pygame.image.load(os.path.join("imgs/crocodileEating.png"))
CROC_IMGS = [pygame.transform.scale(CrocPic1, (135, 168),),
             pygame.transform.scale(CrocOpenEyes, (135, 168),),
             pygame.transform.scale(CrocClosedEyes, (135, 168),),
             pygame.transform.scale(CrocEating, (135, 168),)]

BackgroundStill = pygame.image.load("imgs/bg1.png")
BG_IMG = pygame.transform.scale(BackgroundStill, (WIN_WIDTH, WIN_HEIGHT))

class Frog:
    def __init__(self, x, y):
        self.IMGS = FROG_IMGS
        self.frogImg = self.IMGS[0]
        self.shadowImg = self.IMGS[3]
        self.jumpShadowImg = self.IMGS[4]

        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0

        self.ANIMATION_TIME = 60
        self.img_count = 0
        self.tick_count = 0
        self.count = 0
        self.drownedCount = 0

        self.collidingWithLily = False
        self.right = False
        self.jumping = False
        self.drawShadow = True
        self.dead = False

        self.rightPos = 0
        self.leftPos = 0
        self.botPos = 0
        self.topPos = 0

    def inc_count(self):
        self.count += 1

    def process_jump(self, timeHoldingButton):
        self.collidingWithLily = False
        self.jumping = True
        self.vel_x = 10

        if timeHoldingButton <= 130:
            self.vel_y = 7
        if 131 <= timeHoldingButton <= 230:
            self.vel_y = 12
        if 231<= timeHoldingButton:
            self.vel_y = 18

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

    def set_direction_to_face(self):
        if self.x <= WIN_WIDTH/2 and self.vel_x == 0:
            self.right = False
        if self.x >= WIN_WIDTH/2 and self.vel_x == 0:
            self.right = True

    def if_colliding_with_lily(self, lilyx, lilyy):
        if self.vel_y == 0:
            self.x = lilyx + 17
            self.y = lilyy + 17

    def if_colliding_with_croc(self, crocx, crocy):
        if self.vel_y == 0:
            self.x = crocx + 15
            self.y = crocy + 70

    def set_boundaries(self):
        if not -30 <= self.y <= WIN_HEIGHT + 10:
            main()

    def collision_boundaries(self):
        self.rightPos = self.x + 60
        self.leftPos = self.x
        self.botPos = self.y + 52
        self.topPos = self.y + 50

    def breathing_animation(self):
        if self.img_count < self.ANIMATION_TIME:
            self.frogImg = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.frogImg = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.frogImg = self.IMGS[0]
            self.img_count = 0

    def jump_animation(self):
        if self.jumping:
            self.frogImg = self.IMGS[2]

    def draw(self, win):
        mirrored_frog = pygame.transform.flip(self.frogImg, True, False)

        if self.right:
            if self.jumping:
                win.blit(self.jumpShadowImg, (self.x + 5, self.y + 70))
            elif self.drawShadow:
                win.blit(self.shadowImg, (self.x + 8, self.y + 45))
            win.blit(self.frogImg, (self.x, self.y))
        else:
            if self.jumping:
                win.blit(self.jumpShadowImg, (self.x, self.y + 70))
            elif self.drawShadow:
                win.blit(self.shadowImg, (self.x, self.y + 45))
            win.blit(mirrored_frog, (self.x, self.y))

        self.img_count += 1

class Lilies:
    def __init__(self, x, y):
        self.lily = LILIES_IMG[0]
        self.oddsOfFakeLily = random.randint(1, 6)

        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 4

        self.tick_count = 0
        self.rotatedNum = 0

        self.addPoint = True
        self.wetLily = False
        self.remove = False
        self.setRot = False
        self.passedStartingHeight = False
        self.right = False
        self.collidingWithFrog = False

    def set_if_right_or_left(self):
        if self.x <= WIN_WIDTH/2:
            self.right = False
        if self.x >= WIN_WIDTH/2:
            self.right = True

    def check_if_colliding_with_frog(self, frogRight, frogLeft,
                        frogBot, frogTop, frogVel):
        lilyRight = self.x + 90
        lilyLeft = self.x
        lilyBot = self.y + 88
        lilyTop = self.y + 1

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

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def setRotation(self):
        self.rotatedNum = random.randint(0, 360)
        self.setRot = True

    def draw(self, win):
        rotatedImage = pygame.transform.rotate(self.lily, self.rotatedNum)
        win.blit(rotatedImage, (self.x, self.y))

class Crocodile:
    def __init__(self, x, y):
        self.IMGS = CROC_IMGS
        self.Imgs = self.IMGS[0]
        self.img_count = 0
        self.count = 0

        self.x = x
        self.y = y
        self.vel = 4
        self.ANIMATION_TIME = 60

        self.passedStartingHeight = False
        self.collidingWithFrog = False
        self.closedEyes = False
        self.drawCroc = False
        self.beingDrawn = False

    def move(self):
        self.y += self.vel
        self.img_count += 1

    def check_if_colliding_with_frog(self, frogRight, frogLeft,
                        frogBot, frogTop, frogVel):
        lilyRight = self.x + 135
        lilyLeft = self.x
        lilyBot = self.y + 168
        lilyTop = self.y + 50

        if frogVel == 0:
            if lilyLeft <= frogLeft and frogRight <= lilyRight \
                and lilyTop <= frogTop and frogBot <= lilyBot:
                    self.collidingWithFrog = True
        else:
            self.collidingWithFrog = False

    def if_colliding_with_frog(self):
        if not self.closedEyes:
            self.count += 1
            if self.count >= 5:
                self.Imgs = self.IMGS[0]
            if self.count >= 10:
                self.Imgs = self.IMGS[3]
            if self.count >= 15:
                main()

    def checkIfDrawCroc(self):
        if random.randint(1, 5) == 3:
            self.drawCroc = True
        else:
            self.drawCroc = False

        if self.y >= WIN_HEIGHT:
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

class Background:
    def __init__(self, x):
        self.height = BG_IMG.get_height()
        self.IMG = BG_IMG
        self.vel = 5
        self.x = x
        self.y1 = 0
        self.y2 = self.height

    def move(self):
        self.y1 += self.vel
        self.y2 += self.vel

        if self.y1 + self.height > WIN_HEIGHT:
            self.y2 = self.y1 - self.height

        if self.y2 + self.height > WIN_HEIGHT:
            self.y1 = self.y2 - self.height

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y1))
        win.blit(self.IMG, (self.x, self.y2))

def draw_window(win, frog, lilies, background, score, croc):
    background.draw(win)
    text = FONT.render(str(score), True, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 20 - text.get_width(), 20))
    croc.draw(win)

    for lilyToDraw in lilies:
        if not lilyToDraw.setRot:
            lilyToDraw.setRotation()
        lilyToDraw.draw(win)

    frog.draw(win)
    pygame.display.update()

def checkIfFrogDies(hasFrogCollidedWithLily, hasFrogCollidedWithCroc,
                    frogVel, start, frog, score):
    if not hasFrogCollidedWithLily and not hasFrogCollidedWithCroc\
            and frogVel == 0 and start and score >= 1:
        frog.drownedCount += 1
        frog.drawShadow = False
        frog.dead = True

        frog.frogImg = pygame.transform.rotate(frog.IMGS[7], 340)

        if frog.drownedCount > 2:
            frog.frogImg = pygame.transform.rotate(frog.IMGS[8], 340)
        if frog.drownedCount > 4:
            main()

def main():
    background = Background(0)
    frog = Frog(317, 437)
    crocodile = Crocodile(1000, 1000)
    lilies = [Lilies(300, 420), Lilies(100, 280), Lilies(300, 140), Lilies(100, 0)]
    frogJumpMediumImg = frog.IMGS[5]
    frogJumpPowerfullImg = frog.IMGS[6]

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    setTimeAtStart = 0
    count = 0
    score = 0

    run = True
    calculateDiffForFrogJump = True
    frogIsCollidingWithLily = False
    frogIsCollidingWithCroc = False
    letFrogJump = False
    lilyRight = False
    allowStartJumping = False
    allowInitiateStart = False
    startMovingLilies = False

    while run:
        keys = pygame.key.get_pressed()
        pygame.init()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        frog.breathing_animation()
        frog.jump_animation()
        frog.set_direction_to_face()
        frog.jump()
        frog.set_boundaries()
        frog.collision_boundaries()
        crocodile.blinking_animation()
        crocodile.check_if_colliding_with_frog(frog.rightPos, frog.leftPos,
                frog.botPos, frog.topPos, frog.vel_x)
        crocodile.checkIfDrawCroc()
        lilyToRemove = []
        add_lily = False

        for lily in lilies:
            lily.set_if_right_or_left()
            lily.check_if_colliding_with_frog(frog.rightPos, frog.leftPos,
                                frog.botPos, frog.topPos, frog.vel_x)

            if lily.y >= WIN_HEIGHT:
                lilyToRemove.append(lily)

            if frog.y < lily.y and lily.addPoint:
                lily.addPoint = False
                score += 1

            if not lily.passedStartingHeight and lily.y >= STARTING_HEIGHT:
                add_lily = True
                lily.passedStartingHeight = True

            if not crocodile.passedStartingHeight and crocodile.y >= STARTING_HEIGHT:
                add_lily = True
                crocodile.passedStartingHeight = True

            if startMovingLilies:

                if keys[pygame.K_UP] and allowStartJumping:
                    if calculateDiffForFrogJump:
                        calculateDiffForFrogJump = False
                        setTimeAtStart = pygame.time.get_ticks()

                    timePassed = pygame.time.get_ticks() - setTimeAtStart
                    frog.inc_count()
                    letFrogJump = True

                    if 131 <= timePassed < 230:
                        frog.frogImg = frogJumpMediumImg

                    elif 231 <= timePassed:
                        frog.frogImg = frogJumpPowerfullImg

                elif letFrogJump:
                    calculateDiffForFrogJump = True
                    lily.collidingWithFrog = False
                    letFrogJump = False

                    timePassed = pygame.time.get_ticks() - setTimeAtStart
                    frog.process_jump(timePassed)

                if lily.collidingWithFrog:
                    frogIsCollidingWithLily = True
                    lily.if_colliding_with_frog()
                    frog.if_colliding_with_lily(lily.x, lily.y)

                    if lily.fakeLily:
                        lily.remove = True
                        count += 1
                        if count > 8:
                            lily.wetLily = True
                        if count > 15:
                            frogIsCollidingWithLily = False
                else:
                    lily.move()

                if frog.jumping:
                    if lily.remove:
                        lily.wetLily = True
                    count = 0
                    frogIsCollidingWithLily = False
                    frogIsCollidingWithCroc = False

                if crocodile.collidingWithFrog:
                    frog.if_colliding_with_croc(crocodile.x, crocodile.y)
                    frogIsCollidingWithCroc = True
                    crocodile.if_colliding_with_frog()

            if lily.oddsOfFakeLily == 1:
                if not lily.wetLily:
                    lily.lily = LILIES_IMG[1]
                else:
                    lily.lily = LILIES_IMG[2]
                lily.fakeLily = True
            else:
                lily.lily = LILIES_IMG[0]
                lily.fakeLily = False

        if startMovingLilies:
            crocodile.move()

        if add_lily:
            if lilyRight:
                if crocodile.drawCroc and not crocodile.beingDrawn:
                    crocodile = Crocodile(100, -150)
                    crocodile.beingDrawn = True
                else:
                    lilies.append(Lilies(100, -140))
                lilyRight = False
            else:
                if crocodile.drawCroc and not crocodile.beingDrawn:
                    crocodile = Crocodile(300, -150)
                    crocodile.beingDrawn = True
                else:
                    lilies.append(Lilies(300, -140))
                lilyRight = True

        for r in lilyToRemove:
            lilies.remove(r)

        checkIfFrogDies(frogIsCollidingWithLily, frogIsCollidingWithCroc, frog.vel_x,
                        allowStartJumping, frog, score)
        draw_window(win, frog, lilies, background, score, crocodile)

        if not frog.dead:
            if keys[pygame.K_UP]:
                allowInitiateStart = True
            elif allowInitiateStart:
                startMovingLilies = True

        background.move()

        if not allowStartJumping and startMovingLilies and keys[pygame.K_UP]:
            allowStartJumping = True

    pygame.quit()
    quit()

main()
