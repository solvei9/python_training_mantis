def test_login(app):
    if app.session.is_logged_in_as("administrator"):
        app.session.logout()
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
