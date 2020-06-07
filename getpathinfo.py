import os

def get_path():
    curpath = os.path.dirname(os.path.realpath(__file__))
    return curpath

if __name__ == '__main__':
    print("测试路径",get_path())