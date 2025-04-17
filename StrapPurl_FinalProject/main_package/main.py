# File Name : main.py
# Student Name: Nathan Sharpe
# email: sharpenn@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/30/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decode a location and movie name and take a group photo holding up a sign with 
# a famous quote from that movie and add logic to display that photo within the project.

# Brief Description of what this module does: Ties together content from throughout the semester in a final group project.
# Citations: gemini.google.com

# Anything else that's relevant:

from location_package.location_decoder import *
from movie_name_package.movie_name_decoder import *
from image_package.image_loader import *

if __name__ == "__main__":
    # Instantiate an object of the WordExtractor class that is responsible for decoding the team location
    LocationDecoder = WordExtractor()

    # Call the print words method to extract the location data from the indices provided 
    LocationDecoder.print_words_from_dictionary("Data/EncryptedGroupHints Spring 2025.json", key="Strap Purl")