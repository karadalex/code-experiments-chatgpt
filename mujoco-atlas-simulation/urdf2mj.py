import mujoco_py

model = mujoco_py.load_model_from_path('atlas_v3.urdf.xml')
mjcf_data = mujoco_py.mjcf.from_urdf_string(model.get_xml())
mjcf_data.save_xml('atlas.xml')