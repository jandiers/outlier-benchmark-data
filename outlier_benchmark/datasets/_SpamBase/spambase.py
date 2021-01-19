from dataclasses import dataclass

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class SpamBase(BaseDataset):
    """
    The SpamBase dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     |  2934  |
    +-----------------------+--------+
    |number of features:    |  57    |
    +-----------------------+--------+
    |number of outliers:    |  146   |
    +-----------------------+--------+
    |percentage outliers:   |  4.98 %|
    +-----------------------+--------+
    |number of duplicates:  |   261  |
    +-----------------------+--------+


    This dataset has been taken from [1]_. Details and results for benchmark algorithms may also be found there.
    The dataset provided here is a copy of the dataset taken from the
    `accompanying homepage <https://www.dbs.ifi.lmu.de/research/outlier-evaluation/DAMI/>`_.

    No further preprocessing has been applied. The file is named semantic/SpamBase/SpamBase_05_v01.arff in the
    collection of [1]_.

    Usage:

    >>> from outlier_benchmark.datasets import spambase
    >>> X, y = spambase.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape  # (2934, 57)
    >>> y.sum()  # 146, the number of outliers in the dataset
    >>> X.max()  # 9088.0
    >>> X.min()  # 0.0

    ..  [1] On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study
        by G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenkov�, E. Schubert, I. Assent and M. E. Houle
        Data Mining and Knowledge Discovery 30(4): 891-927, 2016, DOI: 10.1007/s10618-015-0444-8

    """

    name: str = 'SpamBase'
    num_samples: int = 2934
    num_features: int = 57
    num_outlier: int = 146
    number_duplicates: int = 261
