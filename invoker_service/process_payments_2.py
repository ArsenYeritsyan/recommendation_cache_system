def stream_payments(callback_fn):
    for i in range(10):
        callback_fn(i)

def store_payments(amount_iterator):
    for i in amount_iterator:
        print(i)

def process_payments_2():
    amounts = []
    stream_payments(amounts.append)
    store_payments(iter(amounts))

process_payments_2()