class GamePlayer:
    def __init__(self):
        self.food = 0
        self.timesHunted = 0
        self.timesSlacked = 0
        self.playerLogic = None

    def GetReputation(self, other):
    	if ( 0 == timesHunted and 0 == timesSlacked ):
    		return 0
    	else:
    		return timesHunted/(timesHunted + timesSlacked)

    def IsDead(self):
    	return (food <= 0)

    def Clone(self):
    	clonedPlayer = GamePlayer()
    	clonedPlayer.food = food
    	clonedPlayer.timesHunted = timesHunted
    	clonedPlayer.timesSlacked = timesSlacked
    	clonedPlayer.playerLogic = playerLogic.Clone()
    	return clonedPlayer