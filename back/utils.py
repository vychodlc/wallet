import sqlite3

conn = sqlite3.connect('wallet.db')
cur = conn.cursor()

# 创建表
sql_create_user = '''
  CREATE TABLE IF NOT EXISTS User(
    ID INTEGER PRIMARY KEY     AUTOINCREMENT,
    NAME           TEXT    NOT NULL
  );
'''
cur.execute(sql_create_user)
conn.commit()

# 插入
def Insert(table,data):
  values = ""
  for item in data:
    values =  values + str(item) + ',' if (type(item)==int or type(item)==float) else values + "'" + item + "',"
  values = values.strip(',')
  sql_insert = "INSERT INTO %s VALUES (%s);" % (table,values)

  print(sql_insert)
  cur.execute(sql_insert)
  conn.commit()

# 查询
def Select(table,key,val):
  sql_select = "SELECT %s = %s from %s;" % (key,val,table)
  data = cur.execute(sql_select)
  return data

# 删除
def Delete(key,val):
  sql_delete = "DELETE from COMPANY where %s = %s;" % (key,val)
  cur.execute(sql_delete)
  conn.commit()

# 修改
def Update(table,key,val,_key,_val):
  sql_update = "UPDATE %s set %s = %s where %s = %s;" % (table,key,val,_key,_val)
  cur.execute(sql_update)
  conn.commit()