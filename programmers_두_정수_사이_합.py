def solution(a, b):
    if a == b:
        return a
    if a > b:
        a,b = b,a
    return (b-a+1)*(a+b)/2
