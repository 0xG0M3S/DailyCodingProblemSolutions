
class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass

class PeekableIterator(PeekableInterface):
    
    def __init__(self, iterator):
        self.iterator = iterator
        self.peekVar = None

    def peek(self):
        if self.peekVar is None:
            self.peekVar = next(self.iterator)
        return self.peekVar

    def next(self):
        if self.peekVar is not None:
            tmp = self.peekVar
            self.peekVar = None
            return tmp
        
        return next(self.iterator)

    def hasNext(self):
        if self.peekVar is not None:
            return True
        else:
            sentinel = object()
            elem = next(self.iterator, sentinel)
            if elem is sentinel:
                return False
            else:
                return True
        

t = 'abcdefgh'

it = PeekableIterator(iter(t))

print(it.peek()) # a
print(it.peek()) # a
print(it.next()) # a
print(it.peek()) # b
print(it.next()) # b
print(it.next()) # c

