def find_common(word1, word2):

    s = min(len(word1),len(word2))
    if s == len(word1):
        short = word1
        long = word2
    else:
        short = word2
        long = word1

    st = ""
    max_len = 0
    for i in range(s):
        for j in range(i+1,s+1):
            st = short[i:j]
            if (st in long) and len(st) > max_len:
                result = st
                max_len = len(st)

    return result

print(find_common(input(),input()))

