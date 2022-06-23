import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xe51F\xff\x1d\x8fM\\rM\xc3\x1cx\x92\x02\x95'
    MONGODB_SETTINGS = {'db':  'UTA_Enrollment'}
