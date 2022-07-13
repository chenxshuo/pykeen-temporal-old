# -*- coding: utf-8 -*-

"""Temporal KG Datasets, including ICEWS14, ICEWS11-14, GDELTm10."""

from .base import PathDataset


class ICEWS14(PathDataset):
    def __init__(self, create_inverse_triples: bool = False, **kwargs):
        """Initialize the Nations dataset.

        :param create_inverse_triples: Should inverse triples be created? Defaults to false.
        :param kwargs: keyword arguments passed to :class:`pykeen.datasets.base.PathDataset`.
        """
        super().__init__(
            training_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/icews14/train.txt",
            testing_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/icews14/test.txt",
            validation_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/icews14/valid.txt",
            create_inverse_triples=create_inverse_triples,
            **kwargs,
        )

class ICEWS11to14(PathDataset):
    def __init__(self, create_inverse_triples: bool = False, **kwargs):
        """Initialize the Nations dataset.

        :param create_inverse_triples: Should inverse triples be created? Defaults to false.
        :param kwargs: keyword arguments passed to :class:`pykeen.datasets.base.PathDataset`.
        """
        super().__init__(
            training_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/icews11-14/train.txt",
            testing_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/icews14/test.txt",
            validation_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/icews14/valid.txt",
            create_inverse_triples=create_inverse_triples,
            **kwargs,
        )

class GDELTm10(PathDataset):
    def __init__(self, create_inverse_triples: bool = False, **kwargs):
        """Initialize the Nations dataset.

        :param create_inverse_triples: Should inverse triples be created? Defaults to false.
        :param kwargs: keyword arguments passed to :class:`pykeen.datasets.base.PathDataset`.
        """
        super().__init__(
            training_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/gdeltm10/train.txt",
            testing_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/gdeltm10/test.txt",
            validation_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/gdeltm10/valid.txt",
            create_inverse_triples=create_inverse_triples,
            **kwargs,
        )

class SmallSample(PathDataset):
    def __init__(self, create_inverse_triples: bool = False, **kwargs):
        """Initialize the Nations dataset.

        :param create_inverse_triples: Should inverse triples be created? Defaults to false.
        :param kwargs: keyword arguments passed to :class:`pykeen.datasets.base.PathDataset`.
        """
        super().__init__(
            training_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/small_sample/train.txt",
            testing_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/small_sample/train.txt",
            validation_path="/home/wiss/zhang/.data/pykeen-temporal/datasets/small_sample/train.txt",
            create_inverse_triples=create_inverse_triples,
            **kwargs,
        )