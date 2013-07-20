def PrintM(gameRound) :
	print "Value of 'm' for this round: " + str(gameRound.m)

def PrintGameRound(gameRound) :
	gameRound.PrintM()
	for gamePlayer in gameRound.gamePlayerList :
		gamePlayer.Print()

def PrintGameRoundPlayers(gameRound, players) :
	gameRound.PrintM()
	for gamePlayer in gameRound.gamePlayerList :
		if gamePlayer.player in players:
			gamePlayer.Print()

def PrintGameRoundList(gameRoundList) :
	roundCounter = 1
	for gameRound in gameRoundList :
		print "***** NEW ROUND *****"
		print "Round " + str(roundCounter)
		PrintGameRound(gameRound)
		print "***** END ROUND *****"
		roundCounter += 1

def PrintGameRoundListPlayers(gameRoundList, players) :
	for gameRound in gameRoundList :
		print "***** NEW ROUND *****"
		PrintGameRoundPlayers(gameRound, players)
		print "***** END ROUND *****"

def PrintPlayerInfo(gameRoundList, player, roundPrintPeriod = 1) :
	playerIndex = None
	index = 0
	for gamePlayer in gameRoundList[0].gamePlayerList :
		if gamePlayer.player.name == player.name :
			playerIndex = index
			break
		index += 1

	playerFood = gameRoundList[0].gamePlayerList[playerIndex].food

	roundNum = 0
	print "FOOD\tREP\n"
	for gameRound in gameRoundList :
		if 0 == roundPrintPeriod or roundNum % roundPrintPeriod == 0 :
			gamePlayer = gameRound.gamePlayerList[playerIndex]

			foodDiff = gamePlayer.food - playerFood
			foodDiffString = (("+" + str(foodDiff)) if (foodDiff > 0) else str(foodDiff))

			print foodDiffString + "\t" + str(gamePlayer.getReputation()) + "\n"

			playerFood = gamePlayer.food
		
		roundNum += 1