import pygame
import Initialise, Frog, Lilies, Menu, Crocodile, Background, Coin, Log, Functions

def main():
    background = Background.Background(0)
    frog = Frog.Frog(317, 437)
    crocodile = Crocodile.Crocodile(1000, 1000)
    lilies = [Lilies.Lilies(300, 420), Lilies.Lilies(100, 280), Lilies.Lilies(300, 140), Lilies.Lilies(100, 0)]
    coins = [Coin.Coin(Initialise.WIN_WIDTH - 50, 15)]
    logs = [Log.Log(-200, -10000)]
    menu = Menu.Menu()

    win = pygame.display.set_mode((Initialise.WIN_WIDTH, Initialise.WIN_HEIGHT))
    clock = pygame.time.Clock()

    setTimeAtStart = 0
    count = 0
    score = 0
    spawnRange = 0

    coinsBalance = int((open("coinBal.txt", "r")).read())
    highscore = int((open("highscore.txt", "r")).read())

    run = True
    calculateDiffForFrogJump = True
    frog.collidingWithLily = False
    frog.collidingWithCroc = False
    letFrogJump = False
    frogJumpDown = False
    lilyRight = False
    allowStartJumping = False
    allowInitiateStart = False
    startMovingLilies = False
    clicking = False

    while run:
        pygame.init()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicking = True

            elif event.type == pygame.MOUSEBUTTONUP:
                clicking = False

        frog.initiate()
        crocodile.initiate()
        crocodile.check_if_colliding_with_frog(frog.rightPos, frog.leftPos,
                frog.botPos, frog.topPos, frog.vel_x)
        menu.ifClickingSkins()
        menu.ifClickingShop()
        menu.moveSkinsAndShopMenu()
        menu.ifClickingMenuItemEnableBackButton()

        lilyToRemove = []
        coinToRemove = []
        add_object = False
        add_log = False

        for lily in lilies:
            lily.check_if_colliding_with_frog(frog.rightPos, frog.leftPos,
                                frog.botPos, frog.topPos, frog.vel_x)
            lily.set_if_right_or_left()
            lily.removeLily(lilyToRemove)
            lily.checkIfAddCoin()
            lily.changeImgForFakeLily()
            lily.setSpawnRange(score)

            spawnRange = lily.SpawnRange

            if lily.drawCoin:
                coins.append(Coin.Coin(lily.x + 40, lily.y + 30))
                lily.drawCoin = False

            if frog.y < lily.y and lily.addPoint:
                lily.addPoint = False
                score += 1

            if not lily.passedStartingHeight and lily.y >= Initialise.STARTING_HEIGHT:
               add_object = True
               lily.passedStartingHeight = True
            if not crocodile.passedStartingHeight and crocodile.y >= Initialise.STARTING_HEIGHT:
                add_object = True
                crocodile.passedStartingHeight = True

        if startMovingLilies:
            crocodile.move()
            Functions.saveData(coinsBalance)
            Functions.calcAndSaveHighscore(score, highscore)

            for coin in coins:
                if coin != coins[0]:
                    coin.move()

            if not crocodile.alreadyCheckedForCoin:
                crocodile.checkIfAddCoin()
                if crocodile.drawCoin:
                    coins.append(Coin.Coin(crocodile.x + 30, crocodile.y + 90))
                    crocodile.drawCoin = False

            for log in logs:
                log.move()
                log.checkIfSpawnLog()
                log.checkIfRemove(logs)
                log.check_if_colliding_with_frog(frog.rightPos, frog.leftPos,
                                frog.botPos, frog.topPos, frog.vel_x)

                if log.spawn:
                    add_log = True
                    log.spawn = False

                if not log.alreadyCheckedForCoin:
                    log.checkIfAddCoin()
                    if log.drawCoin:
                        coins.append(Coin.Coin(log.x + 30, log.y))
                        log.drawCoin = False

                if log.collidingWithFrog and not frog.dead:
                    frog.if_colliding_with_log(log.x, log.y)
                    log.if_colliding_with_frog()
                    frog.collidingWithLog = True

            for lily in lilies:
                if clicking and allowStartJumping:
                    if calculateDiffForFrogJump:
                        calculateDiffForFrogJump = False
                        setTimeAtStart = pygame.time.get_ticks()

                    timePassed = pygame.time.get_ticks() - setTimeAtStart
                    frog.inc_count()
                    letFrogJump = True

                    frog.JumpPowerAnimation(timePassed)

                    if pygame.mouse.get_pos()[1] > 600:
                        frogJumpDown = True

                elif letFrogJump and not frog.dead:
                    calculateDiffForFrogJump = True
                    lily.collidingWithFrog = False
                    letFrogJump = False

                    timePassed = pygame.time.get_ticks() - setTimeAtStart
                    frog.process_jump(timePassed, frogJumpDown)
                    frogJumpDown = False

                if lily.collidingWithFrog and not frog.dead:
                    frog.collidingWithLily = True
                    lily.if_colliding_with_frog()
                    frog.if_colliding_with_lily(lily.x, lily.y)

                    if lily.fakeLily:
                        lily.remove = True
                        count += 1
                        if count > 18:
                            lily.wetLily = True
                        if count > 24:
                            frog.collidingWithLily = False
                else:
                    lily.move()

                if crocodile.collidingWithFrog and not frog.dead:
                    frog.if_colliding_with_croc(crocodile.x, crocodile.y)
                    frog.collidingWithCroc = True
                    crocodile.if_colliding_with_frog()

                if frog.jumping:
                    if lily.remove:
                        lily.wetLily = True
                    count = 0
                    frog.collidingIsFalse()

        if add_object:
            if lilyRight:
                if crocodile.drawCroc and not crocodile.beingDrawn:
                    crocodile = Crocodile.Crocodile(100, -180)
                    crocodile.beingDrawn = True
                else:
                    lilies.append(Lilies.Lilies(100, -130))
                if add_log and len(logs) <= 2:
                    logs.append(Log.Log(100, spawnRange - 120))
                lilyRight = False
            else:
                if crocodile.drawCroc and not crocodile.beingDrawn:
                    crocodile = Crocodile.Crocodile(300, -160)
                    crocodile.beingDrawn = True
                else:
                    lilies.append(Lilies.Lilies(300, -130))
                if add_log and len(logs) <= 2:
                    logs.append(Log.Log(300, spawnRange - 120))
                lilyRight = True

        for coin in coins:
            coin.initiate()
            coin.checkIfCollidingWithFrog(frog.rightPos, frog.leftPos,
                frog.botPos, frog.y + 10)

            if coin.y >= Initialise.WIN_HEIGHT or coin.collidingWithFrog:
                coinToRemove.append(coin)

            if coin.collidingWithFrog:
                coinsBalance += 1
                coin.collidingWithFrog = False

        for r in lilyToRemove:
            lilies.remove(r)
        for r in coinToRemove:
            coins.remove(r)

        Functions.checkIfFrogDrowns(frog, score)
        Functions.ifFrogIsEaten(frog, crocodile)
        Functions.draw_window(win, frog, lilies, background, score, crocodile, coins,
                    coinsBalance, logs, menu)

        menu.checkIfDrawMenu(allowInitiateStart, highscore)
        menu.checkIfClickingMenuButton(clicking)

        if not frog.drawSelf and clicking:
            main()

        background.move()

        if clicking and not menu.clickingMenu:
            allowInitiateStart = True
        elif allowInitiateStart:
            startMovingLilies = True

        if not allowStartJumping and startMovingLilies and clicking:
            allowStartJumping = True
    pygame.quit()
    quit()

main()