import os
import sys
import threading
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_modified = self.on_modified
        self.event_handler.on_deleted = self.on_deleted
        self.observer = Observer()
        self.running = False

    def run(self):
        self.observer.schedule(
            self.event_handler, self.DIRECTORY_TO_WATCH, recursive=True
        )
        self.observer.start()
        self.running = True
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
        finally:
            self.observer.stop()
            self.observer.join()

    def stop(self):
        self.running = False

    def on_modified(self, event):
        if str(event.src_path).endswith(".py"):
            print(f"Modified File: {event.src_path}")
            print
            self.stop() 
            restart_script()
  

    def on_deleted(self, event):
        if str(event.src_path).endswith(".py"):
            print(f"Deleted File: {event.src_path}")
            self.stop() 
            restart_script()


def start_watcher_in_thread(directory):
    watcher = Watcher(directory)
    watcher_thread = threading.Thread(target=watcher.run, daemon=True)
    watcher_thread.start()
    return watcher


def restart_script():
    print("Restarting...")
    os.execl(sys.executable, sys.executable, *sys.argv)