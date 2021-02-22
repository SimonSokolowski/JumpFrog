import Initialise
import pygame

class Frog:
    def __init__(self, x, y):
        self.IMGS = Initialise.FROG_IMGS
        self.frogImg = self.IMGS[0]
        self.shadowImg = self.IMGS[3]
        self.jumpShadowImg = self.IMGS[4]
        self.drawSelf = True

        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0

        self.ANIMATION_TIME = 60
        self.img_count = 0
        self.tick_count = 0
        self.count = 0
        self.drownedCount = 0
        self.baseTimeBetweenJumps = 150

        self.collidingWithLily = False
        self.collidingWithCroc = False
        self.collidingWithLog = False

        self.right = False
        self.jumping = False
        self.drawShadow = True
        self.dead = False

        self.rightPos = 0
        self.leftPos = 0
        self.botPos = 0
        self.topPos = 0

    def initiate(self):
        self.breathing_animation()
        self.jump_animation()
        self.set_direction_to_face()
        self.jump()
        self.set_boundaries()
        self.collision_boundaries()
        self.removePosIfCollidedWithAnything()

    def inc_count(self):
        self.count += 1

    def process_jump(self, timeHoldingButton, frogJumpDown):
        self.collidingWithLily = False
        self.jumping = True
        self.vel_x = 10
        btbj = self.baseTimeBetweenJumps

        if frogJumpDown:
           self.vel_y = 7
        else:
            if timeHoldingButton < btbj*1.5:
                self.vel_y = 13
            if timeHoldingButton >= btbj*1.5:
                self.vel_y = 18

    def jump_animation(self):
        if self.jumping:
            self.frogImg = self.IMGS[2]

    def JumpPowerAnimation(self, timePassed):
        frogJumpMediumImg = self.IMGS[5]
        frogJumpPowerfullImg = self.IMGS[6]

        if timePassed < self.baseTimeBetweenJumps * 1.5:
            self.frogImg = frogJumpMediumImg
        if timePassed >= self.baseTimeBetweenJumps * 1.5:
            self.frogImg = frogJumpPowerfullImg

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
        if self.x <= Initialise.WIN_WIDTH/2 and self.vel_x == 0:
            self.right = False
        if self.x >= Initialise.WIN_WIDTH/2 and self.vel_x == 0:
            self.right = True

    def if_colliding_with_lily(self, lilyx, lilyy):
        if self.vel_y == 0:
            self.x = lilyx + 20
            self.y = lilyy + 17

    def if_colliding_with_croc(self, crocx, crocy):
        if self.vel_y == 0:
            self.x = crocx + 15
            self.y = crocy + 70

    def if_colliding_with_log(self, logx, logy):
        if self.vel_y == 0:
            self.x = logx + 25
            self.y = logy - 15

    def removePosIfCollidedWithAnything(self):
        if not self.drawSelf:
            self.x = Initialise.WIN_WIDTH*4
            self.y = Initialise.WIN_HEIGHT*4

    def set_boundaries(self):
        if self.y >= Initialise.WIN_HEIGHT + 10:
            self.dead = True
            self.drawSelf = False

    def collidingIsFalse(self):
        self.collidingWithLily = False
        self.collidingWithCroc = False
        self.collidingWithLog = False

    def collision_boundaries(self):
        self.rightPos = self.x + 60
        self.leftPos = self.x
        self.botPos = self.y + 52
        self.topPos = self.y + 51

    def breathing_animation(self):
        if self.img_count < self.ANIMATION_TIME:
            self.frogImg = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.frogImg = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.frogImg = self.IMGS[0]
            self.img_count = 0

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