import mujoco_py

model = mujoco_py.load_model_from_path('atlas.xml')
sim = mujoco_py.MjSim(model)
view = mujoco_py.MjViewer(sim)

# Set initial pose to crouched position
crouched_pos = [0.0, 0.0, 0.9, -1.6, 0.8, 0.0, 0.0, 0.0, 0.0, -0.9, 1.6, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
sim.data.qpos[:] = crouched_pos
sim.forward()

# Simulation parameters
n_steps = 1000
ctrl_freq = 50
ctrl_delay = 10
ctrl_time = 1.0 / ctrl_freq

# PD controller gains
kp = 100
kd = 1

# Main loop
while True:
    # Compute joint torques using PD controller
    qpos = sim.data.qpos
    qvel = sim.data.qvel
    tau = -kp * (qpos - crouched_pos) - kd * qvel

    # Apply torques to robot joints
    sim.data.ctrl[:] = tau

    # Step simulation
    sim.step()
    view.render()

    # Delay control loop
    if i % ctrl_delay == 0:
        mujoco_py.functions.mj_step1(model.ptr, sim.data.ptr)

    # Print robot state
    if i % ctrl_freq == 0:
        print('Step:', i)
        print('Position:', sim.data.qpos[:7])
        print('Velocity:', sim.data.qvel[:6])
