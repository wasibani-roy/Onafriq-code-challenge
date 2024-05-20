from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def open_link():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-ads")
    chrome_service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    # Open a new DevTools session
    driver.execute_cdp_cmd('Network.enable', {})
    driver.execute_cdp_cmd('Network.setBlockedURLs', {"urls": ["*://*.doubleclick.net/*", "*://*.googleadservices.com/*", "*://*.googlesyndication.com/*"]})
    driver.get("https://www.automationexercise.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    driver.find_element(By.NAME, "email").send_keys("qat@mailinator.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    # Find all elements with class "productinfo"
    products = driver.find_elements(By.CLASS_NAME,"productinfo")

    # Initialize a dictionary to store label-price pairs
    label_price_dict = {}
    for product in products:
        # Extract price
        price_element = product.find_element(By.TAG_NAME,"h2")
        price = price_element.text

        # Extract product name
        name_element = product.find_element(By.TAG_NAME,"p")
        name = name_element.text
        if price == "" and name == "":
            continue
        else:
            label_price_dict[name]=price

    sorted_label_price = sorted(label_price_dict.items(), key=lambda x: float(x[1].replace('Rs. ', '')))

    
    for label, price in sorted_label_price:
        print("Label:", label)
        print("Price:", price)
        print()
    time.sleep(2)

    # Wait for the Women category to be visible and then hover over it
    women_category = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "WOMEN"))
    )
    women_category.click()

    # Click on the Women – Tops Products subcategory
    tops_subcategory = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "TOPS"))
    )
    tops_subcategory.click()
    
    # Add Fancy Green Top to the cart
    fancy_green_top_add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Fancy Green Top']/following-sibling::a[contains(@class, 'add-to-cart')]"))
    )
    fancy_green_top_add_to_cart.click()

    # Wait for the modal to appear and then close it
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartModal"))
    )
    close_modal_button = driver.find_element(By.CSS_SELECTOR,"button.close-modal")
    close_modal_button.click()

    # Add Summer White Top to the cart
    summer_white_top_add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Summer White Top']/following-sibling::a[contains(@class, 'add-to-cart')]"))
    )
    summer_white_top_add_to_cart.click()

    # Wait for the modal to appear and then close it
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartModal"))
    )
    close_modal_button = driver.find_element(By.CSS_SELECTOR,"button.close-modal")
    close_modal_button.click()

    move_to_cart = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.LINK_TEXT,"Cart"))
    )
    move_to_cart.click()
    check_out = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "check_out"))
    )
    check_out.click()

    # Add comments
    comments_textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "message"))
    )
    comments_textarea.send_keys("Order placed.")

    # Place order
    driver.find_element(By.LINK_TEXT,"Place Order").click()
    time.sleep(4)

    # Enter card details
    card_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "name_on_card"))
    )
    card_name_input.send_keys("Test Card")

    card_number_input = driver.find_element(By.NAME, "card_number")
    card_number_input.send_keys("4100 0000 0000")

    card_cvv_input = driver.find_element(By.NAME, "cvc")
    card_cvv_input.send_keys("123")

    card_expiration_input = driver.find_element(By.NAME, "expiry_month")
    card_expiration_input.send_keys("01")

    card_expiration_input_year = driver.find_element(By.NAME, "expiry_year")
    card_expiration_input_year.send_keys("1900")

    # Confirm the order
    confirm_order_button = driver.find_element(By.TAG_NAME, "button")
    confirm_order_button.click()

    success = driver.find_element(By.TAG_NAME, "p")
    print(f"The message {success.text}")
    time.sleep(3)
    driver.quit()
open_link()

