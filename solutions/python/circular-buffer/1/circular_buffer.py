class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.slots = [[] for _ in range(capacity)]
        self.current_write = 0
        self.current_read = 0

    def read(self):
        filled = [slot for slot in self.slots if slot]
        if not filled:
            raise BufferEmptyException("Circular buffer is empty")

        read = self.slots[self.current_read].pop()
        self.current_read = (self.current_read + 1) % len(self.slots)
        return read

    def write(self, data):
        has_bandwidth = [slot for slot in self.slots if not slot]
        if not has_bandwidth:
            raise BufferFullException("Circular buffer is full")

        self.slots[self.current_write] = [data]
        self.current_write = (self.current_write + 1) % len(self.slots)

    def overwrite(self, data):
        try:
            self.write(data)
        except BufferFullException:
            self.slots[self.current_write] = [data]
            self.current_read = (self.current_read + 1) % len(self.slots)
            self.current_write = (self.current_write + 1) % len(self.slots)

    def clear(self):
        filled = [slot for slot in self.slots if slot]
        if not filled:
            return
        self.slots[self.current_read].pop()