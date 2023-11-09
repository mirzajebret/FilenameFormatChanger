import os

'''
this will change the whole file format and name inside the directory given. 
use only with one type of files format.
example: all files are PNG, MP4, MKV, MP3, EXE
'''


def main():
    backslash = open('backslash.txt')
    req_path = input('path of the files: ').replace(*backslash, '/') + '/'
    rename_to = input('rename: ')
    format = input('format: ')
    print('files will be enumerated automatically\n')
    i = 1
    for filename in os.listdir(req_path):
        my_dest = f'{rename_to}_{i}.{format}'
        my_source = f'{req_path}{filename}'
        my_dest = req_path + my_dest
        os.rename(my_source, my_dest)
        print(f'new> {my_dest}')
        print(f'old> {my_source}\n')
        i += 1
    print('==========================================')
    print(f'{i - 1} files formatted')


if __name__ == '__main__':
    main()
