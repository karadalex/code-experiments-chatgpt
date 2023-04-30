import gym
from vrep_env import VREPEnv

env = VREPEnv()
observation = env.reset()
for t in range(1000):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
env.close()
