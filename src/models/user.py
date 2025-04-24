from src.database.postgres import get_connection
from src.utils.security import convert_sha_512

class User():

    @classmethod
    def login(self, email: str, password: str):
        try:
            db = get_connection()
            cursor = db.cursor()
            cursor.execute('''
                SELECT u.user_code
                FROM users AS u
                JOIN administrators AS a ON a.user_code = u.user_code
                WHERE (u.user_name || u.user_last_name) = %s AND a.administrator_password = %s;
                            ''',(user_name_entered,convert_sha_512(password_entered)))
            
            user = cursor.fetchone()
            

            if user is not None:
                return {"user_code": user[0]}, 200
            return {"user_code": 0}, 401
        except Exception as ex:
            return {"error": f"login error: {str(ex)}"}, 500
        finally:
            cursor.close()
            db.close()
            