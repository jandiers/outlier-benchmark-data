from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Hepatitis(BaseDataset):
    """
    The Hepatitis dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |    70  |
    +-----------------------+--------+
    |number of features:    |   19   |
    +-----------------------+--------+
    |number of outliers:    |    3   |
    +-----------------------+--------+
    |percentage outliers:   |  4.29 %|
    +-----------------------+--------+
    |number of duplicates:  |    0   |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/Hepatitis/Hepatitis_withoutdupl_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import hepatitis
    >>> X, y = hepatitis.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (70, 19)
    >>> y.sum()
    3
    >>> X.max()
    420.0
    >>> X.min()
    0.0

    ..  [1] Campos, G.O., Zimek, A., Sander, J. et al. On the evaluation of unsupervised outlier detection: measures,
        datasets, and an empirical study. Data Min Knowl Disc 30, 891–927 (2016).
        https://doi.org/10.1007/s10618-015-0444-8

    """

    name: str = field(default='Hepatitis', init=False)
    num_samples: int = field(default=70, init=False)
    num_features: int = field(default=19, init=False)
    num_outlier: int = field(default=3, init=False)
    num_duplicates: int = field(default=0, init=False)


hepatitis = Hepatitis()
