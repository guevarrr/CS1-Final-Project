### working hi-lo game code -- completed

import pygame
import random
from card import Card
from aesthetics import *
from button import button

 
# The deck of cards - List of Objects
deck = []

# Loop for every type of suit
for suit in suits:

	# Loop for every type of card in a suit
	for card in cards:

		# Adding the card to the deck
		deck.append(Card(suit, card))

# Initializing PyGame
pygame.init()


# Setting up the screen and background
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(DARK_GREEN)

# Setting up caption
pygame.display.set_caption("Higher or Lower Game")

# Loading image for the icon
icon = pygame.image.load('icon.jpeg')

# Setting the game icon
pygame.display.set_icon(icon)


# Types of fonts to be used
small_font = pygame.font.SysFont('comicsans', 20)
large_font = pygame.font.SysFont('comicsans', 20)

# High and Low Game Buttons
high_button = button(GREEN,220,370,125,60,'HIGHER')
high_button.draw(screen)

low_button = button(RED,460,370,125,60,text='LOWER')
low_button.draw(screen)


# Load the card image
prev_card = pygame.image.load(r'./cards/card_cover.png')

# Scale the loaded image 
prev_card = pygame.transform.scale(prev_card , (100,160))

# Choose the starting card from the deck
current_card = random.choice(deck)

# Keep choosing until it is not the highest or lowest
while current_card.value == "A" or current_card.value == "K":
	current_card = random.choice(deck)

# Load the card image   
cur_card =  pygame.image.load(r'./cards/' + current_card.value + current_card.suit_type[0] + '.png')

# Scale the loaded card image
cur_card = pygame.transform.scale(cur_card , (100,160))

# Remove the card from the deck
deck.remove(current_card)

# Loading the card image
next_card =  pygame.image.load(r'./cards/card_cover.png')

# Scaling the loaded image
next_card = pygame.transform.scale(next_card , (100,160))

# Number of chances left
chances = 5

# The current score
score = 0

# User's choice initialized
choice = -1

# Used to stop game functioning, if True
over = False

run = True
high_button = button(GREEN,220,370,125,60,'HIGHER')
low_button = button(RED,460,370,125,60,text='LOWER')

# The GAME LOOP
while run:

	# Displaying scoreboard
	pygame.draw.rect(screen, BLACK, [270, 40, 255, 90])
	score_text = small_font.render("YOUR SCORE = "+str(score), True, WHITE)
	score_text_rect = score_text.get_rect()
	score_text_rect.center = (WIDTH//2, 70)


	chances_text = small_font.render("GUESSES LEFT = "+str(chances), True, WHITE)
	chances_text_rect = chances_text.get_rect()
	chances_text_rect.center = (WIDTH//2, 100)  
	
	#score-board texts
	screen.blit(score_text, score_text_rect)
	screen.blit(chances_text, chances_text_rect)
	
	#3 piles, previous card all the way to the left, next card in the center, and the new pile to the right #
	screen.blit(prev_card, (MARGIN_LEFT,MARGIN_TOP))
	screen.blit(cur_card, (MARGIN_LEFT+120, MARGIN_TOP))
	screen.blit(next_card, (MARGIN_LEFT+240, MARGIN_TOP))   
	
	
	# Tracking the mouse movements
	mouse = pygame.mouse.get_pos()

	#Button Selection
	if high_button.isOver(mouse): 
		high_button = button(LIGHT_GREEN,220,370,125,60,'HIGHER')
		high_button.draw(screen)
	else: 
		high_button = button(GREEN,220,370,125,60,'HIGHER')
		high_button.draw(screen)
	if low_button.isOver(mouse):
		low_button = button(LIGHT_RED,460,370,125,60,text='LOWER')
		low_button.draw(screen)
	else: 
		low_button = button(RED,460,370,125,60,text='LOWER')
		low_button.draw(screen)
   
	# Loop events occuring inside the game window 
	for event in pygame.event.get():

		# Qutting event
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		#MOUSE-CLICK
		if not over and event.type == pygame.MOUSEBUTTONDOWN:
			if high_button.isOver(mouse):
				choice = 1 
			if low_button.isOver(mouse):
				choice = 0 

			# Finish the game if the deck is finished
			if len(deck) == 1:
				over = True

			# If a valid choice, the game logic 
			if choice != -1:    

				# Change current card to previous
				previous_card = current_card
				prev_card = pygame.image.load(r'./cards/' + previous_card.value + previous_card.suit_type[0] + '.png')
				prev_card = pygame.transform.scale(prev_card , (100,160))
				 
				# Set up the current card
				current_card = random.choice(deck)
				deck.remove(current_card)

				cur_card =  pygame.image.load(r'./cards/' + current_card.value + current_card.suit_type[0] + '.png')
				cur_card = pygame.transform.scale(cur_card , (100,160))

				# Check the result, that is, High or Low
				if cards_values[current_card.value] > cards_values[previous_card.value]:
					result = 1
				elif cards_values[current_card.value] < cards_values[previous_card.value]:
					result = 0
				else:
					result = -1    

				# Manage the game variables
				if result == -1:
					continue
				elif result == choice:
					score = score + 1
				else:
					chances = chances - 1      

				# End the game if chances are finished
				if chances == 0:
					over = True

				# Reset the choice
				choice = -1
				
				

	# If the game is finished, display the final score
	if over == True:
		screen.fill(PURPLE)
		pygame.draw.rect(screen, BLACK, [270, 40, 255, 90])
		score_text = small_font.render("FINAL SCORE = "+str(score), True, WHITE)
		score_text_rect = score_text.get_rect()
		score_congrats = small_font.render('Great Job!',True, WHITE)
		score_congrats_rect = score_congrats.get_rect()
		score_text_rect.center = (WIDTH//2, 70)
		score_congrats_rect.center = (WIDTH//2, 100) 
		screen.blit(score_text, score_text_rect)
		screen.blit(score_congrats,score_congrats_rect)

	# Update the display after each game loop
	pygame.display.update()