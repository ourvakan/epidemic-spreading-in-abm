import numpy as np


class Agent:
    """ A model of a human being who can be in different states """

    def __init__(self, state='SUSCEPTIBLE', mean_recovery: float = 100, std_recovery: float = 10, death_factor: float = 0.005):
        self.state = state
        self.days_for_recovery = np.random.normal(mean_recovery, std_recovery)
        self.will_die_if_infected = 1 if np.random.uniform() < death_factor else 0
        self.days_infected = 0
