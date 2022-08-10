import time
import winsound

import easyocr

from typing import Union
from pyautogui import screenshot
from PIL import Image


def main() -> None:
    while True:
        scr_minerals = take_scr_minerals()
        scr_gas = take_scr_gas()
        scr_supply = take_scr_supply()
        yell_minerals(recognize_minerals())
        yell_gas(recognize_gas())
        yell_supply(recognize_supply())
        time.sleep(8)


def take_scr_minerals() -> Union[Image.Image, None]:
    """
    takes screenshots with corresponding values
    coordinates are for 1920x1080
    it is assumed that sc2 is run on "main" windows screen
    returns nothing (maybe should return a PIL.Image object if I ever rework this)
    """
    minerals = screenshot('minerals.png', region=(1560, 21, 70, 16))
    # could use this for debug:
    # minerals.show(title=None)


def take_scr_gas() -> Union[Image.Image, None]:
    """
    takes screenshots with corresponding values
    coordinates are for 1920x1080
    it is assumed that sc2 is run on "main" windows screen
    returns nothing (maybe should return a PIL.Image object if I ever rework this)
    """
    gas = screenshot('gas.png', region=(1683, 21, 70, 16))


def take_scr_supply() -> Union[Image.Image, None]:
    """
    takes screenshots with corresponding values
    coordinates are for 1920x1080
    it is assumed that sc2 is run on "main" windows screen
    returns nothing (maybe should return a PIL.Image object if I ever rework this)
    """
    supply = screenshot('supply.png', region=(1807, 21, 96, 16))


def recognize_minerals(minerals_img='minerals.png') -> Union[int, str]:
    """
    extracts number from image
    :param minerals_img: non-default values are used only for testing
    :return: integer or string with error message
    """
    reader = easyocr.Reader(['en'])
    result = reader.readtext(minerals_img, detail=0)
    print('minerals:', result)
    try:
        return int(result[0])
    except ValueError:
        return 'failed to recognize number'
    except IndexError:
        return 'failed to recognize number'


def recognize_gas(gas_img='gas.png') -> Union[int, str]:
    """
    extracts number from image
    :param gas_img: non-default values are used only for testing
    :return: integer or string with error message
    """
    reader = easyocr.Reader(['en'])
    result = reader.readtext(gas_img, detail=0)
    print('gas:', result)
    try:
        return int(result[0])
    except ValueError:
        return 'failed to recognize number'
    except IndexError:
        return 'failed to recognize number'


def recognize_supply(supply_img='supply.png') -> Union[int, str]:
    """
    extracts number from image
    :param supply_img: non-default values are used only for testing
    :return: string
    """
    reader = easyocr.Reader(['en'])
    result = reader.readtext(supply_img, detail=0)
    print('supply:', result)
    try:
        return result[0]
    except IndexError:
        return 'failed to recognize number'


def yell_minerals(mineral) -> None:
    """yells at user if condition is met (too many minerals, low supply...)"""
    if mineral == 'failed to recognize number':
        print('failed to recognize number')
        pass
    elif mineral > 1000:
        # print('too many minerals')
        winsound.PlaySound('sounds/yell_minerals_rus.wav', winsound.SND_FILENAME)


def yell_gas(gas) -> None:
    """yells at user if condition is met (too many minerals, low supply...)"""
    if gas == 'failed to recognize number':
        print('failed to recognize number')
        pass
    elif gas > 600:
        # print('too much gas')
        winsound.PlaySound('sounds/yell_gas_rus.wav', winsound.SND_FILENAME)


def yell_supply(supply) -> None:
    """yells at user if condition is met (too many minerals, low supply...)"""
    if supply == 'failed to recognize number':
        # print('failed to recognize number')
        pass
    else:
        current_supply, max_supply = supply.split('/')
        print(current_supply, max_supply)
        fraction = float(current_supply) / float(max_supply)
        if fraction > 0.8 and int(max_supply) < 200:
            # print('build more supply depos')
            winsound.PlaySound('sounds/yell_supply_rus.wav', winsound.SND_FILENAME)


if __name__ == '__main__':
    main()


'''
TODO:
1. Think about using locateOnScreen(). Could help with different resolutions.
2. Check if jpg faster than png in take_scr()
'''
