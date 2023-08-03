import math

size = 9
section_number = 0
sec_count1 = 0
sec_count2 = 0
sec_count3 = 0
for i in range(0, 81):
    if sec_count1 == 3:
        sec_count1 = 0
        section_number += 1
    if sec_count2 == 9:
        sec_count2 = 0
        section_number -= 3
    if sec_count3 == 27:
        sec_count3 = 0
        section_number += 3
    sec_count1 += 1
    sec_count2 += 1
    sec_count3 += 1
    print("index:{}, SC:{}".format(i+1, section_number))

#     if (i ) % math.isqrt(size) != 0:
