import os

class KeyValueStore:
    def __init__(self, log_file='data.log'):
        self.store = {}
        self.log_file = log_file
        self._load_log()

    def _load_log(self):
        """Rebuild the store by replaying the log."""
        if not os.path.exists(self.log_file):
            return
        with open(self.log_file, 'r') as f:
            for line in f:
                parts = line.strip().split(maxsplit=2)
                if not parts:
                    continue
                command = parts[0]
                if command == 'SET' and len(parts) == 3:
                    key, value = parts[1], parts[2]
                    self.store[key] = value
                elif command == 'DELETE' and len(parts) == 2:
                    key = parts[1]
                    self.store.pop(key, None)

    def _append_log(self, entry: str):
        """Append a command to the log file."""
        with open(self.log_file, 'a') as f:
            f.write(entry + '\n')

    def set(self, key: str, value: str):
        """Set a key to a value and log the operation."""
        self.store[key] = value
        self._append_log(f'SET {key} {value}')

    def delete(self, key: str):
        """Delete a key and log the operation."""
        if key in self.store:
            del self.store[key]
            self._append_log(f'DELETE {key}')

    def get(self, key: str):
        """Retrieve a value by key, or None if not found."""
        return self.store.get(key)

    def items(self):
        """Return all key-value pairs."""
        return self.store.items()
