import pygame 
import random
from aesthetics import *

class button: 
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0) #update these variables to reflect what we called them (i.e., screen instead of win)
        # this is how you set the outline color ^^ 
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '': #adds text
            font = pygame.font.SysFont('comicsans', 20, BLACK)
            text = font.render(self.text, 1, BLACK)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2))) #centers the text for the button 
		
    def isOver(self, mouse): #is the mouse over the top of the value 
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if mouse[0] > self.x and mouse[0] < self.x + self.width:
            if mouse[1] > self.y and mouse[1] < self.y + self.height:
                return True
        return False
        
