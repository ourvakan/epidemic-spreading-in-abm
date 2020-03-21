from abc import ABC, abstractmethod
from typing import List, Dict

import numpy as np


class Topology(ABC):

    @abstractmethod
    def generate_clusters(self, *args, **kwargs) -> Dict[int, np.array]:
        pass


class ExponentialGraph(Topology):

    def __init__(self, n: int):
        """
        :param n: number of agents in the system
        """
        self.n = n

    def generate_clusters(self, params: dict) -> Dict[int, np.array]:
        """
        Generate clusters of integers from 0 to n-1
        with exponentially distributed sizes
        :param params: {beta: float}, exponential factor (inverse temperature)
        :return: Dictionary:
                {num_of_cluster (int): cluster indices (np.array)}
        """

        try:
            beta = params['beta']
        except KeyError:
            beta = 1

        # print('Initializing clusters for ExponentialGraph')
        cluster_indices = []
        ind = 0
        while ind < self.n:
            ind += int(np.random.exponential(scale=beta)) + 1
            cluster_indices.append(np.minimum(ind, self.n - 1))

        clusters = np.split(np.arange(self.n), indices_or_sections=cluster_indices)
        n_clusters = len(clusters)
        # print(f'The total number of clusters is {n_clusters}')

        return dict(zip(range(n_clusters), clusters))
