from dataclasses import dataclass, field

from outlier_benchmark.datasets.base.dataset import BaseDataset


@dataclass
class Cifar100F(BaseDataset):
    """
    The Cifar100F dataset has the following properties:

    +-----------------------+--------+
    |number of samples:     | 10000  |
    +-----------------------+--------+
    |number of features:    |  320   |
    +-----------------------+--------+
    |number of outliers:    |  0     |
    +-----------------------+--------+
    |percentage outliers:   |  0.0 % |
    +-----------------------+--------+
    |number of duplicates:  |   2    |
    +-----------------------+--------+

    This dataset is used for Out of Distribution Detection. Out of Distribution Detection aims to detect images
    that were not included in the classifier's training data.

    In this case, an [EfficientNet]_ was trained on Cifar100 data. Afterwards, the model has been evaluated on the test
    data of Cifar100. The samples in this dataset contain feature-embeddings after the last convolutional layer of
    the trained EfficientNet.

    Note: All instances here are in-distribution data! Therefore, this dataset only contains inliers,
    and no outliers. There are many choices for out-of-distribution data. They all start with cifar100 and end on 'f',
    which stands for 'features'.

    * cifar100beansf
    * cifar100cifar1000f
    * etc.

    See [MISSING_REF] for details.

    Usage:

    >>> from outlier_benchmark.datasets import cifar100f
    >>> X, y = cifar100f.load(download=True)  # download will only take place if not previously downloaded
    >>> X.shape
    (10000, 320)
    >>> y.sum()  #  the number of outliers in the dataset
    0
    >>> X.max().round(2)
    20.73
    >>> X.min().round(2)
    0.0

    .. [EfficientNet] Tan, Mingxing, and Quoc Le. "Efficientnet: Rethinking model scaling for convolutional neural networks."
       International Conference on Machine Learning. PMLR, 2019.

    .. [MISSING_REF] TODO: add reference

    """

    name: str = field(default='Cifar100F', init=False)
    num_samples: int = field(default=10000, init=False)
    num_features: int = field(default=320, init=False)
    num_outlier: int = field(default=0, init=False)
    num_duplicates: int = field(default=2, init=False)


cifar100f = Cifar100F()