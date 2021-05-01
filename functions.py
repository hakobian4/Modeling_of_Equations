import sympy as sym
import numpy as np
import time, re
import pdfkit
from sympy import log, sqrt, E, pi



def create_variables(equations):
    variables = []
    for equation in equations:
        variables.append(re.findall('[a-z]', equation))
    print('var1', variables)
    variables = np.concatenate(variables)
    print('var2', variables)

    variables = np.unique(variables)
    print('var3', variables)

    symbol_variables=[]
    for variable in variables:
        globals()[variable] = sym.symbols(variable)
        symbol_variables.append(globals()[variable])
    print("symbol_variables", symbol_variables)
    return symbol_variables


def sympy_method(equations, values, symbols):

    sym.init_printing()
    F=[]
    for i in range(len(equations)):
        F.append(sym.Eq(equations[i], values[i]))

    return sym.solve(F)


def check_equations_validation(equations):

    symbols = create_variables(equations)
    equals = []
    for equation in equations:
        equals.append((re.findall("=", equation)).count('='))
        # asterisk.append((re.findall("[*]", equation)).count('*'))
        equation.replace('**', '^')
        equation.replace('*', '')
    if len(symbols) > len(equations):
        raise Exception("Your variables' number is not equal to equations' number.")
    elif np.prod(equals) != 1:
        raise Exception("Please check Your equations.")
    else:
        return symbols



def add_asterisks(equations):

    for i in range(len(equations)):
        equation = re.sub(re.compile(r'\s+'), '', equations[i])
        print("eq", equation)
        equation = list(equation)
        print("eqlist", equation)

        result = equation[0]
        for pos in range(len(equation) - 1):

            if len(re.findall("\d+", equation[pos])) > 0:

                if len(re.findall("[a-z]|[(]", equation[pos+1])) > 0:
                    result += '*'

            elif len(re.findall("[a-z]", equation[pos])) > 0:
                if len(re.findall("[a-z]|[(]|[\d]", equation[pos+1])) > 0:
                    result += '*'


            elif equation[pos] == ")":
                if len(re.findall("[a-z]|\d", equation[pos+1])) > 0:
                    result += '*'

            elif equation[pos] == '^':
                result = result[0:-1]
                result += '**'

            result += equation[pos+1]

        equations[i] = result

    return equations



def convert_to_solving_mode(equations):

    values = []
    for i in range(len(equations)):
        equal_pos = equations[i].find('=')
        after_equal = "-1*(" + equations[i][equal_pos + 1:] + ')'
        after_equal = re.sub(re.compile(r'\s+'), '', str(eval(after_equal)))
        if after_equal[0] != '-':
            after_equal = '+' + after_equal

        equations[i] = equations[i][:equal_pos] + after_equal

        equations[i] = re.sub(re.compile(r'\s+'), '', str(eval(equations[i])))
        equations[i] = '+' + equations[i] + '+'

        value = re.findall(r"([+,-]+\d+)+[+,-]", equations[i])
        if len(value) == 0:
            value.append(0)

        if float(value[0]) == int(value[0]):
            values.append(-1 * int(value[0]))
        else:
            values.append(-1 * float(value[0]))

        equations[i] = eval(equations[i][1:-1] + "+" + str(values[-1]))

    return equations, values


 
def solve_equations(equation):
    # f = ["4x + (3y) =-2z+25 ", "-2x + 2y + 3z = -10", "3x - 5y + 2z = -4 "]
    # d = ["2x^2 + 3x +6 =0"]

    symbols = check_equations_validation(equation)
    c = add_asterisks(equation)
    # print(c)
    equations, values = convert_to_solving_mode(c)
    print(equations,'\n',values)
    sympy_result = sympy_method(equations, values, symbols)
    print("sympy result: ", sympy_result)
    data = []

    if str(type(sympy_result)) == "<class 'dict'>":
        data.append(sympy_result)
    else:

        data = sympy_result

    print(data)
    for res in data:
        for key, values in res.items():
            res[key] = round(float(res[key]), 3)
    print("DATA", data)
    return data


#num2str
#str2num
#simplify

#re.findall("[√(]+\d+[,]+\d+[)]", a)

