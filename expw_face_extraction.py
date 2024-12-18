import pandas as pd
import cv2
import os

csv_file = "labels.csv"
images_path = "D:\EXPW\origin"
output_path = "extracted_faces\\" 
os.makedirs(output_path, exist_ok=True)

csv_data = pd.read_csv(csv_file)

for index, row in csv_data.iterrows():
    image_name = row['image_name']
    top_coordinate, left_coordinate, right_coordinate, bottom_coordinate = int(row['face_box_top']), int(row['face_box_left']), int(row['face_box_right']), int(row['face_box_bottom'])

    image_path = os.path.join(images_path, image_name)
    image = cv2.imread(image_path)
    cropped_face = image[top_coordinate:bottom_coordinate, left_coordinate:right_coordinate]
    face_output_path = os.path.join(output_path, f"face_{index}_{image_name}")
    cv2.imwrite(face_output_path, cropped_face)

    print(f"cropped face saved to {face_output_path}")

print("Face extraction completed!")
