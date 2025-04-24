from src.database.postgres import get_connection
import hashlib, re

def convert_sha_512(password):
    return hashlib.sha512(password.encode()).hexdigest()

def is_password_secure(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
    return re.match(pattern, password) is not None

def is_valid_name(name):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.]{2,40}$'
    return re.match(pattern, name) is not None

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email) is not None

def email_exists(email):
    if len(email) <= 320:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute('''
                        SELECT 1 
                        FROM users 
                        WHERE user_email = %s;
                    ''',(email,))
        exists = cursor.fetchone() is not None
        cursor.close()
        db.close()
        return exists
    return False


