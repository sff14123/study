def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    def solve(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    약수 = solve(numer, denom)
    
    return [numer // 약수, denom // 약수]