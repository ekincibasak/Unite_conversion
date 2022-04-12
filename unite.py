
#Basic unit conversion tools from Geometrized unit system

"""
CGS units
"""
grav_constant       = 6.673e-8
light_speed         = 29979245800.0
solar_mass          = 1.98892e+33
MeV                 = 1.1604505e10


class cgs:

    def __init__(self):
        

        self.grav_constant = grav_constant
        self.light_speed = light_speed
        self.solar_mass = solar_mass
        self.MeV = MeV
        
#    Compute the unit mass in the given units


    def unit_mass(self):

        return self.solar_mass
    
#    Compute the unit length in the given units  


    def unit_length(self):
        
 
        
        return self.solar_mass * self.grav_constant / self.light_speed**2
    
    
    
#    Compute the unit time in the given units    
    def unit_time(self):
        
        unit_length=self.unit_length()

        return unit_length / light_speed
    
#    Compute the unit dens in the given units  


    def unit_dens(self):
        unit_mass=self.unit_mass()
        unit_length=self.unit_length()

        return unit_mass/(unit_length)**3
    
    
#    Compute the unit energy in the given units     
    def unit_energy(self):
        unit_mass=self.unit_mass()
        unit_length=self.unit_length()
        unit_time=self.unit_time()

        
        return unit_mass * (unit_length / unit_time)**2
    
#    Compute the unit force in the given units    

    

    def unit_force(self):
        unit_mass=self.unit_mass()
        unit_length=self.unit_length()
        unit_time=self.unit_time()

        return unit_mass * unit_length / (unit_time)**2

#    Compute the unit press in the given units 



    def unit_press(self):
        unit_length=self.unit_length()
        unit_force=self.unit_force()
        return unit_force / (unit_length)**2

#    Compute the unit luminosity in the given units  

    def unit_luminosity(ua):
        unit_time=self.unit_time()
        unit_energy=self.unit_energy()

        return unit_energy(ua)/unit_time(ua)

#    Compute the unit temp in the given units 



    def unit_temp(self):

        return self.MeV

#    Compute the unit velocity in the given units 


    def unit_velocity(self):
        unit_length=self.unit_length()
        unit_time=self.unit_time()
        return unit_length / unit_time

    
    
    
convert=cgs()
print(convert.unit_force())
