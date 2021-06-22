all_results = []
count = int(input())
while count:
    all_lists = []    

    lists_count = int(input())
    while lists_count:
        all_lists.append(set(input().split()[1:]))
        lists_count -= 1

    op_count = int(input())
    while op_count:
        result_list = []
        test_case = input().split()

        if test_case[0] == '1':
            result_list = all_lists[int(test_case[1])-1].intersection(all_lists[int(test_case[2])-1])
        else:            
            result_list = all_lists[int(test_case[1])-1].union(all_lists[int(test_case[2])-1])

        all_results.append(len(result_list))
        op_count -= 1
    
    count -= 1

for result in all_results: 
    print(result)
