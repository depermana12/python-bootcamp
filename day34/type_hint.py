
def police_check(age: int) -> bool:
    if age >= 17:
        driver_license = True
    else:
        driver_license = False
    return driver_license


if police_check(18):
    print("can drive")
else:
    print("not eligible to drive")
