import pygame, os

pygame.font.init()
FONT = pygame.font.Font("font/04B_19__.TTF", 40)
FONT2 = pygame.font.Font("font/04B_19__.TTF", 30)
FONT3 = pygame.font.Font("font/Minercraftory.ttf", 55)
FONT4 = pygame.font.Font("font/Minercraftory.ttf", 32)

WIN_WIDTH = 500
WIN_HEIGHT = 800
STARTING_HEIGHT = 0

skinsMenuImage1 = pygame.image.load("imgs/menu/skinsMenu.png")
skinsMenuWaterImage1 = pygame.image.load("imgs/menu/skinsMenuWater.png")
MENU_IMGS = [pygame.transform.scale(skinsMenuImage1, (350, 800)),
             pygame.transform.scale(skinsMenuWaterImage1, (350, 800))]

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

CoinFront = pygame.image.load(os.path.join("imgs/coinFront.png"))
CoinSide1 = pygame.image.load(os.path.join("imgs/coinSide1.png"))
CoinEdge = pygame.image.load(os.path.join("imgs/coinEdge.png"))
CoinSide2 = pygame.image.load(os.path.join("imgs/coinSide2.png"))
COIN_IMGS = [pygame.transform.scale(CoinFront, (32, 32),),
             pygame.transform.scale(CoinSide1, (32, 32),),
             pygame.transform.scale(CoinEdge, (32, 32),),
             pygame.transform.scale(CoinSide2, (32, 32),)]

Log1 = pygame.image.load(os.path.join("imgs/log.png"))
Log_IMGS = pygame.transform.scale(Log1, (100, 100))

BackgroundStill = pygame.image.load("imgs/bg1.png")
BG_IMG = pygame.transform.scale(BackgroundStill, (WIN_WIDTH, WIN_HEIGHT))