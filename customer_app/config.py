import os

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                         'postgresql://shubham:shubham@localhost:5433/customerdb')
SQLALCHEMY_TRACK_MODIFICATIONS = True
JWT_BLACKLIST_ENABLED = True
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
JWT_SECRET_KEY = "SUPER_DUOER_JWT_SECRET"
