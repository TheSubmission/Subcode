import copy
import random
import sys
from tqdm import tqdm

# S1 = [
#     0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
#     0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
#     0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
#     0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
#     0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
#     0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
#     0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
#     0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
#     0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
#     0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
#     0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
#     0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
#     0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
#     0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
#     0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
#     0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16,]
#
# S2 = [0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05,
# 	0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99,
# 	0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62,
# 	0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6,
# 	0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8,
# 	0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35,
# 	0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87,
# 	0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e,
# 	0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1,
# 	0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3,
# 	0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f,
# 	0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51,
# 	0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8,
# 	0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0,
# 	0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84,
# 	0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48,]
#
# K1 = [0x3B, 0x07, 0x68, 0x54, 0xC1, 0x5E, 0x58, 0x2D, 0x2B, 0xBB, 0xBD, 0xC8, 0xBC, 0x72, 0x65, 0x54, 0xAE, 0x0F, 0xEA, 0x2F, 0xF9]
# K2 = [0xDF, 0xE3, 0x76, 0x4A, 0x86, 0x5F, 0x63, 0xF6, 0xCA, 0xA5, 0x99, 0x0C, 0x24, 0x79, 0xB0, 0x18, 0x59, 0x36, 0x80, 0x35, 0x62]
#
# C1 = [0x8D, 0xB1, 0xDE, 0xE2, 0x77, 0x4B, 0x92, 0xAE, 0x3B, 0x07, 0x68, 0x54, 0xC1, 0xEB, 0xD1, 0x2F, 0xDA, 0x12, 0xBB, 0x4B, 0xF8]
# C2 = [0x19, 0x8C, 0xB0, 0xDF, 0xE3, 0x76, 0x4A, 0x93, 0xAF, 0x3A, 0x06, 0x69, 0x55, 0xC0, 0xFC, 0x78, 0x03, 0xF0, 0x5A, 0x41, 0x25]


# -----------------------------函数设置-------------------------------------------
def F1(input, round):
    output = S1[input ^ K1[round]]
    return output

def F2(input, round):
    output = S2[input ^ K2[round]]
    return output

def F3(input, round):
    output = S3[input ^ K3[round]]
    return output

def F4(input, round):
    output = S4[input ^ K4[round]]
    return output

def F5(input, round):
    output = S5[input ^ K5[round]]
    return output

def F6(input, round):
    output = S6[input ^ K6[round]]
    return output

def F7(input, round):
    output = S7[input ^ K7[round]]
    return output

def F8(input, round):
    output = S8[input ^ K8[round]]
    return output

def F(in0, in1, in2, in3, in4, in5, in6, in7, in8, in9, in10, in11, in12, in13, in14, in15, round):
    out0 = in1 ^ F1(in0, round)
    out4 = in3 ^ F2(in2, round)
    out12 = in5 ^ F3(in4, round)
    out8 = in7 ^ F4(in6, round)
    out6 = in9 ^ F5(in8, round)
    out2 = in11 ^ F6(in10, round)
    out10 = in13 ^ F7(in12, round)
    out14 = in15 ^ F8(in14, round)
    out5 = in0
    out1 = in2
    out7 = in4
    out3 = in6
    out13 = in8
    out9 = in10
    out15 = in12
    out11 = in14

    return out0, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15



def Function(input, round):
    roundout0 = input[0]
    roundout1 = input[1]
    roundout2 = input[2]
    roundout3 = input[3]
    roundout4 = input[4]
    roundout5 = input[5]
    roundout6 = input[6]
    roundout7 = input[7]
    roundout8 = input[8]
    roundout9 = input[9]
    roundout10 = input[10]
    roundout11 = input[11]
    roundout12 = input[12]
    roundout13 = input[13]
    roundout14 = input[14]
    roundout15 = input[15]
    for r in range(round):
        input0 = roundout0
        input1 = roundout1
        input2 = roundout2
        input3 = roundout3
        input4 = roundout4
        input5 = roundout5
        input6 = roundout6
        input7 = roundout7
        input8 = roundout8
        input9 = roundout9
        input10 = roundout10
        input11 = roundout11
        input12 = roundout12
        input13 = roundout13
        input14 = roundout14
        input15 = roundout15
        roundout0, roundout1, roundout2, roundout3, roundout4, roundout5, roundout6, roundout7, roundout8, roundout9, roundout10, roundout11, roundout12, roundout13, roundout14, roundout15 = F(input0, input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, input12, input13, input14, input15, r)
    return [roundout0, roundout1, roundout2, roundout3, roundout4, roundout5, roundout6, roundout7, roundout8, roundout9, roundout10, roundout11, roundout12, roundout13, roundout14, roundout15]

def update_component(BITNUM):
    number = 2 ** BITNUM

    # usednum = []
    # while len(usednum) < number:
    #     num = random.randint(0, number - 1)
    #     if num in usednum:
    #         continue
    #     else:
    #         usednum.append(num)
    # S1 = copy.deepcopy(usednum)
    # usednum = []
    # while len(usednum) < number:
    #     num = random.randint(0, number - 1)
    #     if num in usednum:
    #         continue
    #     else:
    #         usednum.append(num)
    # S2 = copy.deepcopy(usednum)
    # usednum = []
    # while len(usednum) < number:
    #     num = random.randint(0, number - 1)
    #     if num in usednum:
    #         continue
    #     else:
    #         usednum.append(num)
    # S3 = copy.deepcopy(usednum)
    # usednum = []
    # while len(usednum) < number:
    #     num = random.randint(0, number - 1)
    #     if num in usednum:
    #         continue
    #     else:
    #         usednum.append(num)
    # S4 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    K1 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    K2 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    K3 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    K4 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    C1 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    C2 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    C3 = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    C4 = copy.deepcopy(usednum)
    return K1, K2, K3, K4, C1, C2, C3, C4

def update_data(BITNUM):
    number = 2 ** BITNUM

    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    C = copy.deepcopy(usednum)
    usednum = []
    while len(usednum) < number:
        num = random.randint(0, number - 1)
        if num in usednum:
            continue
        else:
            usednum.append(num)
    A0 = copy.deepcopy(usednum)

    return C, A0

def find_period(XVALUEa0, XVALUEa1, BITNUM):
    number = 2 ** BITNUM
    period = 0
    PERIODLIST = []
    XValuexor = dict()
    for x in XVALUEa0.keys():
        XValuexor[x] = XVALUEa0[x] ^ XVALUEa1[x]
    for s in range(1, number):
        x0 = 0
        x1 = x0 ^ s
        out0 = XValuexor[x0]
        out1 = XValuexor[x1]
        if out0 == out1:
            success = 1
            for x0 in range(1, number):
                x1 = x0 ^ s
                out0 = XValuexor[x0]
                out1 = XValuexor[x1]
                if out0 != out1:
                    success = 0
            if success == 1:
                # print("pass s={:x}, a0={:x}, a1={:x}".format(s, a0, a1))
                period += 1
                PERIODLIST.append(s)
    return period, PERIODLIST

def find_special_period(XVALUEa0, XVALUEa1, BITNUM, periodvalue):
    number = 2 ** BITNUM
    period = 0
    PERIODLIST = []
    XValuexor = dict()
    s = periodvalue
    x0 = 0
    x1 = x0 ^ s
    out0 = XVALUEa0[x0]
    out1 = XVALUEa1[x1]
    if out0 == out1:
        success = 1
        for x0 in range(1, number):
            x1 = x0 ^ s
            out0 = XVALUEa0[x0]
            out1 = XVALUEa1[x1]
            if out0 != out1:
                success = 0
        if success == 1:
            # print("pass s={:x}, a0={:x}, a1={:x}".format(s, a0, a1))
            period += 1
            PERIODLIST.append(s)
    return period, PERIODLIST

runningfile = "runningfile.txt"
outputfile = "outfile.txt"
ROUNDS = 9
TESTTIMES = 2**8
BITNUM = 4
BRANCHNUM = 16

if __name__ == '__main__':
    ASITES = [2,3]
    XSITE = 11
    OUTSITE = 1
    periodvalue = 0x6

    # Delta = \
    #     [0x0, 0x0, 0x0, 0x0,
    #      0x0, 0x0, 0x0, 0x0,
    #      0x0, 0x0, 0x0, 0x0,
    #      0x0, 0x0, 0x0, 0x0]
    Delta = \
        [0x0, 0x0, 0xD, 0x1,
         0x0, 0x0, 0x0, 0x0,
         0x0, 0x0, 0x0, 0x0,
         0x0, 0x0, 0x0, 0x0]



    S1 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    S2 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    S3 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    S4 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    S5 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    S6 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    S7 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    S8 = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]
    K1 = []
    K2 = []
    K3 = []
    K4 = []
    K5 = []
    K6 = []
    K7 = []
    K8 = []
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    C7 = []
    C8 = []

    C = []
    A0 = []
    A1 = []


    PERIODTIMES = 0
    WRONGTIMES = 0
    list_period = [0 for _ in range(16)]

    K1, K2, K3, K4, C1, C2, C3, C4 = update_component(BITNUM)
    K5, K6, K7, K8, C5, C6, C7, C8 = update_component(BITNUM)

    for testtime in tqdm(range(TESTTIMES)):

        if testtime % 2**18 == 0:
            K1, K2, K3, K4, C1, C2, C3, C4 = update_component(BITNUM)
            K5, K6, K7, K8, C5, C6, C7, C8 = update_component(BITNUM)
            print("update component")

        C, A0= update_data(BITNUM)
        A1 = []
        for i in range(len(A0)):
            A1.append(A0[i] ^ Delta[i])

        XVALUEa0 = dict()
        XVALUEa1 = dict()
        number = 2 ** BITNUM
        for x in range(number):
            input0 = []
            input1 = []
            for i in range(BRANCHNUM):
                if i == XSITE:
                    input0.append(x)
                    input1.append(x)
                elif i in ASITES:
                    input0.append(A0[i])
                    input1.append(A1[i])
                    if A0[i] == A1[i]:
                        print(A0)
                        print(A1)
                        print(i)
                    assert A0[i] != A1[i]
                else:
                    input0.append(C[i])
                    input1.append(C[i])

            thisoutput0 = Function(input0, ROUNDS)
            thisoutput1 = Function(input1, ROUNDS)
            XVALUEa0[x] = thisoutput0[OUTSITE]
            XVALUEa1[x] = thisoutput1[OUTSITE]

        period, PERIODLIST = find_period(XVALUEa0, XVALUEa1, BITNUM)
        # period, PERIODLIST = find_special_period(XVALUEa0, XVALUEa1, BITNUM, periodvalue)
        if period == 0:
            res = "no"
        elif period == number - 1:
            res = "all"
            WRONGTIMES += 1
        else:
            res = "period = {}: {}".format(period, PERIODLIST)
            list_period[PERIODLIST[0]] += 1
            print(res)
            PERIODTIMES += 1
            print("find a period! {} {}".format(PERIODTIMES, testtime))
        with open(runningfile, "a+") as f:
            f.write("ASITE/XSITE/OUTSITE: {}/{}/{}, {}, a0/a1: {}/{}\n".format(ASITES, XSITE, OUTSITE, res, A0, A1))

    with open(outputfile, "a+") as f:
        f.write("ASITE/XSITE/OUTSITE: {}/{}/{}, PERIOD: {}/{}, possible:{}\n".format(ASITES, XSITE, OUTSITE, PERIODTIMES, TESTTIMES - WRONGTIMES, int(PERIODTIMES//(TESTTIMES - WRONGTIMES))))
    print(list_period)



