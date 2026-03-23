import numpy as np
import time

def array_motivation():
    prices = []
    N = 60*60*24*365
    for i in range(N):
        prices.append(100 + i/100)
    print(prices[:5])
    avg = 0.0
    for p in prices:
        avg += p/len(prices)
    print(avg)

    # With numpy
    prices = 100 + np.arange(N)/100
    print(prices[:5])
    avg = np.mean(prices)
    print(avg)

def array_basics():
    arr = np.array([10,20,30,40,50])
    print(f'arr: {arr} | shape: {arr.shape} | ndim: {arr.ndim} | len: {len(arr)} | dtype: {arr.dtype}')
    arr_2d = np.array([[10,20,60],[30,40,50]])
    print(f'arr: {arr_2d} | shape: {arr_2d.shape} | ndim: {arr_2d.ndim} | len: {len(arr_2d)} | dtype: {arr_2d.dtype}')

def creating_numpy_arrays():
    arr_zeros = np.zeros((3,2), dtype=int)
    print(arr_zeros)
    arr_ones = np.ones((3,2), dtype=int)
    print(arr_ones)
    arr_full = np.full((3,2), 'cats')
    print(arr_full)
    arr_arange = np.arange(start=1, stop=5, step=1)
    print(arr_arange)
    arr_random = np .random.randint(low=1, high=5, size=(3,2))
    print(arr_random)

def indexing_1d_arrays():
    foo = np.array([10,20,30,40,50])
    print(foo[0], foo[-1])
    foo[0] = 99
    foo[-1] = 11
    print(foo)
    print(foo[[0,3,1]])
    #slicing
    print(foo[::2])

def indexing_multidimensional_arrays():
    bar = np.array([[5,10,15,20],
                   [25,30,35,40],
                    [45,50,55,60]])
    print(bar[1,2])
    print(bar[0])
    print(bar[0, None])
    print(bar[:2])
    bar[(0,1,2),(0,1,2)] = np.zeros((1,3))
    print(bar)

def challenge_1():
    dailywts = 185 - np.arange(5*7)/5
    results = (dailywts[5::7]+dailywts[6::7])/2
    print(results)

def challenge_2():
    np.random.seed(5555)
    gold = np.random.randint(low=0, high=10, size=(7,7))
    print(gold)
    locs = np.array([
        [0,4],
        [2,2],
        [2,3],
        [5,1],
        [6,3]
    ])
    print(locs)
    print(locs[:,0])
    print(locs[:,1])
    found_gold = gold[(locs[:,0],locs[:,1])]
    print(found_gold)

def challenge_3():
    

#array_motivation()
#array_basics()
#creating_numpy_arrays()
#indexing_1d_arrays()
#indexing_multidimensional_arrays()
#challenge_1()
#challenge_2()
challenge_3()