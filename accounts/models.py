from django.contrib.auth.models import AbstractUser
from django.db import models

class Sector(models.Model):
    name = models.CharField('Setor', unique=True, max_length=200)
    users = None

    def to_json(self):
        return{
            'id': self.pk,
            'name': self.name
        }

    def __str__(self) -> str:
        return self.name
    
class CustomUser(AbstractUser):
    cell_phone = models.CharField('celular', max_length=100, blank=True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING, blank=True, null=True)
    theme = models.TextField(null=True, blank=True)
    infos_json = None

    @classmethod
    def get_user(cls, pk: int):
        data_user = CustomUser.objects.get(pk=pk)
        data_user.att_json()
        return data_user

    @classmethod
    def get_users(cls, **kwargs):
        data_users = CustomUser.objects.filter(**kwargs)
        print('ex', data_users)
        for user in data_users:
            user.att_json()
        return data_users
    
    def att_json(self):
        self.infos_json = {
        'id': self.pk,
        'name': f'{self.first_name} {self.last_name}',
        'email': self.email,
        'cell_phone': self.cell_phone,
        'sector': {'id': self.sector.pk, 'name': self.sector.name},
        }

    def __str__(self):
        return self.username
