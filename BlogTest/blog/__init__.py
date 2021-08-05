import platform

osName = platform.system()
if (osName == 'Linux'):
    import pymysql
    pymysql.install_as_MySQLdb()