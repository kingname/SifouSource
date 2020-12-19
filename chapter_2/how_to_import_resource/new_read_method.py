from importlib import resources

def read():
    with resources.open_text('how_to_import_resource', 'resource.txt') as f:
        content = f.read()
    return content
