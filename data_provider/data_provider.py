from abc import ABC, abstractmethod


class DataProvider(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get(self, key, start_time, end_time):
        """
        get data based on key and time
        :param key: key
        :param start_time: can be datetime or date
        :param end_time: can be datetime or date
        :return: data
        """
        pass

    @abstractmethod
    def get_key(self):
        """
        return supported key time
        :return: supported key time tuple
        """
        pass
