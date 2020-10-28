from zipfile import ZipFile
import base64

cdpath = "C:\\Users\\felix\\Documents\\GitHub\\competitive\\raziCTF20\\misc\\recurzip\\"
name = "emF3cnVmcHluag==.zip"
password = bytes(str(base64.b64decode(name[:-4]), "utf-8"), "ascii")
# str(base64.b64decode(name[:-4]), "utf-8")
print(password)

while True:
    with ZipFile(cdpath + name, "r") as myzip:
            names = [name for name in myzip.namelist()]
            print(names)
            newname = names[0]
            myzip.extract(newname, pwd=password, path=cdpath)
            password = bytes(str(base64.b64decode(newname[:-4]), "utf-8"), "ascii")
            name = newname
    print("name: ", name)
    print("password: ", password)

# while True:
#     with ZipFile(path + name, "r") as myzip:
#         names = [info.filename for info in myzip.infolist()]
#         print(names)
#         newname = names[0]
#         myzip.extract(newname, pwd=password)
#         password = bytes(str(base64.b64decode(newname[:-4]), "utf-8"), "ascii")
#         name = newname