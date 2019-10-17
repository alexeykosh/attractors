#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Alexey Koshevoy

import math
import matplotlib.pyplot as plt
import numpy as np


class Attractor:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, name=''):
        plt.scatter(self.x, self.y, s=0.1, color='black', marker='x')
        plt.axis('off')
        if name:
            plt.savefig('{}'.format(name))
        plt.show()


class BedheadAttractor(Attractor):

    def __init__(self, a=np.random.uniform(-1, 1), b=np.random.uniform(-1, 1)):
        self.a = a
        self.b = b
        x, y = self.build()
        Attractor.__init__(self, x, y)

    def build(self):

        x = [1]
        y = [1]
        i = 0

        for _ in range(100000):
            x.append(math.sin(x[i] * y[i]/self.b)*y[i] +
                     math.cos(self.a*x[i] - y[i]))
            y.append(x[i] + math.sin(y[i])/self.b)
            i += 1

        return x, y


class FractalDream(Attractor):

    def __init__(self, a=np.random.uniform(-3, 3),
                 b=np.random.uniform(-3, 3),
                 c=np.random.uniform(-0.5, 1.5),
                 d=np.random.uniform(-0.5, 1.5)):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        x, y = self.build()
        Attractor.__init__(self, x, y)

    def build(self):
        x = [0.1]
        y = [0.1]
        i = 0

        for _ in range(10000):
            x.append(math.sin(y[i] * self.b) + self.c * math.sin(x[i] * self.b))
            y.append(math.sin(x[i] * self.a) + self.d * math.sin(y[i] * self.a))
            i += 1

        return x, y


class GumowskiMira(Attractor):

    def __init__(self, a=np.random.uniform(-1, 1),
                 b=np.random.uniform(-1, 1)):
        self.a = a
        self.b = b
        x, y = self.build()
        Attractor.__init__(self, x, y)

    def build(self):
        x = [np.random.uniform(-20, 20)]
        y = [np.random.uniform(-20, 20)]
        i = 0

        for _ in range(10000):
            t = x[i]
            w = self.a * x[i] + ((1 - self.a) * 2 * x[i]**2 / (1 + x[i]**2))
            x.append(self.b * x[i] + w)
            y.append(w - t)
            i += 1

        return x, y