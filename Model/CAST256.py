import operation_6bit_l
import os
import sys

filename = operation_6bit_l.filename

if __name__ == '__main__':
    with open(filename, 'w') as f:
        f.write('')

    #num_R = 8
    num_branch = 4

    num_R_enc = 3
    num_R_dec = 15
    num_R_color = num_R_enc + num_R_dec
    num_R_linear = 0

    num_R_sum = num_R_color
    num_pr = num_branch - 3
    num_xor = 1
    num_roundfunc = 1



    res = ''


    operation_6bit_l.generate_round_state(0, num_branch)
    for r in range(num_R_color):
        if r < num_R_enc:
            operation_6bit_l.generate_round_state(r+1, num_branch)

            #S0
            operation_6bit_l.ROUNDFUNC(r, 0)
            operation_6bit_l.COPY(r, 0)
            res += 'ASSERT(x_0_%s = COPY_IN_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT1_0_%s = ROUNDFUNC_IN_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT2_0_%s = y_0_%s);\n' % (str(r), str(r))

            #S1
            operation_6bit_l.XOR(r, 0)
            res += 'ASSERT(x_1_%s = XOR_IN1_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(ROUNDFUNC_OUT_0_%s = XOR_IN2_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(y_1_%s = XOR_OUT_0_%s);\n' % (str(r), str(r))

            #S2,3
            res += 'ASSERT(x_2_%s = y_2_%s);\n' % (str(r), str(r))
            res += 'ASSERT(x_3_%s = y_3_%s);\n' % (str(r), str(r))

            #nextround:
            for i in range(num_branch):
                res += 'ASSERT(x_%s_%s = y_%s_%s);\n' % (str(i), str(r+1), str((i+1) % num_branch), str(r))
        else:
            operation_6bit_l.generate_round_state(r+1, num_branch)

            #S3
            operation_6bit_l.ROUNDFUNC(r, 0)
            operation_6bit_l.COPY(r, 0)
            res += 'ASSERT(x_3_%s = COPY_IN_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT1_0_%s = ROUNDFUNC_IN_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT2_0_%s = y_0_%s);\n' % (str(r), str(r))

            #S0
            operation_6bit_l.XOR(r, 0)
            res += 'ASSERT(x_0_%s = XOR_IN1_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(ROUNDFUNC_OUT_0_%s = XOR_IN2_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(y_1_%s = XOR_OUT_0_%s);\n' % (str(r), str(r))

            #S1,2
            res += 'ASSERT(x_1_%s = y_2_%s);\n' % (str(r), str(r))
            res += 'ASSERT(x_2_%s = y_3_%s);\n' % (str(r), str(r))

            #nextround:
            for i in range(num_branch):
                res += 'ASSERT(x_%s_%s = y_%s_%s);\n' % (str(i), str(r+1), str(i), str(r))


    if num_R_dec != 0:
        operation_6bit_l.generate_round_state_linear(num_R_color, num_branch)
        for r in range(num_R_color, num_R_linear+num_R_color):
            operation_6bit_l.generate_round_state_linear(r+1, num_branch)
            if r == num_R_color:
                operation_6bit_l.initial(r, num_branch)

            #S3
            operation_6bit_l.ROUNDFUNC_linear(r, 0)
            operation_6bit_l.COPY_linear(r, 0)
            res += 'ASSERT(ylinear_0_%s = COPY_IN_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT1_0_%s = xlinear_3_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT2_0_%s = ROUNDFUNC_IN_0_%s);\n' % (str(r), str(r))

            # S0
            operation_6bit_l.XOR_linear(r, 0)
            res += 'ASSERT(ylinear_1_%s = XOR_IN1_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(ROUNDFUNC_OUT_0_%s = XOR_IN2_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(xlinear_0_%s = XOR_OUT_0_%s);\n' % (str(r), str(r))

            # S1,2
            res += 'ASSERT(ylinear_2_%s = xlinear_1_%s);\n' % (str(r), str(r))
            res += 'ASSERT(ylinear_3_%s = xlinear_2_%s);\n' % (str(r), str(r))

            # nextround:
            for i in range(num_branch):
                res += 'ASSERT(xlinear_%s_%s = ylinear_%s_%s);\n' % (str(i), str(r + 1), str(i), str(r))

    else:
        operation_6bit_l.generate_round_state_linear(num_R_color, num_branch)
        for r in range(num_R_color, num_R_linear+num_R_color):
            operation_6bit_l.generate_round_state_linear(r+1, num_branch)
            if r == num_R_color:
                operation_6bit_l.initial(r, num_branch)

            #S0
            operation_6bit_l.ROUNDFUNC_linear(r, 0)
            operation_6bit_l.COPY_linear(r, 0)
            res += 'ASSERT(ylinear_0_%s = COPY_IN_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT1_0_%s = xlinear_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(COPY_OUT2_0_%s = ROUNDFUNC_IN_0_%s);\n' % (str(r), str(r))

            # S1
            operation_6bit_l.XOR_linear(r, 0)
            res += 'ASSERT(ylinear_1_%s = XOR_IN1_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(ROUNDFUNC_OUT_0_%s = XOR_IN2_0_%s);\n' % (str(r), str(r))
            res += 'ASSERT(xlinear_1_%s = XOR_OUT_0_%s);\n' % (str(r), str(r))

            # S2,3
            res += 'ASSERT(ylinear_2_%s = xlinear_2_%s);\n' % (str(r), str(r))
            res += 'ASSERT(ylinear_3_%s = xlinear_3_%s);\n' % (str(r), str(r))

            # nextround:
            for i in range(num_branch):
                res += 'ASSERT(xlinear_%s_%s = ylinear_%s_%s);\n' % (str(i), str(r + 1), str((i+1) % num_branch), str(r))


    with open(filename, 'a') as f:
        f.write(res)



    operation_6bit_l.KEY_SUM(num_R_sum, num_xor, num_pr)
    operation_6bit_l.period_SUM(num_R_sum, num_roundfunc)

    if num_R_linear == 0:
        operation_6bit_l.END(num_R_color-1, num_branch)

    with open(filename, 'a') as f:
        f.write('QUERY(FALSE);\nCOUNTEREXAMPLE;\n')



