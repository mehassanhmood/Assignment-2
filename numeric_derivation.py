"""
The following function calculate the differene quotient or the average rate of chnage of function 'f'.

"""

def derive(f, x, h=0.0001):
    """
    Parameters:
        - f: the function for which to calculate derivative.
        - x: The point at which to calculate the derivative.
        - h: Small value for the calculation.
    """
    y = (f(x+h) - f(x-h)) /(2*h)
    return y
