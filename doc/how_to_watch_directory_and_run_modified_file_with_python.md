
watching directory, if *.py file create or modified, run it.

## install

# linux
$(which python)/Scripts/pip install watchdog

# windows
$(which python)/Scripts/pip.exe --version
C:\bin\python\Scripts\pip.exe install watchdog

## code

```python:pywatcher
#######!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
  patterns = ["*.py"]

  def process(self, event):
    """
    event.event_type
        'modified' | 'created' | 'moved' | 'deleted'
    event.is_directory
        True | False
    event.src_path
        path/to/observed/file
    """
    # the file will be processed there
    # print event.src_path, event.event_type  # print now only for degug
    print("=" * 80)
    print(event.src_path)
    print("=" * 80)
    subprocess.call(["python", event.src_path])

  def on_modified(self, event):
    self.process(event)

  def on_created(self, event):
    self.process(event)



if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO,
                      format='%(asctime)s - %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')
  path = sys.argv[1] if len(sys.argv) > 1 else '.'
  # event_handler = LoggingEventHandler()
  event_handler = MyHandler()

  observer = Observer()
  observer.schedule(event_handler, path, recursive=True)
  observer.start()
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

```


python watch_for_changes.py c:\

