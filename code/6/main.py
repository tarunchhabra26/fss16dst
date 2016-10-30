from sa import sa
from maxwalksat import mws
from model import Osyczka2
from model import Kursawe
from model import Schaffer

for model in [Schaffer, Osyczka2, Kursawe]:
    for optimizer in [sa, mws]:
           optimizer(model())