def josephus_survivor(n,k):
    i = 0
    n = list(range(1, n + 1))    
    while(len(n) > 1):
        i %= len(n)
        k = (k, 1)[k <= 0]
        print(f'{n} i --> {i}  k--> {k}')
        if(i + 1 == k):
            n = n[:i] + n[i + 1:]        
            k += i
            if (k > len(n)):
                k -= (len(n) + i)
            i -= 1
        i += 1

josephus_survivor(7,3)


'''
test.assert_equals(josephus_survivor(7,3),4)
test.assert_equals(josephus_survivor(11,19),10)
test.assert_equals(josephus_survivor(1,300),1)
test.assert_equals(josephus_survivor(14,2),13)
test.assert_equals(josephus_survivor(100,1),100)
'''