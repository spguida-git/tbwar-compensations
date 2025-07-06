"""Modulo de compensacion"""
from utils.load_json import open_file

files = open_file()
compensation = files["compensation"]
base_values = files["base_values"]

troops_compensation = 0
rss_compesation = 0

for unidad in compensation:
    if unidad == 'RSS':
        for rss in compensation['RSS']:
            rss_cantidad = compensation['RSS'][rss]
            cantidad = rss_cantidad.get("cantidad", 0)
            nivel = rss_cantidad.get("nivel", 1)
            valor_unidad = base_values.get(unidad, 0)
            rss_resultado = valor_unidad * cantidad
            rss_compesation += rss_resultado
    else:
        for recurso in compensation[unidad]:
            cantidad = recurso.get("cantidad", 0)
            nivel = recurso.get("nivel", 1)
            valor_unidad = base_values.get(unidad, 0)
            resultado = cantidad * valor_unidad * nivel
            troops_compensation += resultado

print(f"rss compesation {rss_compesation}, troops compesation {troops_compensation}, total: ",
      troops_compensation + rss_compesation)
