#Variables
finalPos = 0
def run(current_pos: int, dice: int) -> int:
    # TODO
    global finalPos
    finalPos = current_pos + (dice * 2)
    return finalPos


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(finalPos)