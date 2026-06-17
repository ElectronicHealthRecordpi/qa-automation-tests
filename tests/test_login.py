from pages.login_page import LoginPage
from utils.data_loader import load_users
from pytest_html import extras


def test_valid_admin_login(page, extra):
    users = load_users()
    login = LoginPage(page)
    login.open()

    page.screenshot(path="reports/screenshots/login_page.png")
    extra.append(extras.image("screenshots/login_page.png"))

    login.login(users['valid_admin_user']['username'], users['valid_admin_user']['password'])

    page.wait_for_url("**/admin/home")
    page.wait_for_selector("h1:has-text('Panel de administracion')")
    page.screenshot(path="reports/screenshots/home_page.png")
    extra.append(extras.image("screenshots/home_page.png"))

    assert "home" in page.url

def test_valid_patient_login(page, extra):
    users = load_users()
    login = LoginPage(page)
    login.open()

    page.screenshot(path="reports/screenshots/login_page_patient.png")
    extra.append(extras.image("screenshots/login_page_patient.png"))

    login.login(users['valid_patient_user']['username'], users['valid_patient_user']['password'])

    page.wait_for_url("**/patient/home")
    page.wait_for_selector("h1:has-text('Bienvenido,')")
    page.screenshot(path="reports/screenshots/home_page_patient.png")
    extra.append(extras.image("screenshots/home_page_patient.png"))

    assert "patient" in page.url
def test_valid_doctor_login(page, extra):
    users = load_users()
    login = LoginPage(page)
    login.open()

    page.screenshot(path="reports/screenshots/login_page_doctor.png")
    extra.append(extras.image("screenshots/login_page_doctor.png"))

    login.login(users['valid_doctor_user']['username'], users['valid_doctor_user']['password'])

    page.wait_for_url("**/doctor/home")
    page.wait_for_selector("h1:has-text('home')")
    page.screenshot(path="reports/screenshots/home_page_doctor.png")
    extra.append(extras.image("screenshots/home_page_doctor.png"))

    assert "home" in page.url

def test_invalid_login(page, extra):
    users = load_users()
    login = LoginPage(page)
    login.open()

    page.screenshot(path="reports/screenshots/login_page_invalid.png")
    extra.append(extras.image("screenshots/login_page_invalid.png"))
    login.login(users['invalid_user']['username'], users['invalid_user']['password'])
    page.wait_for_selector("span:has-text('Credenciales')")
    page.screenshot(path="reports/screenshots/login_page_invalid_attempt.png")
    extra.append(extras.image("screenshots/login_page_invalid_attempt.png"))
def test_empty_login(page, extra):
    login = LoginPage(page)
    login.open()

    page.screenshot(path="reports/screenshots/login_page_empty.png")
    extra.append(extras.image("screenshots/login_page_empty.png"))
    login.login("", "")
    page.wait_for_selector("span:has-text('Por favor, completa todos los campos.')")
    page.screenshot(path="reports/screenshots/login_page_empty_attempt.png")
    extra.append(extras.image("screenshots/login_page_empty_attempt.png"))
def test_password_is_less_than_6_characters(page, extra):
    login = LoginPage(page)
    login.open()

    page.screenshot(path="reports/screenshots/login_page_short_password.png")
    extra.append(extras.image("screenshots/login_page_short_password.png"))
    login.login("valid_user", "123")
    page.wait_for_selector("span:has-text('La contraseña debe tener al menos 6 caracteres.')")
    page.screenshot(path="reports/screenshots/login_page_short_password_attempt.png")
    extra.append(extras.image("screenshots/login_page_short_password_attempt.png"))
