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

    def Print(self):
        print   player.name +":" + \
                "\n\tFood: " + str(food) + \
                "\n\tTimes Hunted: " + str(timesHunted) + \
                "\n\tTimes Slacked " + str(timesSlacked) + \
                "\n\tReputation" + str(GetReputation()) + \
                "\n"
