# Responses
empty = {"Message": "Field empty"}
wrong_id = {"Error": "Id not found"}
wrong_format = {"Error": "Wrong format"}
wrong_credentials = {"Error": "Wrong credentials"}
any_error = ("Error", str(type({})))
success = {"Message": "Success"}


# Queries
column_name_query = "SELECT column_name FROM information_schema.columns WHERE table_name = 'people' order by ordinal_position"
select_all_query = "Select * from people order by id asc"
insert_query = "insert into people (id, name, age) values(%s, '%s', %s)"
update_all_query = "update people set name='%s', age=%s where id=%s"
update_age_query = "update people set age=%s where id=%s"
update_name_query = "update people set name='%s' where id=%s"
delete_query = "delete from people where id=%s"


# Data
users = {"Anish": "1234", "Ritik": "2345"}
