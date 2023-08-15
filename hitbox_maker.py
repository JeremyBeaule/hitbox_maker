import cv2
import numpy as np
import json
import os

# Paths
MAIN_DIRECTORY_PATH = r"C:\Users\jerem\Desktop\code\Speedyllique\GOKU"

def get_contours(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Convert image to binary using thresholding
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours

def contours_to_polygons(contours, epsilon_factor=0.005):
    polygons = []
    
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = epsilon_factor * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Flatten the list and convert it to a list of coordinates
        polygon = [int(coord) for point in approx for coord in point[0]]
        polygons.append(polygon)
    
    return polygons

def process_directory(directory_path):
    # Get all image files in the directory
    image_files = [f for f in os.listdir(directory_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    image_polygons = {}
    for idx, image_file in enumerate(image_files):
        img_path = os.path.join(directory_path, image_file)
        contours = get_contours(img_path)
        polygons = contours_to_polygons(contours)
        image_polygons[str(idx)] = [{"shape": polygon} for polygon in polygons if len(polygon) >= 4]
    
    # Save polygons to JSON
    output_file_path = os.path.join(directory_path, "data.json")
    with open(output_file_path, "w") as file:
        json.dump(image_polygons, file)

# Process each subdirectory in the main directory
for subdir in os.listdir(MAIN_DIRECTORY_PATH):
    subdir_path = os.path.join(MAIN_DIRECTORY_PATH, subdir)
    if os.path.isdir(subdir_path):
        process_directory(subdir_path)
