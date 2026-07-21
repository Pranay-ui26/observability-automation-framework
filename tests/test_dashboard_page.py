from locators.dashboard_locators import DashboardLocators


def test_dashboard_loads_successfully(
        authenticated_session,
        dashboard_page):

    dashboard_page.verify_dashboard_is_loaded()


def test_dashboard_summary_widgets(
        authenticated_session,
        dashboard_page):

    summary_widgets = [
        DashboardLocators.STATUS_WIDGET,
        DashboardLocators.FIRING_ALERTS_WIDGET,
        DashboardLocators.OPEN_INCIDENTS_WIDGET,
        DashboardLocators.ERROR_RATE_WIDGET,
        DashboardLocators.P95_LATENCY_WIDGET
    ]

    dashboard_page.verify_widgets_are_displayed(summary_widgets)


def test_dashboard_observability_widgets(
        authenticated_session,
        dashboard_page):

    observability_widgets = [
        DashboardLocators.TRACES_WIDGET,
        DashboardLocators.LOGS_WIDGET,
        DashboardLocators.METRICS_WIDGET,
        DashboardLocators.ERRORS_WIDGET,
        DashboardLocators.SERVICES_WIDGET,
        DashboardLocators.ENDPOINTS_WIDGET,
        DashboardLocators.DB_QUERIES_WIDGET,
        DashboardLocators.ALERTS_WIDGET,
        DashboardLocators.INCIDENTS_WIDGET,
        DashboardLocators.ANOMALIES_WIDGET,
        DashboardLocators.HOSTS_WIDGET,
        DashboardLocators.PODS_WIDGET,
        DashboardLocators.K8S_CLUSTERS_WIDGET,
        DashboardLocators.NETWORK_DEVICES_WIDGET
    ]

    dashboard_page.verify_widgets_are_displayed(observability_widgets)


def test_dashboard_ai_widgets(
        authenticated_session,
        dashboard_page):

    ai_widgets = [
        DashboardLocators.LLM_CALLS_WIDGET,
        DashboardLocators.TOKENS_WIDGET,
        DashboardLocators.AGENTS_WIDGET,
        DashboardLocators.CONVERSATIONS_WIDGET,
        DashboardLocators.MCP_SESSIONS_WIDGET,
        DashboardLocators.RAG_WIDGET,
        DashboardLocators.AI_INSIGHTS_WIDGET
    ]

    dashboard_page.verify_widgets_are_displayed(ai_widgets)


def test_dashboard_topology_widget(
        authenticated_session,
        dashboard_page):

    dashboard_page.verify_widget_is_displayed(
        DashboardLocators.TOPOLOGY_WIDGET
    )


def test_dashboard_controls(
        authenticated_session,
        dashboard_page):

    dashboard_page.verify_time_filter(
        DashboardLocators.TIME_FILTER
    )
    dashboard_page.verify_refresh_button(
        DashboardLocators.REFRESH_BUTTON
    )


def test_dashboard_refresh(
        authenticated_session,
        dashboard_page):

    dashboard_page.refresh_dashboard(
        DashboardLocators.REFRESH_BUTTON
    )
    dashboard_page.verify_dashboard_is_loaded()


def test_recent_dashboards_widgets(
        authenticated_session,
        dashboard_page):

    recent_dashboard_widgets = [
        DashboardLocators.RECENT_DASHBOARDS_WIDGET,
        DashboardLocators.HOST_OVERVIEW_WIDGET,
        DashboardLocators.KUBERNETES_CLUSTER_OVERVIEW_WIDGET,
        DashboardLocators.VIEW_ALL_DASHBOARDS_WIDGET
    ]

    dashboard_page.verify_widgets_are_displayed(recent_dashboard_widgets)


def test_active_alerts_widgets(
        authenticated_session,
        dashboard_page):

    active_alert_widgets = [
        DashboardLocators.ACTIVE_ALERTS_WIDGET,
        DashboardLocators.ALL_QUIET_WIDGET,
        DashboardLocators.NO_ACTIVE_ALERTS_WIDGET
    ]

    dashboard_page.verify_widgets_are_displayed(active_alert_widgets)


def test_host_infrastructure_widgets(
        authenticated_session,
        dashboard_page):

    host_widgets = [
        DashboardLocators.HOST_INFRASTRUCTURE_WIDGET,
        DashboardLocators.ONLINE_WIDGET,
        DashboardLocators.AVG_CPU_WIDGET,
        DashboardLocators.AVG_MEMORY_WIDGET,
        DashboardLocators.CPU_UTILIZATION_WIDGET,
        DashboardLocators.VIEW_HOSTS_WIDGET
    ]

    dashboard_page.verify_widgets_are_displayed(host_widgets)