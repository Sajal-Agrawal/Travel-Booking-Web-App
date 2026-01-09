# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:77033pp04@localhost/ai_travel_agency'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'  # Replace with a secure key (e.g., secrets.token_hex(16))