import time

start = time.time()
for _ in range(int(input())):
    all_lists = []

    for _ in range(int(input())):
        all_lists.append(input().split()[1:])

    for _ in range(int(input())):
        result_list = []
        test_case = input().split()

        if test_case[0] == '1':
            result_list = set(all_lists[int(test_case[1])-1]).intersection(set(all_lists[int(test_case[2])-1]))
        else:            
            result_list = set(all_lists[int(test_case[1])-1]).union(set(all_lists[int(test_case[2])-1]))

        print(len(result_list))

print('Time:', time.time()-start)