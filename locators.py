from selenium.webdriver.common.by import By

class UrbanRoutesPage:

    payment_method = None
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.XPATH, '//button[@class="button round"]')
    comfort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_field = (By.CLASS_NAME, 'np-button')
    phone_field_popup = (By.ID, 'phone')
    phone_summit_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    code_field = (By.ID, 'code')
    code_summit_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    payment_method_field = (By.XPATH, "//div[@class='pp-button filled']")
    add_card = (By.XPATH, "//div[@class='pp-row disabled']")
    card_number_field = (By.XPATH, "//input[@id='number']")
    card_code_field = (By.XPATH, "//input[@class='card-input'][@id='code']")
    card_blank_field = (By.XPATH, "//div[@class='plc']")
    card_summit_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    payment_method_close_button = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')
    comment_field = (By.ID, 'comment')
    requirements_dropdown = (By.XPATH, "//div[contains(@class,'reqs')]")
    manta_panuelos_slider = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    helado_plus_button = (By.CLASS_NAME, 'counter-plus')
    call_taxi_button = (By.CLASS_NAME, 'smart-button')
    driver_order_details = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[3]/button')
