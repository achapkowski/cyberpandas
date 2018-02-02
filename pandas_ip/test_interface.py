import pytest
from pandas.tests.extension_arrays.base import BaseArrayTests

import pandas_ip as ip


class TestIP(BaseArrayTests):
    @pytest.fixture
    def test_data(self):
        return ip.IPAddress(list(range(100)))


    @pytest.fixture
    def test_data_missing(self):
        return ip.IPAddress([0, 1])

    @pytest.fixture
    def na_cmp(self):
        """Binary operator for comparing NA values.

        Should return a function of two arguments that returns
        True if both arguments are (scalar) NA for your type.

        By defult, uses ``operator.or``
        """
        return lambda x, y: int(x) == int(y) == 0
