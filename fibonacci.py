def fibonacii(n):
    if n > 1:
        return fibonacii(n-1) + fibonacii(n-2)
    else:
        return 1

assert fibonacii(0) == 1
assert fibonacii(1) == 1
assert fibonacii(2) == 2
assert fibonacii(3) == 3
assert fibonacii(4) == 5
assert fibonacii(5) == 8
assert fibonacii(6) == 13
assert fibonacii(7) == 21
assert fibonacii(8) == 34
assert fibonacii(9) == 55
assert fibonacii(10) == 89