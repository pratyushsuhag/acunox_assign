import os
from collections import defaultdict
def func(filename):
    arr1 = []
    arr2 = []
    with open('logs.csv') as f:
        for i in f.readlines()[1:]:
            a, b = i.strip('\n').split(',')
            arr1.append(a)
            arr2.append(b)

    f = set()
    for i in range(len(arr1)):
        if (arr1[i], arr2[i]) in f:
            raise Exception("Duplicate entry found")
        else:
            f.add((arr1[i], arr2[i]))
    dic = defaultdict(int)
    for i in range(len(arr1)):
        dic[arr2[i]] += 1
    sorted_dic = sorted(dic.items(), key=lambda x: [x[1], x[0]], reverse=True)
    
    return [i for i,j in sorted_dic[:3]]



if __name__ == '__main__':
    print(f'The Top 3 consumed menu items are: {func("logs.csv")}')
    