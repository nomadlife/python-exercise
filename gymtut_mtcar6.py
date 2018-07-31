import math
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from gymtut_mtcar9 import MountainCarEnv

env = MountainCarEnv()

for i_episode in range(30):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
