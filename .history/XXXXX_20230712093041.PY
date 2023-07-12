

def test():
    print('test')
    x = 1
    y = 2
    return x, y

def main():
    x, y = test()
    print(x, y)

if __name__ == '__main__':
    main()