#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import MySQLdb
import re
import sql_list


def mysql_db_conn(host, port, user, paswd, db):

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
    db_exec_result = sql_exec.execute(sql_list)
    db_exec_result.close()
    conn.commit()
    return db_exec_result


def mysql_db_close(db_exec_result, conn):

    #db_exec_result.close()
    #conn.commit()
    conn.close()


if __name__ == "__main__":

    mysql_db_conn()

    None