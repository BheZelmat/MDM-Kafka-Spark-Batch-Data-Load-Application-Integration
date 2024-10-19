import pytest
from AppLib.utils import get_spark_session


@pytest.fixture(scope='session')
def spark():
    return get_spark_session("LOCAL")


def test_blank(spark):
    print(spark.version)
    assert spark.version == "3.5.3"
