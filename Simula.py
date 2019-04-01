# Monty hall problem siumulation

import random


class MontyHall:

    def __init__(self, max_sample = 100000, mode=0):
        self.default_doors = ['goat1','goat2','Lamborgini']
        self.doors_price = ['goat1','goat2','Lamborgini']
        random.shuffle(self.doors_price)
        self.doors = [1,2,3]
        self.mode = mode # mode are in 0 or 1 state: 0 means unchange, 1 means change
        self.max_sample = max_sample
        self.win = 0
        self.lose = 0


    def start(self):
        self.reset()
        for i in range(self.max_sample + 1):
            picks = random.randint(0,2)
            while True:
                other_picks = random.randint(0,2)
                if other_picks != picks and self.doors_price[other_picks] != self.doors_price[picks]:
                    showed =  self.doors_price[other_picks]
                    break

            if self.mode:
                while (True):
                    new_picks = random.randint(0,2)
                    if self.doors_price[new_picks] != self.doors_price[picks] and self.doors_price[new_picks] != showed:
                        picks = new_picks
                        break

            # del self.doors_price[picks]

            if self.doors_price[picks] == 'Lamborgini':
                self.win += 1
            else:
                self.lose +=1
            self.reset()

    def reset(self):
        random.shuffle(self.default_doors)
        self.doors_price = self.default_doors[:]
        self.doors = [1,2,3]


if __name__ == '__main__':
    for
    unchanged = MontyHall()
    unchanged.start()
    print('winning chance when state is unchanged is : ',unchanged.win/unchanged.max_sample)
    changed = MontyHall(mode=1)
    changed.start()
    print('winning chance when state is changed is : ', changed.win / changed.max_sample)