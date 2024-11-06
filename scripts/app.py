from fastapi import FastAPI, Request, Depends
from json import JSONDecodeError

from constants import *
from methods import (
    set_values,
    get_values,
    get_values_mapped,
    update_values,
    update_all_values,
    delete_values,
    verify,
)

app = FastAPI()


@app.get("/id/{id}")
async def read_root(id):
    # , user: str = Depends(verify)
    # if not user:
    #     return wrong_credentials
    try:
        rows = get_values()
        data = {key: val for key, *val in rows}
        if id == "all":
            return get_values_mapped()
        return {id: data[int(id)]}
    except KeyError:
        return wrong_id
    except Exception as e:
        return {any_error[0]: any_error[1].format(e)}


@app.get("/id/")
async def read_root(id, user: str = Depends(verify)):
    if not user:
        return wrong_credentials
    try:
        ids = id.split(",")
        ids = (int(i.strip()) for i in ids)
        mapped_result = get_values_mapped()
        result = [i for i in mapped_result if i["id"] in ids]
        return result
    except Exception as e:
        return {any_error[0]: any_error[1].format(e)}


@app.post("/post/json")
async def create_root(request: Request, user: str = Depends(verify)):
    if not user:
        return wrong_credentials
    try:
        data = await request.json()
        res = set_values(**data)
        return res
    except JSONDecodeError as e:
        return wrong_format
    except Exception as e:
        return {any_error[0]: any_error[1].format(e)}


@app.post("/post/form-data")
async def create_root(request: Request, user: str = Depends(verify)):
    if not user:
        return wrong_credentials
    try:
        data = await request.form()
        if not data:
            return empty
        res = set_values(**data)
        return res
    except Exception as e:
        return {any_error[0]: any_error[1].format(e)}


@app.put("/put/form-data")
async def update_root(request: Request, user: str = Depends(verify)):
    if not user:
        wrong_credentials
    try:
        data = await request.form()
        if not data:
            return empty
        res = update_all_values(**data)
        return res
    except Exception as e:
        return {any_error[0]: any_error[1].format(e)}


@app.patch("/patch/form-data")
async def update_patch_root(request: Request, user: str = Depends(verify)):
    if not user:
        return wrong_credentials
    try:
        data = await request.form()
        if not data:
            return empty
        res = update_values(**data)
        return res
    except Exception as e:
        return {any_error[0]: any_error[1].format(e)}


@app.delete("/delete")
async def delete_root(request: Request, user: str = Depends(verify)):
    if not user:
        return wrong_credentials
    try:
        data = await request.json()
        res = delete_values(**data)
        return res
    except JSONDecodeError as e:
        return wrong_format
    except Exception as e:
        return {any_error[0]: any_error[1].format(e)}
