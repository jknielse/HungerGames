class GamePlayer:
    def __init__(self):
        self.food = 0
        self.timesHunted = 0
        self.timesSlacked = 0
        self.player = None

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
    	clonedPlayer.player = player.Clone()
    	return clonedPlayer

    def print(self):
        print   player.name +":" + \
                "\n\tFood: " + food + \
                "\n\tTimes Hunted: " + timesHunted + \
                "\n\tTimes Slacked " + timesSlacked + \
                "\n\tReputation" + GetReputation()
