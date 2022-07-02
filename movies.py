import sqlite3
con=sqlite3.connect('user.db')
con.execute("create table users(NAME,ACTOR,ACTRESS,DIRECTOR,YEAR);")
con.execute("INSERT INTO users VALUES('Shang-Chi and the Legend of the Ten Rings','Simu Liu','Awkwafina','Destin Daniel Cretton',2021);")
con.execute("INSERT INTO users VALUES('Dune','Timothée Chalamet','Rebecca Ferguson','Denis Villeneuve',2021);")
con.execute("INSERT INTO users VALUES('Spider-Man: Homecoming','Tom Holland','Zendaya','Jon Watts',2017);")
con.execute("INSERT INTO users VALUES('Spider-Man: Far From Home','Tom Holland','Zendaya','Jon Watts',2019);")
con.execute("INSERT INTO users VALUES('Spider-Man: No Way Home','Tom Holland','Zendaya','Jon Watts',2021);")
con.execute("INSERT INTO users VALUES('Avengers','Tonny Stark','Rashmika','Karthishwaren',2023);")

def insertData(name,actor,actress,director,year):
    qry=f'insert into users (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) values ("{name}","{actor}","{actress}","{director}","{year}");'
    con.execute(qry)
    con.commit()
    print("add")

def select(actor):
    qry='select * from users where actor="'+actor+'";'
    result=con.execute(qry)
    for row in result:
        print(row)


ch="y"
while(ch.lower()!='n'):
    print("ENTER 1 FOR INSERT LIST")
    print("Enter 2 FOR SHOW THE Data")
    c=int(input())
    if(c==1):
        print("add record")
        
        name=input("Enter the name of the movie:")
        actor=input("Enter the name of the actor:")
        actress=input("Enter the name of the acterss:")
        director=input("Enter the name of the director: ")
        year=input("Enter the year:")
        insertData(name,actor,actress,director,year)
    elif (c==2):
        print("select")
        select(input("ACTOR NAME:"))
    else:
        print("Invalied option:" + c)
    ch = input("Do you want to continue[Y/n]: ")