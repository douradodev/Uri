all_results = []
for _ in range(input()):
    all_lists = []

    for _ in range(input()):
        all_lists.append(raw_input().split()[1:])

    for _ in range(input()):
        result_list = []
        test_case = raw_input().split()

        if test_case[0] == '1':
            result_list = set(all_lists[int(test_case[1])-1]).intersection(set(all_lists[int(test_case[2])-1]))
        else:            
            result_list = set(all_lists[int(test_case[1])-1]).union(set(all_lists[int(test_case[2])-1]))

        all_results.append(len(result_list))
            
    

for result in all_results: 
    print(result)
