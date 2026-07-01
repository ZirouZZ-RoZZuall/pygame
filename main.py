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
        self.titles = list()

    def set_text(self,number,fsize,text_color = black):
        self.text = self.titles[number]
        self.image = pygame.font.Font(None,fsize).render(self.text, True, text_color)

    def add_text(self,text):
        self.titles.append(text)

    def draw(self,shift_x=0,shift_y=0):
        pygame.draw.rect(window,self.fill_color,self.rect)
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))

quest_card = TextArea(120, 100, 550, 72, (166,202,240))
quest_card.add_text('Вопрос')
quest_card.add_text("Что самым первым вывели в мир при помощи команды 'print'?")
quest_card.set_text(0, 75)
quest_card.add_text("Какой спутник у Земли?")
quest_card.add_text("На каком языке программирования сделана эта программа?")
quest_card.add_text("Корень из 121?")

ans_card = TextArea(120, 240, 135, 72, (166,202,240))
ans_card.add_text('Ответ')
ans_card.set_text(0, 75)

ans_card.add_text("Hello, World!")
ans_card.add_text("Луна")
ans_card.add_text("Python")
ans_card.add_text("11")

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rand = randint(1,len(quest_card.titles) - 1)
                quest_card.set_text(rand,30)

            
            elif event.key == pygame.K_a:
                rand = randint(1,len(ans_card.titles) - 1)
                ans_card.set_text(rand,30)
                
    clock.tick(40)
    pygame.display.update()

    quest_card.draw(10,10)
    ans_card.draw(10,10)
