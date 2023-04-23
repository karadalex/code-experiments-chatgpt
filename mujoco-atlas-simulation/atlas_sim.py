import mujoco_py
import numpy as np

model = mujoco_py.load_model_from_path('atlas.xml')
sim = mujoco_py.MjSim(model)
view = mujoco_py.MjViewer(sim)

# Set initial pose to crouched position
print(sim.data.qpos)
crouched_pos = np.array([0.0, 0.0, 0.9, -1.6, 0.8, 0.0, 0.0, 0.0, 0.0, -0.9, 1.6, -0.8])
sim.data.qpos[:12] = crouched_pos
sim.forward()

# Simulation parameters
n_steps = 1000
ctrl_freq = 50
ctrl_delay = 10
ctrl_time = 1.0 / ctrl_freq

# PD controller gains
kp = 0.5
kd = 0.1

# Desired standing position
# standing_pos = np.array([0.0, 0.0, 1.25, -1.5, 0.0, 0.0, 0.0, 0.0, 0.0, -1.5, 0.0, 0.0])
standing_pos = np.array([0.0, -1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# Main loop
i = 0
while True:
    # Compute joint torques using PD controller
    qpos = sim.data.qpos[:12]
    qvel = sim.data.qvel[:12]
    tau = -kp * (qpos - crouched_pos) - kd * qvel

    # Apply torques to robot joints
    sim.data.ctrl[:12] = tau

    # Step simulation
    sim.step()
    view.render()

    # Delay control loop
    if i % ctrl_delay == 0:
        mujoco_py.functions.mj_step1(model, sim.data)

    # Print robot state
    if i % ctrl_freq == 0:
        print('Step:', i)
        print('Position:', sim.data.qpos[:7])
        print('Velocity:', sim.data.qvel[:6])

    i+=1
