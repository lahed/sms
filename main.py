from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import json

def Login():
    print("Iniciando")
    driver = webdriver.PhantomJS(r"phjs.exe")
    driver.set_window_size(1120, 550)
    driver.get("https://account.xapo.com/")

    print("Iniciando sesión")
    inputEmail = driver.find_element_by_id("user-email")
    inputPin1 = driver.find_element_by_name('pin-number-1')
    inputPin2 = driver.find_element_by_name('pin-number-2')
    inputPin3 = driver.find_element_by_name('pin-number-3')
    inputPin4 = driver.find_element_by_name('pin-number-4')
    elementError = driver.find_element_by_id('login-invalid-pin-message')
    elementError2 = driver.find_element_by_id('login-invalid-message')

    #Relleno campo email
    inputEmail.send_keys(email)
    
    #Relleno Pin1
    inputPin1.send_keys(pin[0])
    
    #Relleno Pin2
    inputPin2.send_keys(pin[1])

    #Relleno Pin3    
    inputPin3.send_keys(pin[2])

    #Relleno Pin4
    inputPin4.send_keys(pin[3])

    #Espero hasta que complete solicitud
    WaitForAjax(driver)

    #Incorrecto
    if elementError.is_displayed() or elementError2.is_displayed():
        print("Credenciales inválidas")
        return

    #Espero hasta que loguee
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_class_name("buy-button"))

    WebDriverWait(driver, 30).until(lambda x: not x.find_element_by_id("loadingMask").is_displayed())

    print("Sesión iniciada")

    print("Ingresando a Security")
    #Clic Menu
    driver.find_element_by_xpath('//*[@id="header-nav-trigger"]').click()

    #Espero a que sea visible el menu
    WaitForVisibleId(driver, 'header-nav-actions')

    driver.find_element_by_xpath('//*[@id="header-nav-actions"]/ul/li[2]/a').click()

    #Espero que cargue pagina Security
    WaitForVisibleId(driver, 'security-save', 30)

    VerifyMobileNumber(driver)

def VerifyMobileNumber(driver):
    #Clic Verify Phone
    driver.find_element_by_xpath('//*[@id="security"]/div/dl/dd[3]/a[1]').click()

    try:
        while (True):
            #selecciono codigo
            selectCodigo = Select(driver.find_element_by_id('header-dlgverifymobile-country'))
            selectCodigo.select_by_value(codigo)

            #Ingreso numero
            driver.find_element_by_id('header-dlgverifymobile-number').send_keys(numero)

            driver.find_element_by_id('header-dlgverifymobile-submit').click()

            WaitForLoading(driver)

            driver.find_element_by_id('header-dlgverifymobilecode-cancel').click()
            print("Enviando Mensaje!!!")
    except KeyboardInterrupt:
        print('Terminado!')

def WaitForAjax(driver, timeout=10):
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return jQuery.active === 0"))

def WaitForLoading(driver, timeout=30):
    WebDriverWait(driver, timeout).until(lambda x: not x.find_element_by_id("loadingMask").is_displayed())

def WaitForVisibleId(driver, id, timeout=10):
    WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_id(id).is_displayed())

if __name__ == "__main__":
    with open('settings.json') as data_file:    
        data = json.load(data_file)

    email = data['email']
    pin = data['pin']

    codigo = data['codigo']
    numero = data['numero']

    Login()