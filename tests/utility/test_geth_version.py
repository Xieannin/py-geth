from geth import get_geth_version

import semantic_version


def test_get_geth_version():
    version = get_geth_version()

    assert isinstance(version, semantic_version.Version)
