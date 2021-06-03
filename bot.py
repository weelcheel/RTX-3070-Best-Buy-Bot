from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import info
import logging
import traceback

# make sure this path is correct to create the chrome selinium driver
PATH = "C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

SIGNIN = "https://www.bestbuy.com/identity/global/signin"

# sign in to best buy
print("Signing in")
driver.get(SIGNIN)

# fill in email and password
emailField = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "fld-e"))
)
emailField.send_keys(info.email)

pwField = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "fld-p1"))
)
pwField.send_keys(info.password)

# click sign in button
signInBtn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cia-form__controls__submit"))
)
signInBtn.click()
print("Signing in")

# wait for the home page search bar
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gh-search-input"))
)

RTX3070LINK1 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3070LINK2 = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912"
XBOXONETEST = "https://www.bestbuy.com/site/microsoft-xbox-one-s-1tb-console-bundle-white/6415222.p?skuId=6415222"
SWITCHCONTROLLER = "https://www.bestbuy.com/site/powera-joy-con-comfort-grip-for-nintendo-switch-black/5729901.p?skuId=5729901"

driver.get(SWITCHCONTROLLER)

isComplete = False

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found.")

    try:
        # add to cart
        atcBtn.click()

        print("Successfully added to cart - beginning check out")

        driver.get("https://www.bestbuy.com/cart")

        checkoutParent = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-buttons__checkout"))
        )

        print("Found checkout button parent.")

        checkoutBtns = checkoutParent.find_elements_by_tag_name("button")
        for btn in checkoutBtns:
            btn.click()

        print("Clicked checkout button.")

        # fill in card cvv if needed
        try:
            cvvField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "credit-card-cvv"))
            )
            cvvField.send_keys(info.cvv)
        except:
            print("No CVV field found. Attempting to continue.")

        print("Attempting to place order")

        # place order
        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
        placeOrderBtn.click()

        # wait for the thank you header
        thankyouDiv = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".thank-you-enhancement__oc-heading"))
        )

        isComplete = True
    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(SWITCHCONTROLLER)
        print("Error - restarting bot")
        logging.error(traceback.format_exc())
        continue

print("Job's done")
driver.close()



