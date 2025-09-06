name = input("File name: ").split('.')[-1]

match name:
    case 'gif'|'jpg'|'jpeg'|'png':
        print(f"image/{name}")
    case 'pdf'|'txt'|'zip':
        print(f"application/{name}")
    case _:
        print("application/octet-stream")
