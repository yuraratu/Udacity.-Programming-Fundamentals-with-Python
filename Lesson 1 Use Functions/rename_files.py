import os
path = r"d:\Files\Study\Udacity\Udacity. Programming Fundamentals with Python\prank\\"


def rename_files():
    files = os.listdir(path)  # get files

    # rename files
    os.chdir(path)
    for file_name in files:
        old_name, new_name = file_name, file_name
        for i in range(0, 10):
            new_name = new_name.replace(str(i), '')
        os.rename(old_name, new_name)
        print('old name: ' + old_name + '   new name: ' + new_name)

rename_files()
