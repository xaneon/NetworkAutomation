# coding: utf-8
get_ipython().run_cell_magic('timeit', '-r 10', 'for elem in range(0, 1000):\n  elem*elem\n  \n')
get_ipython().run_cell_magic('timeit', '-r 10', '[elem*elem for elem in range(0, 1000)]\n\n')
import numpy as np
get_ipython().run_cell_magic('timeit', '-r 10', 'np.arange(0, 1000) * np.arange(0, 1000)\n\n')
