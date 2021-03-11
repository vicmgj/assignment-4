# PROGRAM - TIC TAC TOE

# AUTHOR - VICTOR GARCIA

# *** SUMMARY ***

#   This program simulates one player playing tic tac toe 
#   against a computer. The RULES ARE:
#       Paper covers rock, paper wins
#       Scissors cut paper, scissors win
#       Rock breaks scissors, rock wins
#       All matching combinations are ties

#       Each player starts with $100
#       Each loss results in payment of $10 to other player

#       The player keeps playing until either player busts ($0)
#       OR 20 games have been played.

# *** INPUT ***
#       The player interactively enters each number they pick during play.

# *** OUTPUT ***
#       The output will consist of 1) the choice each player made (both number and corresponding word),
#       2) who won the game (Player 1 or 2), and 3) the amount of money left from each player.

#       When 20 games are played or someone busts, the final output
#       will be 1) the total number of games played, 2) total number of games won/tied,
#       3) the win percentage for both players and 4) the winner of tic tac toe.

import random # import random module

#===================================
    # initalize win, loss. and tie for tallying in printResults()
win = 0
loss = 0
tie = 0
    
    # create constants
player1_Winnings = 100 # starting balance for player 1, with each win/loss  balance will reflect that
player2_Winnings = 100 # starting balance for player 2/computer, with each win/loss balance will reflect that
betPerMatch = 10 # what player puts down each game

    # create variables
numPicked = 0 # number picked by player 1
numDrawn = 0  # number drawn from random module for player 2
betNumber = 0 # number of current game; if betNumber > 20, game will terminate and printResults
won = False   # flag, reset to True if either player wins

userInput = ""
comInput = ""

#====================================
def main():
    global numPicked, numDrawn, betNumber, player2_Winnings, player1_Winnings, win, loss, tie
    # print intro 
    print(
        '''
        Rock, Paper, and Scissors
        ------------------------
        This program plays the game of Rock, Paper, and Scissors. Two players choose either
        Rock, Paper. or Scissors, and the results of their picks are compared. Each match is
        determined as follows:
            Player 1        Player 2        Result
            --------        --------        ------
            Rock            Paper           Paper covers Rock.      Player 2 wins!
            Paper           Scissors        Scissors cut Paper      Player 2 wins!
            Scissors        Rock            Rock breaks Scissors    Player 2 wins!
            ---             ---         Any matching combo.         A tie!

        Now you are about to play against a computer. You are Player 1, and the computer
        is Player 2. Player 2's moves are randomly chosen by the computer. Both players
        start with $100 and the game is finished when either one player reaches $0 or there 
        have been 20 matches played. The bet per match is $10.
        ''')

    while (player1_Winnings != 0 and player2_Winnings != 0) and (betNumber != 20): # if either player hits $0 or games played are 20, program will exit out of loop

        # ask for player choice
        numPicked = playerChoice()

        # get computer choice
        numDrawn = computerChoice()
        
        # print results
        results()
    
    # print final results if conditions are met and game is terminated
    player1_win = (win/betNumber) * 100 # calculation to determine player 1's percentage won
    player2_win = (loss/betNumber) * 100 # calculation to determine player 2's percentage won
    
    if player1_win > player2_win: # player 1 will win if their win percentage is higher than player 2
        winner = 'Player 1!'
    elif player1_win == player2_win: # neither player will win if their win percentage is equal
        winner = 'No one'
    else: 
        winner = 'Player 2!' # player 2 will win if their win percentage is higher than player 1
    

    print(f'''
    -----------------------------------------------------------------
    And there you have it, folks, the final matchoff between our two
    contestants. The final results for tonight's game are as follows:

                        Player 1        Player 2
                        --------        --------
    Games Won:          {win}               {loss}
    Percent Won:        {player1_win:.2f}            {player2_win:.2f}

    Total games tied: {tie}

    Total games played: {betNumber}

    The overall winner is: {winner}

    Stop in again to play another exciting match'''.format(win, loss, player1_win, player2_win, tie, betNumber))

#======================================
def playerChoice():
    global numPicked
    global userInput
    
    # getting player 1's choice
    numPicked = int(input('''
    Player 1, enter your choice of
    1 - Rock
    2 - Paper
    3 - Scissors --> '''))

    # error checking for inputs outside of the range [1-3]
    while (numPicked < 1 or numPicked >3):
        numPicked = int(input('''
    Invalid input! Please try again.
    1 - Rock
    2 - Paper
    3 - Scissors --> '''))

    # checking input and storing numPicked integer as a string for reference later
    if numPicked == 1:
        userInput = 'Rock'
    elif numPicked == 2:
        userInput = 'Paper'
    else:
        userInput = 'Scissors'
    return numPicked # return value of player's choice



#======================================
def computerChoice():
    global comInput, numDrawn
    # use random module to select number between range of [1-3]
    numDrawn = random.randint(1,3)

    # checking random selection and storing numPicked integer as a string for reference later
    if numDrawn == 1:
        comInput = 'Rock'
    elif numDrawn == 2:
        comInput = 'Paper'
    else:
        comInput = 'Scissors'
    return numDrawn # return value of computer's choice

#======================================
def results():
    global betNumber, player1_Winnings, player2_Winnings
    global numPicked, numDrawn, win, loss, tie
    
    # print results of move
    if numPicked == numDrawn:
        result = 'Tie!'
        tie += 1
        betNumber += 1
    elif (userInput == 'Rock') and (comInput == 'Scissors'):
        won = True
        result = 'Player 1 wins!'
        betNumber += 1
        player2_Winnings -= betPerMatch
        player1_Winnings += 20
        win += 1
    elif (userInput == 'Scissors') and (comInput == 'Paper'):
        won = True
        result = 'Player 1 wins!'
        betNumber += 1
        player2_Winnings -= betPerMatch
        player1_Winnings += 20
        win += 1
    elif (userInput == 'Paper') and (comInput == 'Rock'):
        won = True
        result = 'Player 1 wins!'
        betNumber += 1
        player2_Winnings -= betPerMatch
        player1_Winnings += 20
        win += 1
    else:
        won = True
        result = 'Player 2 wins!'
        betNumber += 1
        player1_Winnings -= betPerMatch
        player2_Winnings += 20
        loss += 1

    # print results
    print (f'''
    RESULTS OF THIS MOVE
    --------------------
    Player 1            Player 2            Player 1's        Player 2's
    Number  Action      Number   Action       Money             Money
    ------  ------      ------   ------     ----------       -----------
    {numPicked}       {userInput}       {numDrawn}        {comInput}        {player1_Winnings}              {player2_Winnings}
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    '''.format(numPicked, userInput, numDrawn, comInput, player1_Winnings, player2_Winnings))

#======================================
    # plays game
main()

