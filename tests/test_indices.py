import numpy as np
import pytest

from phylogenetic_indices.indices import (
    extensive_quadratic_entropy,
    species_richness,
    taxonomic_distinction,
    taxonomic_diversity,
)


def test_species_richness_error():
    hist_list = [0, 5, 8, 0, 3]

    with pytest.raises(ValueError, match='Unsupported data type'):
        species_richness(hist_list)


def test_taxonomic_distinction_error():
    hist_list = [0, 5, 8, 0, 3]

    with pytest.raises(ValueError, match='Unsupported data type'):
        taxonomic_distinction(hist_list)


def test_taxonomic_diversity_error():
    hist_list = [0, 5, 8, 0, 3]

    with pytest.raises(ValueError, match='Unsupported data type'):
        taxonomic_diversity(hist_list)


def test_extensive_quadratic_entropy_error():
    hist_list = [0, 5, 8, 0, 3]

    with pytest.raises(ValueError, match='Unsupported data type'):
        extensive_quadratic_entropy(hist_list)
