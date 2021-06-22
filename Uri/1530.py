def count_subs(string):
    total_subs = ((1 + len(string))*len(string)/2)
        
    for char in list(set(string)):
        total_subs = total_subs - (string.count(char) - 1)

    return int(total_subs)

def std_count(string):
    return ((1 + len(string))*len(string)/2)


print(count_subs('abc'))


range()




