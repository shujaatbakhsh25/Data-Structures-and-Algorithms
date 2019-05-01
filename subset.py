def power_set(items):
    N = len(items)
    # enumerate the 2 ** N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            
            if (i >> j) % 2 == 1:
                combo.append(items[j])
            print(i)
            print(combo)
        yield combo
print(list(power_set([1,2,3])))
print(5>>1)