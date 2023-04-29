import gym
import vrep_env

env = gym.make('VREPEnv-v0')
observation = env.reset()
for t in range(1000):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
env.close()
