import tensorflow as tf
import numpy as np


class Actor(tf.keras.Model):
    def __init__(self):
        super(Actor, self).__init__()
        self.dense1 = tf.keras.layers.Dense(64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(64, activation='relu')
        self.dense3 = tf.keras.layers.Dense(6, activation='tanh')

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        x = self.dense3(x)
        return x

class DDPGAgent:
    def __init__(self, env, actor, critic, actor_lr=0.001, critic_lr=0.001, gamma=0.99):
        self.env = env
        self.actor = actor
        self.critic = critic
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=actor_lr)
        self.critic_optimizer = tf.keras.optim
