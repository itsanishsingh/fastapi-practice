import os
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
import psycopg2

from constants import *


security = HTTPBasic()


def verify(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username not in users:
        return False
    if credentials.password != users.get(credentials.username):
        return False
    return True


def connector(func):
    def wrapper(*args, **kwargs):
        try:
            load_dotenv()
            config = {
                "host": os.getenv("host"),
                "database": os.getenv("database"),
                "user": os.getenv("user"),
                "password": os.getenv("password"),
            }
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    result = func(cur, *args, **kwargs)
                    return result
        except Exception as e:
            return {any_error[0]: any_error[1].format(e)}

    return wrapper


@connector
def get_values_mapped(cur):
    cur.execute(column_name_query)
    columns = cur.fetchall()
    columns = [i[0] for i in columns]
    rows = get_values()
    result = {"columns": columns, "rows": rows}
    return result


@connector
def get_values(cur):
    cur.execute(select_all_query)
    rows = cur.fetchall()
    return rows


@connector
def set_values(cur, **kwargs):
    cur.execute(insert_query % (kwargs["id"], kwargs["name"], kwargs["age"]))
    return success


@connector
def update_all_values(cur, **kwargs):
    rows = get_values()
    ids = (i[0] for i in rows)
    if int(kwargs.get("id")) in ids:
        cur.execute(update_all_query % (kwargs["name"], kwargs["age"], kwargs["id"]))
        return success
    return wrong_id


@connector
def update_values(cur, **kwargs):
    rows = get_values()
    ids = (i[0] for i in rows)
    if int(kwargs.get("id")) in ids:
        if kwargs.get("age"):
            cur.execute(update_age_query % (kwargs["age"], kwargs["id"]))
        if kwargs.get("name"):
            cur.execute(update_name_query % (kwargs["name"], kwargs["id"]))
        return success
    return wrong_id


@connector
def delete_values(cur, **kwargs):
    id = kwargs["id"]
    cur.execute(delete_query % (id))
    return success
