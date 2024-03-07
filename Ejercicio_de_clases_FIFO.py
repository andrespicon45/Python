class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    pass

class Queue:
    def __init__(self,nombre):
        self.lista=[]
        self.nombre=nombre

    def put(self, elem):
        self.lista.insert(0, elem)

    def get(self):
        if len(self.lista)==0:
            raise QueueError
        else:
            val=self.lista[-1]
            del self.lista[-1]
            return val


class SuperQueue(Queue):
    def isempty(self):
        return len(self.lista) == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")