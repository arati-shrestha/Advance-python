from multiprocessing import Pool
def cube(number):
    return number * number * number



if __name__ =="__main__":
    numbers = range(10)

    pool = Pool()

#methods in POOL:map, apply, join, close
    result = pool.map(cube, numbers)
    # print(pool.apply(cube, (numbers[4],)))
    
    pool.close()
    pool.join()

    print(result)

