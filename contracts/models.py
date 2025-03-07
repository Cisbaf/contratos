from django.db import models
from accounts.models import CustomUser, Sector
import datetime

class Contract(models.Model):
    number_contract = models.CharField('Numero do Contrato', max_length=200)
    number_process = models.CharField('Numero do Processo', max_length=200)
    object = models.TextField('Objeto de Contrato')
    company = models.CharField('Empresa', max_length=200)
    cnpj_cpf = models.CharField('CNPJ/CPF', max_length=200)
    value_global = models.CharField('Valor Global', max_length=200)
    value_mensal = models.CharField('Valor Mensal', max_length=200)
    fiscais = models.ManyToManyField(CustomUser, blank=True, null=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    font = models.CharField('Fonte de Recurso', max_length=200, blank=True, null=True)
    ta = models.CharField('TA',
                        null=True,
                        blank=True,
                        max_length=200,
                        choices=(('1', 'TA 1'), ('2', 'TA 2'), ('3', 'TA 3'), ('4', 'TA 4'), ('5', 'TA 5'), ('6', 'TA 6')))
    diference = None
    infos_json = None

    def att_json(self):
        fiscais = self.fiscais.all()
        for fiscal in fiscais:
            fiscal.att_json()

        self.infos_json = {
            'id': self.pk,
            'number_contract': self.number_contract,
            'number_process': self.number_process,
            'object': self.object,
            'company': self.company,
            'cnpj_cpf': self.cnpj_cpf,
            'value_global': self.value_global,
            'value_mensal': self.value_mensal,
            'fiscais': [fiscal.infos_json for fiscal in fiscais],
            'start_date': self.start_date.strftime("%d/%m/%Y"),
            'end_date': self.end_date.strftime("%d/%m/%Y"),
            'ta': self.ta if self.ta else '--',
            'font': self.font,
        }


    def __str__(self) -> str:
        return self.object

