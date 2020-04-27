from wallapopy.src.client import WallapopClient


class TestClient:
    def test_instantiation(self):
        """just checking that client can be instantiated"""
        assert type(WallapopClient()) == WallapopClient
