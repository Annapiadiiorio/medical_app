from django.db import models

class Patient(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    eta = models.IntegerField()
    genere = models.CharField(max_length=1, choices=[('M', 'Maschio'), ('F', 'Femmina')])
    
    tipologia = models.CharField(
        max_length=100,
        choices=[
            ('Ambulatoriale', 'Ambulatoriale'),
            ('Ricoverato', 'Ricoverato')
        ],
        default='Ambulatoriale'
    )
    diagnosi = models.CharField(max_length=200)
    modalita_diagnosi = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome} {self.cognome}"


class Exam(models.Model):
    paziente = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='esami')
    nome_esame = models.CharField(max_length=100)
    appropriato = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome_esame} ({'Appropriato' if self.appropriato else 'Non appropriato'})"
