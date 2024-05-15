import func.molar as molar
import func.acidCalcs as acidCalcs

class ChemPy():
    def __init__(self, unitSystem) -> None:
        self.unitSystem = unitSystem

    ## Molar Calculations
    def moles_mass_mr(self, moles=None, mass=None, mr=None, decimal_places=2):
        print(molar.mass_moles_mr(moles, mass, mr, decimal_places))

    def volume_moles_concentration(self, volume=None, moles=None, concentration=None, decimal_places=2):
        print(molar.volume_moles_concentration(volume, moles, concentration, decimal_places))

    def number_moles_water_in_hydrated(self, moles_unhydrated, moles_hydrated, decimal_places=2):
        print(molar.number_moles_water_in_hydrated(moles_unhydrated, moles_hydrated, decimal_places))



    ## Acid Calculations
    def pH(self, H_concentration):
        print(acidCalcs.pH(H_concentration))

    def H_concentration(self, pH):
        print(acidCalcs.H_concentration(pH))

    def kW_H_OH(self, kW=None, H_concentration=None, OH_concentration=None, decimal_places=2):
        print(acidCalcs.kW_H_OH(kW, H_concentration, OH_concentration))


