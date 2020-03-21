import numpy as np


class Agent:
    """ A model of a human being who can be in different states """
    # TODO:  make days_infected a property (so that it updates when the step in simulation changes)

    def __init__(self, state='SUSCEPTIBLE', mean_recovery: float = 100, std_recovery: float = 10, death_factor: float = 0.005):
        self.state = state  # 'IMMUNE', 'INFECTED', 'RECOVERED', 'SUSCEPTIBLE', maybe it is worth adding 'QUARANTEENED'
        self.days_for_recovery = np.random.normal(mean_recovery, std_recovery)
        self.will_die_if_infected = 1 if np.random.uniform() < death_factor else 0
        self.days_infected = 0


if __name__ == '__main__':

    import pandas as pd

    d1 = np.ones(20).reshape(-1, 4)
    d2 = np.ones(20).reshape(-1, 4)
    d3 = np.ones(16).reshape(-1, 4)
    df1 = pd.DataFrame(d1)
    df2 = pd.DataFrame(d2)
    df3 = pd.DataFrame(d3)

    print(df3)

    results = [df1, df2, df3]
    dfm = pd.concat(results).sum(level=0)

    print(dfm)
