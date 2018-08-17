import sys
import gym
output = sys.stdout
file = open('gym/help_gym_out.txt','w')
sys.stdout = file

help(gym)

sys.stdout = output
file.close()