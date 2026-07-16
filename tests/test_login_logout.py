def test_login(login):

    login.login_to_application()

    login.verify_url_contains("overview")

def test_logout(login, dashboard_page):

    login.login_to_application()

    dashboard_page.profile.logout()