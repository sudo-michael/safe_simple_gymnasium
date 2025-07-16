from gymnasium.envs.registration import register

register(
     id="SafeCartPole-Arushi-v0",
     entry_point="safe_simple_gymnasium.envs:SafeCartPoleEnv",
     max_episode_steps=200,
     kwargs={'zero_cost_zone': 'arushi'}
)

register(
     id="SafeCartPole-ArushiModify-v0",
     entry_point="safe_simple_gymnasium.envs:SafeCartPoleEnv",
     max_episode_steps=200,
     kwargs={'zero_cost_zone':'arushi-modify'}
)

register(
     id="SafeCartPole-RightSide-v0",
     entry_point="safe_simple_gymnasium.envs:SafeCartPoleEnv",
     max_episode_steps=200,
     kwargs={'zero_cost_zone': 'right-side'}
)

register(
     id="SafeCartPole-FarRightSide-v0",
     entry_point="safe_simple_gymnasium.envs:SafeCartPoleEnv",
     max_episode_steps=200,
     kwargs={'zero_cost_zone':'far-right-side'}
)