def read_file(file_path):

    with open(file_path, mode='r') as opened_file:
        data = opened_file.read()

    return data
