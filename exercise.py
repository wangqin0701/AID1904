"""
  练习:dict下创建数据表 words
      id  word  mean三个字段 ,要求存储单词本
"""

import pymysql
import re
import time

# # 连接数据库
# db = pymysql.connect(host = "localhost",
#                      port = 3306,
#                      user = "root",
#                      password = "123456",
#                      database = "dict",
#                      charset = "utf8")
#
# # 获取游标(用于进行数据操作的对象,承载操作结果)
# cur = db.cursor()
#
# DICT_TEXT = "./dict.txt"
# fd = open(DICT_TEXT,"r")
# sql = "insert into words (word,means) values (%s,%s)"
# # cur.execute(sql)
#
# # i = 0
# # for line in fd:
# #     i += 1
# #     word = line.split(" ")[0]
# #     means = " ".join(line.split(" ")[2:]).strip()
# #     # print(word,means)
# #     try:
# #         # sql = "insert into words (word,means) values ('%s','%s')"%(word,means)
# #         # cur.execute(sql)
# #         sql = "insert into words (word,means) values (%s,%s)"
# #         cur.execute(sql)
# #
# #         db.commit()
# #     except Exception as e:
# #         db.rollback()
# #         print(e)
# #     if not word:
# #         time.sleep(0.1)
# #         fd.close()
# #         break
#
#
# for line in fd:
#     # 获取word和mean
#     tup = re.findall(r"(\S+)\s+(.*)",line)[0]
#     # print(tup)
#
#     try:
#         cur.execute(sql,tup)
#         db.commit()
#     except Exception as e:
#         db.rollback()
#
# fd.close()
# cur.close()
# db.close()

# ------------------------------------------------------

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")
# 创建游标
cur = db.cursor()

sql = "insert into words (word, mean) values(%s,%s)"
# fd = open("dict.txt")
with open("dict.txt") as fd:
    for line in fd:
        tup = re.findall(r"(\S+)\s+(.*)", line)[0]
        print(tup)
        try:
            cur.execute(sql,tup)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

fd.close()
cur.close()
db.close()