from django.core.exceptions import ValidationError

def validar_ci(value):
    if not value.isdigit() or int(value) == 0 or len(value) < 6:
        raise ValidationError("El CI debe tener al menos 6 dígitos numéricos o ser mayor a 0.")
                                                            
def validar_texto(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("El texto no debe contener números.")