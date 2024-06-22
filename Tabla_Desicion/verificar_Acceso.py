def verificar_acceso(es_admin, tiene_permisos, hora, es_dia_laboral):
    if es_admin:
        return "Acceso permitido"
    elif tiene_permisos and es_dia_laboral and (9 <= hora <= 17):
        return "Acceso permitido"
    else:
        return "Acceso denegado"

# Pruebas de tabla de decisión
pruebas = [
    (True, False, 10, True),
    (False, True, 10, True),
    (False, True, 18, True),
    (False, False, 10, True),
    (False, True, 10, False),
    (False, True, 8, True),
    (True, True, 15, False)
]

for es_admin, tiene_permisos, hora, es_dia_laboral in pruebas:
    resultado = verificar_acceso(es_admin, tiene_permisos, hora, es_dia_laboral)
    print(f"Admin: {es_admin}, Permisos: {tiene_permisos}, Hora: {hora}, Día Laboral: {es_dia_laboral} - Resultado: {resultado}")
