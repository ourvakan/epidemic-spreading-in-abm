from typing import List
import numpy as np
from abc import ABC, abstractmethod

from agent import Agent


class Policy(ABC):

    @abstractmethod
    def apply_policy(self, agents: List[Agent]):
        pass


class MolecularPolicy(Policy):

    def __init__(self, spread_factor: float):
        self.sf = spread_factor

    def apply_policy(self, agents: List[Agent]):
        """
        In molecular policy the probability spreads among cluster participants
        proportionally to total probability
        :param agents:
        :return:
        """

        n_infected = sum([1 for agent in agents if agent.state == 'INFECTED'])

        if n_infected == 0 or n_infected == len(agents):
            return

        if len(agents) - n_infected > 0:
            prob = self.sf * n_infected / (len(agents) - n_infected)

            for k in range(len(agents)):
                if agents[k].state == 'SUSCEPTIBLE':
                    if np.random.uniform() < prob:
                        agents[k].state = 'INFECTED'
