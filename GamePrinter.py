def printM(gameRound):
	print "Value of 'm' for this round: " gameRound.m

def printGameRound(gameRound):
	gameRound.printM()
	for gamePlayer in gameRound.gamePlayerList :
		gamePlayer.print()

def printGameRoundPlayer(gameRound, player):