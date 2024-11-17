def solution(strArr):
    result = []
    for i in range(len(strArr)):
        if i % 2:  # 홀수 인덱스
            result.append(strArr[i].upper())
        else:      # 짝수 인덱스
            result.append(strArr[i].lower())
    return result

def solution(strArr):
    return list(map(lambda x: x[1].upper() if x[0] % 2 else x[1].lower(), 
                   enumerate(strArr)))
