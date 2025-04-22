# File Name : location_decoder.py
# Student Name: Evan Bolin and Ian McDaniel
# email: bolinen@mail.uc.edu and mcdanip@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/30/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decode a location and movie name and take a group photo holding up a sign with 
# a famous quote from that movie and add logic to display that photo within the project.

# Brief Description of what this module does: Ties together content from throughout the semester in a final group project.
# Citations: https://openai.com/chatgpt/

# Anything else that's relevant: The cryptography package is required for the code to run

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
    
    def decrypt_movie_title(self):
        """
        Decrypts the movie title for the specified team using the provided Fernet key.
        @return: The decrypted movie title as a string.
        """
        with open(self.encrypted_file_path, 'r') as f:
            encrypted_data = json.load(f)

        encrypted_message = encrypted_data[self.team_name][0].encode()
        fernet = Fernet(self.fernet_key)
        decrypted = fernet.decrypt(encrypted_message).decode()
        return decrypted
