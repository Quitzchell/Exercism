import operator

ops = {
    'plus': operator.add,
    'minus': operator.sub,
    'multiplied': operator.mul,
    'divided': operator.truediv,
}

ilegal_ops = ['cubed']

def answer(question):
    equation = []
    words = [word.strip("?") for word in question.split()]
    
    for word in words:
        if word in ops.keys():
            equation.append(ops[word])
        if word.lstrip("-+").isdigit():
            equation.append(int(word))
        if word in ilegal_ops:
            raise ValueError("unknown operation")
    
    if not equation:
        raise ValueError("syntax error")
    
    while len(equation) > 1:
        try:
            x_value, operation, y_value, *rest = equation            
            equation = [operation(x_value, y_value)]
            if rest:
                equation = equation + rest
        except:
            # Code for what to do when an error gets thrown in the code above.
            # This could be one error, or more complicated logging, error checking and messaging.
            raise ValueError("syntax error")
    
    return equation[0]