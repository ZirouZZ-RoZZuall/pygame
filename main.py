import pygame
from random import *
pygame.init()

window = pygame.display.set_mode(400,400)
window.fill((148, 137, 216))
clock = pygame.time.Clock()
black = (0,0,0)
class TextArea():
    def __init__(self,x = 0,y = 0,height = 10,weight = 10,color = (255,255,255)):
        self.rect = pygame.Rect(x,y,height,weight)
        self.fill_color = color

    def set_text(self,text,fsize,text_color = black):
        self.text = text
        self.image = pygame.font.Font(None,fsize).render(text, True, text_color)

    def draw(self,shift_x=0,shift_y=0):
        pygame.draw.rect(window,self.fill_color,self.rect)
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))


quest_card = TextArea(120, 100, 550, 50, (166,202,240))
quest_card.set_text("", 75)


ans_card = TextArea(120, 240, 130, 50, (166,202,240))
ans_card.set_text("", 75)



while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rand = randint(1,3)
                if rand == 1:
                    quest_card.set_text("Что самым первым вывели в мир при помощи команды 'print'?",30)

                elif rand == 2:
                    quest_card.set_text("Какой спутник у Земли?",30)

                else:
                    quest_card.set_text("На каком языке программирования сделана эта программа?",30)

            
            elif event.key == pygame.K_a:
                rand = randint(1,3)
                if rand == 1:
                    ans_card.set_text("Hello, World!", 30)
                elif rand == 2:
                    ans_card.set_text("Луна", 30)
                else:
                    ans_card.set_text("Python", 30)

    clock.tick(40)
    pygame.display.update()

    quest_card.draw(10,10)
    ans_card.draw(10,10)
