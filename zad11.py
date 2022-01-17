import os


def rotatefile(count, file_size, file_name):
    indX = 0
    while indX < count:
        with open(file_name, "a") as fd:
            ##
            fd.write("SOME text\n")
            ##
            if int(os.path.getsize(file_name)) > file_size:
                indX += 1
                file_name = "new_file"+str(indX)+".txt"


if __name__ == "__main__":
    count = 3
    file_size = 100
    file_name = "new_file.txt"
    rotatefile(count, file_size, file_name)
    print(os.stat('new_file.txt').st_size)
    print(os.stat('new_file1.txt').st_size)
    print(os.stat('new_file2.txt').t_size)