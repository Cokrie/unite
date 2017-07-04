#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import MySQLdb
import sql_list

def mysql_db_conn():

    conn= MySQLdb.connect(
        host=str(raw_input('please input the db_host_ip')),
        port = 3306,
        user='root',
        passwd='123456',
        db='test'

    )
    return conn


def mysql_db_exec(conn):

    sql_exec = conn.cursor()
    aa = sql_exec.execute(sql_list)
    return aa


def mysql_db_close():

    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":

    mysql_db_conn()
    None