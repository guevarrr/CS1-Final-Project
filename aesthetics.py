import pygame
import random

# window size
width = 800
height = 600

#margins
left_margin = 230
top_margin = 150

#colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (110, 110, 110)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 120, 0)
RED = (255, 0, 0)
LIGHT_RED = (120, 0, 0)
DARK_GREEN = (0,100,0)
PURPLE = (171,130,255)

#card values
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}

