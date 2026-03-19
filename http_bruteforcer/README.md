# Directory Brute Forcer

Simple Python tool for discovering hidden directories on web servers.

This tool performs a simple HTTP brute-forcer that takes a URL and a wordlist as input.
It uses multiple threads to check for the existence of directories or files on the target website by appending words from the wordlist to the base URL. 
The worker function sends HTTP GET requests to the constructed URLs and checks for specific status codes (200, 301, 302, 403) to determine if the resource exists. 
The main function manages the user input, initializes the queue with words from the wordlist, and starts the worker threads.


## Features

- Multithreaded directory brute-forcing
- Supports custom wordlists
- Handles HTTP request timeouts
- Detects valid endpoints based on status codes (200, 301, 302, 403)


## Requirements

- Python 3
- requests

Install dependencies:
```pip install -r requirements.txt```

## Usage

```bash
python http_bruteforcer.py