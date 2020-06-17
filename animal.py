import sys
def default():
    print('hello')
def cat():
    print('meow meow')
def main():
    if sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    else:
        default()
def dog():
    print('dog is barking, bho! bho! get afraid')
if __name__ =='__main__':
    main()
