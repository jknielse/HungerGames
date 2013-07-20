class GamePlayer:
    def __init__(self):
        self.food = None
        self.timesHunted = None
        self.timesSlacked = None
        self.playerLogic = None

    def GetReputation(self, other):
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