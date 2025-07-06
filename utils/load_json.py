"""Se carga el json"""

from pathlib import Path
import json

def open_file():
    """load entry files"""
    path_base_values = Path("data") / "base_values.json"
    path_compensation = Path("data") / "compensation.json"
    with open(path_base_values, 'r', encoding="utf-8") as open_base_values:
        base_values = json.load(open_base_values)
    with open(path_compensation, 'r', encoding="utf-8") as open_compensation:
        compensation = json.load(open_compensation)
    return {
        "base_values": base_values,
        "compensation": compensation
    }
