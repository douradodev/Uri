import time

start = time.time()

all_results = []
count = int(input())
while count:
    all_lists = []    

    lists_count = int(input())
    while lists_count:
        all_lists.append(input().split()[1:])
        lists_count -= 1

    op_count = int(input())
    while op_count:        
        test_case = input().split()

        if test_case[0] == '1':
            all_results.append(len(set(all_lists[int(test_case[1])-1]).intersection(all_lists[int(test_case[2])-1])))
        else:            
            all_results.append(len(set(all_lists[int(test_case[1])-1]).union(all_lists[int(test_case[2])-1])))
        
        op_count -= 1
    
    count -= 1

for result in all_results: 
    print(result)

print('Time:', time.time()-start)