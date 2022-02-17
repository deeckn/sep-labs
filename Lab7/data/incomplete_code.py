from abc import ABC, abstractmethod


class Transportation(ABC):
    """Abstract base class"""
    @abstractmethod
    def __init__(self, start, end, distance):
        if self.__class__ == Transportation:
            raise NotImplementedError
        self.start = start
        self.end = end
        self.distance = distance

    @abstractmethod
    def find_cost(self):
        """Abstract method; derived classes must override"""
        raise NotImplementedError


class Walk(Transportation):
    def __init__(self, start, end, distance):
        Transportation.__init__(self, start, end, distance)

    def find_cost(self):
        return 0


class Taxi(Transportation):
   
   def __init__(self, start, end, distance):
      Transportation.__init__(self, start, end, distance)
   
   def find_cost(self):
      return self.distance * 40


class Train(Transportation):
    def __init__(self, start, end, cost, stations):
        Transportation.__init__(self, start, end, None)
        self.__stations = stations
        self.__cost = cost

    def find_cost(self):
        return self.__stations * self.__cost


# main program
travel_cost = 0

trip = [Walk("KMITL", "KMITL SCB Bank", 0.6),
        Taxi("KMITL SCB Bank", "Ladkrabang Station", 5),
        Train("Ladkrabang Station", "Payathai Station", 40, 6),
        Taxi("Payathai Station", "The British Council", 3)]

for travel in trip:
    travel_cost += travel.find_cost()
print(travel_cost)
