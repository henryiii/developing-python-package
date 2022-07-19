import example_package

import platform
import pytest


@pytest.fixture(params=["Linux", "Darwin", "Windows"])
def platform_system(request, monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: request.param)
    return request.param


def test_plat(platform_system):
    assert example_package.platform_system() == platform_system
