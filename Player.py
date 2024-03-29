# This file is intended to be a final submission. python tester.py Player.py
# should work at all times. If it does not, there is a bug.
# If you're just trying to test a solution, scroll down to the Player
# class.

# This file is intended to be in the same format as a valid solution, so
# that users can edit their solution into Player and then submit just this
# file to the contest. If you see any reason this would not work, please submit
# an Issue to https://github.com/ChadAMiller/hungergames/issues or email me.

# You can see more sample player classes in bots.py

class BasePlayer(object):
    '''
    Base class so I don't have to repeat bookkeeping stuff.
    Do not edit unless you're working on the simulation.
    '''
    
    def __str__(self):
        try:
            return self.name
        except AttributeError:
            # Fall back on Python default
            return super(BasePlayer, self).__repr__()
    
    def hunt_choices(*args, **kwargs):
        raise NotImplementedError("You must define a strategy!")
        
    def hunt_outcomes(*args, **kwargs):
        pass
        
    def round_end(*args, **kwargs):
        pass


class Player(BasePlayer):
    
    def __init__(self):
        self.name = "Player"
        self.lower = 0.05
        self.upper = 0.1

    def hunt_choices(
                    self,
                    round_number,
                    current_food,
                    current_reputation,
                    m,
                    player_reputations,
                    ):
        # Behaviour:
        # If the reputation of the other player is within a certain range above (self.upper) or a certain range below (self.lower), 
        # and their repution is *not* 100%, then we will hunt with them.
        return ['h' if (abs(rep - current_reputation) < self.upper) and (rep >= current_reputation - self.lower) and (rep != 1.0) else 's' for rep in player_reputations]
        

    def hunt_outcomes(self, food_earnings):
        '''Required function defined in the rules'''
        pass
        

    def round_end(self, award, m, number_hunters):
        '''Required function defined in the rules'''
        pass
        
