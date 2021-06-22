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


def main():   
    while True:
        try:
            string_min, string_max = input(), input()

            if len(string_min) > len(string_max):
                string_min, string_max = string_max, string_min

            sub_string_size = 0
            while len(string_min):
                sub_string_test = ''
                start_idx = 0

                idx = 0
                while idx < len(string_min):
                    sub_string_test += string_min[idx]

                    if find_substr(string_max, sub_string_test):
                        if sub_string_test in string_max:
                            if len(sub_string_test) > sub_string_size:
                                sub_string_size = len(sub_string_test)

                    idx += 1

                start_idx += 1
                string_min = slice_str(string_min, 1)

            
            print(sub_string_size)
        
        except EOFError:
            break


main()