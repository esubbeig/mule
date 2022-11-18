import pyodbc

server = 'userinfoserver.database.windows.net'
database = 'user-info'
username = 'user-info-admin'
password = '{Asp-Fall@2022}'   
driver= '{ODBC Driver 17 for SQL Server}'

def save_to_db(full_name, email, gender, degree_category):

    conn =  pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    SQLCommand = ('''
            INSERT INTO user_info (full_name, email, gender, degree_category) 
            VALUES ('{0}','{1}','{2}', '{3}')
            ''').format(full_name, email, gender, degree_category)
    cursor.execute(SQLCommand)
    conn.commit()