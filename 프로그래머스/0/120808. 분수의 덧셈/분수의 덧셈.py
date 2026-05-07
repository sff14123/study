def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    def solve(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    rst = solve(numer, denom)
    
    # 3. 약분
    return [numer // rst, denom // rst]