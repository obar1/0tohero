# pylint: disable=W0621,W0613

import pytest

from zero_to_one_hundred.configs.config_map import ConfigMap, MAP
from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return ZTOHFactoryProvider(persist_fs, process_fs)


def test_provide__pass(get_factory_provider):
    actual: ConfigMap = get_factory_provider.provide().config_map
    assert actual.get_type == MAP
    assert actual.get_repo_path is not None
    assert actual.get_repo_sorted is False
    assert actual.get_repo_map_md == "0to100.md"
