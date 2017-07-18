from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from ScholarConfig.config import DB_CONFIG
server = SSHTunnelForwarder(
        ('13.113.193.188',22),
        ssh_username="ubuntu",
        ssh_pkey="C:/Users/tonylu/Desktop/eb-web(1).pem",
        remote_bind_address=('localhost',3306)
        )
server.start()

print(server.local_bind_port)
enginee = create_engine("mysql+pymysql://root:root@localhost:{}/eb".format(server.local_bind_port))
Session=sessionmaker(bind=enginee)
b=Session()
c=b.execute("select * from groups")
print(c.)