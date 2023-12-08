import numpy as np


def species_richness(hist: np) -> int:
    """
    Conta o número de espécies de uma imagem com base em um histograma fornecido.

    Parameters:
        hist: A entrada que representa o histograma da imagem.

    Returns:
        O número de espécies presentes no histograma.

    Raises:
        ValueError: Se o tipo de características não for suportado (não é uma array NumPy).

    Examples:
        >>> import numpy as np
        >>> hist = np.array([1, 2, 3, 1, 2, 3, 4])
        >>> species_richness(hist)
        7
    """
    if not isinstance(hist, np.ndarray):
        raise ValueError('Unsupported data type')

    return len(hist)


def taxonomic_distinction(hist: np) -> int:
    """
    Calcula o índice de distinção taxonômica.

    O índice de distinção taxonômica (∆∗) calcula a distância taxonômica média entre dois indivíduos de espécies diferentes

    Args:
      hist: Histograma de abundância de espécies.

    Returns:
      O índice de distinção taxonômica.

    Raises:
        ValueError: Se o tipo de características não for suportado (não é uma array NumPy).

    Examples:
        >>> import numpy as np
        >>> hist = np.array([10, 20, 30])
        >>> taxonomic_distinction(hist)
        0.7777777777777778
    """

    if not isinstance(hist, np.ndarray):
        raise ValueError('Unsupported data type')

    richness = species_richness(hist)

    taxonomic_diversity_distancies = []
    individual_number_products = []

    for i in range(richness):
        taxonomic_distance = 0
        individual_number_product = 0
        for j in range(richness):
            dist = abs(i - j)
            taxonomic_distance += dist * hist[i] * hist[j]
            individual_number_product += hist[i] * hist[j]

        taxonomic_diversity_distancies.append(taxonomic_distance)
        individual_number_products.append(individual_number_product)

    taxonomic_diversity = np.sum(taxonomic_diversity_distancies) / (
        np.sum(individual_number_products)
    )

    return taxonomic_diversity


def taxonomic_diversity(hist: np) -> int:
    """
    Calcula o índice de diversidade taxonômica.

    O índice de diversidade taxonômica (∆) calcula a distância taxonômica média entre dois indivíduos escolhidos aleatoriamente em uma comunidade

    Args:
      hist: Histograma de abundância de espécies.

    Returns:
        O índice de diversidade taxonômica.

    Examples:
        >>> import numpy as np
        >>> hist = np.array([10, 20, 30])
        >>> taxonomic_diversity(hist)
        1.5819209039548023
    """

    if not isinstance(hist, np.ndarray):
        raise ValueError('Unsupported data type')

    num_species = species_richness(hist)

    taxonomic_diversity_distancies = []
    for i in range(num_species):
        taxonomic_distance = 0
        for j in range(num_species):
            dist = abs(i - j)
            taxonomic_distance += dist * hist[i] * hist[j]

        taxonomic_diversity_distancies.append(taxonomic_distance)

    total_number_species = np.sum(hist)

    taxonomic_diversity = (
        2
        * np.sum(taxonomic_diversity_distancies)
        / (total_number_species * (total_number_species - 1))
    )

    return taxonomic_diversity
