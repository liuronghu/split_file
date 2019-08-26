#coding:utf8
import sys
import os
# 使用方法
# 分割 python 要执行的py文件名 split关键字 要分割的文件 分割的份数 （会在分割的文件同路径生成去掉后缀文件夹）
# 示例：python split_file.py split D:\1.zip 2000
# 合并 python 要执行的py文件名 merge关键字 要合并的目录（会合并这个目录下所有文件） 生成的文件路径名
# 示例：python split_file.py merge D:\1 3
# 方法
metmod = sys.argv[1]

def split_file(file_name,copies):
    filepath,fullflname = os.path.split(file_name)
    file_dirs = os.sep.join(file_name.split(".")[:-1])
    if not os.path.exists(file_dirs):
        os.makedirs(file_dirs)
    file_size = os.path.getsize(file_name)

    chunk_size = file_size // copies

    finally_chunk_size = file_size % copies
    #print(file_size,chunk_size,finally_chunk_size)
    with open(file_name,'rb') as f:
        for num in range(1,copies+2): 
            data = f.read(chunk_size)
            path = file_dirs + os.sep  + '%s'%num
            print(path)
            open(path,'wb').write(data)

def merge_file(file_dir,file_name):
    dir_file = [int(x) for x in os.listdir(file_dir)]
    dir_file.sort()
    #print(dir_file)
    with open(file_name,'wb') as f:
        for name in dir_file:
            path = file_dir + os.sep + str(name)
            #print(path)
            f.write(open(path,'rb').read())
    #    print(name)

if __name__ == "__main__":
    if metmod == "split":
        #文件名字
        file_name = sys.argv[2]
        #分割的份数
        copies = int(sys.argv[3])
        split_file(file_name,copies)
    elif metmod == "merge":
        #要合并的目录
        file_dir = sys.argv[2]
        #合并后的文件名字
        file_name = sys.argv[3]
        merge_file(file_dir,file_name)