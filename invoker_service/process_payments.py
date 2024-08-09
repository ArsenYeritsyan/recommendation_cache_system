from io import BytesIO

def get_payments_storage():
    return BytesIO()

def stream_payments_to_storage(storage):
    for _ in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))

def process_payments():
    storage = get_payments_storage()
    stream_payments_to_storage(storage)
    storage.seek(0)
    checksum = sum(storage.read())
    print(checksum)

process_payments()