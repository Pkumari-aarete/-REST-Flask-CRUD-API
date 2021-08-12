from configparser import ConfigParser
config=ConfigParser()

config['DEFAULT']={
    'SQLALCHEMY_DATABASE_URI' : 'sqlite:///test.db',
    'SECRET_KEY':'supersecretsecret',
}

with open('./config.ini','w') as f:
    config.write(f)