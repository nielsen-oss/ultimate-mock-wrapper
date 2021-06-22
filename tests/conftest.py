from __future__ import annotations
from unittest.mock import MagicMock

from pytest import fixture

from ultimate_mock_wrapper import MockWrapper


@fixture
def mock_wrapper() -> MockWrapper:
    return MockWrapper(MagicMock())
