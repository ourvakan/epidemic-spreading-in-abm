from typing import List
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import multiprocessing as mp
from multiprocessing.pool import ThreadPool

import numpy as np
import pandas as pd

from topology import Topology, ExponentialGraph
from agent import Agent
from policy import Policy, MolecularPolicy
from collector import Collector
from visualization.plots import plot_history, area_plot


class Simulation:

    def __init__(self, topology: Topology = None, agents: List[Agent] = None,
                 spread_policy: Policy = None, **model_parameters):
        self.topology = topology
        self.agents = agents
        self.model_parameters = model_parameters
        self.spread_policy = spread_policy
        self.collector = Collector()
        self.step = 0
        self.history_path = None

    def run(self):
        """
        advance in one time stamp
        """
        total_infected = 1

        while total_infected > 0:
            # first determine what happens to the agents according to their history
            Simulation.update_agents_states(self.agents)

            # cluster according to the probability of collisions
            new_clusters = self.topology.generate_clusters(self.model_parameters)

            # recalculate states of agents
            for cluster, clustered_agents_ind in new_clusters.items():
                agents_in_cluster = [self.agents[i] for i in clustered_agents_ind]
                self.spread_policy.apply_policy(agents_in_cluster)

            total_infected = self.collector.log_step(self.step, self.agents)
            self.step += 1

        return self.collector.history_as_df()

    @staticmethod
    def save_history(df: pd.DataFrame, reuse: bool = True, prefix: str = ''):
        """ Save history in a csv file"""

        new_path = f'./data/simulations/{prefix}_{datetime.now().strftime("%m-%d-%Y__%H-%M-%S")}.csv'
        df.to_csv(new_path)
        return new_path

    @staticmethod
    def plot_history(pth):
        # plot_history(pth)
        area_plot(pth)

    @staticmethod
    def update_agents_states(agents):

        for agent in agents:
            if agent.state == 'INFECTED':
                if agent.days_for_recovery > agent.days_infected:
                    agent.days_infected += 1
                else:
                    agent.state = 'DEAD' if agent.will_die_if_infected else 'RECOVERED'

    def set_up(self,
               n_agents=10000,
               mean_recovery=200,
               std_recovery=6,
               death_factor=0.02,
               spread_factor=0.1,  # coefficient of proportionality between number of infected and probability to infect
               p_immune=0.3,  # percentage of immune citizens
               number_of_infected=1):

        expgraph = ExponentialGraph(n=n_agents)
        spread_pol = MolecularPolicy(spread_factor=spread_factor)

        all_agents = [Agent(state='IMMUNE' if np.random.uniform() < p_immune else 'SUSCEPTIBLE',
                            mean_recovery=mean_recovery,
                            std_recovery=std_recovery,
                            death_factor=death_factor)
                      for _ in range(n_agents)]

        # infiltrate the virus!
        for _ in range(number_of_infected):
            k = np.random.choice(len(all_agents))
            all_agents[k].state = 'INFECTED'

        self.topology = expgraph
        self.agents = all_agents
        self.spread_policy = spread_pol


def smooth(sim: Simulation, n=20):

    pool = ThreadPool(mp.cpu_count() - 1)
    results = pool.starmap(sim.run, [() for _ in range(n)])

    mean = pd.concat(results).mean(level=0)
    history_path = sim.save_history(mean, prefix='mean')
    sim.plot_history(history_path)


def simple_run(sim):

    history = sim.run()
    history_path = sim.save_history(history)
    sim.plot_history(history_path)


if __name__ == '__main__':

    n_agents = 1000

    beta = 100
    mean_recovery = 40
    sf = 0.05

    simulation = Simulation(beta=beta)
    simulation.set_up(n_agents=n_agents,
                      mean_recovery=mean_recovery,
                      std_recovery=6,
                      death_factor=0.02,
                      spread_factor=sf,  # proportionality between number of infected and probability to infect
                      p_immune=0.2,  # percentage of immune citizens
                      number_of_infected=1)

    smooth(simulation, n=100)

