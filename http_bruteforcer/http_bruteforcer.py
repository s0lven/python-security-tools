import requests
import threading
import os
from queue import Queue

NUM_THREADS = 20

"""
This code defines a simple HTTP brute-forcer that takes a URL and a wordlist as input.
It uses multiple threads to check for the existence of directories or files on the target website by appending words from the wordlist to the base URL. 
The worker function sends HTTP GET requests to the constructed URLs and checks for specific status codes (200, 301, 302, 403) to determine if the resource exists. 
The main function manages the user input, initializes the queue with words from the wordlist, and starts the worker threads.

"""

def worker(queue, url):
    while not queue.empty():
        word = queue.get()
        url_and_words = f"{url}/{word}"

        try: 
            response = requests.get(url_and_words, timeout=5)

            if response.status_code in [200, 301, 302, 403]:
                print(f"[+] Found: {url_and_words}")

        except requests.exceptions.RequestException:
            pass

        finally:
            queue.task_done()


def check_website():
    url = input("Enter the URL: ")
    wordlist_path = input("Enter wordlist path: ")

    while not os.path.isfile(wordlist_path):
        print("Wordlist not found.")
        wordlist_path = input("Enter wordlist path: ")

    queue = Queue()


    # every line in the wordlist is added to the queue for processing by the worker threads

    with open(wordlist_path, 'r') as file:
        for line in file:
            queue.put(line.strip())

    threads = []
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(queue, url)) # creating a thread that will execute the worker function, passing the queue and url as arguments
        t.daemon = True
        t.start()
        threads.append(t)

    # wait for all tasks in the queue to be processed before proceeding
    queue.join()

    print("Done!")


if __name__ == "__main__":
    check_website()