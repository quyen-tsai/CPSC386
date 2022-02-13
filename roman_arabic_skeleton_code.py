di_roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
            'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
di_arabic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L',
             40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
arabic_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

# # OPTIONAL :  TODO:  you do NOT have to deal with illegal combinations -- but you may do so
# illegal_combinations = ['IIV', 'IIX', 'IIL', 'IIC', 'IID', 'IIM',     # illegal combinations
#                         'XXL', 'XXC', 'XXD', 'XXM',
#                         'CCD', 'CCM', 'VVV', 'LLL', 'DDD',
#                         'IIV', 'IIX', 'XXL', 'XXC', 'CCD', 'CCM']
#
#
def to_arabic(s):
    z = 0
    for i in range(0, len(s) - 1):
        if di_roman[s[i]] < di_roman[s[i + 1]]:
            z -= di_roman[s[i]]
        else:
            z += di_roman[s[i]]
    return z + di_roman[s[-1]]


def to_roman(arabic) -> str:
    res = ""

    for i in di_arabic:
        res += (arabic // i) * di_arabic[i]
        arabic %= i

    return res


def print_spaced(li_tuples, field_width=0):
    i = 0
    for el, v in li_tuples:
        print(f'{el :{field_width}} is {v}')
        i += 1
        if i % 5 == 0:
            print()


def run_to_roman_to_arabic_tests(begin=1, end=100, step=1):
    romans = []
    arabics = []
    for el in range(begin, end, step):
        romans.append((el, to_roman(el)))
    print_spaced(romans)

    for k, v in romans:
        arabics.append((v, to_arabic(v)))
    print_spaced(arabics, field_width=10)


def main():
    run_to_roman_to_arabic_tests(begin=10, end=301, step=10)


if __name__ == '__main__':
    main()

#OUTPUT:
# /usr/local/bin/python3.7 /Users/williammccarthy/PycharmProjects/roman/main.py
# 10 is X
# 20 is XX
# 30 is XXX
# 40 is XL
# 50 is L
#
# 60 is LX
# 70 is LXX
# 80 is LXXX
# 90 is XC
# 100 is C
#
# 110 is CX
# 120 is CXX
# 130 is CXXX
# 140 is CXL
# 150 is CL
#
# 160 is CLX
# 170 is CLXX
# 180 is CLXXX
# 190 is CXC
# 200 is CC
#
# 210 is CCX
# 220 is CCXX
# 230 is CCXXX
# 240 is CCXL
# 250 is CCL
#
# 260 is CCLX
# 270 is CCLXX
# 280 is CCLXXX
# 290 is CCXC
# 300 is CCC
#
# 310 is CCCX
# 320 is CCCXX
# 330 is CCCXXX
# 340 is CCCXL
# 350 is CCCL
#
# 360 is CCCLX
# 370 is CCCLXX
# 380 is CCCLXXX
# 390 is CCCXC
# 400 is CD
#
# 410 is CDX
# 420 is CDXX
# 430 is CDXXX
# 440 is CDXL
# 450 is CDL
#
# 460 is CDLX
# 470 is CDLXX
# 480 is CDLXXX
# 490 is CDXC
# 500 is D
#
# 510 is DX
# 520 is DXX
# 530 is DXXX
# 540 is DXL
# 550 is DL
#
# 560 is DLX
# 570 is DLXX
# 580 is DLXXX
# 590 is DXC
# X          is 10
# XX         is 20
# XXX        is 30
# XL         is 40
# L          is 50
#
# LX         is 60
# LXX        is 70
# LXXX       is 80
# XC         is 90
# C          is 100
#
# CX         is 110
# CXX        is 120
# CXXX       is 130
# CXL        is 140
# CL         is 150
#
# CLX        is 160
# CLXX       is 170
# CLXXX      is 180
# CXC        is 190
# CC         is 200
#
# CCX        is 210
# CCXX       is 220
# CCXXX      is 230
# CCXL       is 240
# CCL        is 250
#
# CCLX       is 260
# CCLXX      is 270
# CCLXXX     is 280
# CCXC       is 290
# CCC        is 300
#
# CCCX       is 310
# CCCXX      is 320
# CCCXXX     is 330
# CCCXL      is 340
# CCCL       is 350
#
# CCCLX      is 360
# CCCLXX     is 370
# CCCLXXX    is 380
# CCCXC      is 390
# CD         is 400
#
# CDX        is 410
# CDXX       is 420
# CDXXX      is 430
# CDXL       is 440
# CDL        is 450
#
# CDLX       is 460
# CDLXX      is 470
# CDLXXX     is 480
# CDXC       is 490
# D          is 500
#
# DX         is 510
# DXX        is 520
# DXXX       is 530
# DXL        is 540
# DL         is 550
#
# DLX        is 560
# DLXX       is 570
# DLXXX      is 580
# DXC        is 590
#
# Process finished with exit code 0


# TODO: my output:
# 10 is X
# 20 is XX
# 30 is XXX
# 40 is XL
# 50 is L
#
# 60 is LX
# 70 is LXX
# 80 is LXXX
# 90 is XC
# 100 is C
#
# 110 is CX
# 120 is CXX
# 130 is CXXX
# 140 is CXL
# 150 is CL
#
# 160 is CLX
# 170 is CLXX
# 180 is CLXXX
# 190 is CXC
# 200 is CC
#
# 210 is CCX
# 220 is CCXX
# 230 is CCXXX
# 240 is CCXL
# 250 is CCL
#
# 260 is CCLX
# 270 is CCLXX
# 280 is CCLXXX
# 290 is CCXC
# 300 is CCC
#
# X          is 10
# XX         is 20
# XXX        is 30
# XL         is 40
# L          is 50
#
# LX         is 60
# LXX        is 70
# LXXX       is 80
# XC         is 90
# C          is 100
#
# CX         is 110
# CXX        is 120
# CXXX       is 130
# CXL        is 140
# CL         is 150
#
# CLX        is 160
# CLXX       is 170
# CLXXX      is 180
# CXC        is 190
# CC         is 200
#
# CCX        is 210
# CCXX       is 220
# CCXXX      is 230
# CCXL       is 240
# CCL        is 250
#
# CCLX       is 260
# CCLXX      is 270
# CCLXXX     is 280
# CCXC       is 290
# CCC        is 300

