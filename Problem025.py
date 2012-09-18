# Problem25
# Fibonacci

term = 2
Fn_1 = 1
Fn_2 = 1
Fn = 0


while True:
    Fn = Fn_2 + Fn_1
    term += 1
    if len(str(Fn)) == 1000:
        print '{0}th term has over 1000 digits!'.format(term)
        break
    else:
        Fn_2 = Fn_1
        Fn_1 = Fn
