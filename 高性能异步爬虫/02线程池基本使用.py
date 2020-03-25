# import time

# def get_page(str):
#     print("正在下载:", str)
#     time.sleep(2)
#     print("下载成功:", str)

# name_list = ["xiaozi", "aa", "bb", "cc"]

# start_time = time.time()

# for i in name_list:
#     get_page(i)

# end_time = time.time()

# print(end_time - start_time)

import time

from multiprocessing.dummy import Pool

def get_page(str):
    print("正在下载:", str)
    time.sleep(2)
    print("下载成功:", str)

name_list = ["xiaozi", "aa", "bb", "cc"]

start_time = time.time()

pool = Pool(4)
pool.map(get_page, name_list)

end_time = time.time()

print(end_time - start_time)