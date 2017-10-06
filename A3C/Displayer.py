
import os

import numpy as np
import matplotlib.pyplot as plt

import parameters


def save(saver, fig_name):
    if parameters.DISPLAY:
        for path, data in saver:
            plt.plot(data)
        fig = plt.gcf()
        fig.savefig(fig_name)
        plt.show(block=False)
    else:
        for path, data in saver:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            data = " ".join(map(str, data))
            with open(path, "w") as file:
                file.write(data)


class Displayer:

    def __init__(self):
        self.rewards = [[] for a in range(parameters.THREADS + 1)]
        self.sequential_rewards = []

    def add_reward(self, reward, n_agent):
        self.rewards[n_agent].append(reward)
        if n_agent != 0:
            self.sequential_rewards.append(reward)
        if n_agent == 1 and len(self.rewards[1]) % 100 == 0:
            if parameters.DISPLAY:
                self.disp_one()
            else:
                print(self.rewards[1][max(0, -50):])

    def disp_all(self):
        saver = [("results/All_rewards/All_rewards_" + str(i), self.rewards[i])
                 for i in range(len(self.rewards))]
        save(saver, "results/All_rewards.png")

    def disp_one(self):
        reward = self.rewards[1]
        mean_reward = [np.mean(reward[max(1, i - 100):i])
                       for i in range(2, len(reward))]
        saver = [("results/One_reward", reward),
                 ("results/One_mean_reward", mean_reward)]
        save(saver, "results/One_reward.png")

    def disp_seq(self):
        mean_reward = [np.mean(self.sequential_rewards[max(1, i - 100):i])
                       for i in range(2, len(self.sequential_rewards))]
        saver = [("results/Seq_reward", self.sequential_rewards),
                 ("results/Seq_mean_reward", mean_reward)]
        save(saver, "results/Seq_reward.png")


DISPLAYER = Displayer()
