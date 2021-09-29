from abc import ABCMeta, abstractmethod

class CaajPlugin(metaclass=ABCMeta):
  @abstractmethod
  def can_handle(self, transaction):
    pass

  @abstractmethod
  def get_caajs(self, transaction, subject_address):
    pass
