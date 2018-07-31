import gym
import time
env = gym.make('CartPole-v0')
for i_episode in range(30):
    observation = env.reset()
    for t in range(100):
        env.render()
        time.sleep(0.01)
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break