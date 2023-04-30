import gym
import pybullet_envs
import numpy as np


class KukaGraspingEnv(gym.Env):
    def __init__(self):
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(14,))
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(6,))
        self.reward_range = (-float('inf'), float('inf'))
        self.env = gym.make('KukaBulletEnv-v0', renders=True, isDiscrete=False)
        self.env.render(mode='human')

    def reset(self):
        self.env.reset()
        obs = self._get_obs()
        return obs

    def step(self, action):
        self.env.applyAction(action)
        obs = self._get_obs()
        reward = self._get_reward()
        done = self._get_done()
        info = {}
        return obs, reward, done, info

    def render(self, mode='human'):
        self.env.render(mode=mode)

    def close(self):
        self.env.close()

    def _get_obs(self):
        state = self.env.getExtendedObservation()
        obs = np.concatenate([state[0], state[1]])
        return obs

    def _get_reward(self):
        state = self.env.getExtendedObservation()
        gripper_pos = state[0][:3]
        target_pos = state[1][:3]
        dist = np.linalg.norm(gripper_pos - target_pos)
        if dist < 0.1:
            reward = 1
        else:
            reward = -0.1
        return reward

    def _get_done(self):
        state = self.env.getExtendedObservation()
        gripper_pos = state[0][:3]
        target_pos = state[1][:3]
        dist = np.linalg.norm(gripper_pos - target_pos)
        done = dist < 0.1
        return done
