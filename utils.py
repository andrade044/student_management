import sqlite3
import pandas as pd 


DB_NAME = 'alunos.db'
def get_connection():
    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row
    return conn

def creat_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
    nome_completo TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL PRIMARY KEY, 
    telefone TEXT NOT NULL,
    pagamento REAL NOT NULL,
    turno TEXT NOT NULL,
    parte_processo TEXT NOT NULL)
""")
    conn.commit()
    conn.close()


def register_student(cpf, name, phone, rotation, payment, process_part):
    creat_table()
    conn = get_connection()
    cursor = conn.cursor()
    info_table ="""nome_completo, cpf, telefone, pagamento, turno,parte_processo"""
    
    qntd = "?,?,?,?,?,?"
    sql_insert = f"""
        INSERT INTO alunos ({info_table})
        VALUES ({qntd});
    """
    values = (name, cpf, phone, payment, rotation, process_part)
    cursor.execute(sql_insert,values)
    
    conn.commit()
    conn.close()

def delele_student(cpf):
    creat_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM alunos WHERE cpf = {cpf}")
    conn.commit()
    conn.close()


def update_student(cpf, new_name, new_phone, new_rotation, new_payment, new_process_part):
    
    
    conn = get_connection()
    cursor = conn.cursor()
    
  
    sql_update = """
        UPDATE alunos 
        SET nome_completo = ?,
            telefone = ?,
            turno = ?,
            pagamento = ?,
            parte_processo = ?
        WHERE cpf = ?; 
    """

    
    values = (new_name, new_phone, new_rotation, new_payment, new_process_part, cpf)
    
    try:
        cursor.execute(sql_update, values)
        conn.commit()
        rows_affected = cursor.rowcount
        
        if rows_affected > 0:
            print(f"Aluno com CPF {cpf} atualizado com sucesso.")
        else:
            print(f"Nenhuma alteração feita. Aluno com CPF {cpf} não encontrado.")
            
    except Exception as e:
        print(f" Erro ao atualizar o aluno {cpf}: {e}")
        conn.rollback() 

    finally:
        cursor.close()
        conn.close()

def consult_studant(cpf):
    creat_table()
    conn = get_connection()
    cursor = conn.cursor()
    sql_query = "SELECT * FROM alunos WHERE CPF = ?"

    cursor.execute(sql_query,(cpf))

    alunos_data = cursor.fetchall()

    return alunos_data
    
def get_filtered_data(cpf):
    conn = get_connection()
    

    if cpf:
        search_pattern = f"%{cpf}%"
        query = "SELECT * FROM alunos WHERE cpf LIKE  ?"

        df = pd.read_sql_query(query, conn, params=(search_pattern,))

    else:
        query = "SELECT * FROM alunos"
        df = pd.read_sql_query(query,conn)
    
    return df