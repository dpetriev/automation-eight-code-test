import sys
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import socket

class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("access_points.json"):
            with open(event.src_path, "r") as f:
                content = f.read()
                # send updated content to app_2 via socket
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(("localhost", 12345))
                client_socket.sendall(content.encode("utf-8"))
                client_socket.close()

if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
