from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    id_paciente = models.CharField(max_length=8)

    def __str__(self):
        return self.nome

class Enfermeiro(models.Model):
    nome = models.CharField(max_length=100)
    id_funcionario = models.CharField(max_length=11)
    turno = models.CharField(max_length=8)    

    def __str__(self):
        return self.nome
