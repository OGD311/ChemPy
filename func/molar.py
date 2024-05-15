def mass_moles_mr(mass:float=None, moles:float=None, mr:float=None, decimal_places:int=2) -> float:
    """
    mass
    moles
    mr

    moles = mass/mr

    """

    if sum(x is not None for x in [mass, moles, mr]) != 2: #Raise error if not enough detail provided
        raise ValueError("You must supply more than one value")
    
    if mass and moles:
        return round(mass/moles, decimal_places)
    
    elif mass and mr:
        return round(mass/mr, decimal_places)
    
    elif moles and mr:
        return round(moles * mr, decimal_places)
    
    else:
        return "Im not even sure how you triggered this but well done!"


def volume_moles_concentration(volume:float=None, moles:float=None, concentration:float=None, decimal_places:int=2) -> float:
    """
    volume
    moles
    concentration

    moles = volume * concentration

    """

    if sum(x is not None for x in [volume, moles, concentration]) != 2: #Raise error if not enough detail provided
        raise ValueError("You must supply more than one value")
    
    if volume and moles:
        return round(moles/volume, decimal_places)
    
    elif volume and concentration:
        return round(volume * concentration, decimal_places)
    
    elif moles and concentration:
        return round(moles/concentration, decimal_places)
    
    else:
        return "Im not even sure how you triggered this but well done!"
    

def number_moles_water_in_hydrated(moles_unhydrated:float, moles_hydrated:float, decimal_places=2) -> float:
    return round(moles_hydrated / moles_unhydrated, decimal_places)
