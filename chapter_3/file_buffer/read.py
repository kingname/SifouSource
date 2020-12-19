import time

while True:
    with open('resource.txt') as f:
        content = f.read()
        print(content)
    time.sleep(1)
