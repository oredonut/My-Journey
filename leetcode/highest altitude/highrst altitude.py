class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int

        Pseudocode
    
     currentAltitude =0
     highestAltitudee =0
       for each value in gain
       currentAltitude =currentAltitude +value

       if currentAltitude > highestAltitude
       highestAltitude =currentAltitude

       return highest altitude
       """
        current_altitude =0
        highest_altitude =0

        for value in gain:
            current_altitude += value
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude
