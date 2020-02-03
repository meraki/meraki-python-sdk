# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki_sdk.decorators import lazy_property
from meraki_sdk.configuration import Configuration
from meraki_sdk.controllers.api_usage_controller import APIUsageController
from meraki_sdk.controllers.action_batches_controller import ActionBatchesController
from meraki_sdk.controllers.admins_controller import AdminsController
from meraki_sdk.controllers.alert_settings_controller import AlertSettingsController
from meraki_sdk.controllers.bluetooth_clients_controller import BluetoothClientsController
from meraki_sdk.controllers.camera_quality_retention_profiles_controller import CameraQualityRetentionProfilesController
from meraki_sdk.controllers.cameras_controller import CamerasController
from meraki_sdk.controllers.clients_controller import ClientsController
from meraki_sdk.controllers.config_templates_controller import ConfigTemplatesController
from meraki_sdk.controllers.connectivity_monitoring_destinations_controller import ConnectivityMonitoringDestinationsController
from meraki_sdk.controllers.content_filtering_categories_controller import ContentFilteringCategoriesController
from meraki_sdk.controllers.content_filtering_rules_controller import ContentFilteringRulesController
from meraki_sdk.controllers.dashboard_branding_policies_controller import DashboardBrandingPoliciesController
from meraki_sdk.controllers.devices_controller import DevicesController
from meraki_sdk.controllers.events_controller import EventsController
from meraki_sdk.controllers.firewalled_services_controller import FirewalledServicesController
from meraki_sdk.controllers.floorplans_controller import FloorplansController
from meraki_sdk.controllers.group_policies_controller import GroupPoliciesController
from meraki_sdk.controllers.http_servers_controller import HTTPServersController
from meraki_sdk.controllers.intrusion_settings_controller import IntrusionSettingsController
from meraki_sdk.controllers.licenses_controller import LicensesController
from meraki_sdk.controllers.link_aggregations_controller import LinkAggregationsController
from meraki_sdk.controllers.mgdhcp_settings_controller import MGDHCPSettingsController
from meraki_sdk.controllers.mglan_settings_controller import MGLANSettingsController
from meraki_sdk.controllers.mg_connectivity_monitoring_destinations_controller import MGConnectivityMonitoringDestinationsController
from meraki_sdk.controllers.mg_port_forwarding_rules_controller import MGPortForwardingRulesController
from meraki_sdk.controllers.mg_subnet_pool_settings_controller import MGSubnetPoolSettingsController
from meraki_sdk.controllers.mg_uplink_settings_controller import MGUplinkSettingsController
from meraki_sdk.controllers.mrl_3_firewall_controller import MRL3FirewallController
from meraki_sdk.controllers.mv_sense_controller import MVSenseController
from meraki_sdk.controllers.mx_11_nat_rules_controller import MX11NATRulesController
from meraki_sdk.controllers.mx_1_many_nat_rules_controller import MX1ManyNATRulesController
from meraki_sdk.controllers.mxl_3_firewall_controller import MXL3FirewallController
from meraki_sdk.controllers.mxl_7_application_categories_controller import MXL7ApplicationCategoriesController
from meraki_sdk.controllers.mxl_7_firewall_controller import MXL7FirewallController
from meraki_sdk.controllers.mxvlan_ports_controller import MXVLANPortsController
from meraki_sdk.controllers.mxvpn_firewall_controller import MXVPNFirewallController
from meraki_sdk.controllers.mx_cellular_firewall_controller import MXCellularFirewallController
from meraki_sdk.controllers.mx_inbound_firewall_controller import MXInboundFirewallController
from meraki_sdk.controllers.mx_port_forwarding_rules_controller import MXPortForwardingRulesController
from meraki_sdk.controllers.mx_static_routes_controller import MXStaticRoutesController
from meraki_sdk.controllers.mx_warm_spare_settings_controller import MXWarmSpareSettingsController
from meraki_sdk.controllers.malware_settings_controller import MalwareSettingsController
from meraki_sdk.controllers.management_interface_settings_controller import ManagementInterfaceSettingsController
from meraki_sdk.controllers.meraki_auth_users_controller import MerakiAuthUsersController
from meraki_sdk.controllers.monitored_media_servers_controller import MonitoredMediaServersController
from meraki_sdk.controllers.named_tag_scope_controller import NamedTagScopeController
from meraki_sdk.controllers.netflow_settings_controller import NetflowSettingsController
from meraki_sdk.controllers.networks_controller import NetworksController
from meraki_sdk.controllers.open_api_spec_controller import OpenAPISpecController
from meraki_sdk.controllers.organizations_controller import OrganizationsController
from meraki_sdk.controllers.pii_controller import PIIController
from meraki_sdk.controllers.radio_settings_controller import RadioSettingsController
from meraki_sdk.controllers.saml_roles_controller import SAMLRolesController
from meraki_sdk.controllers.sm_controller import SMController
from meraki_sdk.controllers.snmp_settings_controller import SNMPSettingsController
from meraki_sdk.controllers.ssids_controller import SsidsController
from meraki_sdk.controllers.security_events_controller import SecurityEventsController
from meraki_sdk.controllers.splash_login_attempts_controller import SplashLoginAttemptsController
from meraki_sdk.controllers.splash_settings_controller import SplashSettingsController
from meraki_sdk.controllers.switch_acls_controller import SwitchAclsController
from meraki_sdk.controllers.switch_port_schedules_controller import SwitchPortSchedulesController
from meraki_sdk.controllers.switch_ports_controller import SwitchPortsController
from meraki_sdk.controllers.switch_profiles_controller import SwitchProfilesController
from meraki_sdk.controllers.switch_settings_controller import SwitchSettingsController
from meraki_sdk.controllers.switch_stacks_controller import SwitchStacksController
from meraki_sdk.controllers.syslog_servers_controller import SyslogServersController
from meraki_sdk.controllers.traffic_analysis_settings_controller import TrafficAnalysisSettingsController
from meraki_sdk.controllers.traffic_shaping_controller import TrafficShapingController
from meraki_sdk.controllers.uplink_settings_controller import UplinkSettingsController
from meraki_sdk.controllers.vlans_controller import VlansController
from meraki_sdk.controllers.webhook_logs_controller import WebhookLogsController
from meraki_sdk.controllers.wireless_health_controller import WirelessHealthController
from meraki_sdk.controllers.wireless_settings_controller import WirelessSettingsController


class MerakiSdkClient(object):

    config = Configuration

    @lazy_property
    def api_usage(self):
        return APIUsageController()

    @lazy_property
    def action_batches(self):
        return ActionBatchesController()

    @lazy_property
    def admins(self):
        return AdminsController()

    @lazy_property
    def alert_settings(self):
        return AlertSettingsController()

    @lazy_property
    def bluetooth_clients(self):
        return BluetoothClientsController()

    @lazy_property
    def camera_quality_retention_profiles(self):
        return CameraQualityRetentionProfilesController()

    @lazy_property
    def cameras(self):
        return CamerasController()

    @lazy_property
    def clients(self):
        return ClientsController()

    @lazy_property
    def config_templates(self):
        return ConfigTemplatesController()

    @lazy_property
    def connectivity_monitoring_destinations(self):
        return ConnectivityMonitoringDestinationsController()

    @lazy_property
    def content_filtering_categories(self):
        return ContentFilteringCategoriesController()

    @lazy_property
    def content_filtering_rules(self):
        return ContentFilteringRulesController()

    @lazy_property
    def dashboard_branding_policies(self):
        return DashboardBrandingPoliciesController()

    @lazy_property
    def devices(self):
        return DevicesController()

    @lazy_property
    def events(self):
        return EventsController()

    @lazy_property
    def firewalled_services(self):
        return FirewalledServicesController()

    @lazy_property
    def floorplans(self):
        return FloorplansController()

    @lazy_property
    def group_policies(self):
        return GroupPoliciesController()

    @lazy_property
    def http_servers(self):
        return HTTPServersController()

    @lazy_property
    def intrusion_settings(self):
        return IntrusionSettingsController()

    @lazy_property
    def licenses(self):
        return LicensesController()

    @lazy_property
    def link_aggregations(self):
        return LinkAggregationsController()

    @lazy_property
    def mg_dhcp_settings(self):
        return MGDHCPSettingsController()

    @lazy_property
    def mg_lan_settings(self):
        return MGLANSettingsController()

    @lazy_property
    def mg_connectivity_monitoring_destinations(self):
        return MGConnectivityMonitoringDestinationsController()

    @lazy_property
    def mg_port_forwarding_rules(self):
        return MGPortForwardingRulesController()

    @lazy_property
    def mg_subnet_pool_settings(self):
        return MGSubnetPoolSettingsController()

    @lazy_property
    def mg_uplink_settings(self):
        return MGUplinkSettingsController()

    @lazy_property
    def mr_l_3_firewall(self):
        return MRL3FirewallController()

    @lazy_property
    def mv_sense(self):
        return MVSenseController()

    @lazy_property
    def mx_1_1_nat_rules(self):
        return MX11NATRulesController()

    @lazy_property
    def mx_1_many_nat_rules(self):
        return MX1ManyNATRulesController()

    @lazy_property
    def mx_l_3_firewall(self):
        return MXL3FirewallController()

    @lazy_property
    def mx_l_7_application_categories(self):
        return MXL7ApplicationCategoriesController()

    @lazy_property
    def mx_l_7_firewall(self):
        return MXL7FirewallController()

    @lazy_property
    def mx_vlan_ports(self):
        return MXVLANPortsController()

    @lazy_property
    def mx_vpn_firewall(self):
        return MXVPNFirewallController()

    @lazy_property
    def mx_cellular_firewall(self):
        return MXCellularFirewallController()

    @lazy_property
    def mx_inbound_firewall(self):
        return MXInboundFirewallController()

    @lazy_property
    def mx_port_forwarding_rules(self):
        return MXPortForwardingRulesController()

    @lazy_property
    def mx_static_routes(self):
        return MXStaticRoutesController()

    @lazy_property
    def mx_warm_spare_settings(self):
        return MXWarmSpareSettingsController()

    @lazy_property
    def malware_settings(self):
        return MalwareSettingsController()

    @lazy_property
    def management_interface_settings(self):
        return ManagementInterfaceSettingsController()

    @lazy_property
    def meraki_auth_users(self):
        return MerakiAuthUsersController()

    @lazy_property
    def monitored_media_servers(self):
        return MonitoredMediaServersController()

    @lazy_property
    def named_tag_scope(self):
        return NamedTagScopeController()

    @lazy_property
    def netflow_settings(self):
        return NetflowSettingsController()

    @lazy_property
    def networks(self):
        return NetworksController()

    @lazy_property
    def open_api_spec(self):
        return OpenAPISpecController()

    @lazy_property
    def organizations(self):
        return OrganizationsController()

    @lazy_property
    def pii(self):
        return PIIController()

    @lazy_property
    def radio_settings(self):
        return RadioSettingsController()

    @lazy_property
    def saml_roles(self):
        return SAMLRolesController()

    @lazy_property
    def sm(self):
        return SMController()

    @lazy_property
    def snmp_settings(self):
        return SNMPSettingsController()

    @lazy_property
    def ssids(self):
        return SsidsController()

    @lazy_property
    def security_events(self):
        return SecurityEventsController()

    @lazy_property
    def splash_login_attempts(self):
        return SplashLoginAttemptsController()

    @lazy_property
    def splash_settings(self):
        return SplashSettingsController()

    @lazy_property
    def switch_acls(self):
        return SwitchAclsController()

    @lazy_property
    def switch_port_schedules(self):
        return SwitchPortSchedulesController()

    @lazy_property
    def switch_ports(self):
        return SwitchPortsController()

    @lazy_property
    def switch_profiles(self):
        return SwitchProfilesController()

    @lazy_property
    def switch_settings(self):
        return SwitchSettingsController()

    @lazy_property
    def switch_stacks(self):
        return SwitchStacksController()

    @lazy_property
    def syslog_servers(self):
        return SyslogServersController()

    @lazy_property
    def traffic_analysis_settings(self):
        return TrafficAnalysisSettingsController()

    @lazy_property
    def traffic_shaping(self):
        return TrafficShapingController()

    @lazy_property
    def uplink_settings(self):
        return UplinkSettingsController()

    @lazy_property
    def vlans(self):
        return VlansController()

    @lazy_property
    def webhook_logs(self):
        return WebhookLogsController()

    @lazy_property
    def wireless_health(self):
        return WirelessHealthController()

    @lazy_property
    def wireless_settings(self):
        return WirelessSettingsController()


    def __init__(self,
                 x_cisco_meraki_api_key=None):
        if x_cisco_meraki_api_key is not None:
            Configuration.x_cisco_meraki_api_key = x_cisco_meraki_api_key

