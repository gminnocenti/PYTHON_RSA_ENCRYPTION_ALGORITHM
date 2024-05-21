def load_key():
    with open("secret.key", "rb") as key_file:
        key_bytes = key_file.read()
    return key_bytes

def bytes_to_int(bytes_data):
    return int.from_bytes(bytes_data, byteorder='big')


def cargar_p():
# Load the key from the file
    key_bytes = load_key()

    # Convert the bytes back to an integer
    key_int = bytes_to_int(key_bytes)
    
    return key_int

