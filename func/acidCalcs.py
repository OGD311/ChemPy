import math
import func.constants as constants

def pH(H_concentration):
    return -(math.log10(H_concentration))

def H_concentration(pH):
    return 10 ** -pH

def kW_H_OH(kW:float=constants.IONIC_PRODUCT_OF_WATER, H_concentration:float=None, OH_concentration:float=None, decimal_places=2) -> float:
    """
    kW
    H_concentration
    OH_concentration

    kW = H_concentration * OH_concentration

    """

    if sum(x is not None for x in [kW, H_concentration, OH_concentration]) != 2: #Raise error if not enough detail provided
        raise ValueError("You must supply more than one value")
    
    if OH_concentration and H_concentration:
        return round(H_concentration * OH_concentration, decimal_places)
    
    elif OH_concentration and kW:
        return round(kW / OH_concentration, decimal_places)
    
    elif H_concentration and kW:
        return round(kW/H_concentration, decimal_places)
    
    else:
        return "Im not even sure how you triggered this but well done!"