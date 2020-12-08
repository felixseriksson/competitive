from zipfile import ZipFile
import base64

cdpath = "C:\\Users\\felix\\Documents\\GitHub\\competitive\\djulkalendern20\\day8\\"
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                name = "19460{}{}{}00{}4".format(a, b, c, d)
                password = bytes(name, "ascii")
                with ZipFile(cdpath + "secrets.zip") as myzip:
                    # names = [name for name in myzip.namelist()]
                    # names = ["secrets\\secret.txt"]
                    # for n in names:
                    try:
                        myzip.extractall(pwd=password)
                        print(password)
                        print("finished")
                        exit(0)
                    except:
                        pass
                    # try:
                    #     myzip.extractall(pwd=password, path=cdpath)
                    #     print("finished")
                    #     exit(0)
                    #     # input()
                    # except:
                    #     pass
                # try: 
                #     with open(cdpath + "secret\\secrets.txt")

# while True:
#     with ZipFile(path + name, "r") as myzip:
#         names = [info.filename for info in myzip.infolist()]
#         print(names)
#         newname = names[0]
#         myzip.extract(newname, pwd=password)
#         password = bytes(str(base64.b64decode(newname[:-4]), "utf-8"), "ascii")
#         name = newname