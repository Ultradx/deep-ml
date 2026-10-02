import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    upper = derivativeResult(g_coeffs, x)*polynomialResult(h_coeffs,x) - polynomialResult(g_coeffs, x)*derivativeResult(h_coeffs, x)
    lower = abs(polynomialResult(h_coeffs, x))**2
    return upper/lower

def polynomialResult(coeffs, x):
    sum = 0
    for i in range(len(coeffs)):
        sum += coeffs[i]*x**((len(coeffs)-1)-i)
    return sum

def derivativeResult(coeffs, x):
    result = 0

    for i in range(len(coeffs) - 1):
        degree = (len(coeffs) - 1) - i
        result += degree * coeffs[i] * x**(degree - 1)

    return result



    