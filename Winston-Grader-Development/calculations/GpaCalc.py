# letter grade from each quarter into variables (capital)
Q1 = "A"  # -4inputs from frontEnd
Q2 = "E"
Q3 = "D"
Q4 = "B"

# letter grade recieved on yout final exam
Fg = "C"  # -input from frontend

# command calculate final letter grade for class


def GCalculate(Q1, Q2, Q3, Q4, Fg):
    # add variables together so that we can search for amounts of each letter grade
    Added = Q1 + Q2 + Q3 + Q4
    pointVal = 0
    print(Added)

    aq = Added.count('A')*12
    bq = Added.count('B')*9
    cq = Added.count('C')*6
    dq = Added.count('D')*3
    eq = Added.count('E')*0
    pointVal = pointVal + aq + bq + cq + dq + eq
    # print(pointVal) #uncomment for progress test

    af = Fg.count('A')*8
    bf = Fg.count('B')*6
    cf = Fg.count('C')*4
    df = Fg.count('D')*2
    ef = Fg.count('E')*0
    pointVal = pointVal + af + bf + cf + df + ef
    # print(pointVal) #uncomment for progress test

    # calculate letter grade based off of final point value
    if pointVal <= 7:
        print("E")
    elif pointVal <= 22:
        print("D")
    elif pointVal <= 35:
        print("C")
    elif pointVal <= 49:
        print("B")
    else:
        print("A")
    # export Printed letters (Ex. A,B,C,D,E) to frontEnd


GCalculate(Q1, Q2, Q3, Q4, Fg)
