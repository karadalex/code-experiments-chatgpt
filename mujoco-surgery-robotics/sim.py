import mujoco_py
import numpy as np

model = mujoco_py.load_model_from_path("robot.xml")
sim = mujoco_py.MjSim(model)
view = mujoco_py.MjViewer(sim)

while True:
    sim.step()
    view.render()
