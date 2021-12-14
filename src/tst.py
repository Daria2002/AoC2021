s1 = "NCNBCHB"
s2 = "NBCCNBBBCBHCB"
s3 = "NBBBCNCCNBBNBNBBCHBHHBCHB"
s4 = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
ss = [s1, s2, s3, s4]

def count_all_elements(s):
    count_elements = {}
    for el in s:
        if el not in count_elements:
            count_elements[el] = 0
        count_elements[el] += 1
    return count_elements

for s in ss:
    print(f'count of all elements = {count_all_elements(s)}')