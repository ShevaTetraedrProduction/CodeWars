def pick_peaks(ar):
    arr = ar[::]
    print(arr)
    pos = []
    peaks = []
    tmp = arr[0]
    ps = 0
    for i in range(len(arr) - 1):
        if(tmp == ar[i] and i != len(ar) - 2):
            continue
        tmp = arr[i]
        if(ar[i-1] <= tmp):
                arr[ps] = -1
        if(ar[i + 1] < tmp and i):
            ps = i

    print(arr)

pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])





'''
test.assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
test.assert_equals(pick_peaks([]),{"pos":[],"peaks":[]})
test.assert_equals(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})
'''