# File Name : location_decoder.py
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

import re # Import regular expressions module for better word splitting
import os # Import os module to handle file paths
import json # Import json module to work with JSON files

class WordExtractor:
    """
    A class to read a fixed text file ('Data/UCEnglish.txt'), extract words into a list
    (treating words with apostrophes and hyphens as single units), and retrieve words based
    on values from a dictionary. Words are split by whitespace and common punctuation
    (except internal apostrophes and hyphens).
    """

    def __init__(self):
        """
        Initializes the WordExtractor instance.
        The file path for the text file is fixed to "Data/UCEnglish.txt".
        """
        # Hardcoded file path for the text file
        self.text_file_path = os.path.join("Data", "UCEnglish.txt")
        self.words = []
        self._load_words()

    def _load_words(self):
        """
        Private method to load and process words from the fixed text file path.
        Handles potential file errors and treats words with internal apostrophes
        and hyphens as single units.
        """
        try:
            # Ensure the file exists before trying to open it
            print(f"Attempting to load words from: '{self.text_file_path}'")
            if not os.path.exists(self.text_file_path):
                # Provide a more helpful error message if the directory doesn't exist
                if not os.path.exists(os.path.dirname(self.text_file_path)):
                     raise FileNotFoundError(f"Error: Directory '{os.path.dirname(self.text_file_path)}' not found.")
                raise FileNotFoundError(f"Error: File not found at '{self.text_file_path}'. "
                                        f"Please ensure the file exists in the correct location.")

            with open(self.text_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Convert to lowercase for consistency
                content_lower = content.lower()
                # Use regex to find sequences of letters, numbers, apostrophes, and hyphens.
                # This treats words like "don't", "it's", or "well-being" as single words.
                # It effectively splits on spaces and other punctuation.
                self.words = re.findall(r"[a-z0-9'-]+", content_lower)

                print(f"Successfully loaded {len(self.words)} words from '{self.text_file_path}'.")

        except FileNotFoundError as e:
            print(e)
            self.words = [] # Ensure words list is empty if file not found
        except IOError as e:
            print(f"Error reading file {self.text_file_path}: {e}")
            self.words = [] # Ensure words list is empty on IO error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.words = []

    def get_words_from_indices(self, index_source):
        """
        Retrieves words from the stored list based on values from a dictionary.
        @param index_source dict: A dictionary where the values are integer indices
                                  specifying which words to retrieve.
        @return list: A list containing the words corresponding to the valid indices
                      found in the dictionary values, or an empty list if no valid
                      indices are found or if the words list is empty.
        """
        if not self.words:
            # Check if the file path exists to give a more specific warning
            if not os.path.exists(self.text_file_path):
                 print(f"Warning: Word list is empty because the file '{self.text_file_path}' was not found or couldn't be read.")
            else:
                 print("Warning: Word list is empty. Cannot retrieve words.")
            return []

        result_words = []
        max_index = len(self.words) - 1

        if isinstance(index_source, dict):
            indices_to_check = index_source.values()
        elif isinstance(index_source, list):
            indices_to_check = index_source
        else:
            print(f"Warning: Input 'index_source' must be a dictionary or a list. Received '{type(index_source).__name__}'. Skipping.")
            return []

        for index_value in indices_to_check:
            if isinstance(index_value, int) and 0 <= index_value <= max_index:
                result_words.append(self.words[index_value])
            elif isinstance(index_value, int):
                print(f"Warning: Index {index_value} from the dictionary is out of bounds (valid range: 0-{max_index}). Skipping.")
            else:
                print(f"Warning: Value '{index_value}' in the dictionary is not a valid integer index. Skipping.")

        return result_words

    def print_words_from_dictionary(self, dictionary_path, key=None):
        """
        Loads a dictionary from a JSON file and prints words based on integer
        values (or integer values within lists) in the dictionary.
        @param dictionary_path str: The path to the JSON file.
        @param key str (optional): If provided, only the value (which should be a
                                   list of strings representing integers) associated
                                   with this key will be used as indices. If None,
                                   all values in the dictionary (which should be
                                   lists of strings representing integers) will be used.
        @return None
        """
        try:
            print(f"Attempting to load dictionary from: '{dictionary_path}'")
            with open(dictionary_path, 'r') as f:
                data = json.load(f)
                print(f"Successfully loaded dictionary from '{dictionary_path}'.")

                indices_to_process = []

                if key:
                    if key in data:
                        value = data[key]
                        if isinstance(value, list):
                            for item in value:
                                try:
                                    index = int(item)
                                    indices_to_process.append(index)
                                except ValueError:
                                    print(f"Warning: Could not convert '{item}' in key '{key}' to an integer. Skipping.")
                        else:
                            print(f"Warning: Value for key '{key}' is not a list. Skipping.")
                    else:
                        print(f"Warning: Key '{key}' not found in the dictionary.")
                else:
                    for value in data.values():
                        if isinstance(value, list):
                            for item in value:
                                try:
                                    index = int(item)
                                    indices_to_process.append(index)
                                except ValueError:
                                    print(f"Warning: Could not convert '{item}' in a value to an integer. Skipping.")
                        else:
                            print(f"Warning: A value in the dictionary is not a list. Skipping.")

                if indices_to_process:
                    selected_words = self.get_words_from_indices(indices_to_process)
                    print("\nSelected words from dictionary values:")
                    if selected_words:
                        print(" ".join(selected_words))
                    else:
                        print("No valid words found for the processed indices.")
                else:
                    print("No valid integer indices found in the dictionary values.")

        except FileNotFoundError:
            print(f"Error: Dictionary file not found at '{dictionary_path}'.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{dictionary_path}'. Please ensure it's a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred while processing the dictionary: {e}")
