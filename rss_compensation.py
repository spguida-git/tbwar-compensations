"""calculo de compesacion para los RSS"""
from utils.load_json import open_file

def calc_rss():
    """se obtienen los recursos para completar la compesacion"""
    files = open_file()
    compensation = files["compensation"]
    rss_values = {}
    for rss in compensation['RSS']:
        rss_cantidad = compensation['RSS'][rss].get("cantidad", 0)
        rss_values[rss] = rss_cantidad
    return rss_values
