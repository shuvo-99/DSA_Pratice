class Rickshaw:
  def __init__(self,capacity=2):
    self.capacity=capacity
    self.booked = False
    self.passenger=[]
    self.dict={}
    self.fare=0

  def addPassengers(self,*info):

    if self.booked == False:
      self.info = list(info)
      self.km = self.info.pop()
      count = 0
      for i in range(len(self.info)):
        self.names=''
        if count < self.capacity:
          self.passenger.append(self.info[i])
          self.names += self.info[i]+', '
          count+=1
          
          self.names = self.names[:-2]
          self.booked = True
          print(f'{self.names} is ready to ride {self.km} km(s)')

        else:
          self.names += self.info[i]+', '
          self.names = self.names[:-2]
          print(f'Sorry, {self.names}. No more capacity.')       

    else:
      print(f'{len(self.passenger)} person(s) already booked the Rickshaw. Take another vehicle.')

  def dropPassengers(self):
    if len(self.passenger) != 0:
      self.fare += self.km * 20
      self.passenger.clear()
      self.booked = False
      print('All the passengers were dropped off.')

    else:
      print('No passenger to drop.')
  
  def showInfo(self):
    return f"Capacity: {self.capacity}\nCurrent Passengers: {self.passenger}\nToday's Total Fare: {self.fare} Taka"
      


    


    
    # if self.capacity > 0 :
    #   count = 0
    #   for i in range(len(self.info)):
    #     self.names=''
    #     if count < self.capacity:
    #       self.names += self.info[i]+', '
    #       count+=1
    #       self.names = self.names[:-2]
    #       print(f'{self.names} is ready to ride {self.km} km(s)')
    #       self.capacity = self.capacity - count
    #     else:
    #       self.names += self.info[i]+', '
    #       self.names = self.names[:-2]
    #       print(f'Sorry, {self.names}. No more capacity.')
          

    # if (self.capacity - len(self.info)) > 0:  #3 - 4
    #   self.names=''
    #   self.total_capacity = self.capacity

    #   for i in range(len(self.info)):
    #     self.names += self.info[i]+', '
    #   self.names = self.names[:-2]
    #   print(f'{self.names} is ready to ride {self.km} km(s)')
    #   self.capacity = self.capacity - len(self.info)
    
    # else:
      
    #   print(f'{self.capacity} person(s) already booked the Rickshaw. Take another vehicle.')




  
r1 = Rickshaw()
print("1===========================")
r1.addPassengers("Rony", 3)
print("2===========================")
print(r1.showInfo())
print("3===========================")
r1.addPassengers("Shanto", "Shakib","Riyad", "Yasir", 4)
print("4===========================")
r2 = Rickshaw(3)
r2.addPassengers("Shanto", "Shakib","Riyad", "Yasir", 4)
print("5===========================")
r1.dropPassengers()
print("6===========================")
print(r2.showInfo())
print("7===========================")
r1.dropPassengers()
print("8===========================")
r1.addPassengers("Yasir", 4)
print("9===========================")
r2.dropPassengers()
r1.dropPassengers()
print("10===========================")
print(r1.showInfo())
print("11===========================")
print(r2.showInfo())
