import math
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from gymtut_mtcar9 import MountainCarEnv

test = MountainCarEnv()
test.reset()
for _ in range(1000):
    test.render()
    test.step(test.action_space.sample())
