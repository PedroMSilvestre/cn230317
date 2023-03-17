# multiplier.py
import sys


def multiplier(pList: list):
    result = 1
    for n in pList:
        result *= float(n)
    # for
    return result
# def multiplier

if(len(sys.argv)>1):
    the_values: list = sys.argv[1:] #excepto o nome do script
    the_multiplication = multiplier(the_values)
    the_output = \
        f"The mult of {the_values} is {the_multiplication}"

    print(the_output)
else:
    the_output =