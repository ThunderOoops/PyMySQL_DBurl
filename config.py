class Config:
    DB_URL = "mysql+pymysql://root:password@localhost:3306/flaskdb"
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
