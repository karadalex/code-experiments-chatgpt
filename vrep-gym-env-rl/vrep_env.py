import gym
import numpy as np
import pyrep
# import pyrep.robots


class VREPEnv(gym.Env):
    def __init__(self):
        self.pyrep = pyrep.PyRep()
        self.pyrep.launch('./vrep-scene.ttt')
        self.agent = pyrep.robots.UR5('UR5')
        self.action_space = gym.spaces.Box(
            low=-1.0,
            high=1.0,
            shape=(self.agent.get_joint_count(),),
            dtype=np.float32
        )
        self.observation_space = gym.spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(self.agent.get_joint_count() + 1,),
            dtype=np.float32
        )

    def step(self, action):
        self.agent.set_joint_target_velocities(action)
        self.pyrep.step()
        observation = np.concatenate([self.agent.get_joint_positions(), self.agent.get_tip().get_position()])
        reward = 0
        done = False
        info = {}
        return observation, reward, done, info

    def reset(self):
        self.pyrep.stop()
        self.pyrep.start()
        self.agent.reset_dynamic_object()
        observation = np.concatenate([self.agent.get_joint_positions(), self.agent.get_tip().get_position()])
        return observation

    def render(self, mode='human'):
        pass

