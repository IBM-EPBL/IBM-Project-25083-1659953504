import ibm_db
import random
import  string
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bmd88020;PWD=wcxrFr0o8c29Ybco","", "")
print("Connection Successful")
print(conn)


def signinusersdb(email,password):
    stmt = ibm_db.exec_immediate(conn, "select PASSWORD from users where EMAIL={e};".format(e=email))
    while ibm_db.fetch_row(stmt) != False:
        value = ibm_db.result(stmt, 0)
        if(value == password):
            return "found"
    return "Not found"

def signupusersdb(name,email,password):
    # key = ''.join(random.choices(string.ascii_lowercase +string.digits, k=25))
    # stmt = "insert into users (NAME, EMAIL, PASSWORD ) values ({n} , {e} , {p});".format(n = name , e= email , p= password)
    # if ibm_db.exec_immediate(conn , stmt):
    #     return "Done"
    # return "Error"
    sql = "insert into users (NAME, EMAIL, PASSWORD ) values(? , ? , ?)"
    stmt = ibm_db.prepare(conn , sql)
    ibm_db.bind_param(stmt ,1 , name)
    ibm_db.bind_param(stmt ,2 , email)
    ibm_db.bind_param(stmt ,3 , password)
    result =  ibm_db.execute(stmt)
    if(result):
        return result
    return "Error"