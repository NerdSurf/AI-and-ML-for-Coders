
## traditional programming logic example ##

streetlamp_status: bool = False
light: float = 1.50

def streetlamp_on_off(light_brightness, light_status):
    if light_brightness > 1.00:
        light_status = False
    elif light_brightness < 1.00:
        light_status = True
    return light_status

def main():
    streetlamp_on_off(light, streetlamp_status)