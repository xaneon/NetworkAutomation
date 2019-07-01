import numpy as np

n = 1000  # Problemgroesse
a = np.random.randn(n)  # a sei ein Array[n] mit Zufallszahlen

j = 0  # setze j = 0,                               1 +
while j < n:  # solange j kleiner n, mache          n * (
    i = 0  # setze i = 0                            1 +
    while i < n-1:   # solange i kleiner n-1,       (n-1) * (
        if a[i] < a[i+1]:  # wenn a[i]...
            # tausche a[i] mit a[i+1]
            temp = a[i]  #                          1 +
            a[i] = a[i+1]  #                        1 +
            a[i+1] = temp  #                        1 +
        i = i + 1  # erhoehe i um 1                 1 ) +
    j = j + 1  # erhoehe j um 1                     1 )
# 1 + n * (1 + (n-1) * (1 + 1 + 1 + 1) + 1 )
# = 1 + n * (4n - 2) = 1 + 4n**2-2n = 4n**2 - 2n+1
# => O(4n**2) bzw. O(n**2)
