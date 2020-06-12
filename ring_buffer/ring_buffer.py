class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.items = []
        self.order = []

    def append(self, item):
        # check if we are still under capacity
        if self.size < self.capacity:
            # append our item to both lists and increase size
            self.items.append(item)
            self.order.append(item)
            self.size += 1
        else:  # we are at capacity
            # find the index of the oldest item
            # in items in our ordered list
            index = self.order.index(self.items[0])
            self.items.pop(0)
            self.order[index] = item
            self.items.append(item)

    def get(self):
        return self.order  # return our ordered list of items
