def solution(roman):
    dict = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    arr = [dict[i] for i in roman]
    return sum([(-arr[i], arr[i]) [arr[i] >= arr[i + 1]] for i in range(len(arr) - 1)]) + arr[-1]



print(solution('MMVIII'))