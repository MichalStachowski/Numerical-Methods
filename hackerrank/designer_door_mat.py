# https://www.hackerrank.com/challenges/designer-door-mat/problem

pattern = ".|."
r, c = map(int, input().split())
c_middle = c // 2
r_middle = r // 2
pattern_center_index = [c_middle]  # list of index where to put "|" char
s = "-" * c  # original string. Modifications will be made based on this

# Print top part
for i in range(r_middle):
    temp_s = s
    for j in range(c):
        if j in pattern_center_index:
            temp_s = temp_s[:j - 1] + pattern + temp_s[j + 2:]  # ------- => --.|.--
    print(temp_s)
    first = pattern_center_index[0]
    last = pattern_center_index[-1]
    pattern_center_index.append(first-3)
    pattern_center_index.append(last+3)
    pattern_center_index.sort()

# Print the middle
welcome_string = s[:c_middle - 3] + "WELCOME" + s[c_middle + 4:]
print(welcome_string)

# Print the bottom
for i in range(r_middle):
    temp_s = s
    del pattern_center_index[0]
    del pattern_center_index[-1]

    for j in range(c):
        if j in pattern_center_index:
            temp_s = temp_s[:j - 1] + pattern + temp_s[j + 2:]  # --.|..|..|.-- => -----.|.-----
    print(temp_s)
