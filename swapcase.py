def swap_case(s):
    swapped =""
    for ch in s:
        if ch.isupper():
            swapped += ch.lower()
        else:
            swapped += ch.upper()
    return swapped

if __name__ == '__main__':
