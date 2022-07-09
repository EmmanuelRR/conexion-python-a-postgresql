
class usuario:
    def __init__(self, id=None, user=None, passw=None):
        self._id=id
        self._user= user
        self._passw= passw
    def __str__(self):
        return f'usuario: {self._id} , {self._user}, {self._passw}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id=id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def passw(self):
        return self._passw

    @passw.setter
    def passw(self, passw):
        self._passw = passw


if __name__=='__main__':
    Usuario=usuario(id=2,user='rxn', passw='coldplay')
    print(Usuario.id)