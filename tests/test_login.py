from pages.login_page import LoginPage
from utils.data_loader import load_users
from pytest_html import extras


def test_valid_login(page, extra):
    users = load_users()
    login = LoginPage(page)
    login.open()

    page.screenshot(path="reports/screenshots/login_page.png")
    extra.append(extras.image("screenshots/login_page.png"))

    login.login(users['valid_user']['username'], users['valid_user']['password'])

    page.wait_for_url("**/admin/home")
    page.wait_for_selector("h1:has-text('Panel de administracion')")
    page.screenshot(path="reports/screenshots/home_page.png")
    extra.append(extras.image("screenshots/home_page.png"))

    assert "home" in page.url
