import numpy as np


def count_species(features: np) -> int:
    """
    Conta o número de espécies com base nas características fornecidas.

    Parameters:
        features: A entrada que representa as características da imagem.

    Returns:
        O número de espécies presentes nas características.

    Raises:
        ValueError: Se o tipo de características não for suportado (não é uma matriz NumPy).

    Examples:
    >>> import numpy as np
    >>> features = np.array([1, 2, 3, 1, 2, 3, 4])
    >>> count_species(features)
    4
    """
    if isinstance(features, np.ndarray):

        unique_species = np.unique(features)
        num_species = len(unique_species)

        return num_species
    else:
        raise ValueError('Tipo de características não suportado.')
