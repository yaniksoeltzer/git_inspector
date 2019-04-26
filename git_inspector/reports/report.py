from abc import abstractmethod


class Report:
    @abstractmethod
    def number_of_alerts(self):
        pass

    @abstractmethod
    def number_of_warnings(self):
        pass
