import os
import shutil

def segregate_images_by_gender_and_emotion(source_directory, destination_directory):
    img_count=0
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    gender_map = {'F': 'Female', 'M': 'Male'}
    emotion_map = {'N': 'Neutral', 'A': 'Angry', 'F': 'Fear', 'HC': 'Happy_ClosedMouth', 'HO': 'Happy_OpenMouth'}
    ethnicity_map={'A':'Asian American','B':'Black','I':'Indian Asian','L':'Latino/a','M':'Multiracial American','W':'White'} 

    for folder in os.listdir(source_directory):
        folder_path = os.path.join(source_directory, folder)

        if not os.path.isdir(folder_path):
            continue

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.jpg'):
                parts = file_name.split('-')
                if len(parts) < 5:
                    #print(f"Skipping {file_name}, does not have the correct formatting.")
                    continue

                gender_key = parts[1][1]
                emotion_key = parts[4].split(".")[0]
                ethnicity_key=parts[1][0]
                #print("gender"+""+gender_key)
                #print("emotion"+""+emotion_key)  
                #print("==================================")

                gender_folder = gender_map.get(gender_key)
                ethnicity_folder=ethnicity_map.get(ethnicity_key)
                emotion_folder = emotion_map.get(emotion_key)

                target_folder = os.path.join(destination_directory,gender_folder,ethnicity_folder,emotion_folder)
                os.makedirs(target_folder, exist_ok=True)

                src_file_path = os.path.join(folder_path, file_name)
                dst_file_path = os.path.join(target_folder, file_name)
                shutil.copy(src_file_path, dst_file_path)
                print(f"Copied {file_name} to {target_folder}")
                img_count+=1
    return img_count

source_directory_path = "D:\CFD\Images\CFD"
destination_directory_path = "D:\CFD\Segregated_Images"
count=segregate_images_by_gender_and_emotion(source_directory_path, destination_directory_path)
print(count)
