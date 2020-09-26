from zipfile import ZipFile

path = "C:\\Users\\felix\\Documents\\GitHub\\competitive\\foictf2020\\övriga\\zips\\"
name = "3466.zip"
password = b"4342"

while True:
    with ZipFile(path + name, "r") as myzip:
        names = [info.filename for info in myzip.infolist()]
        password = bytes(str(names[0][:4]), "ascii")
        print(names)
        myzip.extractall(path, pwd=password)
        name = names[0]