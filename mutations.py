def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    string = ''.join(s)
    return(string)

if __name__ == '__main__':
