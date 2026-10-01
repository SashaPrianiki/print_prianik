from pygame import *
from random import randint
init()

mixer.music.load('galaxy_rock.mp3')
mixer.music.play(-1)

click = mixer.Sound('click sound.wav')
nowi_coin = mixer.Sound('money_sound.wav')

mw = display.set_mode((700, 500))
display.set_caption('пиши пряники')

def napisanie_prianika():
    print('прянички')


font1 = font.Font(None, 36)
font2 = font.Font(None, 100)

timer = time.Clock()
FPS = 60

skolko = randint(5, 10)

background = (69, 127, 81)
mw.fill(background)

gde_raz = 10
raunds = 0
coins = 0
gde_coins = 10
shifr_prianikov = 0
col_vo_prianikov = 0

finish = False

game = True
while game:

    Napishi = font1.render('напиши пряник', True, (169, 127, 81))
    mw.blit(Napishi, (5, 10))  

    raz = font1.render(f'{str(skolko)}', True, (169, 127, 81))
    uberi_raz = font1.render(f'{str(skolko)}', True, (69, 127, 81))
    mw.blit(raz, (205, 10)) 

    raz_slovo = font1.render('раз(а)', True, (169, 127, 81))
    mw.blit(raz_slovo, (240, 10))

    skolko_coinov = font1.render('коинов', True, (169, 127, 81))
    mw.blit(skolko_coinov, (600, 10))      

    skolko_coinov_chislo = font1.render(str(coins), True, (169, 127, 81))
    uberi_coin = font1.render(str(coins), True, (69, 127, 81))
    mw.blit(skolko_coinov_chislo, (575, 10))  

    prianik_napisan = 0
    for e in event.get():
        if e.type == QUIT:
            game = False 

        if e.type == KEYDOWN:
            click.play()
            if e.key == K_g:
                click.play()
                NAPISANIE_PRIANIKI_g = font2.render('П', True, (169, 127, 81))
                mw.blit(NAPISANIE_PRIANIKI_g, (120, 200))
                shifr_prianikov += 1
                print(shifr_prianikov)

        if e.type == KEYDOWN:
            if e.key == K_h:
                click.play()
                NAPISANIE_PRIANIKI_h = font2.render('Р', True, (169, 127, 81))
                mw.blit(NAPISANIE_PRIANIKI_h, (170, 200))
                shifr_prianikov += 1
                print(shifr_prianikov)

        if e.type == KEYDOWN:
            if e.key == K_z:
                click.play()
                NAPISANIE_PRIANIKI_z = font2.render('Я', True, (169, 127, 81))
                mw.blit(NAPISANIE_PRIANIKI_z, (215, 200))
                shifr_prianikov += 1
                print(shifr_prianikov)

        if e.type == KEYDOWN:
            if e.key == K_y:
                click.play()
                NAPISANIE_PRIANIKI_y = font2.render('Н', True, (169, 127, 81))
                mw.blit(NAPISANIE_PRIANIKI_y, (265, 200))
                shifr_prianikov += 1
                print(shifr_prianikov)

        if e.type == KEYDOWN:
            if e.key == K_b:
                click.play()
                NAPISANIE_PRIANIKI_b = font2.render('И', True, (169, 127, 81))
                mw.blit(NAPISANIE_PRIANIKI_b, (315, 200))
                shifr_prianikov += 1
                print(shifr_prianikov)

        if e.type == KEYDOWN:
            if e.key == K_r:
                click.play()
                NAPISANIE_PRIANIKI_r = font2.render('К', True, (169, 127, 81))
                mw.blit(NAPISANIE_PRIANIKI_r, (365, 200))
                shifr_prianikov += 1
                print(shifr_prianikov)
                coins += 1
                print('коинов:',coins)
                nowi_coin.play()

    if finish != True:

        if shifr_prianikov == 6:
            shifr_prianikov = 0
            col_vo_prianikov += 1
            uberi = font2.render('ПРЯНИК', True, (69, 127, 81))
            mw.blit(uberi, (120, 200))
            mw.blit(uberi, (130, 200))
            print('победа')

            mw.blit(uberi_raz, (205, 10)) 
            mw.blit(uberi_coin, (575, 10))
            if skolko > 1:
                skolko -= 1
                gde_raz += 30
                gde_coins += 30
                print(skolko)
                mw.blit(raz, (205, int(gde_raz)))

                mw.blit(skolko_coinov_chislo, (575, int(gde_coins)))
                
                
    
            else:
                pobeda = font2.render('следующий раунд!', True, (169, 127, 251))
                mw.blit(pobeda, (10, 200))
                raunds += 1

            

            if raunds == 1:
                print('раунд')
                raunds - 1

            display.update()
        if col_vo_prianikov == skolko:
            finish = True

        display.update()
        timer.tick(FPS)

    else:
        gde_raz = 10
        raunds = 0
        gde_coins = 10
        shifr_prianikov = 0
        skolko = randint(5, 10)
        finish = False
        mw.fill((69, 127, 81))
        time.delay(1500)
    