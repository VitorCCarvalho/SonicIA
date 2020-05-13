import retro
from random import randint
import numpy as np

env = retro.make('SonicTheHedgehog-Genesis', state='GreenHillZone.Act1') 

env.reset() 

while True:
    act = np.random.randint(2,size=12)
    arr = act[0:12]
    obs, rew, info, done = env.step(act)
    

    env.render()