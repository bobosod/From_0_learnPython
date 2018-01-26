import win32com.client

engine = win32com.client.Dispatch("DAO.DBEngine.36")
db = engine.OpenDatabase("address.mdb")
rs = db.OpenRecordset("address")
rs = db.OpenRecordset("select * from address")

while not rs.EOF:
    print((rs.Fields("address").Value).encode("gb2312"))
    rs.MoveNext()