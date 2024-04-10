# [MIT] Copyright (C) 2024  Michel Novus

import unittest
from typing import NewType, List

__version__ = "2.0.0"

Sueldo = NewType("Sueldo", float)
AguinaldoNominal = NewType("AguinaldoNominal", float)


class TipoSueldoError(Exception):
    def __str__(self) -> str:
        respuesta = ""
        if self.args[0]:
            respuesta = f"El valor '{self.args[0]}' no es válido!"
        elif self.args[1]:
            respuesta = f"El valor '{self.args[0]}' no es válido, se esperaba '{self.args[1]}'"
        else:
            respuesta = "Tipo de Sueldo no válido"
        return respuesta


def colectar_salarios_mensuales(contenido_archivo: str) -> List[Sueldo]:
    """Colecta los valores de `contenido_archivo`.

    Es función falible:
      - `TipoSueldoError` si algún valor de entrada es inválido
      - `OverflowError` la lista resultante tiene más de 12 valores
    """
    sueldos: List[Sueldo] = []
    for valor in map(str.strip, contenido_archivo.split("\n")):
        if len(sueldos) > 12:
            raise OverflowError(
                "No tiene sentido más de doce remuneraciones. (ver ley Nº 12.840, art 2)"
            )
        if not valor.startswith("#") and valor != "":
            try:
                sueldos.append(Sueldo(float(valor)))
            except Exception:
                raise TipoSueldoError(valor, "un número")
    return sueldos


def calcular_aguinaldo_nominal_anual(
    sueldos: List[Sueldo],
) -> AguinaldoNominal:
    """Calcula el valor del aguinaldo anual resultante de la lista de
    sueldos (ley Nº 12.840).

    Función falible:
      - `OverflowError` si hay más de 12 sueldos listados
    """
    return AguinaldoNominal(0)


def calcular_aguinaldo_nominal_complementario(
    sueldos: List[Sueldo],
) -> AguinaldoNominal:
    """Calcula el valor del aguinaldo complementario resultante de la
    lista de sueldos (ley Nº 14.525).

    Función falible:
      - `OverflowError` si hay más de 6 sueldos listados
    """
    return AguinaldoNominal(0)


def main():
    pass


class TestCore(unittest.TestCase):
    def test_colectar_salarios_mensuales(self):
        script_1 = """
            # Primera línea, debe ignorarse.
            # Ésta también

            22.5
            55
            1

            0.2
            44.2452
            # Valor intermedio inútil
            33.1


        """
        self.assertEqual(
            colectar_salarios_mensuales(script_1),
            [22.5, 55, 1, 0.2, 44.2452, 33.1],
        )
        script_2 = "cadena random 123\n44"
        self.assertRaises(
            TipoSueldoError, colectar_salarios_mensuales, script_2
        )
        script_3 = """
            
            
            1
            4 # comentario ilegal
        """
        self.assertRaises(
            TipoSueldoError, colectar_salarios_mensuales, script_3
        )
