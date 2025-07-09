from gymnasium.envs.registration import register

register(
     id="SafePendulum-v0",
     entry_point="safe_simple_gymnasium.envs:SafePendulumEnv",
     max_episode_steps=200,
)

register(
     id="SafeCartPole-v0",
     entry_point="safe_simple_gymnasium.envs:SafeCartPoleEnv",
     max_episode_steps=200,
)