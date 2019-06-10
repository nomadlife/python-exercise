import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
    #print(env.step(action))
    #print(env.observation_space,env.observation_space.high)