from .models import *

class User_GroupManager(models.Manager):
    def Owen(self, pk):
        names=[]
        #query = "select auth_user.email, accounts_user_group.name from accounts_user_group_users LEFT JOIN auth_user on accounts_user_group_users.user_id = auth_user.id LEFT JOIN accounts_user_group ON accounts_user_group_users.user_group_id = accounts_user_group.id WHERE auth_user.id = " +str(pk) + ";"
        obj = self.all()
        for i in obj:
            names.append(i.users)
        return names
