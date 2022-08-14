def farenheit_to_c(farn,bool):
    temp = (farn - 32) * 5/9
    if bool == True:
        result = int(temp)
        return result
    elif bool == False:
        return temp
def celsium_to_f(cels,bool):
    temp = cels * 9/5 +32
    if bool == True:
        result = int(temp)
        return result
    elif bool == true:
        return temp
