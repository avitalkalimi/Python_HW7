"""
INTRO
"""


class Plant:
    """
    A representation of a plant. Implements a constructor with defaulting values(except one),
     a represent overload and 2 more methods:
    # get_maintenance_cost.
    # purchase_decision.
    """
    def __init__(self, name: str,
                 aesthetics: int = 1,
                 water_consumption_month: int = 1,
                 average_month_yield: int = 1,
                 seasonal: bool = False):
        """
        Initializes an instance of Plant.
        :param name: (str) the name of the plant.
        :param aesthetics: (int) the level of aesthetics the plant is valued at.
        :param water_consumption_month: (int) the plant's monthly consumption of water amount
        :param average_month_yield: (int) the value the plant creates every month
        :param seasonal: (bool) whether the plant is year-round (True) plantation or only 6 months (False).
        """
        self.name = name
        self.aesthetics = aesthetics
        self.water_consumption_month = water_consumption_month
        self.average_month_yield = average_month_yield
        self.seasonal = seasonal

    def get_maintenance_cost(self, func1):
        """
        Invokes the given argument as a function with the instance itself (self) as input argument.
        :param func1: a function object.
        :return:
        """
        return func1(self)

    def purchase_decision(self, func1, func2):
        """
        Invokes the first given argument as a function with two inputs (by order):
         the instance itself, and the result of the second argument invoked as a function with the instance
         itself (self) as input argument.
        :param func1: a function object.
        :param func2: a function object.
        :return:
        """
        return func1(self, func2(self))

    def __repr__(self):
        """
        overloads the python object __repr__ method.
        :return: str
        """
        return "name={}".format(self.name)


class GardenManager:
    """
    A representation of a garden management system. Implements a constructor with no defaulting values,
     a represent overload and 1 more methods:
     # action.
    """
    def __init__(self, plants_in_garden: list):
        """
        Initializes an instance of GardenManager.
        :param plants_in_garden: a list of the plants which are in the garden.
        """
        self.plants_in_garden = plants_in_garden

    def action(self, func1):
        """
        Invokes the given argument as a function with the instance itself (self) as input argument.
        :param func1: a function object.
        :return:
        """
        return func1(self)

    def __repr__(self):
        """
        overloads the python object __repr__ method.
        :return: str
        """
        return "Number of plants = {0}".format(len(self.plants_in_garden))
#

"""
PART A - Lambda functions
"""

# Q1
get_cost_lmbd = lambda x: x.water_consumption_month  # return water_consumption_month of flower

# Q2
get_yearly_cost_lmbd = lambda x: x.water_consumption_month*6 if x.seasonal else x.water_consumption_month*12   # return water_consumption_year of flower

# Q3
worth_investing_lmbd = lambda x: True if x.average_month_yield > x.water_consumption_month else False  # chek yield vs consumption

# Q4
declare_purchase_lmbd = lambda x,y: "{A}:{B}".format(A = x.name, B = "yes" if y is True or x.aesthetics >= x.water_consumption_month else "no") # str name:True/False

# Q5

get_plants_names_lmbd = lambda x: sorted(map(lambda x: x.name, x.plants_in_garden)) # return sorted list of flowers names


"""
PART B - High order functions
"""

from functools import reduce

# Q1 -
def retrospect(garden_manager):  #  list with name of flowers that have flowers more then water consumption
    A = list(filter(lambda x: x.water_consumption_month < x.average_month_yield, garden_manager.plants_in_garden))
    return list(map(lambda y: y.name, A))

# Q2 -
def get_total_yearly_cost(garden_manager):  # the sum of water consumption of the flowers in the garden in one year
    A = list(map(lambda x: get_yearly_cost_lmbd(x) , garden_manager.plants_in_garden))
    return reduce(lambda x, y: x + y, A)

# Q3 -
def get_aesthetics(garden_manager):  # list of aesthetics value of all the flowers in the garden
    return list(map(lambda x: x.aesthetics, garden_manager.plants_in_garden))


"""
PART C - University gate
"""


class GateLine:
    def __init__(self, max_capacity):
        self.values = {}
        self.capacity = max_capacity

    def new_in_line(self, student_id, priority_id_holder):
        if len(self.values) >= self.capacity:  # if the capacity is full in the queue
            if priority_id_holder == True:
                ll1 = []
                for i in self.values:
                    if self.values.get(i) == True:
                        ll1.append(i)
                if len(ll1) >= self.capacity:
                    self.values.update({student_id: priority_id_holder})
                if len(ll1) < self.capacity:
                    my_queue = GateLine.show_who_is_in_line(self)
                    the_last = my_queue[-1]
                    self.values.pop(the_last)
                    self.values.update({student_id: priority_id_holder})
        else:
            self.values.update({student_id: priority_id_holder})

    def open_gate(self):  # return how is the next in the queue
        if self.is_empty():
            return None
        else:
            my_queue = GateLine.show_who_is_in_line(self)
            the_next = my_queue[0]
            self.values.pop(the_next)
            return the_next

    def is_empty(self):
        return len(self.values) == 0

    def show_who_is_in_line(self):
        ll1 = []
        ll2 = []
        ll3 = []
        for i in self.values:
            if self.values.get(i) == True:
                ll1.append(i)
        for i in self.values:
            if self.values.get(i) == False:
                ll2.append(i)
        for i in ll1:
            ll3.append(i)
        for i in ll2:
            ll3.append(i)
        return ll3

