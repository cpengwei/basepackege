#encoding:utf-8

import pymysql

'''
查询数据库中都有哪几个表is_delete字段有Y,1的数据
'''
db_info = {
    "host":"192.168.11.30",
    "user":"root",
    "passwd":"changme",
    "database":"xz_cpm",
    "port":20008,
    "charset":"utf8"
}

sql1 = r'''SELECT DISTINCT TABLE_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE COLUMN_NAME IN ('is_delete') AND TABLE_SCHEMA='xz_cpm_online' '''

db = pymysql.connect(host='192.168.11.30',user='root',password='changeme',db='xz_cpm_online',port=20008,charset='utf8')
cursor = db.cursor()
cursor.execute(sql1)
data = cursor.fetchall()
for one in data:
    cursor.execute("select is_delete from {} where is_delete in ('1','Y')".format(one[0]))
    r=cursor.fetchall()
    if r:
        print(r)
db.close()