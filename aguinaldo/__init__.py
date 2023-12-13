# [MIT] Copyright (C) 2024  Michel Novus

import sys

__version__ = "1.0.0"
APORTE_DE_LEY = 21.5  # Porcentual


def main():
    salarios_mensuales = []
    try:
        with open(sys.argv[1], "rt") as file:
            for line in file.readlines():
                if not line.startswith("#") and line == "":
                    if "#" in line:
                        line = line[: line.index("#")]
                    salarios_mensuales.append(float(line.strip()))
    except (OSError, PermissionError, FileNotFoundError):
        print(f"Problemas al intentar abrir el archivo {sys.argv[1]}")
        sys.exit(1)

    salario_total_neto = sum(salarios_mensuales)
    medio_aguinaldo = salario_total_neto / 12
    # medio_aguinaldo -= medio_aguinaldo * (APORTE_DE_LEY / 100)
    print(f"Medio aguinaldo generado: {round(medio_aguinaldo)}")
