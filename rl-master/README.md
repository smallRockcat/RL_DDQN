# Reinforcement Learning

Let's train an AI agent to play games from OpenAI Gym


## Setup
* Install python 3.9
```
python3 -m virtualenv env
source env/bin/activate ##可以直接用Ubuntu跑 那就不用打這行
pip install -r requirements.txt
```

## How to run it?


1. activate env

    ```
    source env/bin/activate
    ```

2. execute

    ```
    python3 -m rl.main --display yes --episodes 1000 --game lunar_lander --agent simple_double_dqn --config rl/cfgs/lunar_lander.json --model small2
    ```

## How to draw the model?

```
python3 -m rl.plot_model --game lunar_lander --agent simple_double_dqn --config rl/cfgs/lunar_lander.json --model small2 --to_file model.png
```
## if you only want to test the model (run without train)

```
python3 -m rl.main --game lunar_lander --model small2 --config rl/cfgs/simple_no_train.json --agent simple_double_dqn --display yes
```
