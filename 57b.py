#1 + 1/2 = 3/2 = 1.5
#1 + 1/(2 + 1/2) = 7/5 = 1.4
#1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

#1 + 1/(2)

#1 + 1/(2  + 1/(2))

#1 + 1/(2  + 1/(2 + 1/(2))))

#1 + 1/  [(2 + 1/] (2)[)]

def cont_frac(iter):
    frac = "1.0 + 1.0 / "
    frac += (iter - 1) * "(2.0 + 1.0/"
    frac += "2.0"
    frac += (iter - 1) * ")"
    #print frac
    return eval(frac)

print cont_frac(50)