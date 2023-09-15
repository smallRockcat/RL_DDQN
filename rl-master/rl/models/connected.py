from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


def create_model(cfg, layer_count, dense_count):
    assert layer_count > 1, 'at least one layer'
    model = Sequential()
    for i in range(layer_count):
        if i == 0:
            model.add(Dense(dense_count[i], input_dim=cfg['input'], activation='relu'))
        else:
            model.add(Dense(dense_count[i], activation='relu'))
    model.add(Dense(cfg['output'], activation='linear'))
    model.compile(loss='mse', optimizer=Adam(learning_rate=cfg['learning_rate']))
    return model


def create_model_factory(layer_count, dense_count):
    assert layer_count > 1, 'at least one layer'

    class ConnectedModel:
        @staticmethod
        def create(cfg):
            return create_model(cfg, layer_count, dense_count)
    return ConnectedModel

def create_DQN():
    class DQN:
        @staticmethod
        def create(cfg):
            return build_model(cfg)
    return DQN

def build_model(cfg):

            model = Sequential()
            model.add(Dense(150, input_dim=cfg['input'], activation='relu'))
            model.add(Dense(120, activation='relu'))
            model.add(Dense(cfg['output'], activation='linear'))
            model.compile(loss='mse', optimizer=Adam(learning_rate=cfg['learning_rate']))
            return model