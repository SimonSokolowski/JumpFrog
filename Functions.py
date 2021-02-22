import Initialise, pygame

def draw_window(win, frog, lilies, background, score, croc, coins, coinsBalance,
                logs, menu):
    background.draw(win)
    scoreText = Initialise.FONT.render(str(score), True, (255, 255, 255))
    win.blit(scoreText, (20, 10))

    croc.draw(win)

    for logToDraw in logs:
        logToDraw.draw(win)

    for lilyToDraw in lilies:
        if not lilyToDraw.setRot:
            lilyToDraw.setRotation()
        lilyToDraw.draw(win)

    for coinToDraw in coins:
        coinToDraw.draw(win)

    coinBalText = Initialise.FONT.render(str(coinsBalance), True, (255,205,0))
    win.blit(coinBalText, (Initialise.WIN_WIDTH - 50 - coinBalText.get_width(), 10))

    if frog.drawSelf:
        frog.draw(win)

    menu.draw(win)

    pygame.display.update()

def checkIfFrogDrowns(frog, score):
    if not frog.collidingWithLily and not frog.collidingWithCroc\
            and not frog.collidingWithLog and frog.vel_x == 0 and score >= 1:
        ifFrogDrowns(frog)

def ifFrogIsEaten(frog, crocodile):
    if crocodile.frogDead:
        crocodile.count += 1
        if crocodile.count >= 5:
            crocodile.Imgs = crocodile.IMGS[0]
        if crocodile.count >= 10:
            crocodile.Imgs = crocodile.IMGS[3]
        if crocodile.count >= 15:
            frog.drawSelf = False

def ifFrogDrowns(frog):
    frog.drownedCount += 1
    frog.drawShadow = False
    frog.frogImg = pygame.transform.rotate(frog.IMGS[7], 340)
    frog.dead = True

    if frog.drownedCount > 5:
        frog.frogImg = pygame.transform.rotate(frog.IMGS[8], 340)
    if frog.drownedCount > 10:
        frog.drawSelf = False

def saveData(coinsBalance):
    file = open("coinBal.txt", "w")
    file.write(str(coinsBalance))
    file.close()

def calcAndSaveHighscore(score, highscore):
    if score > highscore:
        file = open("highscore.txt", "w")
        file.write(str(score))
        file.close()