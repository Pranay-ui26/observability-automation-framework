def test_dashboard_loads_successfully(
        authenticated_session,
        dashboard_page):

    dashboard_page.verify_dashboard_is_loaded()

    dashboard_page.verify_dashboard_container()

def test_dashboard_widgets(authenticated_session, dashboard_page):

    dashboard_page.verify_dashboard_is_loaded()

    dashboard_page.verify_topology_widget_is_displayed()

    dashboard_page.verify_active_alerts_widget_is_displayed()

    dashboard_page.verify_infrastructure_health_widget_is_displayed()

    dashboard_page.verify_ai_insights_widget_is_displayed()

def test_dashboard_time_filter_displayed(
        authenticated_session,
        dashboard_page):

    dashboard_page.verify_time_filter()

def test_dashboard_refresh(
        authenticated_session,
        dashboard_page):

    dashboard_page.refresh_dashboard()

    dashboard_page.verify_dashboard_is_loaded()