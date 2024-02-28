def smallest_substrings(string, x):
    substr = []
    for i in range(len(string)):
        for j in range(i + x - 1, len(string)):
            if string[i] == string[j]:
                if j - i + 1 >= x:
                    substr.append(string[i:j + 1])
    if not substr:
        print("not-found")
    else:
        short_length = min(len(substring) for substring in substr)
        str_list = []
        for m in substr:
            if len(m) == short_length:
                str_list.append(m)
        print(" ".join(str_list))

string= "abccdbacca"
x = 3
smallest_substrings(string, x)