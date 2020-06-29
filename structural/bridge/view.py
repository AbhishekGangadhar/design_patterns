from abc import ABC, abstractmethod
from structural.bridge.media_resource import IMediaResource


class IView(ABC):
    def __init__(self, media_resource: IMediaResource):
        self.media_resource = media_resource

    @abstractmethod
    def show(self) -> str:
        pass


class HorizontalView(IView):
    def show(self) -> str:
        return "{}: {}".format(self.media_resource.get_title(), self.media_resource.get_snippet())


class VerticalView(IView):
    def show(self) -> str:
        return "{}\n{}".format(self.media_resource.get_title(), self.media_resource.get_snippet())
