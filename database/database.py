from .model import Users

def getUsers():
    return Users.query.all()



