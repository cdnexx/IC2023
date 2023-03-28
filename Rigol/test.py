import os


def list_saved_configs():
    directory = os.listdir('configs')
    files = []
    for file in directory:
        if '.json' in file:
            # Remove file extension
            files.append(file[:file.find('.')])
    return files


print(list_saved_configs())
