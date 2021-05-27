from abc import ABC, abstractmethod


class Father(ABC):

	@abstractmethod
	def disp(self):
		pass

	@abstractmethod
	def disp2(self):
		pass


class Child(Father):

	def disp(self):
		pass

	def hh(self):
		print("hhh")


ch = Child()
ch.hh()
