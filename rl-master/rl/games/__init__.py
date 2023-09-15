
from .lunar_lander import LunarLander
from .lunar_lander_reward import LunarLanderReward


GAME_MAP = {

    'lunar_lander': LunarLander,
    'lunar_lander_reward': LunarLanderReward,

}


def create_game(game, cfg, agent_cls, model_cls):
    assert game in GAME_MAP, f'game {game} is not supported'
    return GAME_MAP[game](cfg, agent_cls, model_cls)
