from django.db import models
from django.conf import settings 

class Computadora(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'En Mantenimiento'),
    ]
    numero = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=50, blank=True)  
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    especificaciones = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"Equipo {self.numero} - {self.nombre or 'Sin nombre'}"

 
class SesionUso(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sesiones')
    computadora = models.ForeignKey(Computadora, on_delete=models.PROTECT)
    inicio = models.DateTimeField(auto_now_add=True)
    fin = models.DateTimeField(blank=True, null=True)
    tiempo_solicitado_minutos = models.PositiveIntegerField(help_text="0 si es tiempo libre o fraccionado")
    pagado = models.BooleanField(default=False)
    total_a_pagar = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Sesión {self.id} - Usuario: {self.usuario.username} en PC {self.computadora.numero}"

class Tarifa(models.Model):
    nombre = models.CharField(max_length=50) 
    precio_por_hora = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} (${self.precio_por_hora}/h)"
    
class Juego(models.Model):
    CATEGORIAS = [
        ('shooter', 'Shooter / FPS'),
        ('moba', 'MOBA'),
        ('carreras', 'Carreras'),
        ('deportes', 'Deportes'),
        ('estrategia', 'Estrategia'),
    ]
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS, default='shooter')
    requiere_cuenta_propia = models.BooleanField(default=False)
    computadoras = models.ManyToManyField(Computadora, related_name='juegos', blank=True)

    def __str__(self):
        return self.nombre
