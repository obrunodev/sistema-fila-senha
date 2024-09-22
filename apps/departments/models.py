from apps.users.models import User
from core.models import BaseModel
from django.db import models


class Department(BaseModel):
    name = models.CharField('Nome do departamento', max_length=100)
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.name


class Table(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    table_number = models.SmallIntegerField('Número da mesa')
    active = models.BooleanField('Mesa está ativa?', default=True)

    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
    
    def __str__(self):
        return '%s - Mesa %s' % (
            self.department.name,
            self.table_number,
        )


class Queue(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    queue_number = models.SmallIntegerField('Número da senha')
    is_priority = models.BooleanField('Preferencial?', default=False)

    class Meta():
        verbose_name = 'Senha'
        verbose_name_plural = 'Senhas'
    
    def __str__(self):
        return '%s%s' % (
            'N' if not self.is_priority else 'P',
            self.queue_number,
        )
