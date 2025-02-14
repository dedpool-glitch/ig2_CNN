import os

def create_dataset_dict(source_folder):
    dataset = {}
    emotion_map = {'N': 0, 'A': 1, 'F': 2, 'HC': 3, 'HO': 3}

    for folder in os.listdir(source_folder):
        folder_path = os.path.join(source_folder, folder)

        if not os.path.isdir(folder_path):
            continue

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.jpg'):
                parts = file_name.split('-')
                if len(parts) < 5:
                    continue 

                emotion_key = parts[4].split(".")[0] 
                label = emotion_map.get(emotion_key, None)

                if label is not None:
                    dataset[folder_path+file_name] = label

    return dataset

# Example Usage
source_directory_path = "D:\Integrated_gap_gradients\ig2_CNN\gpu_env_ig2\CFD"
dataset_dict = create_dataset_dict(source_directory_path)

print(f"Total Images: {len(dataset_dict)}")
