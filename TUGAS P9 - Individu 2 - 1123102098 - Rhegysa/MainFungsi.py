import os

def CreateDirectory(namaFolder):
    if not os.path.exists(namaFolder):
        os.makedirs(namaFolder);

def CreateNewFile(path):
    f = open(path, "w");
    f.write("");
    f.close();

def WriteToFile(path, data):
    with open(path, "a") as file:
        file.write(data + "\n");

def DoesFileExist(path):
    return os.path.isfile(path)

def WriteToFile2(path, data, response):
    fullPath = os.path.join(path, data)
    with open(fullPath, 'wb') as f:
        f.write(response.content)