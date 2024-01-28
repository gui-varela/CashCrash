def calcular_montante(capital: float, taxa: float, dias_passados: int):
  """
    Calcula o montante de um investimento aplicado em juros compostos.

    Args:
        capital (float): O capital (valor inicial do investimento).
        taxa (float): A taxa de juros diária.
        dias_passados (int): O número de dias de capitalização.

    Returns:
        float: O montante total (incluindo o capital e os juros compostos).
    """
  montante = capital * (1 + taxa) ** dias_passados
  return montante