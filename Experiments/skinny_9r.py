import copy
import time
from tqdm import tqdm
import random

S = [12, 6, 9, 0, 1, 10, 2, 11, 3, 8, 5, 13, 4, 14, 7, 15]

K = [
    [6, 3, 4, 8, 15, 13, 14, 5, 10, 1, 11, 12, 9, 2, 0, 7],
    [11, 15, 7, 2, 0, 13, 5, 14, 6, 8, 10, 4, 1, 9, 12, 3],
    [15, 10, 1, 0, 13, 3, 7, 11, 12, 14, 4, 8, 9, 5, 6, 2],
    [11, 8, 1, 3, 13, 14, 2, 0, 15, 4, 9, 5, 10, 6, 12, 7],
    [7, 12, 9, 6, 14, 13, 0, 15, 3, 1, 2, 11, 4, 5, 8, 10],
    [13, 10, 6, 4, 0, 1, 5, 8, 14, 3, 9, 12, 2, 15, 11, 7],
    [3, 15, 12, 7, 8, 5, 11, 6, 4, 2, 13, 1, 10, 0, 9, 14],
    [11, 7, 9, 15, 6, 12, 5, 4, 0, 2, 1, 13, 8, 10, 3, 14],
    [8, 6, 11, 3, 12, 0, 5, 10, 2, 13, 15, 9, 7, 14, 4, 1],
    [15, 14, 7, 10, 4, 12, 9, 3, 5, 13, 8, 0, 6, 11, 2, 1],
    [3, 0, 11, 14, 6, 7, 12, 2, 9, 13, 10, 5, 4, 8, 15, 1],
    [10, 15, 4, 8, 5, 9, 11, 13, 1, 0, 3, 7, 12, 14, 6, 2],
    [7, 0, 8, 5, 12, 11, 1, 14, 10, 9, 3, 6, 4, 15, 13, 2],
    [4, 8, 0, 15, 13, 7, 5, 12, 6, 3, 14, 2, 10, 1, 9, 11],
    [8, 3, 2, 1, 11, 5, 12, 4, 13, 9, 0, 7, 10, 15, 14, 6],
    [2, 8, 0, 9, 13, 10, 14, 1, 7, 5, 4, 11, 3, 15, 6, 12],
]

C = [
    [14, 4, 0, 11, 12, 8, 7, 10, 15, 6, 13, 1, 5, 3, 9, 2],
    [15, 11, 9, 5, 7, 3, 8, 6, 13, 4, 10, 12, 2, 11, 0, 1],
    [2, 8, 2, 5, 1, 12, 13, 9, 10, 6, 3, 0, 7, 14, 11, 4],
    [9, 3, 7, 10, 6, 8, 5, 12, 15, 4, 14, 11, 2, 13, 0, 1],
    [10, 6, 5, 9, 12, 15, 1, 13, 14, 8, 2, 4, 3, 11, 6, 0],
    [11, 0, 8, 3, 12, 7, 2, 1, 14, 5, 9, 4, 15, 6, 13, 10],
    [5, 3, 6, 1, 0, 10, 15, 8, 13, 4, 11, 14, 2, 12, 7, 9],
    [14, 7, 5, 1, 8, 3, 0, 10, 4, 15, 9, 11, 13, 12, 5, 6],
    [8, 11, 2, 0, 13, 4, 12, 3, 5, 9, 7, 14, 1, 10, 6, 15],
    [13, 5, 1, 11, 8, 4, 10, 13, 12, 2, 9, 7, 3, 15, 0, 6],
    [9, 3, 5, 14, 11, 10, 2, 4, 13, 7, 6, 0, 1, 3, 12, 8],
    [4, 7, 13, 2, 7, 12, 15, 1, 9, 5, 6, 11, 0, 8, 14, 10],
    [2, 1, 8, 15, 7, 10, 6, 9, 4, 3, 5, 11, 13, 0, 14, 12],
    [8, 9, 15, 3, 7, 12, 11, 9, 5, 4, 6, 2, 13, 1, 10, 14],
    [2, 0, 14, 8, 15, 9, 12, 13, 3, 5, 11, 1, 7, 10, 4, 6],
    [6, 7, 11, 8, 13, 6, 3, 12, 5, 9, 14, 0, 15, 4, 10, 1],
    [3, 15, 8, 7, 14, 9, 6, 2, 12, 1, 13, 5, 10, 0, 4, 11],
    [10, 2, 7, 0, 11, 9, 12, 4, 6, 3, 5, 13, 15, 14, 8, 1],
    [3, 6, 2, 13, 8, 5, 9, 12, 4, 1, 7, 15, 0, 10, 14, 11],
    [7, 4, 0, 8, 14, 12, 3, 10, 13, 11, 6, 2, 15, 9, 1, 5],
    [3, 2, 14, 11, 9, 10, 6, 5, 12, 1, 0, 4, 13, 15, 7, 8],
    [8, 9, 11, 12, 3, 13, 4, 0, 1, 15, 14, 2, 6, 5, 10, 7],
    [10, 2, 1, 8, 11, 7, 14, 3, 5, 9, 6, 0, 15, 13, 4, 12],
    [5, 10, 15, 0, 1, 13, 2, 12, 4, 8, 9, 6, 3, 14, 7, 11],
    [9, 8, 13, 4, 7, 11, 6, 10, 3, 12, 1, 14, 0, 5, 2, 15],
    [7, 14, 13, 11, 9, 0, 10, 4, 5, 15, 3, 1, 12, 2, 6, 8],
    [1, 3, 7, 9, 12, 11, 13, 4, 2, 8, 0, 14, 6, 5, 10, 15],
    [4, 3, 7, 10, 5, 14, 13, 8, 15, 6, 9, 11, 12, 1, 2, 0],
    [9, 3, 11, 14, 10, 8, 2, 7, 0, 1, 13, 5, 15, 12, 4, 6],
    [7, 15, 11, 5, 1, 9, 13, 10, 0, 12, 14, 2, 8, 3, 6, 4],
    [8, 9, 14, 15, 13, 6, 10, 2, 0, 3, 7, 12, 1, 5, 4, 11],
    [7, 10, 2, 9, 6, 8, 15, 13, 14, 1, 5, 0, 11, 12, 3, 4],
]

def F_first(input, round):
    S_out = [-1 for i in range(16)]
    for i in range(16):
        S_out[i] = input[i]
    AC_out = [-1 for i in range(16)]
    for i in range(16):
        if i == 0 or i == 4 or i == 8:
            AC_out[i] = S_out[i] ^ C[round][i]
        else:
            AC_out[i] = S_out[i]
    ART_out = [-1 for i in range(16)]
    for i in range(8):
        ART_out[i] = AC_out[i] ^ K[round][i]
    for i in range(8, 16):
        ART_out[i] = AC_out[i]
    SR_out = [-1 for i in range(16)]
    SR_out[0] = ART_out[0]
    SR_out[1] = ART_out[1]
    SR_out[2] = ART_out[2]
    SR_out[3] = ART_out[3]
    SR_out[4] = ART_out[7]
    SR_out[5] = ART_out[4]
    SR_out[6] = ART_out[5]
    SR_out[7] = ART_out[6]
    SR_out[8] = ART_out[10]
    SR_out[9] = ART_out[11]
    SR_out[10] = ART_out[8]
    SR_out[11] = ART_out[9]
    SR_out[12] = ART_out[13]
    SR_out[13] = ART_out[14]
    SR_out[14] = ART_out[15]
    SR_out[15] = ART_out[12]

    MC_out = [-1 for i in range(16)]
    a = 0
    b = 4
    c = 8
    d = 12
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    a = 1
    b = 5
    c = 9
    d = 13
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    a = 2
    b = 6
    c = 10
    d = 14
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    a = 3
    b = 7
    c = 11
    d = 15
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    return MC_out

def F(input, round):
    S_out = [-1 for i in range(16)]
    for i in range(16):
        S_out[i] = S[input[i]]
    AC_out = [-1 for i in range(16)]
    for i in range(16):
        if i == 0 or i == 4 or i == 8:
            AC_out[i] = S_out[i] ^ C[round][i]
        else:
            AC_out[i] = S_out[i]
    ART_out = [-1 for i in range(16)]
    for i in range(8):
        ART_out[i] = AC_out[i] ^ K[round][i]
    for i in range(8, 16):
        ART_out[i] = AC_out[i]
    SR_out = [-1 for i in range(16)]
    SR_out[0] = ART_out[0]
    SR_out[1] = ART_out[1]
    SR_out[2] = ART_out[2]
    SR_out[3] = ART_out[3]
    SR_out[4] = ART_out[7]
    SR_out[5] = ART_out[4]
    SR_out[6] = ART_out[5]
    SR_out[7] = ART_out[6]
    SR_out[8] = ART_out[10]
    SR_out[9] = ART_out[11]
    SR_out[10] = ART_out[8]
    SR_out[11] = ART_out[9]
    SR_out[12] = ART_out[13]
    SR_out[13] = ART_out[14]
    SR_out[14] = ART_out[15]
    SR_out[15] = ART_out[12]

    MC_out = [-1 for i in range(16)]
    a = 0
    b = 4
    c = 8
    d = 12
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    a = 1
    b = 5
    c = 9
    d = 13
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    a = 2
    b = 6
    c = 10
    d = 14
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    a = 3
    b = 7
    c = 11
    d = 15
    MC_out[a] = SR_out[a] ^ SR_out[c] ^ SR_out[d]
    MC_out[b] = SR_out[a]
    MC_out[c] = SR_out[b] ^ SR_out[c]
    MC_out[d] = SR_out[a] ^ SR_out[c]
    return MC_out

def F_noMC(input, round):
    S_out = [-1 for i in range(16)]
    for i in range(16):
        S_out[i] = S[input[i]]
    AC_out = [-1 for i in range(16)]
    for i in range(16):
        if i == 0 or i == 4 or i == 8:
            AC_out[i] = S_out[i] ^ C[round][i]
        else:
            AC_out[i] = S_out[i]
    ART_out = [-1 for i in range(16)]
    for i in range(8):
        ART_out[i] = AC_out[i] ^ K[round][i]
    for i in range(8, 16):
        ART_out[i] = AC_out[i]
    SR_out = [-1 for i in range(16)]
    SR_out[0] = ART_out[0]
    SR_out[1] = ART_out[1]
    SR_out[2] = ART_out[2]
    SR_out[3] = ART_out[3]
    SR_out[4] = ART_out[7]
    SR_out[5] = ART_out[4]
    SR_out[6] = ART_out[5]
    SR_out[7] = ART_out[6]
    SR_out[8] = ART_out[10]
    SR_out[9] = ART_out[11]
    SR_out[10] = ART_out[8]
    SR_out[11] = ART_out[9]
    SR_out[12] = ART_out[13]
    SR_out[13] = ART_out[14]
    SR_out[14] = ART_out[15]
    SR_out[15] = ART_out[12]

    return SR_out

if __name__ == '__main__':
    with open("result.txt", "w") as f:
        pass

    end = 11
    ROUND = 9
    TIMES = 2**18
    invalid = 0

    # usednum = []
    # while len(usednum) < 16:
    #     num = random.randint(0, 15)
    #     if num in usednum:
    #         continue
    #     else:
    #         usednum.append(num)
    # S = copy.deepcopy(usednum)
    C = [[0x0 for i in range(16)] for j in range(16)]
    for i in range(16):
        usednum = []
        while len(usednum) < 16:
            num = random.randint(0, 15)
            if num in usednum:
                continue
            C[i][len(usednum)] = num
            usednum.append(num)
    K = [[0x0 for i in range(16)] for j in range(16)]
    for i in range(16):
        usednum = []
        while len(usednum) < 16:
            num = random.randint(0, 15)
            if num in usednum:
                continue
            K[i][len(usednum)] = num
            usednum.append(num)

    for thistime in tqdm(range(TIMES)):


        a00 = random.randint(0, 15)
        a10 = random.randint(0, 15)
        a20 = random.randint(0, 15)
        a30 = random.randint(0, 15)
        a40 = random.randint(0, 15)
        a50 = random.randint(0, 15)
        a60 = random.randint(0, 15)
        a70 = random.randint(0, 15)
        a80 = random.randint(0, 15)
        a90 = random.randint(0, 15)
        a100 = random.randint(0, 15)
        a110 = random.randint(0, 15)
        a120 = random.randint(0, 15)
        a130 = random.randint(0, 15)
        a140 = random.randint(0, 15)
        a150 = random.randint(0, 15)
        a01 = random.randint(0, 15)
        a11 = random.randint(0, 15)
        a21 = random.randint(0, 15)
        a31 = random.randint(0, 15)
        a41 = random.randint(0, 15)
        a51 = random.randint(0, 15)
        a61 = random.randint(0, 15)
        a71 = random.randint(0, 15)
        a81 = random.randint(0, 15)
        a91 = random.randint(0, 15)
        a101 = random.randint(0, 15)
        a111 = random.randint(0, 15)
        a121 = random.randint(0, 15)
        a131 = random.randint(0, 15)
        a141 = random.randint(0, 15)
        a151 = random.randint(0, 15)
        c0 = random.randint(0, 15)
        c1 = random.randint(0, 15)
        c2 = random.randint(0, 15)
        c3 = random.randint(0, 15)
        c4 = random.randint(0, 15)
        c5 = random.randint(0, 15)
        c6 = random.randint(0, 15)
        c7 = random.randint(0, 15)
        c8 = random.randint(0, 15)
        c9 = random.randint(0, 15)
        c10 = random.randint(0, 15)
        c11 = random.randint(0, 15)
        c12 = random.randint(0, 15)
        c13 = random.randint(0, 15)
        c14 = random.randint(0, 15)
        c15 = random.randint(0, 15)

        start = time.time()
        counter = 0

        if a00 == a01 or a10 == a11 or a140 == a141 or a150 == a151:
            invalid += 1
            continue

        XVALUEa0 = dict()
        XVALUEa1 = dict()
        for x in range(16):
            inp = [a00, a10, c2, c3,
                     a10, c5, c6, c7,
                     c8, c9, a00, a10,
                     c12, c13, x^a140, a150]
            for r in range(0, 1):
                out = F_first(inp, r)
            inp = out
            for r in range(1, ROUND-1):
                out = F(inp, r)
                inp = out
            out = F_noMC(inp, ROUND-1)
            # for outnum in range(16):
            #     print("{:2}, ".format(out[outnum]), end="")
            # print("")
            XVALUEa0[x] = out[end]

            inp = [a01, a11, c2, c3,
                   a11, c5, c6, c7,
                   c8, c9, a01, a11,
                   c12, c13, x^a141, a151]
            for r in range(0, 1):
                out = F_first(inp, r)
            inp = out
            for r in range(1, ROUND-1):
                out = F(inp, r)
                inp = out
            out = F_noMC(inp, ROUND - 1)
            # for outnum in range(16):
            #     print("{:2}, ".format(out[outnum]), end="")
            # print("")
            XVALUEa1[x] = out[end]

        period = 1
        s = a140 ^ a141

        for x in range(16):
            if XVALUEa0[x ^ s] != XVALUEa1[x]:
                period = -1
        if period == 1:
            print('pass, s={}. a00={}, a01={}, a10={}, a11={}. a140={}. a141={}, a150={}, a151={}'.format(str(s), str(a00), str(a01), str(a10), str(a11), str(a140), str(a141), str(a150), str(a151)))
            print(XVALUEa0)
            print(XVALUEa1)
        if len(set(XVALUEa0.values())) == 1 and len(set(XVALUEa1.values())) == 1:
            print('a0', XVALUEa0)
            print('a1', XVALUEa1)
        # print("count: {}/{}".format(counter, 256))
        with open("result.txt", "a+") as f:
            f.write("{}\n".format(counter))
        # print(time.time()-start)
    print("invalid:{}".format(invalid))
    print("final test number:{}".format(TIMES - invalid))



