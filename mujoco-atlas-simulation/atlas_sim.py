import mujoco_py

model = mujoco_py.load_model_from_path('atlas.xml')
sim = mujoco_py.MjSim(model)

while True:
    sim.step()
