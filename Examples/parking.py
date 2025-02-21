"""

Write code for low level design of a parking lot with multiple floors.
The parking lot has two kinds of parking spaces: type = 2, for 2 wheeler vehicles and type = 4, for 4 wheeler vehicles.

There are multiple floors in the parking lot. On each floor, vehicles are parked in parking spots arranged in rows and columns.
For simplicity, lets assume that each floor will have same number of rows and each row will have same number of columns.

You can solve this question in either Java or Python
Implement the below methods in Solution class:

init(Helper helper, int [][][] parking)
- helper has methods like, helper.print("") and helper.println("") which you can use for printing logs
- parking[i][j][k] : parking spot on i-th floor, j-th row and k-th column.
- each item in parking array is of the following type.
    4 : 4 wheeler parking spot,
    2 : 2 wheeler parking spot,
    0 : inactive spot, no vehicle can be parked here

park(int vehicleType, String vehicleNumber, String ticketId, int parkingStrategy)
returns spotId
- This function assigns an empty parking spot to vehicle and maps vehicleNumber and ticketId to the assigned spotId
- spotId is floor+"-"+row+"-"+column
e.g. parking[2][0][15] = parking spot at 2nd floor , 0th row and 15th column (0 based index),
its spotId will be: "2-0-15"
- parkingStrategy has two values, 0 and 1

parkingStrategy = 0
- Get the parking spot at lowest index i.e. lowest floor, row and column
e.g. park() is called with vehicleType 4 and we have free 4-wheeler spots at
parking[0][0][0], parking[0][0][1] and parking[1][0][2]
here we will return parking[0][0][0] because its index (floor, row, column) comes before the other two.

parkingStrategy = 1 :
- Get the floor with maximum number of free spots for the given vehicle type.
- If multiple floors have maximum free spots then choose the floor at lowest index from them.
e.g. park() is called with vehicleType 4 and floor[0] has 2 free 4 wheeler parking spots and
floor[1] and floor[3] both have 3 empty 4-wheeler parking spots.
here we will return the free 4-wheeler parking spot at lowest index from floor[1],
because apart from having highest number of free 4-wheeler spots it also comes before floor[3],
which also has 3 empty 4-wheeler parking spots.

removeVehicle(String spotId)
- Unparks or removes vehicle from parking spot.
- returns true if vehicle is removed
- returns false if vehicle not found or any other error


String searchVehicle(String query)
- searches the latest parking details of a vehicle parked in previous park() method calls.
- returns spotId e.g. 2-0-15 or empty string ""
- Query will be either vehicleNumber or ticketId.

int getFreeSpotsCount(int floor, int vehicleType)
- At any point of time get the number of free spots of vehicle type (2 or 4 wheeler).
- 0>= floor < parking.length (parking array from init() method).


Constraints:
- type = 2 for two-wheeler vehicle, type = 4 for 4 wheeler vehicle
- 1<=floors<=5, 1<=rows<=10,000, 1<=columns<=10,000, 1<=rows*columns<=10,000

Input Example
parking = [[
[4, 4, 2, 2],
[2, 4, 2, 0],
[0, 2, 2, 2],
[4, 4, 4, 0]]]
Above input has 1 floor.
It has 4 rows and 4 columns on floor 0.
Total 7 active 2-wheeler vehicles and
6 active 4-wheeler vehicles are there.

e.g park(2, "bh234", "tkt4534", 0)
will return spotId: "0-0-2"
i.e. parking spot from floor 0, row 0 and column 2 is assigned.

- search("bh234") or search("tkt4534")
at this point should return spotId = "0-0-2"
i.e. we can use vehicleNumber: "bh234" or ticketId: "tkt4534" to find the parking spot id where vehicle is parked.

- getFreeSpotsCount(0, 2)
will return 6.

- removeVehicle("0-0-2")
should unpark the parked vehicle and

- getFreeSpotsCount(0, 2)
after unparking, getFreeSpotsCount will now return 7.

"""






class vehicle:
    def __init__(self, vehicleNumber, ticketId):
        self.__vehicleNumber = vehicleNumber
        self.__ticketId = ticketId
        
    def get_vehicleNumber(self):
        return self.__vehicleNumber

    def get_ticketId(self):
        return self.__ticketId
    
    def set_vehicleNumber(self, newVehicleNumber):
        if newVehicleNumber != "":
            self.__vehicleNumber = newVehicleNumber
    
    def set_ticketId(self, newTicketId):
        if newTicketId != "":
            self.__ticketId = newTicketId



class parkingManagement:
    def __init__(self, parkingSpace, rows, cols):
        self.__rows = -1
        self.__cols = -1
        self.__carData = {}     # Dictionary storing info of the parked cars
        self.__availableParkingFloorWise = []    # Bike, Car

        if(len(parkingSpace) == rows and len(parkingSpace[0]) == cols):
            self.__rows = rows
            self.__cols = cols

        if rows != -1 and cols != -1:
            self.__parkingSpace = parkingSpace
            self.__currParkingStatus = self.__parkingSpace

            for floor in self.__parkingSpace:                 # updating available parking space floor-wise
                currFreeSpaceCar = 0
                currFreeSpaceBike = 0
                for space in floor:
                    if space == 2:
                        currFreeSpaceBike+=1
                    if space == 4:
                        currFreeSpaceCar+=1
                self.__availableParkingFloorWise.append([currFreeSpaceBike, currFreeSpaceCar])
        else:
            print("Invalid inputs provided")

    # def park(2, "bh234", "tkt4534", 0):


    # private functions
    def __parkWithStrategy0(self, vehicleType, vehicleNumber, ticketId):
        # Get the parking spot at lowest index i.e. lowest floor, row and column
        spotId = ""
        for floor in range(self.__rows):
            for parkingSpot in range(self.__cols):
                if(self.__currParkingStatus[floor][parkingSpot] == vehicleType):    # appropriate space found
                    self.__currParkingStatus[floor][parkingSpot] = vehicleNumber
                    spotId = str(floor)+"-"+str(parkingSpot)
                    self.__carData[vehicleNumber] = spotId
                    self.__carData[ticketId] = spotId

                    if(vehicleType == 2):
                        self.__availableParkingFloorWise[floor][0] -= 1
                    else:
                        self.__availableParkingFloorWise[floor][1] -= 1

                    return spotId
        
        return spotId

    def __parkWithStrategy1(self, vehicleType, vehicleNumber, ticketId):
        # Get the floor with maximum number of free spots for the given vehicle type.
        # If multiple floors have maximum free spots then choose the floor at lowest index from them.
        spotId = ""
        floorWithMaxFreeSpots = 0
        maxFreeSpotsObserved = 0
        for floor in range(self.__rows):
            currFreeSpaces = 0
            for parkingSpot in range(self.__cols):
                if(self.__currParkingStatus[floor][parkingSpot] == vehicleType):
                    currFreeSpaces+=1
            if(currFreeSpaces > maxFreeSpotsObserved):
                floorWithMaxFreeSpots = floor
                maxFreeSpotsObserved = currFreeSpaces

        for parkingSpot in range(self.__cols):
            if(self.__currParkingStatus[floorWithMaxFreeSpots][parkingSpot] == vehicleType):
                self.__currParkingStatus[floorWithMaxFreeSpots][parkingSpot] = vehicleNumber 
                spotId = str(floorWithMaxFreeSpots)+"-"+str(parkingSpot)
                self.__carData[vehicleNumber] = spotId
                self.__carData[ticketId] = spotId

                if(vehicleType == 2):
                    self.__availableParkingFloorWise[floorWithMaxFreeSpots][0] -= 1
                else:
                    self.__availableParkingFloorWise[floorWithMaxFreeSpots][1] -= 1

        return spotId


    # public functions
    def set_parking(self, newParkingSpace, newRows, newCols):
        if(len(newParkingSpace) == newRows and len(newParkingSpace[0]) == newCols):
            self.__rows = newRows
            self.__cols = newCols

        if self.__rows == newRows and self.__cols == newCols:
            self.__parkingSpace = newParkingSpace
            self.__currParkingStatus = newParkingSpace
        else:
            print("Invalid inputs provided")

    def curr_parkingStatus(self):
        print("             0 -> Inactive Spot")
        print("             2 -> Available 2-wheeler parking space")
        print("             4 -> Available 4-wheeler parking space")
        print("vehicle_number -> Occupied by the vehicle having number as specified\n")
        for currFloor in self.__currParkingStatus:
            print(currFloor)

    def park(self, vehicleType, vehicleNumber, ticketId, parkingStrategy):
        if parkingStrategy == 0:
            return self.__parkWithStrategy0(vehicleType, vehicleNumber, ticketId)
        if parkingStrategy == 1:
            return self.__parkWithStrategy1(vehicleType, vehicleNumber, ticketId)
        else:
            print("Invalid Parking Strategy Demanded")

    def removeVehicle(self, spotId):
        spotIdData = spotId.split("-")
        
        # vehicleFloor = int(spotIdData[0])
        vehicleRow = int(spotIdData[0])
        vehicleCol = int(spotIdData[1])
        
        # check if the spot is empty or not
        if(self.__currParkingStatus[vehicleRow][vehicleCol] in [0,2,4]):
            return False
        else:
            originalSpotType = self.__parkingSpace[vehicleRow][vehicleCol]
            if(originalSpotType == 2):
                self.__availableParkingFloorWise[vehicleRow][0] += 1
            else:
                self.__availableParkingFloorWise[vehicleRow][1] += 1

            self.__currParkingStatus[vehicleRow][vehicleCol] = originalSpotType

            keysToRemove = []
            for entry in self.__carData:
                if(self.__carData.get(entry) == spotId):
                    keysToRemove.append(entry)
            for key in keysToRemove:
                self.__carData.pop(key)
                
            return True;                        # vehicle removed successfully

    def searchVehicle(self, query):
        if query in self.__carData.keys():
            return self.__carData.get(query)
        else:
            return ""

    def getFreeSpotsCount(self, floor, vehicleType):
        if 0 > floor or floor >= self.__rows:
            print("Invalid floor number provided")
        else:
            if vehicleType == 2:
                return self.__availableParkingFloorWise[floor][0]
            if vehicleType == 4:
                return self.__availableParkingFloorWise[floor][1]



if __name__ == "__main__":
    parkingSlots = [
                    [4, 4, 2, 2],
                    [2, 4, 2, 0],
                    [0, 2, 2, 2],
                    [4, 4, 4, 0]
                    ]
    parking1 = parkingManagement(parkingSlots, 4, 4)


    car1SpotId = parking1.park(2, "bh234", "tkt4534", 0)
    print("Spot Id : ", car1SpotId)

    if(parking1.searchVehicle("bh234")):
        print("Vehicle Present")
    else:
        print("Vehicle not present")

    freeSpots = parking1.getFreeSpotsCount(0,2)
    print("Free Spots : ", freeSpots)

    if(parking1.removeVehicle("0-2")):
        print("Vehicle removed successfully")
    else:
        print("Not parked here")

    freeSpots = parking1.getFreeSpotsCount(0,2)
    print("Free Spots : ", freeSpots)