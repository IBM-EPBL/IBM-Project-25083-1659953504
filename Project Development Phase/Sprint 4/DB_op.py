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
        # print(value)
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




def get_savedNews(id):
    stmt = ibm_db.exec_immediate(conn, "select * from news where USERID='"+id+"';")
    if ibm_db.fetch_row(stmt)== True:
        # print(ibm_db.fetch_assoc(stmt))
        value =  ibm_db.fetch_assoc(stmt)
        article = []
        while value != False:
            dict = {'image_url':value["IMAGE"] , 'title': value["TITLE"] , 'link': value["LINK"],'description': value["DESCRP"]}
            article.append(dict)
            value = ibm_db.fetch_assoc(stmt)
        return article
    return '{"result":"Not Found"}'


def addNewsDb(id,link,title,image , descrp):
    stmt = ibm_db.exec_immediate(conn, "select * from news where LINK='"+link+"';")
    if ibm_db.fetch_row(stmt)== False:
        stmt2 = "insert into news (USERID, TITLE, IMAGE, LINK ,DESCRP ) values ('"+id+"','"+title+"','"+image +"','"+link+"' , '"+descrp+"');"
        if ibm_db.exec_immediate(conn, stmt2):
             return '{"result":"Done"}'
        return '{"result":"Already Found"}'
    return '{"result":"Already Found"}'
   


