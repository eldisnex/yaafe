import pyodbc

server = "MANDIBULA-DE-PE"
database = "details"
conn_str = (
    f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION=True"
)
connection = pyodbc.connect(conn_str)

try:
    connection.autocommit = True
    connection.execute(
        "CREATE TABLE details(id INT NOT NULL PRIMARY KEY IDENTITY(1, 1),stationid VARCHAR(255),dt DATETIME,shazam varchar(255))"
    )
    print("Database created")
except pyodbc.Error as e:
    print("Database was actually created")


def insert(stationId, datetime, shazam):  # 2008-11-11 13:23:44
    try:
        connection.autocommit = True
        connection.execute(
            f"SET DATEFORMAT 'YMD';INSERT INTO details (stationid, dt, shazam) VALUES ('{stationId}', '{datetime}', '{shazam}');"
        )
    except pyodbc.Error as e:
        print(f"Error: {e}")


def close():
    if "connection" in locals():
        connection.close()
