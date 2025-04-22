from cryptography.fernet import Fernet
import json

class MovieDecryptor:
    """
    A class to decrypt an encrypted movie title for a specific team using a provided Fernet key.
    """

    def __init__(self, team_name, encrypted_file_path, fernet_key_str):
        """
        Initializes the MovieDecryptor with team information and decryption key.
        @param team_name: The name of the team whose movie title is to be decrypted.
        @param encrypted_file_path: Path to the JSON file containing encrypted messages.
        @param fernet_key_str: The Fernet key as a string used for decryption.
        """
        self.team_name = team_name
        self.encrypted_file_path = encrypted_file_path
        self.fernet_key = fernet_key_str.encode()