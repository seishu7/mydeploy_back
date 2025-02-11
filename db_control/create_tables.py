from db_control.mymodels_MySQL import Base  # User, Comment
from db_control.connect_MySQL import engine

import platform
print(platform.uname())


print("Creating tables >>> ")
Base.metadata.create_all(bind=engine)
