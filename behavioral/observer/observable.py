from abc import ABC
from behavioral.observer.observer import IObserver


class IObservable(ABC):
    def __init__(self):
        self.observers = set()

    def register_observer(self, observer: IObserver):
        if observer not in self.observers:
            self.observers.add(observer)

    def unregister_observer(self, observer: IObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

