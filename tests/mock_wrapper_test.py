from __future__ import annotations
from unittest.mock import MagicMock
from pytest import mark
from ultimate_mock_wrapper import MockWrapper

FORWARD_KEY = "encrypt"
BACK_KEY = "decrypt"


# noinspection PyTypeChecker


@mark.unittest
class TestMockWrapper:
    def test_all_instances(self, mock_wrapper: MockWrapper) -> None:
        all_instances = MockWrapper.all_instances()
        assert len(all_instances) == 1
        assert all_instances[0] == mock_wrapper

    def test_by_id(self, mock_wrapper: MockWrapper) -> None:
        by_id = MockWrapper.get_by_id(mock_wrapper.id)
        assert by_id == mock_wrapper

    def test_is_id_exist(self, mock_wrapper: MockWrapper) -> None:
        assert MockWrapper.is_id_exist(mock_wrapper.id)

    def test_change_id(self, mock_wrapper: MockWrapper) -> None:
        new_id = 555
        MockWrapper.change_id(old_id=mock_wrapper.id, new_id=new_id)
        by_id = MockWrapper.get_by_id(new_id)
        assert by_id == mock_wrapper

    def test_by_mock(self) -> None:
        mock = MagicMock()
        wrapper = MockWrapper(mock)
        by_mock = MockWrapper.get_by_mock(mock)
        assert by_mock == wrapper

    def test_clear_cache(self, mock_wrapper: MockWrapper) -> None:
        assert len(MockWrapper.all_instances()) > 0
        MockWrapper.clear_all_cache()
        assert len(MockWrapper.all_instances()) == 0
