def main():
    while True:
        try:
            dna = input()
            test = input()
        except EOFError:
            break

        if find_substr(dna, test):
            print("Resistente")
        else:
            print("Nao resistente")


def slice_str(string, start=0, end=-1, step=1):
        sliced_str = ''
        if end == -1:
                end = len(string) - 1

        while start <= end:
                sliced_str += string[start]
                start += step

        return sliced_str


def find_substr(string, sub_string):
        if len(string) < len(sub_string): # Fail Fast
                return False
       
        idx = 0
        while (idx + len(sub_string)-1) < len(string):
                if slice_str(string, idx, idx+len(sub_string)-1) == sub_string:
                        return True
                idx += 1
        
        return False


main()
    