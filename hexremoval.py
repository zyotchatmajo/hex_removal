import os

folder_input = input("Enter the path for the input folder: ")
folder_output = folder_input+r'_Extracted'

bytes_toremove = 56 # For Break the Chains should be 56 bytes


os.makedirs(folder_output, exist_ok=True)

def RemoveBytes(file):
    with open(folder_input + "\\" + file, 'rb') as f:
        data = f.read()
    with open(folder_output + "\\" + file, 'wb') as f:
        f.write(data[bytes_toremove:])


for file in os.listdir(folder_input):
    RemoveBytes(file)
