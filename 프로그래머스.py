def solution(strArr):
    result = []
    for i in range(len(strArr)):
        if i % 2 != 0:  # 홀수 인덱스
            result.append(strArr[i].upper())
        else:           # 짝수 인덱스
            result.append(strArr[i].lower())
    return result

