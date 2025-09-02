from db import connection
import streamlit as st

create_conn = connection.create_connection()

def create_table_books():
    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    db_cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS books
                            (
                                book_id INT PRIMARY KEY AUTO_INCREMENT,
                                title VARCHAR(100) NOT NULL UNIQUE,
                                author VARCHAR(100) NOT NULL,
                                category VARCHAR(50) NOT NULL,
                                total_copies INT NOT NULL,
                                available_copies INT NOT NULL
                            )
                        """
                    )

                    db_conn.commit()
                    print("books table created successfully!")
                
                except Exception as e:
                    print("Cannot create books table", e)

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def create_table_members():
    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    db_cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS members
                            (
                                member_id INT PRIMARY KEY AUTO_INCREMENT,
                                name VARCHAR(100) NOT NULL,
                                email VARCHAR(100),
                                join_date DATE NOT NULL,
                                status ENUM('active', 'inactive')
                            )
                        """
                    )

                    db_conn.commit()
                    print("members table created successfully!")
                
                except Exception as e:
                    print("Cannot create members table", e)

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def create_table_book_issues():
    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                try:
                    db_cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS book_issues
                            (
                                issue_id INT PRIMARY KEY AUTO_INCREMENT,
                                book_id INT NOT NULL,
                                member_id INT NOT NULL,
                                issue_date DATE,
                                due_date DATE,
                                return_date DATE,
                                FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
                                FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
                            )
                        """
                    )

                    db_conn.commit()
                    print("book_issues table created successfully!")
                
                except Exception as e:
                    print("Cannot create book_issues table", e)

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def insert_book(book_title: str,
                book_author: str,
                book_category: str,
                total_copies: int,
                available_copies: int):
     
        if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                insert_books_query = """
                            INSERT INTO books (title, author, category, total_copies, available_copies)
                            VALUES
                            (%s, %s, %s, %s, %s)
                        """

                try:
                    db_cursor.execute(insert_books_query,
                                      (book_title,
                                       book_author,
                                       book_category,
                                       total_copies,
                                       available_copies)
                                       )
                
                    db_conn.commit()
                    print(f"{book_title} book inserted successfully!")
                    return True
                
                except Exception as e:
                    print(f"Cannot add {book_title} book", e)
                    return False

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def insert_member(name: str,
                  email: str,  
                  status: str):

    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                insert_members_query = """
                            INSERT INTO members (name, email, join_date, status)
                            VALUES
                            (%s, %s, CURDATE(), %s)
                        """

                try:
                    db_cursor.execute(insert_members_query,
                                      (name,
                                       email,
                                       status)
                                       )
                
                    db_conn.commit()
                    print(f"{name} member inserted successfully!")
                    return True
                
                except Exception as e:
                    print(f"Cannot add {name} member", e)
                    return False

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db() 
        

def get_book_id(title: str):

    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                get_book_id_query= """
                            SELECT book_id FROM books
                            WHERE title = %s
                        """

                try:
                    db_cursor.execute(get_book_id_query, (title,))
                    result = db_cursor.fetchone()

                    if result:
                        print(f"{title} id fetched successfully!")
                        return True, result[0]
                    else:
                        print(f"Book titled '{title}' not found.")
                        return False, f"Id for '{title}' doesn't exist"
                    
                except Exception as e:
                    print(f"Cannot find {title} id", e)
                    return False, f"Id for {title} doesn't exist"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def get_member_id(email: str):

    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                get_book_id_query= """
                            SELECT member_id FROM members
                            WHERE email = %s
                        """

                try:
                    db_cursor.execute(get_book_id_query, (email,))
                    result = db_cursor.fetchone()

                    if result:
                        print(f"{email} member id fetched successfully!")
                        return True, result[0]
                    else:
                        print(f"'{email}' member not found.")
                        return False, f"Id for '{email}' member doesn't exist"
                    
                except Exception as e:
                    print(f"Error finding {email} member id", e)
                    return False, f"Error finding {email} member id"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()
     

def see_all_books():
    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                select_books_query= """
                            SELECT title, author, category, total_copies, available_copies FROM books
                        """

                try:
                    db_cursor.execute(select_books_query)
                    result = db_cursor.fetchall()

                    if result:
                        print(f"All Books fetched successfully!")
                        return True, result
                    else:
                        print(f"No books found.")
                        return False, "No books found"
                    
                except Exception as e:
                    print(f"Error finding books", e)
                    return False, "Error finding books"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()
     

def see_all_members():
     if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                select_members_query= """
                            SELECT name, email, join_date, status FROM members
                        """

                try:
                    db_cursor.execute(select_members_query)
                    result = db_cursor.fetchall()

                    if result:
                        print(f"All members fetched successfully!")
                        return True, result
                    else:
                        print(f"No members found.")
                        return False, "No members found"
                    
                except Exception as e:
                    print(f"Error finding members", e)
                    return False, "Error finding members"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db()


def issue_book(book_id: int, member_id: int):
     
    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                issue_book_query = """
                            INSERT INTO book_issues 
                            (book_id, member_id, issue_date, due_date, return_date)
                            VALUES
                            (%s, %s, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY), NULL)
                        """
                
                decrement_available_copies_query = """
                            UPDATE books
                            SET available_copies = available_copies - 1
                            WHERE book_id = %s AND available_copies > 0;
                        """

                try:
                    db_cursor.execute(issue_book_query, (book_id, member_id))
                    if db_cursor.rowcount > 0:  # only update if a book was actually returned
                        db_cursor.execute(decrement_available_copies_query, (book_id,))
                
                    db_conn.commit()
                    print(f"{book_id} book id issued successfully!")
                    return True
                
                except Exception as e:
                    print(f"Cannot issue {book_id} book id", e)
                    return False

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db() 


def return_book(book_id, member_id):
    if create_conn:
            db_conn = connection.connect_db()

            if db_conn:
                db_cursor = db_conn.cursor()

                return_book_query = """
                    UPDATE book_issues
                    SET return_date = CURDATE()
                    WHERE member_id = %s AND book_id = %s AND return_date IS NULL;
                """
                increment_available_copies_query = """
                            UPDATE books
                            SET available_copies = available_copies + 1
                            WHERE book_id = %s;
                        """
                
                try:
                    db_cursor.execute(return_book_query, (member_id, book_id))
                    if db_cursor.rowcount > 0:  # only update if a book was actually returned
                        db_cursor.execute(increment_available_copies_query, (book_id,))

                    db_conn.commit()
                    print(f"Book {book_id} returned succesfully")
                    return True, "Book returned successfully!"
                    
                except Exception as e:
                    db_conn.rollback()
                    print(f"Error returning book {book_id}", e)
                    return False, "Error returning book"

                finally:
                    db_cursor.close()

            else:
                db_cursor = connection.reconnect_db() 
    

# def insert(username, password):
#     if create_conn:

#             db_conn = connection.connect_db()

#             if db_conn:
#                 db_cursor = db_conn.cursor()

#                 try:
#                     values = (username, password)
#                     insert_query = f"""
#                             INSERT INTO {st.secrets["mysql"]["table"]}
#                             (username, password)
#                             VALUES
#                             (%s, %s)
#                         """
#                     db_cursor.execute(insert_query, values)

#                     db_conn.commit()
#                     print("Inserted successfully!")
#                     return True
                
                
#                 except Exception as e:
#                     print("Cannot insert", e)
#                     return False

#                 finally:
#                     db_cursor.close()

#             else:
#                 db_cursor = connection.reconnect_db()


# def check_login_credentials(username, password):
#      if create_conn:

#             db_conn = connection.connect_db()

#             if db_conn:
#                 db_cursor = db_conn.cursor()

#                 try:
#                     credentials_query = f"""
#                             SELECT 1 FROM {st.secrets["mysql"]["table"]}
#                             WHERE username = %s AND password = %s
#                             LIMIT 1
#                         """

#                     db_cursor.execute(credentials_query, (username, password))
#                     result = db_cursor.fetchone()

#                     if result:
#                         print("Credentials Validated")
#                         return True, "Credentials Validated"
#                     else:
#                         print("Credentials NOT validated")
#                         return False, "Credentials NOT validated"
                
                
#                 except Exception as e:
#                     print("Cannot find credentials", e)
#                     return False, "Cannot find credentials"

#                 finally:
#                     db_cursor.close()

#             else:
#                 db_cursor = connection.reconnect_db()
         

# def check_username(username):
#      if create_conn:

#             db_conn = connection.connect_db()

#             if db_conn:
#                 db_cursor = db_conn.cursor()

#                 try:
#                     check_username_query = f"""
#                             SELECT username FROM {st.secrets["mysql"]["table"]}
#                             WHERE username = %s
#                             LIMIT 1
#                         """

#                     db_cursor.execute(check_username_query, (username,))
#                     result = db_cursor.fetchone()

#                     if result:
#                         print("Username found")
#                         return True
#                     else:
#                         print("Unique username")
#                         return False
                
                
#                 except Exception as e:
#                     print("Cannot find username", e)
#                     return False

#                 finally:
#                     db_cursor.close()

#             else:
#                 db_cursor = connection.reconnect_db()


# def select_data(column: str, condition: str, value):
#      if create_conn:

#             db_conn = connection.connect_db()

#             if db_conn:
#                 db_cursor = db_conn.cursor()

#                 try:
#                     select_query = f"""
#                             SELECT {column} FROM {st.secrets["mysql"]["table"]}
#                             WHERE {condition} = %s
#                             LIMIT 1
#                         """

#                     db_cursor.execute(select_query, (value,))
#                     result = db_cursor.fetchone()

#                     if result:
#                         print(f"{column} Found")
#                         return True, result[0]
#                     else:
#                         print(f"{column} for {value} Not Found")
#                         return False, None
                
                
#                 except Exception as e:
#                     print(f"Cannot find {column} data", e)
#                     return False, None

#                 finally:
#                     db_cursor.close()

#             else:
#                 db_cursor = connection.reconnect_db()


# def update_data(column: str, value, id: int):
#      if create_conn:

#             db_conn = connection.connect_db()

#             if db_conn:
#                 db_cursor = db_conn.cursor()

#                 try:
#                     update_query = f"""
#                             UPDATE {st.secrets["mysql"]["table"]}
#                             SET {column} = %s
#                             WHERE userid = %s
#                         """

#                     db_cursor.execute(update_query, (value, id))
#                     db_conn.commit()

#                     return True, f"{column.title()} Updated!"
                
                
#                 except Exception as e:
#                     print(f"Cannot update username", e)
#                     return False, "Cannot update username!"

#                 finally:
#                     db_cursor.close()

#             else:
#                 db_cursor = connection.reconnect_db()


# def delete_user(username: str):
#      if create_conn:

#             db_conn = connection.connect_db()

#             if db_conn:
#                 db_cursor = db_conn.cursor()

#                 try:
#                     delete_query = f"""
#                             DELETE FROM {st.secrets["mysql"]["table"]}
#                             WHERE username = %s
#                         """

#                     db_cursor.execute(delete_query, (username,))
#                     db_conn.commit()

#                     return True, f"{username} account Deleted!"
                
                
#                 except Exception as e:
#                     print(f"Cannot delete username", e)
#                     return False, "Cannot delete username!"

#                 finally:
#                     db_cursor.close()

#             else:
#                 db_cursor = connection.reconnect_db()





