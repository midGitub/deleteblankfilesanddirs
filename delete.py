#coding:utf-8
import os
def clearfile(path,dirname):
    full_path = os.path.join(path,dirname)
    listdir = os.listdir(full_path)
    if len(listdir)==0:
        os.rmdir(full_path)
        print ("正在删除%s"%full_path)
    for item in listdir:
        index = item.rfind('.')
        if index<0:
            full_dir_name = os.path.join(full_path,item)
            clearfile(full_path,item)
        else:
            file_name = os.path.join(full_path,item)
            if os.path.getsize(file_name)==0:
                os.remove(file_name)
                print ("正在删除%s文件"%file_name)

def main():
    dirname = input('输入要清除的文件夹:')
    clearfile(os.getcwd(),dirname)
    print ("complete!")
if __name__ == "__main__":
    main()
