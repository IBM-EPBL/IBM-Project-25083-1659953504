import ibm_db
import random
import  string
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zlm67833;PWD=NZvlsYswjWw1U7Yr","", "")
print("Connection Successful")
print(conn)


def signinusersdb(name,password):
    stmt = ibm_db.exec_immediate(conn, "select user_password from users where user_name='"+name+"';")
    while ibm_db.fetch_row(stmt) != False:
        value = ibm_db.result(stmt, 0)
        if(value == password):
            return "found"
    return "Not found"

def signupusersdb(name,email,password):
    key = ''.join(random.choices(string.ascii_lowercase +string.digits, k=25))
    stmt = "insert into users (display_name, user_name, user_password, random_key) values ('"+name+"','"+email+"','"+password+"','"+key+"');"
    if ibm_db.exec_immediate(conn, stmt):
        return "Done"
    return "Error"
  