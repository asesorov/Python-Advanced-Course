import multiprocessing
import time
import sys
import codecs


def process_a(queue_ab, pipe_ab):
    while True:
        if not queue_ab.empty():
            message = queue_ab.get()
            processed_message = message.lower()
            pipe_ab.send(processed_message)
        time.sleep(5)

def process_b(pipe_ab, parent_conn):
    while True:
        if parent_conn.poll():
            processed_message = pipe_ab.recv()
            encoded_message = codecs.encode(processed_message, 'rot_13')
            parent_conn.send(encoded_message)

def main():
    queue_ab = multiprocessing.Queue()
    parent_conn, child_conn = multiprocessing.Pipe()

    p_a = multiprocessing.Process(target=process_a, args=(queue_ab, child_conn))
    p_b = multiprocessing.Process(target=process_b, args=(child_conn, parent_conn))

    p_a.start()
    p_b.start()

    try:
        while True:
            message = input("Enter a message to send to Process A: ")
            queue_ab.put(message)

            if parent_conn.poll():
                encoded_message = parent_conn.recv()
                print(f"{time.strftime('%H:%M:%S')} - Encoded message from Process B: {encoded_message}")

    except KeyboardInterrupt:
        p_a.terminate()
        p_b.terminate()
        sys.exit()

if __name__ == "__main__":
    main()
