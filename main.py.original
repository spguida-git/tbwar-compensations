"""Modulo de compensacion"""

import json

with open('base_values.json', 'r') as base_values_file:
    values_file = json.load(base_values_file)

with open('compensation.json', 'r') as file:
    compensation_file = json.load(file)

compensation = 0
rss_compesation = 0

for unidad in compensation_file:
    if unidad == 'RSS':
        for rss in compensation_file['RSS']:
            rss_cantidad = compensation_file['RSS'][rss]
            cantidad = rss_cantidad.get("cantidad", 0)
            nivel = rss_cantidad.get("nivel", 1)
            valor_base = values_file.get(unidad, 0)
            rss_resultado = valor_base * cantidad
            rss_compesation += rss_resultado
    else:
        for recurso in compensation_file[unidad]:
            cantidad = recurso.get("cantidad", 0)
            nivel = recurso.get("nivel", 1)
            valor_base = values_file.get(unidad, 0)
            resultado = cantidad * valor_base * nivel
            compensation += resultado

print(f"rss compesation {rss_compesation}, compesation {compensation}, total: ",
      compensation + rss_compesation)
