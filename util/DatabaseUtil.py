# -*- coding: UTF-8 -*-
import mysql.connector
import ConfigParser
import pandas as pd
from sqlalchemy import create_engine


# config = {'host':'127.0.0.1', 'user':'root', 'password':'root', 'database':'stockmarket2', 'charset':'utf8'}
# config = {'host':'rm-m5e1bn54y57k9722o.mysql.rds.aliyuncs.com', 'user':'stockmarket', 'password':'J1nma02007', 'database':'stockmarket2', 'charset':'utf8'}


def get_database_config():
    config = {}
    config_file = ConfigParser.SafeConfigParser()
    config_file.read("./ss_config.ini")

    config['host'] = config_file.get('database', 'host')
    config['user'] = config_file.get('database', 'user')
    config['password'] = config_file.get('database', 'password')
    config['database'] = config_file.get('database', 'database')
    config['charset'] = config_file.get('database', 'charset')
    return config


def get_data(sql):
    config = get_database_config()
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception, e:
        print e
    finally:
        cursor.close()
        cnx.close()


def update(sql):
    config = get_database_config()
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
        cnx.commit()
    except Exception, e:
        print e
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()


def call(procname, args=()):
    config = get_database_config()
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        cursor.callproc(procname, args)
        cnx.commit()
    except Exception, e:
        print e
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()


def get_pd_data(sql):
    config = get_database_config()
    db_conn = mysql.connector.connect(**config)
    data = pd.read_sql_query(sql=sql, con=db_conn)
    db_conn.close()
    return data


def save_pd_data(table_name, table_data, if_exists='append', index=True):
    if table_data is None:
        return

    try:
        config = get_database_config()
        conn = 'mysql://' + config['user'] + ':' + config['password'] + '@' + config['host'] + '/' + config['database'] + '?charset=' + config['charset']
        engine = create_engine(conn)
        table_data.to_sql(table_name, engine, if_exists=if_exists, index=index)
    except Exception as e:
        print e

