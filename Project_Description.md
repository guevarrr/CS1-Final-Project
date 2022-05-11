# CS1-Final-Project

High-Low Game (also known as "Ride the Bus")

Background: 

We chose to implement a High-Low guessing game using pygames. We chose this game due to its similarity to a beloved college drinking game that involves a deck of cards, a dealer, and various participants. 

Premise & Rules: 

0. There will be a three piles of cards displayed on the screen upon initialization of the game. The left-most pile represents the previous card drawn (at the start of the game, there will be no card face shown), the center pile is the card that has just been drawn, and the right-most pile represents the deck that is being drawn from, and will always be facedown. There will also be a scoreboard above the cards that will keep track of the player's score and the player's remaining chances (total of 5). Below the cards there will be two buttons, one labelled "higher" and one labelled "lower." These buttons represent the player's "guess" regarding whether or not the next card that will be drawn will be higher or lower than the card displayed in the middle pile. 
1. Upon game initiation, the player will make an educated guess as to whether or not the next card that is drawn will be higher or lower than the center card. The player will then click on the "higher" button or the "lower" button to guess. 
2. If the player is correct in their guess, their score will increase by 1, and their remaining guesses will not decrement. If the player is incorrect in their guess, their score will not increase, and their remaining guesses will decrement by 1 chance. If the card is of the same value, the player will neither gain a point, nor lose an opportunity to guess. 
3. Once the player has exhausted their chances, their final score will be displayed on the screen! 
