from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from colorama import Fore, Style

# Read IP addresses from the file
documento = open('direcciones_ip.txt', 'r').read().split('\n')

# Tool selection input
eleccion = input(Fore.GREEN + "Escribe el número de la herramienta que quieras utilizar para analizar las direcciones IP: "
                 + Fore.YELLOW + """\n1 - Symantec
2 - AbuseIP
3 - Virustotal: \n""" + Style.RESET_ALL + "¿Cuál es tu elección? --> ")

def find_search_box(driver, tool):
    if tool == "1":
        return driver.find_element('css selector', '#txtUrl')
    elif tool == "2":
        return driver.find_element('css selector', '#ip-search')
    elif tool == "3":
        return driver.find_element('css selector', '#searchInput')

# Open the browser
driver = webdriver.Chrome()

# List to store webdriver instances
tabs = [driver]

if eleccion in ["1", "2", "3"]:
    for ip in documento:
        url = ""
        if eleccion == "1":
            url = "https://sitereview.bluecoat.com/#/"
        elif eleccion == "2":
            url = "https://www.abuseipdb.com/"
        elif eleccion == "3":
            url = "https://www.virustotal.com/gui/home/search"

        # Open a new tab
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        tabs.append(driver)

        driver.get(url)
        time.sleep(3)  # Adjust this delay as needed

        search_box = find_search_box(driver, eleccion)

        if search_box is not None:
            search_box.clear()
            search_box.send_keys(ip)
            search_box.send_keys(Keys.RETURN)

            time.sleep(3)  # Adjust this delay as needed
        else:
            print(f"Search box not found for tool {eleccion}.")

