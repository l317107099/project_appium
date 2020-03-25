from concurrent import futures
import requests


a = ['a','b','c','d','e','f','g','h','i']

def save(cc):
    with open(cc+'.txt','w') as f:
        f.write("hello")


def download_one(cc):
    save(cc)

def download_many(cc_list):
    with futures.ThreadPoolExecutor(5) as exectu:
        res = exectu.map(download_one, cc_list)

    # return len(list(res))

def main(download):
    download(a)

import threading


def aa(a):

    print(a)
import time
def thread_down():
    a = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(a)):
        t1 = time.time()
        t = threading.Thread(target=aa, args=(a[i],))
        t.start()
        t2 = time.time()
        print(t2-t1)

if __name__ == '__main__':
    # main(download_many)
    thread_down()