# Monty hall problem siumulation

import random
from matplotlib import pyplot as plt


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
                    showed =  other_picks
                    break

            if self.mode:
                # print(picks, showed)
                picks = 3 - picks - showed
                # print('new picks:', picks)

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
    mode_0 = []
    mode_1 = []
    for i in range(20):
        unchanged = MontyHall()
        unchanged.start()
        print('winning chance when state is unchanged is : ',unchanged.win/unchanged.max_sample)
        mode_0.append(unchanged.win/unchanged.max_sample)

        changed = MontyHall(mode=1)
        changed.start()
        print('winning chance when state is changed is : ', changed.win / changed.max_sample)
        mode_1.append(changed.win / changed.max_sample)

    plt.suptitle('Monty Hall Problem Simulation ')
    plt.title('Monty Hall Problem Simulation')
    plt.subplot(121)
    plt.title('probablity distribution of getting price when state unchanged')
    plt.plot(range(20),mode_0)

    plt.subplot(122)
    plt.title('probablity distribution of getting price when state changed')
    plt.plot(range(20),mode_1)
    plt.show()
