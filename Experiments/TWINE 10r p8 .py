import copy
import random
import sys

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


ROUNDS = 10
TESTTIMES = 2**16
BITNUM = 4
BRANCHNUM = 16

if __name__ == '__main__':

    ASITES = [6,7,11,14,15]
    XSITE = 9
    OUTSITE = 1

    # Delta = \
    #     [0x0, 0x0, 0x0, 0x0,
    #      0x0, 0x0, 0x0, 0x0,
    #      0x0, 0x0, 0x0, 0x0,
    #      0x0, 0x0, 0x0, 0x0]
    Delta = \
        [0x0, 0x0, 0x0, 0x0,
         0x0, 0x0, 0x9, 0x8,
         0x0, 0x0, 0x0, 0x7,
         0x0, 0x0, 0x9, 0x8]



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

    for testtime in range(TESTTIMES):

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

    print(list_period)



