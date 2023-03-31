def sqrt(x):
    EPS = 1e-9
    if x == 0:
        return 0
    else:
        left, right = 1, x
        while right - left > EPS:
            mid  = (left + right) / 2
            if mid * mid < x:
                left = mid 
            else:
                right = mid
                
    return (left + right) / 2

def main():
    print(sqrt(3))
    
    