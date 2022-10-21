def digital_root(x):
    if x < 0:
        return
    
    def sum_x(x):
        s = 0
        while x != 0:
            s += x % 10
            x //= 10
        return s
    
    while x >= 10:
        x = sum_x(x)
    
    return x

def main():
    print("123:",digital_root(123))
    print("4923:",digital_root(4923))
    print("9847:",digital_root(9847))
    print("11:",digital_root(11))
main()             