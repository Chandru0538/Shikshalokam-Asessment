def modify_string(s):
    result = list(s)
    modified = set()
    for i, char in enumerate(s):
        ascii_val = ord(char)
        if i not in modified:
            if ascii_val % 2 == 0:
                next_index = i + 1
                if next_index < len(s):
                    new_ascii = ascii_val + (ascii_val % 7)
                    if new_ascii > 127:
                        new_ascii = 83
                    result[next_index] = chr(new_ascii)
                    modified.add(next_index)
            else:
                prev_index = i - 1
                if prev_index >= 0:
                    new_ascii = ascii_val - (ascii_val % 5)
                    if new_ascii < 0:
                        new_ascii = 83
                    result[prev_index] = chr(new_ascii)
                    modified.add(prev_index)
    return ''.join(result)
s = "sHQen}"
result = modify_string(s)
print("Final Answer:", result)