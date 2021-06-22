for _ in range(int(input())):
    wrong_line = input()
    mid_idx = len(wrong_line)//2
    print(wrong_line[mid_idx-1::-1] + wrong_line[:mid_idx-1:-1])