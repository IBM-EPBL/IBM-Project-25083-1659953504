import ibm_db
import random
import  string
from hashing import *
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bmd88020;PWD=wcxrFr0o8c29Ybco","", "")
print("Connection Successful")
print(conn)


def signinusersdb(email,password):
    stmt = ibm_db.exec_immediate(conn, "select password,uid,random_key,name from users1 where EMAIL='"+email+"';")
    while ibm_db.fetch_row(stmt) != False:
        value = ibm_db.result(stmt, 0)
        key = ibm_db.result(stmt, 1)
        randomid = ibm_db.result(stmt, 2)
        dname = ibm_db.result(stmt,3)
        print(value)
        r = rehashing(value,password,key,randomid,dname)
        # print(r)
        return r
    return '{"result":"Not Found"}'

def signupusersdb(name,email,password):
    key = ''.join(random.choices(string.ascii_lowercase +string.digits, k=25))
    # key = ''.join(random.choices(string.ascii_lowercase +string.digits, k=25))
    arr = hashing(password)
    stmt = "insert into users1 (NAME, EMAIL, PASSWORD, random_key) values ('"+name+"','"+ email+"','"+ str(arr.decode()) +"','"+ key+"' );"
    if ibm_db.exec_immediate(conn, stmt):
         return '{"result":"Done"}'
    return '{"result":"Not Found"}'


    # sql = "insert into users1 (NAME, EMAIL, PASSWORD , RANDOM_KEY ) values(? , ? , ? , ?)"
    # stmt = ibm_db.prepare(conn , sql)
    # ibm_db.bind_param(stmt ,1 , name)
    # ibm_db.bind_param(stmt ,2 , email)
    # ibm_db.bind_param(stmt ,3 , password)
    # ibm_db.bind_param(stmt ,4 , key)
    # result =  ibm_db.execute(stmt)
    # if(result):
    #    return '{"result":"Done"}'
    # return '{"result":"Not Found"}'