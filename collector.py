from typing import Union, List
from collections import defaultdict
import pandas as pd

from agent import Agent


class Collector:
    """ Collects statistics called history """

    def __init__(self):

        self._history = defaultdict(lambda: defaultdict(int))
        self.agents = {}
        self.history_df = None
    #     self.max_infected = 1
    #
    # @property
    # def max_infected(self):
    #     pass

    def log_step(self, step: int, agents: List[Agent]) -> int:

        for agent in agents:
            self._history[step][agent.state] += 1

        return self._history[step]['INFECTED']

    def modify_history(self, step: int, agent_state: str, n_agents: int = 1):

        for _ in range(n_agents):
            if agent_state == 'INFECTED':
                self._history[step]['INFECTED'] += 1
            elif agent_state == 'SUSCEPTIBLE':
                self._history[step]['SUSCEPTIBLE'] += 1
            elif agent_state == 'RECOVERED':
                self._history[step]['RECOVERED'] += 1

    def add_statistics(self, property_, value):

        if not property_ in self.__dict__:
            setattr(self, property_, value)
        print(self.__dict__)

    def history_as_df(self, reuse=False):

        if reuse:
            if self.history_df:
                return self.history_df

        rows = [{'step': step,
                 'infected': self._history[step]['INFECTED'],
                 'recovered': self._history[step]['RECOVERED'],
                 'dead': self._history[step]['DEAD'],
                 'susceptible': self._history[step]['SUSCEPTIBLE'],
                 'immune': self._history[step]['IMMUNE']} for step in range(len(self._history))]

        self.history_df = pd.DataFrame(rows)
        return self.history_df

