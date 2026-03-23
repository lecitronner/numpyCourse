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
    print(dailywts)
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
    print(locs[:0])
    print(locs[:1])
    print(locs[:,0])
    print(locs[:,1])
    found_gold = gold[(locs[:,0],locs[:,1])]
    print(found_gold)

def challenge_3():
    dist = np.abs(np.linspace([17,32],[28,36], num=3, axis=1) - 30)
    print(dist)
    print(dist[[0,1],[2,0]])

def broadcasting():
    arr1 = np.random.randint(low=0, high=10, size=(3,3,1))
    arr2 = np.random.randint(low=0, high=10, size=(1,2))
    arr3 = np.random.randint(low=0, high=10, size=(1,3))
    print(arr1, arr2, arr3, sep='\n---\n')
    result = arr1 + arr3
    print(result)

def newaxis():
    arr1 = np.arange(4)
    arr2 = np.arange(3)
    results = arr1[:,np.newaxis] - arr2[np.newaxis,:]
    print(results)

def reshape():
    arr1 = np.arange(8)
    print(arr1)
    bar = arr1.reshape(2,4)
    print(bar)
    bar = bar.reshape((4,2), order='F')
    print(bar)
    bar = bar.reshape((2,-1))
    print(bar)

def booleanindexing():
    arr = np.array([[3,9,7],[2,0,3],[3,3,1]])
    print(arr)

    mask = arr == 3
    arr[mask] = 0
    print(arr)

    rows_1and_3 = np.array([True, False, True])
    cols_2and_3 = np.array([False, True, True])

    print(arr[rows_1and_3])
    print(arr[cols_2and_3])
    print(arr[rows_1and_3,cols_2and_3])

    names = np.array(['Dennis', 'Dee', 'Charlie', 'Mac', 'Frank'])
    ages = np.array([43, 44, 43, 42, 74])
    genders = np.array(['M', 'F', 'M', 'M','M'])

    # Who is at least 44?
    agemask = ages >= 44
    print(agemask)
    print(f'names at least 44: {names[agemask]}')
    # Which males are over 42 ?
    mask = (genders == 'M') & (ages > 42)
    print(mask)
    print(f'males above 42 are: {names[mask]}')
    # Who are not a male or is younger than 43
    mask = ~(genders == 'M') | (ages < 43)
    print(mask)
    print(f'Not male or younger than 43 are: {names[mask]}')

def random():
    arr = np.random.randint(low=1, high=7, size=3)
    print(arr)

def challenge_4():
    generator = np.random.default_rng(1010)
    love_scores = np.round(generator.uniform(low=0, high=100, size=10), 2)
    print(love_scores)
    love_scores_bis = love_scores[:,np.newaxis]
    print(love_scores_bis)
    results = np.abs(love_scores - love_scores_bis)
    print(results)

def challenge_5():
    generator = np.random.default_rng(80085)
    scores = np.round(generator.uniform(low=30, high=100, size=15))
    print(scores)

    scores[(scores < 60).nonzero()[0][:3]] = 0
    print(scores)

def challenge_6():
    fields = np.zeros(shape=(10,10))
    print(fields)
    print('\n-----\n')
    generator = np.random.default_rng(1234)
    vals = np.round(generator.normal(size=20),2)
    print(vals)
    print('\n-----\n')
    locs = generator.choice(fields.size, len(vals), replace=False)
    print(locs)
    print('\n-----\n')
    fields.ravel()[locs] = vals
    print(fields)



#array_motivation()
#array_basics()
#creating_numpy_arrays()
#indexing_1d_arrays()
#indexing_multidimensional_arrays()
#challenge_1()
#challenge_2()
#challenge_3()
#broadcasting()
#newaxis()
#reshape()
#booleanindexing()
#random()
#challenge_4()
#challenge_5()
challenge_6()