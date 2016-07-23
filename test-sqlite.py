#! /usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":

    print("insert test")
    connector = sqlite3.connect("sqlite_test.db")

    sql = "drop table test_table"
    connector.execute(sql)
    sql = "create table test_table(code, name)"
    connector.execute(sql)

    sql = "insert into test_table values('1','python')"
    connector.execute(sql)
    sql = "insert into test_table values('2','パイソン')"
    connector.execute(sql)
    sql = "insert into test_table values('3','ぱいそん')"
    connector.execute(sql)

    connector.commit()
    connector.close()

    print("select test")

    connector = sqlite3.connect("sqlite_test.db")
    cursor    = connector.cursor()
    cursor.execute("select * from test_table order by code")

    result = cursor.fetchall()

    for row in result:
        print "===== Hit! ====="
        print "code -- " + unicode(row[0])
        print "name -- " + unicode(row[1])

    cursor.close()
    connector.close()
