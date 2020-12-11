#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != 
    "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = argv[1]
            b = argv[3]
            ai = int(a, 10)
            bi = int(b, 10)
            if argv[2] is "+":
                res = add(ai, bi)
            elif argv[2] is "-":
                res = sub(ai, bi)
            elif argv[2] is "*":
                res = mul(ai, bi)
            elif argv[2] is "/":
                res = div(ai, bi)
            print("{:d} {} {:d} = {:d}".format(ai, argv[2], bi, res))
