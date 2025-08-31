from db import connection
import streamlit as st

create_conn = connection.create_connection()

def create_table_users():
    if create_conn:

            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    db_cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS users
                            (
                                userid INT PRIMARY KEY AUTO_INCREMENT,
                                username VARCHAR(100) NOT NULL UNIQUE,
                                password VARCHAR(100) NOT NULL
                            )
                        """
                    )

                    db_conn.commit()
                    print("Table created successfully!")
                
                
                
                except Exception as e:
                    print("Cannot create table", e)

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()

def insert(username, password):
    if create_conn:

            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    values = (username, password)
                    insert_query = f"""
                            INSERT INTO {st.secrets["mysql"]["table"]}
                            (username, password)
                            VALUES
                            (%s, %s)
                        """
                    db_cursor.execute(insert_query, values)

                    db_conn.commit()
                    print("Inserted successfully!")
                    return True
                
                
                except Exception as e:
                    print("Cannot insert", e)
                    return False

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def check_login_credentials(username, password):
     if create_conn:

            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    credentials_query = f"""
                            SELECT 1 FROM {st.secrets["mysql"]["table"]}
                            WHERE username = %s AND password = %s
                            LIMIT 1
                        """

                    db_cursor.execute(credentials_query, (username, password))
                    result = db_cursor.fetchone()

                    if result:
                        print("Credentials Validated")
                        return True, "Credentials Validated"
                    else:
                        print("Credentials NOT validated")
                        return False, "Credentials NOT validated"
                
                
                except Exception as e:
                    print("Cannot find credentials", e)
                    return False, "Cannot find credentials"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()
         

def check_username(username):
     if create_conn:

            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    check_username_query = f"""
                            SELECT username FROM {st.secrets["mysql"]["table"]}
                            WHERE username = %s
                            LIMIT 1
                        """

                    db_cursor.execute(check_username_query, (username,))
                    result = db_cursor.fetchone()

                    if result:
                        print("Username found")
                        return True
                    else:
                        print("Unique username")
                        return False
                
                
                except Exception as e:
                    print("Cannot find username", e)
                    return False

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def select_data(column: str, condition: str, value):
     if create_conn:

            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    select_query = f"""
                            SELECT {column} FROM {st.secrets["mysql"]["table"]}
                            WHERE {condition} = %s
                            LIMIT 1
                        """

                    db_cursor.execute(select_query, (value,))
                    result = db_cursor.fetchone()

                    if result:
                        print(f"{column} Found")
                        return True, result[0]
                    else:
                        print(f"{column} for {value} Not Found")
                        return False, None
                
                
                except Exception as e:
                    print(f"Cannot find {column} data", e)
                    return False, None

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def update_data(column: str, value, id: int):
     if create_conn:

            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    update_query = f"""
                            UPDATE {st.secrets["mysql"]["table"]}
                            SET {column} = %s
                            WHERE userid = %s
                        """

                    db_cursor.execute(update_query, (value, id))
                    db_conn.commit()

                    return True, f"{column.title()} Updated!"
                
                
                except Exception as e:
                    print(f"Cannot update username", e)
                    return False, "Cannot update username!"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def delete_user(username: str):
     if create_conn:

            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    delete_query = f"""
                            DELETE FROM {st.secrets["mysql"]["table"]}
                            WHERE username = %s
                        """

                    db_cursor.execute(delete_query, (username,))
                    db_conn.commit()

                    return True, f"{username} account Deleted!"
                
                
                except Exception as e:
                    print(f"Cannot delete username", e)
                    return False, "Cannot delete username!"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()





