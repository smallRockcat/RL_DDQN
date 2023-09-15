# Reinforcement Learning

Let's train an AI agent to play games from OpenAI Gym
照README走可以試用模組跑Lunar_Lander

rl資料夾裡放著主要部件:
agent 資料夾裡有 DQN(simple.py) 和 DOUBLE DQN(simple_double_dqn.py) 主體
Hidden Layer 在 models 資料夾裡定義
cfgs 調整 Learning rate 之類的參數

weights資料夾裡放著訓練好的模組
如要重新訓練新模組直接把裡面東西清空或改名就行

## Setup
* Install python 3.9

##可以直接用Ubuntu跑 那就不用打這行
```
python3 -m virtualenv env
source env/bin/activate
```

##下載需要的函式庫，基於相容性我有修改過，函式庫有衝突沒辦法從這裡解決的可以直接問 chat gpt

```
pip install -r requirements.txt
```

## How to run it?


1. activate env (不一定要)

    ```
    source env/bin/activate
    ```

2. execute (打這行執行就會開始訓練ㄌ)

    ```
    python3 -m rl.main --display yes --episodes 1000 --game lunar_lander --agent simple_double_dqn --config rl/cfgs/lunar_lander.json --model small2
    ```

## How to draw the model? (可畫出目前 model 的 Layer 圖)

```
python3 -m rl.plot_model --game lunar_lander --agent simple_double_dqn --config rl/cfgs/lunar_lander.json --model small2 --to_file model.png
```
## if you only want to test the model (純跑模組不訓練)

```
python3 -m rl.main --game lunar_lander --model small2 --config rl/cfgs/simple_no_train.json --agent simple_double_dqn --display yes
```
