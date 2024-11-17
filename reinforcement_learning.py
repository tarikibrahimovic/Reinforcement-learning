# import gymnasium as gym
# from moviepy.editor import ImageSequenceClip
# from moviepy.config import change_settings

# from gymnasium.envs.registration import registry
# from ale_py import ALEInterface

# ale = ALEInterface()
# print(ale.getAvailableModes())


# print("Available environments:")
# print([env_spec.id for env_spec in registry.values()])

# env = gym.make("CartPole-v0")
# print("Environment loaded successfully!")

# epochs = 0

# frames = []  # for animation
# done = False

# env = gym.make("ALE/Breakout-v5", render_mode="rgb_array")
# observation, info = env.reset()

# while not done:
#     action = env.action_space.sample()
#     observation, reward, terminated, truncated, info = env.step(action)

#     # Put each rendered frame into dict for animation
#     frames.append(
#         {
#             "frame": env.render(),
#             "state": observation,
#             "action": action,
#             "reward": reward,
#         }
#     )

#     epochs += 1
#     if epochs == 1000:
#         break


# def create_gif(frames: dict, filename, fps=100):
#     """
#     Creates a GIF animation from a list of RGBA NumPy arrays.

#     Args:
#         frames: A list of RGBA NumPy arrays representing the animation frames.
#         filename: The output filename for the GIF animation.
#         fps: The frames per second of the animation (default: 10).
#     """
#     rgba_frames = [frame["frame"] for frame in frames]

#     clip = ImageSequenceClip(rgba_frames, fps=fps)
#     clip.write_gif(filename, fps=fps)


# # Example usage
# create_gif(frames, "animation.gif")  # saves the GIF locally
# change_settings({"FFMPEG_BINARY": "/usr/bin/ffmpeg"})

import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make("CartPole-v1", render_mode="human", max_episode_steps=1000)
observation, info = env.reset()

for episode in range(10):  # Pokreće 10 epizoda
    observation, info = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()  # Nasumična akcija
        observation, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated


env.close()
