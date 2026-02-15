import os

def rename_files(folder_path, prefix):
    try:
        files = os.listdir(folder_path)
        count = 1

        for filename in files:
            old_path = os.path.join(folder_path, filename)

            # Skip if it's not a file
            if not os.path.isfile(old_path):
                continue

            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{prefix}_{count}{file_extension}"
            new_path = os.path.join(folder_path, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")

            count += 1

        print("\nAll files renamed successfully!")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix_name = input("Enter new file prefix: ")

    rename_files(folder, prefix_name)
