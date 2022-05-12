### working hi-lo game code -- completed

import pygame
import random
from card import Card
from aesthetics import *
from button import button

 
# The deck of cards - empty list 
deck = []
# Loop for every type of suit and every type of card in a suit, add card to deck 
for suit in suits:
	for card in cards:
		deck.append(Card(suit, card))

# initializing game loop
pygame.init()

#screen & background
screen = pygame.display.set_mode((width, height))
screen.fill(DARK_GREEN)

#caption
pygame.display.set_caption("Higher or Lower Game")

#font to use
small_font = pygame.font.SysFont('comicsans', 20)

# higher and lower buttons
higher_button = button(GREEN,220,370,125,60,'HIGHER')
higher_button.draw(screen)

lower_button = button(RED,460,370,125,60,text='LOWER')
lower_button.draw(screen)

#choose card
current_card = random.choice(deck)
while current_card.value == "A" or current_card.value == "K":
	current_card = random.choice(deck)
	
#previous card- just cover
card_before = pygame.image.load(r'./cards/card_cover.png')
card_before = pygame.transform.scale(card_before , (100,160))

#current card
card_current =  pygame.image.load(r'./cards/' + current_card.value + current_card.suit_type[0] + '.png')
card_current = pygame.transform.scale(card_current , (100,160))

#next card- just cover
card_after =  pygame.image.load(r'./cards/card_cover.png')
card_after = pygame.transform.scale(card_after , (100,160))

#remove the card
deck.remove(current_card)

#scoreboard
guesses = 5
score = 0
choice = -1

#game logistics
over = False
run = True

#button creation
higher_button = button(GREEN,220,370,125,60,'HIGHER')
lower_button = button(RED,460,370,125,60,text='LOWER')

# LETS PLAY!! 
while run:

	#scoreboard
	pygame.draw.rect(screen, BLACK, [270, 40, 255, 90])
	score_text = small_font.render("YOUR SCORE = "+str(score), True, WHITE)
	score_text_rect = score_text.get_rect()
	score_text_rect.center = (width//2, 70)

	guesses_text = small_font.render("GUESSES LEFT = "+str(guesses), True, WHITE)
	guesses_text_rect = guesses_text.get_rect()
	guesses_text_rect.center = (width//2, 100)  

	screen.blit(score_text, score_text_rect)
	screen.blit(guesses_text, guesses_text_rect)
	
	#3 piles, previous card all the way to the left, next card in the center, and the new pile to the right #
	screen.blit(card_before, (left_margin,top_margin))
	screen.blit(card_current, (left_margin+120, top_margin))
	screen.blit(card_after, (left_margin+240, top_margin))   
	
	
	#track mouse
	mouse = pygame.mouse.get_pos()

	#button selection - use functions from button class 
	if higher_button.hover(mouse): 
		higher_button = button(LIGHT_GREEN,220,370,125,60,'HIGHER')
		higher_button.draw(screen)
	else: 
		higher_button = button(GREEN,220,370,125,60,'HIGHER')
		higher_button.draw(screen)
	if lower_button.hover(mouse):
		lower_button = button(LIGHT_RED,460,370,125,60,text='LOWER')
		lower_button.draw(screen)
	else: 
		lower_button = button(RED,460,370,125,60,text='LOWER')
		lower_button.draw(screen)
   
	#loop of events
	for event in pygame.event.get():

		#exit game
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		#click
		if not over and event.type == pygame.MOUSEBUTTONDOWN:
			if higher_button.hover(mouse):
				choice = 1 
			if lower_button.hover(mouse):
				choice = 0 

			# finish the game if the deck is finished
			if len(deck) == 1:
				over = True
			if choice != -1:    
				#current card to previous
				previous_card = current_card
				card_before = pygame.image.load(r'./cards/' + previous_card.value + previous_card.suit_type[0] + '.png')
				card_before = pygame.transform.scale(card_before , (100,160))
				
				#current card
				current_card = random.choice(deck)
				deck.remove(current_card)
				#card image
				card_current =  pygame.image.load(r'./cards/' + current_card.value + current_card.suit_type[0] + '.png')
				card_current = pygame.transform.scale(card_current , (100,160))

				#are results higher or lower, do they match guess?
				if cards_values[current_card.value] > cards_values[previous_card.value]:
					result = 1
				elif cards_values[current_card.value] < cards_values[previous_card.value]:
					result = 0
				else:
					result = -1    

				#change the scoreboard
				if result == -1:
					continue
				elif result == choice:
					score = score + 1
				else:
					guesses = guesses - 1      

				#if chances finished: end game 
				if guesses == 0:
					over = True

				#reset choices 
				choice = -1
				
	#if the game is finished, display the final score 
	if over == True:
		screen.fill(PURPLE)
		pygame.draw.rect(screen, BLACK, [270, 40, 255, 90])
		score_text = small_font.render("FINAL SCORE = "+str(score), True, WHITE)
		score_text_rect = score_text.get_rect()
		score_congrats = small_font.render('Great Job!',True, WHITE)
		score_congrats_rect = score_congrats.get_rect()
		score_text_rect.center = (width//2, 70)
		score_congrats_rect.center = (width//2, 100) 
		screen.blit(score_text, score_text_rect)
		screen.blit(score_congrats,score_congrats_rect)

	#update display after loops finished 
	pygame.display.update()
