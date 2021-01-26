with open("out9.txt", "w") as fw, open("in9.txt", "r") as fr:
    fw.writelines(l for l in fr)
