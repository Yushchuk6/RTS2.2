from math import sin, cos, pi, pow, sqrt, fabs
from random import random
import matplotlib.pyplot as plt


def generate(n, w, N):
  wStep = w / n
  harm = [[random() * sin(wStep * i * j + random()) for i in range(N)] for j in range(n)]
  return [sum(b) for b in zip(*harm)]


def my_fft(x):
  N = len(x)
  fR1, fI1, fR2, fI2 = ([0] * N for i in range(4))
  for p in range(N):
    for k in range(int(N / 2)):
      fR1[p] += x[2 * k] * cos((2 * pi) / (N / 2) * p * k * 2)
      fR2[p] += x[2 * k + 1] * cos((2 * pi) / (N / 2) * p * (k * 2 + 1))

      fI1[p] += x[2 * k] * sin((2 * pi) / (N / 2) * p * k * 2)
      fI2[p] += x[2 * k + 1] * sin((2 * pi) / (N / 2) * p * (k * 2 + 1))
    yield sqrt(pow(fR1[p] + fR2[p], 2) + pow(fI1[p] + fI2[p], 2))


def main():
  gen = generate(8, 1100, 256)
  resMy = list(my_fft(gen))
  plt.plot(resMy)
  plt.show()


main()
