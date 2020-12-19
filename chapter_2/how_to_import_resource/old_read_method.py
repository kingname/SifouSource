import os


def read():
    folder = os.path.dirname(__file__)
    resource_path = os.path.join(folder, 'resource.txt')
    with open(resource_path) as f:
        content = f.read()
    return content

