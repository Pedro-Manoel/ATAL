def string_matching(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)

    for s in range(0, text_len - pattern_len):
        j = 0
        while j < pattern_len and pattern[j] == text[s + j]: 
            j += 1
        if j == pattern_len:
            print(f'pattern occurs with offset {s}')

# Example
text = 'HELLO WORLD'
pattern = 'O WO'
string_matching(text, pattern) # 4