#image-loader.py
# Student Name: Zach Bell
# email: bellzj@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/30/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decrypt a location and movie name and take a group photo holding up a sign with 
# a famous quote from that movie and add code to display that photo within the project.

# Brief Description of what this module does: Ties together content from throughout the semester in a final group project.
# Citations: gemini.google.com chatgpt 

# Anything else that's relevant:

from PIL import Image
import os

class PhotoLoader:
    """
    A class to load and display an image from a specified package and file name.
    """
    def __init__(self, package_name: str, file_name: str):
        """
        Initializes the PhotoLoader with the package name and file name.
        @param package_name string: The name of the package where the image is located.
        @param file_name string: The name of the image file to load.
        @return: None
        """
        self.package_name = package_name
        self.file_name = file_name
        self.image = None

    def load_image(self):
        """
        Loads the image from the specified package and file name.
        @return: None
        """
        image_path = os.path.join(self.package_name, self.file_name)
        try:
            self.image = Image.open(image_path)
            self.image = self.image.rotate(-90, expand=True)  # Rotate 90° clockwise
            print(f"Image loaded and rotated successfully from {image_path}")
        except FileNotFoundError:
            print(f"Error: File {image_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_image(self):
        """
        Displays the loaded image.  
        @return: None
        """
        if self.image:
            self.image.show()
        else:
            print("Image not loaded yet.")



