"""
LeetCode 1396: Design Underground System

Problem:
Design an underground system to track customer journeys.

The system needs to:
1. checkIn(id, stationName, time) - Customer checks in at a station
2. checkOut(id, stationName, time) - Customer checks out at a station  
3. getAverageTime(startStation, endStation) - Get average travel time between two stations

Example:
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
undergroundSystem.getAverageTime("Paradise", "Cambridge")  # 14.0
undergroundSystem.getAverageTime("Leyton", "Waterloo")     # 11.0
undergroundSystem.checkIn(10, "Leyton", 24)
undergroundSystem.getAverageTime("Leyton", "Waterloo")     # 11.0
undergroundSystem.checkOut(10, "Waterloo", 38)
undergroundSystem.getAverageTime("Leyton", "Waterloo")     # 12.0

THOUGHT PROCESS FOR INTERVIEWER:
- We need to track active customers (who checked in but haven't checked out)
- We need to store journey statistics (total time, count) for each route
- Use two data structures:
  1. Dictionary to track active customers: {id: (station, check_in_time)}
  2. Dictionary to track route statistics: {(start, end): (total_time, count)}
- When checking out, calculate journey time and update route statistics
- For average time, return total_time / count for that route
"""

class UndergroundSystem:
    def __init__(self):
        # Track active customers: {customer_id: (station_name, check_in_time)}
        self.active_customers = {}
        
        # Track route statistics: {(start_station, end_station): (total_time, count)}
        self.route_stats = {}
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """
        Customer checks in at a station.
        Store their current location and check-in time.
        """
        self.active_customers[id] = (stationName, t)
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """
        Customer checks out at a station.
        Calculate journey time and update route statistics.
        """
        if id not in self.active_customers:
            return  # Invalid customer ID
        
        # Get customer's check-in information
        start_station, check_in_time = self.active_customers[id]
        
        # Calculate journey time
        journey_time = t - check_in_time
        
        # Create route key
        route = (start_station, stationName)
        
        # Update route statistics
        if route not in self.route_stats:
            self.route_stats[route] = (0, 0)  # (total_time, count)
        
        total_time, count = self.route_stats[route]
        self.route_stats[route] = (total_time + journey_time, count + 1)
        
        # Remove customer from active customers
        del self.active_customers[id]
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        """
        Get average travel time between two stations.
        """
        route = (startStation, endStation)
        
        if route not in self.route_stats:
            return 0.0  # No data for this route
        
        total_time, count = self.route_stats[route]
        return total_time / count


# Test the solution
if __name__ == "__main__":
    underground = UndergroundSystem()
    
    # Test case 1
    underground.checkIn(45, "Leyton", 3)
    underground.checkIn(32, "Paradise", 8)
    underground.checkIn(27, "Leyton", 10)
    underground.checkOut(45, "Waterloo", 15)
    underground.checkOut(27, "Waterloo", 20)
    underground.checkOut(32, "Cambridge", 22)
    
    print("Average time Paradise -> Cambridge:", underground.getAverageTime("Paradise", "Cambridge"))  # 14.0
    print("Average time Leyton -> Waterloo:", underground.getAverageTime("Leyton", "Waterloo"))        # 11.0
    
    # Test case 2
    underground.checkIn(10, "Leyton", 24)
    print("Average time Leyton -> Waterloo:", underground.getAverageTime("Leyton", "Waterloo"))        # 11.0
    underground.checkOut(10, "Waterloo", 38)
    print("Average time Leyton -> Waterloo:", underground.getAverageTime("Leyton", "Waterloo"))        # 12.0
