from math import sin, cos, pi, pow, sqrt, fabs
from random import random
import matplotlib.pyplot as plt
from numpy import fft
from timeit import default_timer as timer


def generate(n, w, N):
  wStep = w / n
  harm = [[random() * sin(wStep * i * j + random()) for i in range(N)] for j in range(n)]
  return [sum(b) for b in zip(*harm)]


def my_fft(x):
  N = len(x)
  fR1, fI1, fR2, fI2 = ([0] * N for i in range(4))
  for p in range(N):
    for k in range(int(N / 2)):
      fR1[p] += x[2 * k] * cos((2 * pi) / N * p * k * 2)
      fR2[p] += x[2 * k + 1] * cos((2 * pi) / N * p * (k * 2 + 1))

      fI1[p] += x[2 * k] * sin((2 * pi) / N * p * k * 2)
      fI2[p] += x[2 * k + 1] * sin((2 * pi) / N * p * (k * 2 + 1))
    yield sqrt(pow(fR1[p] + fR2[p], 2) + pow(fI1[p] + fI2[p], 2))


def main():
  gen = generate(8, 1100, 256)
  t1 = timer()
  resMy = list(my_fft(gen))
  t2 = timer()
  resNum = list(fft.fft(gen))
  t3 = timer()
  plt.plot(resMy)
  plt.show()
  print(F"Time my fft {t2 - t1}\nTime numpy fft {t3 - t2}")


main()
