from src.database.postgres import get_connection
import bcrypt, re

def convert_bcrypt(password_entered):
    hashed_password = bcrypt.hashpw(password_entered.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode()

def validate_password(password_entered, password_recovered):
    return bcrypt.checkpw(password_entered.encode('utf-8'), password_recovered.encode('utf-8'))

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


