import binascii
from os import urandom
from pathlib import Path
from typing import Optional

from cosmpy.common.loggers import get_logger
from cosmpy.crypto.address import Address
from cosmpy.crypto.keypairs import PrivateKey

_logger = get_logger(__name__)


class CosmosCrypto:
    """
    Class that represents user on a blockchain.
    Hold private key to one user and can sign transactions.
    """

    def __init__(
        self,
        private_key_str: Optional[str] = None,
        private_key: Optional[PrivateKey] = None,
        keyfile_path: Optional[str] = None,
        prefix: str = "fetch",
        account_number: Optional[int] = None,
    ):
        """
        Init ledger crypto key.

        :param private_key: Optional Cosmos PrivateKey instance
        :param private_key_str: Optional hex string representing Cosmos PrivateKey
        :param keyfile_path: Optional path to private key file
        :param prefix: Cosmos string addresses prefix
        :param account_number: optional account number.
        """

        if private_key is not None:
            self.private_key = private_key
        elif private_key_str is not None:
            self.private_key = CosmosCrypto._load_key_from_str(private_key_str)
        elif keyfile_path is not None:
            self.private_key = CosmosCrypto._load_key_from_file(keyfile_path)
        else:
            self.private_key = CosmosCrypto._generate_key()

        self.prefix = prefix
        self.account_number = account_number

    @staticmethod
    def _load_key_from_str(key_str: str) -> PrivateKey:
        """
        Load private key from string

        :return: Private key
        """

        return PrivateKey(bytes.fromhex(key_str))

    @staticmethod
    def _load_key_from_file(keyfile_path: str) -> PrivateKey:
        """
        Load private key from file

        :return: Private key
        """

        return CosmosCrypto._load_key_from_str(Path(keyfile_path).read_text())

    @staticmethod
    def _generate_key() -> PrivateKey:
        """
        Generate random private key

        :return: Private key from random hex string
        """

        key_str = binascii.b2a_hex(urandom(32)).decode("utf-8")
        return CosmosCrypto._load_key_from_str(key_str)

    def get_address(self) -> str:
        """
        Get address.

        :return: address as str
        """

        return str(Address(self.private_key, prefix=self.prefix))

    def get_pubkey_as_str(self) -> str:
        """
        Get public key as string.

        :return: public key as str
        """
        return self.private_key.public_key

    def get_pubkey_as_bytes(self) -> bytes:
        """
        Get public key as bytes.

        :return: public key as bytes
        """
        return self.private_key.public_key_bytes

    def save_key_to_file(self, filename: str):
        """
        Save private key to file.

        :param filename: str, path to file to save key
        """
        Path(filename).write_text(self.as_str())

    def as_str(self) -> str:
        """
        Get private key as string.

        :return: str
        """
        return self.private_key.private_key_hex

    def __bytes__(self) -> bytes:
        """
        Get private key as bytes.

        :return: bytes
        """
        return self.private_key.private_key_bytes
