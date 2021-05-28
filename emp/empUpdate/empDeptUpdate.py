# -*- coding: utf-8 -*-

import datetime
import MySQLdb

host = "114.115.161.26"
user = "ctgehr_dev"
passwd = "dj^kj3k672DA"
port = 3306
db = "ctgehr"

def mytask():
        # 服务器地址 ,端口， 登录账号 , 密码 ,数据库名称
        conn = MySQLdb.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset='utf8',)
        cursor = conn.cursor()
        sql = ("CALL emp_update_dept();")
        cursor.execute(sql)
        print(sql+"执行成功")
        #对fetchall获取到的结果SQL结果集做换行显示
        print('\n'.join(str(e) for e in cursor.fetchall()))
        cursor.close()
        conn.close()

mytask()



# class SelectMySQL(object):
#     def select_data(self, sql):
#         result = []
#         try:
#             conn = MySQLdb.connect(host=host,
#                                    port=port,
#                                    user=user,
#                                    passwd=passwd,
#                                    db=db,
#                                    charset='utf8', )
#             cur = conn.cursor()
#             cur.execute(sql)
#             alldata = cur.fetchall()
#             print(alldata \n)
#             for rec in alldata:
#                 result.append(rec[5])  # 注意，我这里只是把查询出来的第一列数据保存到结果中了,如果是多列的话，稍微修改下就ok了
#         except Exception as e:
#             print('Error msg: ' + e)
#         finally:
#             cur.close()
#             conn.close()
#
#         return result
#
#     def get_result(self, sql, filename):
#         print(sql)
#         results = self.select_data(sql)
#         print('The amount of datas: %d' % (len(results)))
#         with open(filename, 'w') as f:
#             for result in results:
#                 f.write(str(result) + '\n')
#         print('Data write is over!')
#         return results
#
#
# if __name__ == '__main__':
#     sql = "CALL emp_update_dept();"
#     select = SelectMySQL()
#     result1 = select.get_result(sql, 'namemsg.txt')
#     print(result1)

