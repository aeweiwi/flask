import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY='you will never get me'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    POSTS_PER_PAGE=3
    #MAIL_SERVER =''
    #MAIL_PROT =''
    #MAIL_USE_TLS =''
    #MAIL_USERNAME =''
    #MAIL_PASSWORD = ''
    #ADMINS = ['email address']
