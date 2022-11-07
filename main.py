import sys
from word_map import WordMap

def main():
    f = open(sys.argv[1], 'r')
    inLines = f.read().split('\n')
    f.close()
    wm = WordMap(inLines)
    letters, path = wm.traverse()
    #uncomment for saving output to file
    #file_path = 'output.txt'
    #sys.stdout = open(file_path, "w")
    print("Letters " + letters)
    print("Path as characters " + path)
    #sys.stdout.close()


if __name__ == '__main__':
    main()