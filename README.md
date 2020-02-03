**Note: This SDK is being deprecated in favor of the library maintained at [https://github.com/meraki/dashboard-api-python/](https://github.com/meraki/dashboard-api-python/).**


# Getting started

The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.

> Date: 03 February, 2020
>
> [What's New](https://meraki.io/whats-new/)

---

[API Documentation](https://meraki.io/api)

[Community Support](https://meraki.io/community)

[Meraki Homepage](https://www.meraki.com)


## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Meraki-Python)


## How to Use

The following section explains how to use the Meraki SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Meraki-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Meraki-Python&projectName=meraki_sdk)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Meraki-Python&projectName=meraki_sdk)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Meraki-Python&projectName=meraki_sdk)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Meraki-Python&libraryName=meraki_sdk.meraki_sdk_client&projectName=meraki_sdk&className=MerakiSdkClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Meraki-Python&libraryName=meraki_sdk.meraki_sdk_client&projectName=meraki_sdk&className=MerakiSdkClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| x_cisco_meraki_api_key | TODO: add a description |



API client can be initialized as following.

```python
# Configuration parameters and credentials
x_cisco_meraki_api_key = 'x_cisco_meraki_api_key'

client = MerakiSdkClient(x_cisco_meraki_api_key)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [APIUsageController](#api_usage_controller)
* [ActionBatchesController](#action_batches_controller)
* [AdminsController](#admins_controller)
* [AlertSettingsController](#alert_settings_controller)
* [BluetoothClientsController](#bluetooth_clients_controller)
* [CameraQualityRetentionProfilesController](#camera_quality_retention_profiles_controller)
* [CamerasController](#cameras_controller)
* [ClientsController](#clients_controller)
* [ConfigTemplatesController](#config_templates_controller)
* [ConnectivityMonitoringDestinationsController](#connectivity_monitoring_destinations_controller)
* [ContentFilteringCategoriesController](#content_filtering_categories_controller)
* [ContentFilteringRulesController](#content_filtering_rules_controller)
* [DashboardBrandingPoliciesController](#dashboard_branding_policies_controller)
* [DevicesController](#devices_controller)
* [EventsController](#events_controller)
* [FirewalledServicesController](#firewalled_services_controller)
* [FloorplansController](#floorplans_controller)
* [GroupPoliciesController](#group_policies_controller)
* [HTTPServersController](#http_servers_controller)
* [IntrusionSettingsController](#intrusion_settings_controller)
* [LicensesController](#licenses_controller)
* [LinkAggregationsController](#link_aggregations_controller)
* [MGDHCPSettingsController](#mgdhcp_settings_controller)
* [MGLANSettingsController](#mglan_settings_controller)
* [MGConnectivityMonitoringDestinationsController](#mg_connectivity_monitoring_destinations_controller)
* [MGPortForwardingRulesController](#mg_port_forwarding_rules_controller)
* [MGSubnetPoolSettingsController](#mg_subnet_pool_settings_controller)
* [MGUplinkSettingsController](#mg_uplink_settings_controller)
* [MRL3FirewallController](#mrl3_firewall_controller)
* [MVSenseController](#mv_sense_controller)
* [MX11NATRulesController](#mx11_nat_rules_controller)
* [MX1ManyNATRulesController](#mx1_many_nat_rules_controller)
* [MXL3FirewallController](#mxl3_firewall_controller)
* [MXL7ApplicationCategoriesController](#mxl7_application_categories_controller)
* [MXL7FirewallController](#mxl7_firewall_controller)
* [MXVLANPortsController](#mxvlan_ports_controller)
* [MXVPNFirewallController](#mxvpn_firewall_controller)
* [MXCellularFirewallController](#mx_cellular_firewall_controller)
* [MXInboundFirewallController](#mx_inbound_firewall_controller)
* [MXPortForwardingRulesController](#mx_port_forwarding_rules_controller)
* [MXStaticRoutesController](#mx_static_routes_controller)
* [MXWarmSpareSettingsController](#mx_warm_spare_settings_controller)
* [MalwareSettingsController](#malware_settings_controller)
* [ManagementInterfaceSettingsController](#management_interface_settings_controller)
* [MerakiAuthUsersController](#meraki_auth_users_controller)
* [MonitoredMediaServersController](#monitored_media_servers_controller)
* [NamedTagScopeController](#named_tag_scope_controller)
* [NetflowSettingsController](#netflow_settings_controller)
* [NetworksController](#networks_controller)
* [OpenAPISpecController](#open_api_spec_controller)
* [OrganizationsController](#organizations_controller)
* [PIIController](#pii_controller)
* [RadioSettingsController](#radio_settings_controller)
* [SAMLRolesController](#saml_roles_controller)
* [SMController](#sm_controller)
* [SNMPSettingsController](#snmp_settings_controller)
* [SsidsController](#ssids_controller)
* [SecurityEventsController](#security_events_controller)
* [SplashLoginAttemptsController](#splash_login_attempts_controller)
* [SplashSettingsController](#splash_settings_controller)
* [SwitchAclsController](#switch_acls_controller)
* [SwitchPortSchedulesController](#switch_port_schedules_controller)
* [SwitchPortsController](#switch_ports_controller)
* [SwitchProfilesController](#switch_profiles_controller)
* [SwitchSettingsController](#switch_settings_controller)
* [SwitchStacksController](#switch_stacks_controller)
* [SyslogServersController](#syslog_servers_controller)
* [TrafficAnalysisSettingsController](#traffic_analysis_settings_controller)
* [TrafficShapingController](#traffic_shaping_controller)
* [UplinkSettingsController](#uplink_settings_controller)
* [VlansController](#vlans_controller)
* [WebhookLogsController](#webhook_logs_controller)
* [WirelessHealthController](#wireless_health_controller)
* [WirelessSettingsController](#wireless_settings_controller)

## <a name="api_usage_controller"></a>![Class: ](https://apidocs.io/img/class.png ".APIUsageController") APIUsageController

### Get controller instance

An instance of the ``` APIUsageController ``` class can be accessed from the API Client.

```python
 api_usage_controller = client.api_usage
```

### <a name="get_organization_api_requests"></a>![Method: ](https://apidocs.io/img/method.png ".APIUsageController.get_organization_api_requests") get_organization_api_requests

> List the API requests made by an organization

```python
def get_organization_api_requests(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 31 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| adminId |  ``` Optional ```  | Filter the results by the ID of the admin who made the API requests |
| path |  ``` Optional ```  | Filter the results by the path of the API requests |
| method |  ``` Optional ```  | Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE') |
| responseCode |  ``` Optional ```  | Filter the results by the response code of the API requests |
| sourceIp |  ``` Optional ```  | Filter the results by the IP address of the originating API request |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 13.8189657236538
collect['timespan'] = timespan

per_page = 13
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before

admin_id = 'adminId'
collect['admin_id'] = admin_id

path = 'path'
collect['path'] = path

method = 'method'
collect['method'] = method

response_code = 13
collect['response_code'] = response_code

source_ip = 'sourceIp'
collect['source_ip'] = source_ip


result = api_usage_controller.get_organization_api_requests(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="action_batches_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ActionBatchesController") ActionBatchesController

### Get controller instance

An instance of the ``` ActionBatchesController ``` class can be accessed from the API Client.

```python
 action_batches_controller = client.action_batches
```

### <a name="create_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.create_organization_action_batch") create_organization_action_batch

> Create an action batch

```python
def create_organization_action_batch(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationActionBatch |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_action_batch = CreateOrganizationActionBatchModel()
collect['create_organization_action_batch'] = create_organization_action_batch


result = action_batches_controller.create_organization_action_batch(collect)

```


### <a name="get_organization_action_batches"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.get_organization_action_batches") get_organization_action_batches

> Return the list of action batches in the organization

```python
def get_organization_action_batches(self,
                                        organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = action_batches_controller.get_organization_action_batches(organization_id)

```


### <a name="get_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.get_organization_action_batch") get_organization_action_batch

> Return an action batch

```python
def get_organization_action_batch(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| actionBatchId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

action_batch_id = 'actionBatchId'
collect['action_batch_id'] = action_batch_id


result = action_batches_controller.get_organization_action_batch(collect)

```


### <a name="delete_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.delete_organization_action_batch") delete_organization_action_batch

> Delete an action batch

```python
def delete_organization_action_batch(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| actionBatchId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

action_batch_id = 'actionBatchId'
collect['action_batch_id'] = action_batch_id


action_batches_controller.delete_organization_action_batch(collect)

```


### <a name="update_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.update_organization_action_batch") update_organization_action_batch

> Update an action batch

```python
def update_organization_action_batch(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| actionBatchId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationActionBatch |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

action_batch_id = 'actionBatchId'
collect['action_batch_id'] = action_batch_id

update_organization_action_batch = UpdateOrganizationActionBatchModel()
collect['update_organization_action_batch'] = update_organization_action_batch


result = action_batches_controller.update_organization_action_batch(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="admins_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AdminsController") AdminsController

### Get controller instance

An instance of the ``` AdminsController ``` class can be accessed from the API Client.

```python
 admins_controller = client.admins
```

### <a name="get_organization_admins"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.get_organization_admins") get_organization_admins

> List the dashboard administrators in this organization

```python
def get_organization_admins(self,
                                organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = admins_controller.get_organization_admins(organization_id)

```


### <a name="create_organization_admin"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.create_organization_admin") create_organization_admin

> Create a new dashboard administrator

```python
def create_organization_admin(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationAdmin |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_admin = CreateOrganizationAdminModel()
collect['create_organization_admin'] = create_organization_admin


result = admins_controller.create_organization_admin(collect)

```


### <a name="update_organization_admin"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.update_organization_admin") update_organization_admin

> Update an administrator

```python
def update_organization_admin(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationAdmin |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

id = 'id'
collect['id'] = id

update_organization_admin = UpdateOrganizationAdminModel()
collect['update_organization_admin'] = update_organization_admin


result = admins_controller.update_organization_admin(collect)

```


### <a name="delete_organization_admin"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.delete_organization_admin") delete_organization_admin

> Revoke all access for a dashboard administrator within this organization

```python
def delete_organization_admin(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

id = 'id'
collect['id'] = id


admins_controller.delete_organization_admin(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="alert_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AlertSettingsController") AlertSettingsController

### Get controller instance

An instance of the ``` AlertSettingsController ``` class can be accessed from the API Client.

```python
 alert_settings_controller = client.alert_settings
```

### <a name="get_network_alert_settings"></a>![Method: ](https://apidocs.io/img/method.png ".AlertSettingsController.get_network_alert_settings") get_network_alert_settings

> Return the alert configuration for this network

```python
def get_network_alert_settings(self,
                                   network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = alert_settings_controller.get_network_alert_settings(network_id)

```


### <a name="update_network_alert_settings"></a>![Method: ](https://apidocs.io/img/method.png ".AlertSettingsController.update_network_alert_settings") update_network_alert_settings

> Update the alert configuration for this network

```python
def update_network_alert_settings(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkAlertSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_alert_settings = UpdateNetworkAlertSettingsModel()
collect['update_network_alert_settings'] = update_network_alert_settings


result = alert_settings_controller.update_network_alert_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="bluetooth_clients_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BluetoothClientsController") BluetoothClientsController

### Get controller instance

An instance of the ``` BluetoothClientsController ``` class can be accessed from the API Client.

```python
 bluetooth_clients_controller = client.bluetooth_clients
```

### <a name="get_network_bluetooth_clients"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothClientsController.get_network_bluetooth_clients") get_network_bluetooth_clients

> List the Bluetooth clients seen by APs in this network

```python
def get_network_bluetooth_clients(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 7 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| includeConnectivityHistory |  ``` Optional ```  | Include the connectivity history for this client |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

timespan = 13.8189657236538
collect['timespan'] = timespan

per_page = 13
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before

include_connectivity_history = False
collect['include_connectivity_history'] = include_connectivity_history


result = bluetooth_clients_controller.get_network_bluetooth_clients(collect)

```


### <a name="get_network_bluetooth_client"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothClientsController.get_network_bluetooth_client") get_network_bluetooth_client

> Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.

```python
def get_network_bluetooth_client(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| bluetoothClientId |  ``` Required ```  | TODO: Add a parameter description |
| includeConnectivityHistory |  ``` Optional ```  | Include the connectivity history for this client |
| connectivityHistoryTimespan |  ``` Optional ```  | The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

bluetooth_client_id = 'bluetoothClientId'
collect['bluetooth_client_id'] = bluetooth_client_id

include_connectivity_history = False
collect['include_connectivity_history'] = include_connectivity_history

connectivity_history_timespan = 13
collect['connectivity_history_timespan'] = connectivity_history_timespan


result = bluetooth_clients_controller.get_network_bluetooth_client(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="camera_quality_retention_profiles_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CameraQualityRetentionProfilesController") CameraQualityRetentionProfilesController

### Get controller instance

An instance of the ``` CameraQualityRetentionProfilesController ``` class can be accessed from the API Client.

```python
 camera_quality_retention_profiles_controller = client.camera_quality_retention_profiles
```

### <a name="get_network_camera_quality_retention_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.get_network_camera_quality_retention_profiles") get_network_camera_quality_retention_profiles

> List the quality retention profiles for this network

```python
def get_network_camera_quality_retention_profiles(self,
                                                      network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = camera_quality_retention_profiles_controller.get_network_camera_quality_retention_profiles(network_id)

```


### <a name="create_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.create_network_camera_quality_retention_profile") create_network_camera_quality_retention_profile

> Creates new quality retention profile for this network.

```python
def create_network_camera_quality_retention_profile(self,
                                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkCameraQualityRetentionProfile |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_camera_quality_retention_profile = CreateNetworkCameraQualityRetentionProfileModel()
collect['create_network_camera_quality_retention_profile'] = create_network_camera_quality_retention_profile


result = camera_quality_retention_profiles_controller.create_network_camera_quality_retention_profile(collect)

```


### <a name="get_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.get_network_camera_quality_retention_profile") get_network_camera_quality_retention_profile

> Retrieve a single quality retention profile

```python
def get_network_camera_quality_retention_profile(self,
                                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qualityRetentionProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

quality_retention_profile_id = 'qualityRetentionProfileId'
collect['quality_retention_profile_id'] = quality_retention_profile_id


result = camera_quality_retention_profiles_controller.get_network_camera_quality_retention_profile(collect)

```


### <a name="update_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.update_network_camera_quality_retention_profile") update_network_camera_quality_retention_profile

> Update an existing quality retention profile for this network.

```python
def update_network_camera_quality_retention_profile(self,
                                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qualityRetentionProfileId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCameraQualityRetentionProfile |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

quality_retention_profile_id = 'qualityRetentionProfileId'
collect['quality_retention_profile_id'] = quality_retention_profile_id

update_network_camera_quality_retention_profile = UpdateNetworkCameraQualityRetentionProfileModel()
collect['update_network_camera_quality_retention_profile'] = update_network_camera_quality_retention_profile


result = camera_quality_retention_profiles_controller.update_network_camera_quality_retention_profile(collect)

```


### <a name="delete_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.delete_network_camera_quality_retention_profile") delete_network_camera_quality_retention_profile

> Delete an existing quality retention profile for this network.

```python
def delete_network_camera_quality_retention_profile(self,
                                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qualityRetentionProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

quality_retention_profile_id = 'qualityRetentionProfileId'
collect['quality_retention_profile_id'] = quality_retention_profile_id


camera_quality_retention_profiles_controller.delete_network_camera_quality_retention_profile(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="cameras_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CamerasController") CamerasController

### Get controller instance

An instance of the ``` CamerasController ``` class can be accessed from the API Client.

```python
 cameras_controller = client.cameras
```

### <a name="get_device_camera_quality_and_retention_settings"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.get_device_camera_quality_and_retention_settings") get_device_camera_quality_and_retention_settings

> Returns quality and retention settings for the given camera

```python
def get_device_camera_quality_and_retention_settings(self,
                                                         serial)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
serial = 'serial'

result = cameras_controller.get_device_camera_quality_and_retention_settings(serial)

```


### <a name="update_device_camera_quality_and_retention_settings"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.update_device_camera_quality_and_retention_settings") update_device_camera_quality_and_retention_settings

> Update quality and retention settings for the given camera

```python
def update_device_camera_quality_and_retention_settings(self,
                                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceCameraQualityAndRetentionSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

update_device_camera_quality_and_retention_settings = UpdateDeviceCameraQualityAndRetentionSettingsModel()
collect['update_device_camera_quality_and_retention_settings'] = update_device_camera_quality_and_retention_settings


result = cameras_controller.update_device_camera_quality_and_retention_settings(collect)

```


### <a name="get_network_camera_schedules"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.get_network_camera_schedules") get_network_camera_schedules

> Returns a list of all camera recording schedules.

```python
def get_network_camera_schedules(self,
                                     network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = cameras_controller.get_network_camera_schedules(network_id)

```


### <a name="generate_network_camera_snapshot"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.generate_network_camera_snapshot") generate_network_camera_snapshot

> Generate a snapshot of what the camera sees at the specified time and return a link to that image.

```python
def generate_network_camera_snapshot(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| generateNetworkCameraSnapshot |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

generate_network_camera_snapshot = GenerateNetworkCameraSnapshotModel()
collect['generate_network_camera_snapshot'] = generate_network_camera_snapshot


result = cameras_controller.generate_network_camera_snapshot(collect)

```


### <a name="get_network_camera_video_link"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.get_network_camera_video_link") get_network_camera_video_link

> Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

```python
def get_network_camera_video_link(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| timestamp |  ``` Optional ```  | [optional] The video link will start at this timestamp. The timestamp is in UNIX Epoch time (milliseconds). If no timestamp is specified, we will assume current time. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

timestamp = 'timestamp'
collect['timestamp'] = timestamp


result = cameras_controller.get_network_camera_video_link(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="clients_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ClientsController") ClientsController

### Get controller instance

An instance of the ``` ClientsController ``` class can be accessed from the API Client.

```python
 clients_controller = client.clients
```

### <a name="get_device_clients"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_device_clients") get_device_clients

> List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.

```python
def get_device_clients(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

t_0 = 't0'
collect['t_0'] = t_0

timespan = 227.095792497087
collect['timespan'] = timespan


result = clients_controller.get_device_clients(collect)

```


### <a name="get_network_clients"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_clients") get_network_clients

> List the clients that have used this network in the timespan

```python
def get_network_clients(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

timespan = 227.095792497087
collect['timespan'] = timespan

per_page = 227
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = clients_controller.get_network_clients(collect)

```


### <a name="provision_network_clients"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.provision_network_clients") provision_network_clients

> Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.

```python
def provision_network_clients(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| provisionNetworkClients |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

provision_network_clients = ProvisionNetworkClientsModel()
collect['provision_network_clients'] = provision_network_clients


result = clients_controller.provision_network_clients(collect)

```


### <a name="get_network_client"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client") get_network_client

> Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id


result = clients_controller.get_network_client(collect)

```


### <a name="get_network_client_events"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_events") get_network_client_events

> Return the events associated with this client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client_events(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 100. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

per_page = 227
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = clients_controller.get_network_client_events(collect)

```


### <a name="get_network_client_latency_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_latency_history") get_network_client_latency_history

> Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.

```python
def get_network_client_latency_history(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 791 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 791 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day. |
| resolution |  ``` Optional ```  | The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 227.095792497087
collect['timespan'] = timespan

resolution = 227
collect['resolution'] = resolution


result = clients_controller.get_network_client_latency_history(collect)

```


### <a name="get_network_client_policy"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_policy") get_network_client_policy

> Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client_policy(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id


result = clients_controller.get_network_client_policy(collect)

```


### <a name="update_network_client_policy"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.update_network_client_policy") update_network_client_policy

> Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def update_network_client_policy(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkClientPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

update_network_client_policy = UpdateNetworkClientPolicyModel()
collect['update_network_client_policy'] = update_network_client_policy


result = clients_controller.update_network_client_policy(collect)

```


### <a name="get_network_client_splash_authorization_status"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_splash_authorization_status") get_network_client_splash_authorization_status

> Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client_splash_authorization_status(self,
                                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id


result = clients_controller.get_network_client_splash_authorization_status(collect)

```


### <a name="update_network_client_splash_authorization_status"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.update_network_client_splash_authorization_status") update_network_client_splash_authorization_status

> Update a client's splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def update_network_client_splash_authorization_status(self,
                                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkClientSplashAuthorizationStatus |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

update_network_client_splash_authorization_status = UpdateNetworkClientSplashAuthorizationStatusModel()
collect['update_network_client_splash_authorization_status'] = update_network_client_splash_authorization_status


result = clients_controller.update_network_client_splash_authorization_status(collect)

```


### <a name="get_network_client_traffic_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_traffic_history") get_network_client_traffic_history

> Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client_traffic_history(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

per_page = 227
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = clients_controller.get_network_client_traffic_history(collect)

```


### <a name="get_network_client_usage_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_usage_history") get_network_client_usage_history

> Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client_usage_history(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id


result = clients_controller.get_network_client_usage_history(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="config_templates_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConfigTemplatesController") ConfigTemplatesController

### Get controller instance

An instance of the ``` ConfigTemplatesController ``` class can be accessed from the API Client.

```python
 config_templates_controller = client.config_templates
```

### <a name="get_organization_config_templates"></a>![Method: ](https://apidocs.io/img/method.png ".ConfigTemplatesController.get_organization_config_templates") get_organization_config_templates

> List the configuration templates for this organization

```python
def get_organization_config_templates(self,
                                          organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = config_templates_controller.get_organization_config_templates(organization_id)

```


### <a name="delete_organization_config_template"></a>![Method: ](https://apidocs.io/img/method.png ".ConfigTemplatesController.delete_organization_config_template") delete_organization_config_template

> Remove a configuration template

```python
def delete_organization_config_template(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| configTemplateId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

config_template_id = 'configTemplateId'
collect['config_template_id'] = config_template_id


config_templates_controller.delete_organization_config_template(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="connectivity_monitoring_destinations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConnectivityMonitoringDestinationsController") ConnectivityMonitoringDestinationsController

### Get controller instance

An instance of the ``` ConnectivityMonitoringDestinationsController ``` class can be accessed from the API Client.

```python
 connectivity_monitoring_destinations_controller = client.connectivity_monitoring_destinations
```

### <a name="get_network_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".ConnectivityMonitoringDestinationsController.get_network_connectivity_monitoring_destinations") get_network_connectivity_monitoring_destinations

> Return the connectivity testing destinations for an MX network

```python
def get_network_connectivity_monitoring_destinations(self,
                                                         network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = connectivity_monitoring_destinations_controller.get_network_connectivity_monitoring_destinations(network_id)

```


### <a name="update_network_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".ConnectivityMonitoringDestinationsController.update_network_connectivity_monitoring_destinations") update_network_connectivity_monitoring_destinations

> Update the connectivity testing destinations for an MX network

```python
def update_network_connectivity_monitoring_destinations(self,
                                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkConnectivityMonitoringDestinations |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_connectivity_monitoring_destinations = UpdateNetworkConnectivityMonitoringDestinationsModel()
collect['update_network_connectivity_monitoring_destinations'] = update_network_connectivity_monitoring_destinations


result = connectivity_monitoring_destinations_controller.update_network_connectivity_monitoring_destinations(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="content_filtering_categories_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ContentFilteringCategoriesController") ContentFilteringCategoriesController

### Get controller instance

An instance of the ``` ContentFilteringCategoriesController ``` class can be accessed from the API Client.

```python
 content_filtering_categories_controller = client.content_filtering_categories
```

### <a name="get_network_content_filtering_categories"></a>![Method: ](https://apidocs.io/img/method.png ".ContentFilteringCategoriesController.get_network_content_filtering_categories") get_network_content_filtering_categories

> List all available content filtering categories for an MX network

```python
def get_network_content_filtering_categories(self,
                                                 network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = content_filtering_categories_controller.get_network_content_filtering_categories(network_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="content_filtering_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ContentFilteringRulesController") ContentFilteringRulesController

### Get controller instance

An instance of the ``` ContentFilteringRulesController ``` class can be accessed from the API Client.

```python
 content_filtering_rules_controller = client.content_filtering_rules
```

### <a name="get_network_content_filtering"></a>![Method: ](https://apidocs.io/img/method.png ".ContentFilteringRulesController.get_network_content_filtering") get_network_content_filtering

> Return the content filtering settings for an MX network

```python
def get_network_content_filtering(self,
                                      network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = content_filtering_rules_controller.get_network_content_filtering(network_id)

```


### <a name="update_network_content_filtering"></a>![Method: ](https://apidocs.io/img/method.png ".ContentFilteringRulesController.update_network_content_filtering") update_network_content_filtering

> Update the content filtering settings for an MX network

```python
def update_network_content_filtering(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkContentFiltering |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_content_filtering = UpdateNetworkContentFilteringModel()
collect['update_network_content_filtering'] = update_network_content_filtering


result = content_filtering_rules_controller.update_network_content_filtering(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="dashboard_branding_policies_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DashboardBrandingPoliciesController") DashboardBrandingPoliciesController

### Get controller instance

An instance of the ``` DashboardBrandingPoliciesController ``` class can be accessed from the API Client.

```python
 dashboard_branding_policies_controller = client.dashboard_branding_policies
```

### <a name="get_organization_branding_policies"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.get_organization_branding_policies") get_organization_branding_policies

> List the branding policies of an organization

```python
def get_organization_branding_policies(self,
                                           organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = dashboard_branding_policies_controller.get_organization_branding_policies(organization_id)

```


### <a name="create_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.create_organization_branding_policy") create_organization_branding_policy

> Add a new branding policy to an organization

```python
def create_organization_branding_policy(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationBrandingPolicy |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_branding_policy = CreateOrganizationBrandingPolicyModel()
collect['create_organization_branding_policy'] = create_organization_branding_policy


result = dashboard_branding_policies_controller.create_organization_branding_policy(collect)

```


### <a name="get_organization_branding_policies_priorities"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.get_organization_branding_policies_priorities") get_organization_branding_policies_priorities

> Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

```python
def get_organization_branding_policies_priorities(self,
                                                      organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = dashboard_branding_policies_controller.get_organization_branding_policies_priorities(organization_id)

```


### <a name="update_organization_branding_policies_priorities"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.update_organization_branding_policies_priorities") update_organization_branding_policies_priorities

> Update the priority ordering of an organization's branding policies.

```python
def update_organization_branding_policies_priorities(self,
                                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationBrandingPoliciesPriorities |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

update_organization_branding_policies_priorities = UpdateOrganizationBrandingPoliciesPrioritiesModel()
collect['update_organization_branding_policies_priorities'] = update_organization_branding_policies_priorities


result = dashboard_branding_policies_controller.update_organization_branding_policies_priorities(collect)

```


### <a name="get_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.get_organization_branding_policy") get_organization_branding_policy

> Return a branding policy

```python
def get_organization_branding_policy(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| brandingPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

branding_policy_id = 'brandingPolicyId'
collect['branding_policy_id'] = branding_policy_id


result = dashboard_branding_policies_controller.get_organization_branding_policy(collect)

```


### <a name="update_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.update_organization_branding_policy") update_organization_branding_policy

> Update a branding policy

```python
def update_organization_branding_policy(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| brandingPolicyId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationBrandingPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

branding_policy_id = 'brandingPolicyId'
collect['branding_policy_id'] = branding_policy_id

update_organization_branding_policy = UpdateOrganizationBrandingPolicyModel()
collect['update_organization_branding_policy'] = update_organization_branding_policy


result = dashboard_branding_policies_controller.update_organization_branding_policy(collect)

```


### <a name="delete_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.delete_organization_branding_policy") delete_organization_branding_policy

> Delete a branding policy

```python
def delete_organization_branding_policy(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| brandingPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

branding_policy_id = 'brandingPolicyId'
collect['branding_policy_id'] = branding_policy_id


dashboard_branding_policies_controller.delete_organization_branding_policy(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="devices_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DevicesController") DevicesController

### Get controller instance

An instance of the ``` DevicesController ``` class can be accessed from the API Client.

```python
 devices_controller = client.devices
```

### <a name="get_network_devices"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.get_network_devices") get_network_devices

> List the devices in a network

```python
def get_network_devices(self,
                            network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = devices_controller.get_network_devices(network_id)

```


### <a name="claim_network_devices"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.claim_network_devices") claim_network_devices

> Claim a device into a network

```python
def claim_network_devices(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| claimNetworkDevices |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

claim_network_devices = ClaimNetworkDevicesModel()
collect['claim_network_devices'] = claim_network_devices


devices_controller.claim_network_devices(collect)

```


### <a name="get_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.get_network_device") get_network_device

> Return a single device

```python
def get_network_device(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


result = devices_controller.get_network_device(collect)

```


### <a name="update_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.update_network_device") update_network_device

> Update the attributes of a device

```python
def update_network_device(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkDevice |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

update_network_device = UpdateNetworkDeviceModel()
collect['update_network_device'] = update_network_device


result = devices_controller.update_network_device(collect)

```


### <a name="blink_network_device_leds"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.blink_network_device_leds") blink_network_device_leds

> Blink the LEDs on a device

```python
def blink_network_device_leds(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| blinkNetworkDeviceLeds |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

blink_network_device_leds = BlinkNetworkDeviceLedsModel()
collect['blink_network_device_leds'] = blink_network_device_leds


result = devices_controller.blink_network_device_leds(collect)

```


### <a name="get_network_device_lldp_cdp"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.get_network_device_lldp_cdp") get_network_device_lldp_cdp

> List LLDP and CDP information for a device

```python
def get_network_device_lldp_cdp(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| timespan |  ``` Optional ```  | The timespan for which LLDP and CDP information will be fetched. Must be in seconds and less than or equal to a month (2592000 seconds). LLDP and CDP information is sent to the Meraki dashboard every 10 minutes. In instances where this LLDP and CDP information matches an existing entry in the Meraki dashboard, the data is updated once every two hours. Meraki recommends querying LLDP and CDP information at an interval slightly greater than two hours, to ensure that unchanged CDP / LLDP information can be queried consistently. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

timespan = 63
collect['timespan'] = timespan


result = devices_controller.get_network_device_lldp_cdp(collect)

```


### <a name="get_network_device_loss_and_latency_history"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.get_network_device_loss_and_latency_history") get_network_device_loss_and_latency_history

> Get the uplink loss percentage and latency in milliseconds for a wired network device.

```python
def get_network_device_loss_and_latency_history(self,
                                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| ip |  ``` Required ```  | The destination IP used to obtain the requested stats. This is required. |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 31 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |
| resolution |  ``` Optional ```  | The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60. |
| uplink |  ``` Optional ```  | The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

ip = 'ip'
collect['ip'] = ip

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 63.5910743887495
collect['timespan'] = timespan

resolution = 63
collect['resolution'] = resolution

uplink = UplinkEnum.WAN1
collect['uplink'] = uplink


result = devices_controller.get_network_device_loss_and_latency_history(collect)

```


### <a name="get_network_device_performance"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.get_network_device_performance") get_network_device_performance

> Return the performance score for a single device. Only primary MX devices supported. If no data is available, a 204 error code is returned.

```python
def get_network_device_performance(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


result = devices_controller.get_network_device_performance(collect)

```


### <a name="reboot_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.reboot_network_device") reboot_network_device

> Reboot a device

```python
def reboot_network_device(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


result = devices_controller.reboot_network_device(collect)

```


### <a name="remove_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.remove_network_device") remove_network_device

> Remove a single device

```python
def remove_network_device(self,
                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


devices_controller.remove_network_device(collect)

```


### <a name="get_network_device_uplink"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.get_network_device_uplink") get_network_device_uplink

> Return the uplink information for a device.

```python
def get_network_device_uplink(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


result = devices_controller.get_network_device_uplink(collect)

```


### <a name="get_organization_devices"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.get_organization_devices") get_organization_devices

> List the devices in an organization

```python
def get_organization_devices(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| configurationUpdatedAfter |  ``` Optional ```  | Filter results by whether or not the device's configuration has been updated after the given timestamp |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

per_page = 63
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before

configuration_updated_after = 'configurationUpdatedAfter'
collect['configuration_updated_after'] = configuration_updated_after


result = devices_controller.get_organization_devices(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="events_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EventsController") EventsController

### Get controller instance

An instance of the ``` EventsController ``` class can be accessed from the API Client.

```python
 events_controller = client.events
```

### <a name="get_network_events"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.get_network_events") get_network_events

> List the events for the network

```python
def get_network_events(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| productType |  ``` Optional ```  | The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway |
| includedEventTypes |  ``` Optional ```  ``` Collection ```  | A list of event types. The returned events will be filtered to only include events with these types. |
| excludedEventTypes |  ``` Optional ```  ``` Collection ```  | A list of event types. The returned events will be filtered to exclude events with these types. |
| deviceMac |  ``` Optional ```  | The MAC address of the Meraki device which the list of events will be filtered with |
| deviceSerial |  ``` Optional ```  | The serial of the Meraki device which the list of events will be filtered with |
| deviceName |  ``` Optional ```  | The name of the Meraki device which the list of events will be filtered with |
| clientIp |  ``` Optional ```  | The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks. |
| clientMac |  ``` Optional ```  | The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks. |
| clientName |  ``` Optional ```  | The name, or partial name, of the client which the list of events will be filtered with |
| smDeviceMac |  ``` Optional ```  | The MAC address of the Systems Manager device which the list of events will be filtered with |
| smDeviceName |  ``` Optional ```  | The name of the Systems Manager device which the list of events will be filtered with |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

product_type = 'productType'
collect['product_type'] = product_type

included_event_types = ['includedEventTypes']
collect['included_event_types'] = included_event_types

excluded_event_types = ['excludedEventTypes']
collect['excluded_event_types'] = excluded_event_types

device_mac = 'deviceMac'
collect['device_mac'] = device_mac

device_serial = 'deviceSerial'
collect['device_serial'] = device_serial

device_name = 'deviceName'
collect['device_name'] = device_name

client_ip = 'clientIp'
collect['client_ip'] = client_ip

client_mac = 'clientMac'
collect['client_mac'] = client_mac

client_name = 'clientName'
collect['client_name'] = client_name

sm_device_mac = 'smDeviceMac'
collect['sm_device_mac'] = sm_device_mac

sm_device_name = 'smDeviceName'
collect['sm_device_name'] = sm_device_name

per_page = 63
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = events_controller.get_network_events(collect)

```


### <a name="get_network_events_event_types"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.get_network_events_event_types") get_network_events_event_types

> List the event type to human-readable description

```python
def get_network_events_event_types(self,
                                       network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = events_controller.get_network_events_event_types(network_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="firewalled_services_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FirewalledServicesController") FirewalledServicesController

### Get controller instance

An instance of the ``` FirewalledServicesController ``` class can be accessed from the API Client.

```python
 firewalled_services_controller = client.firewalled_services
```

### <a name="get_network_firewalled_services"></a>![Method: ](https://apidocs.io/img/method.png ".FirewalledServicesController.get_network_firewalled_services") get_network_firewalled_services

> List the appliance services and their accessibility rules

```python
def get_network_firewalled_services(self,
                                        network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = firewalled_services_controller.get_network_firewalled_services(network_id)

```


### <a name="get_network_firewalled_service"></a>![Method: ](https://apidocs.io/img/method.png ".FirewalledServicesController.get_network_firewalled_service") get_network_firewalled_service

> Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')

```python
def get_network_firewalled_service(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| service |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

service = 'service'
collect['service'] = service


result = firewalled_services_controller.get_network_firewalled_service(collect)

```


### <a name="update_network_firewalled_service"></a>![Method: ](https://apidocs.io/img/method.png ".FirewalledServicesController.update_network_firewalled_service") update_network_firewalled_service

> Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP')

```python
def update_network_firewalled_service(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| service |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkFirewalledService |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

service = 'service'
collect['service'] = service

update_network_firewalled_service = UpdateNetworkFirewalledServiceModel()
collect['update_network_firewalled_service'] = update_network_firewalled_service


result = firewalled_services_controller.update_network_firewalled_service(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="floorplans_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FloorplansController") FloorplansController

### Get controller instance

An instance of the ``` FloorplansController ``` class can be accessed from the API Client.

```python
 floorplans_controller = client.floorplans
```

### <a name="get_network_floor_plans"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.get_network_floor_plans") get_network_floor_plans

> List the floor plans that belong to your network

```python
def get_network_floor_plans(self,
                                network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = floorplans_controller.get_network_floor_plans(network_id)

```


### <a name="create_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.create_network_floor_plan") create_network_floor_plan

> Upload a floor plan

```python
def create_network_floor_plan(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkFloorPlan |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_floor_plan = CreateNetworkFloorPlanModel()
collect['create_network_floor_plan'] = create_network_floor_plan


result = floorplans_controller.create_network_floor_plan(collect)

```


### <a name="get_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.get_network_floor_plan") get_network_floor_plan

> Find a floor plan by ID

```python
def get_network_floor_plan(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| floorPlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

floor_plan_id = 'floorPlanId'
collect['floor_plan_id'] = floor_plan_id


result = floorplans_controller.get_network_floor_plan(collect)

```


### <a name="update_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.update_network_floor_plan") update_network_floor_plan

> Update a floor plan's geolocation and other meta data

```python
def update_network_floor_plan(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| floorPlanId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkFloorPlan |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

floor_plan_id = 'floorPlanId'
collect['floor_plan_id'] = floor_plan_id

update_network_floor_plan = UpdateNetworkFloorPlanModel()
collect['update_network_floor_plan'] = update_network_floor_plan


result = floorplans_controller.update_network_floor_plan(collect)

```


### <a name="delete_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.delete_network_floor_plan") delete_network_floor_plan

> Destroy a floor plan

```python
def delete_network_floor_plan(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| floorPlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

floor_plan_id = 'floorPlanId'
collect['floor_plan_id'] = floor_plan_id


floorplans_controller.delete_network_floor_plan(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="group_policies_controller"></a>![Class: ](https://apidocs.io/img/class.png ".GroupPoliciesController") GroupPoliciesController

### Get controller instance

An instance of the ``` GroupPoliciesController ``` class can be accessed from the API Client.

```python
 group_policies_controller = client.group_policies
```

### <a name="get_network_group_policies"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.get_network_group_policies") get_network_group_policies

> List the group policies in a network

```python
def get_network_group_policies(self,
                                   network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = group_policies_controller.get_network_group_policies(network_id)

```


### <a name="create_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.create_network_group_policy") create_network_group_policy

> Create a group policy

```python
def create_network_group_policy(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkGroupPolicy |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_group_policy = CreateNetworkGroupPolicyModel()
collect['create_network_group_policy'] = create_network_group_policy


result = group_policies_controller.create_network_group_policy(collect)

```


### <a name="get_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.get_network_group_policy") get_network_group_policy

> Display a group policy

```python
def get_network_group_policy(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| groupPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

group_policy_id = 'groupPolicyId'
collect['group_policy_id'] = group_policy_id


result = group_policies_controller.get_network_group_policy(collect)

```


### <a name="update_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.update_network_group_policy") update_network_group_policy

> Update a group policy

```python
def update_network_group_policy(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| groupPolicyId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkGroupPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

group_policy_id = 'groupPolicyId'
collect['group_policy_id'] = group_policy_id

update_network_group_policy = UpdateNetworkGroupPolicyModel()
collect['update_network_group_policy'] = update_network_group_policy


result = group_policies_controller.update_network_group_policy(collect)

```


### <a name="delete_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.delete_network_group_policy") delete_network_group_policy

> Delete a group policy

```python
def delete_network_group_policy(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| groupPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

group_policy_id = 'groupPolicyId'
collect['group_policy_id'] = group_policy_id


group_policies_controller.delete_network_group_policy(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="http_servers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".HTTPServersController") HTTPServersController

### Get controller instance

An instance of the ``` HTTPServersController ``` class can be accessed from the API Client.

```python
 http_servers_controller = client.http_servers
```

### <a name="get_network_http_servers"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.get_network_http_servers") get_network_http_servers

> List the HTTP servers for a network

```python
def get_network_http_servers(self,
                                 network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = http_servers_controller.get_network_http_servers(network_id)

```


### <a name="create_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.create_network_http_server") create_network_http_server

> Add an HTTP server to a network

```python
def create_network_http_server(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkHttpServer |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_http_server = CreateNetworkHttpServerModel()
collect['create_network_http_server'] = create_network_http_server


result = http_servers_controller.create_network_http_server(collect)

```


### <a name="create_network_http_servers_webhook_test"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.create_network_http_servers_webhook_test") create_network_http_servers_webhook_test

> Send a test webhook for a network

```python
def create_network_http_servers_webhook_test(self,
                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkHttpServersWebhookTest |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_http_servers_webhook_test = CreateNetworkHttpServersWebhookTestModel()
collect['create_network_http_servers_webhook_test'] = create_network_http_servers_webhook_test


result = http_servers_controller.create_network_http_servers_webhook_test(collect)

```


### <a name="get_network_http_servers_webhook_test"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.get_network_http_servers_webhook_test") get_network_http_servers_webhook_test

> Return the status of a webhook test for a network

```python
def get_network_http_servers_webhook_test(self,
                                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = http_servers_controller.get_network_http_servers_webhook_test(collect)

```


### <a name="get_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.get_network_http_server") get_network_http_server

> Return an HTTP server for a network

```python
def get_network_http_server(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = http_servers_controller.get_network_http_server(collect)

```


### <a name="update_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.update_network_http_server") update_network_http_server

> Update an HTTP server

```python
def update_network_http_server(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkHttpServer |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

update_network_http_server = UpdateNetworkHttpServerModel()
collect['update_network_http_server'] = update_network_http_server


result = http_servers_controller.update_network_http_server(collect)

```


### <a name="delete_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.delete_network_http_server") delete_network_http_server

> Delete an HTTP server from a network

```python
def delete_network_http_server(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


http_servers_controller.delete_network_http_server(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="intrusion_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".IntrusionSettingsController") IntrusionSettingsController

### Get controller instance

An instance of the ``` IntrusionSettingsController ``` class can be accessed from the API Client.

```python
 intrusion_settings_controller = client.intrusion_settings
```

### <a name="get_network_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.get_network_security_intrusion_settings") get_network_security_intrusion_settings

> Returns all supported intrusion settings for an MX network

```python
def get_network_security_intrusion_settings(self,
                                                network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = intrusion_settings_controller.get_network_security_intrusion_settings(network_id)

```


### <a name="update_network_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.update_network_security_intrusion_settings") update_network_security_intrusion_settings

> Set the supported intrusion settings for an MX network

```python
def update_network_security_intrusion_settings(self,
                                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSecurityIntrusionSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_security_intrusion_settings = UpdateNetworkSecurityIntrusionSettingsModel()
collect['update_network_security_intrusion_settings'] = update_network_security_intrusion_settings


result = intrusion_settings_controller.update_network_security_intrusion_settings(collect)

```


### <a name="get_organization_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.get_organization_security_intrusion_settings") get_organization_security_intrusion_settings

> Returns all supported intrusion settings for an organization

```python
def get_organization_security_intrusion_settings(self,
                                                     organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = intrusion_settings_controller.get_organization_security_intrusion_settings(organization_id)

```


### <a name="update_organization_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.update_organization_security_intrusion_settings") update_organization_security_intrusion_settings

> Sets supported intrusion settings for an organization

```python
def update_organization_security_intrusion_settings(self,
                                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSecurityIntrusionSettings |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

update_organization_security_intrusion_settings = UpdateOrganizationSecurityIntrusionSettingsModel()
collect['update_organization_security_intrusion_settings'] = update_organization_security_intrusion_settings


result = intrusion_settings_controller.update_organization_security_intrusion_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="licenses_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LicensesController") LicensesController

### Get controller instance

An instance of the ``` LicensesController ``` class can be accessed from the API Client.

```python
 licenses_controller = client.licenses
```

### <a name="get_organization_licenses"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.get_organization_licenses") get_organization_licenses

> List the licenses for an organization

```python
def get_organization_licenses(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| deviceSerial |  ``` Optional ```  | Filter the licenses to those assigned to a particular device |
| networkId |  ``` Optional ```  | Filter the licenses to those assigned in a particular network |
| state |  ``` Optional ```  | Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'unused', 'unusedActive' or 'recentlyQueued' |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

per_page = 155
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before

device_serial = 'deviceSerial'
collect['device_serial'] = device_serial

network_id = 'networkId'
collect['network_id'] = network_id

state = StateEnum.ACTIVE
collect['state'] = state


result = licenses_controller.get_organization_licenses(collect)

```


### <a name="assign_organization_licenses_seats"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.assign_organization_licenses_seats") assign_organization_licenses_seats

> Assign SM seats to a network. This will increase the managed SM device limit of the network

```python
def assign_organization_licenses_seats(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| assignOrganizationLicensesSeats |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

assign_organization_licenses_seats = AssignOrganizationLicensesSeatsModel()
collect['assign_organization_licenses_seats'] = assign_organization_licenses_seats


result = licenses_controller.assign_organization_licenses_seats(collect)

```


### <a name="move_organization_licenses"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.move_organization_licenses") move_organization_licenses

> Move licenses to another organization. This will also move any devices that the licenses are assigned to

```python
def move_organization_licenses(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| moveOrganizationLicenses |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

move_organization_licenses = MoveOrganizationLicensesModel()
collect['move_organization_licenses'] = move_organization_licenses


result = licenses_controller.move_organization_licenses(collect)

```


### <a name="move_organization_licenses_seats"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.move_organization_licenses_seats") move_organization_licenses_seats

> Move SM seats to another organization

```python
def move_organization_licenses_seats(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| moveOrganizationLicensesSeats |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

move_organization_licenses_seats = MoveOrganizationLicensesSeatsModel()
collect['move_organization_licenses_seats'] = move_organization_licenses_seats


result = licenses_controller.move_organization_licenses_seats(collect)

```


### <a name="renew_organization_licenses_seats"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.renew_organization_licenses_seats") renew_organization_licenses_seats

> Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license

```python
def renew_organization_licenses_seats(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| renewOrganizationLicensesSeats |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

renew_organization_licenses_seats = RenewOrganizationLicensesSeatsModel()
collect['renew_organization_licenses_seats'] = renew_organization_licenses_seats


result = licenses_controller.renew_organization_licenses_seats(collect)

```


### <a name="get_organization_license"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.get_organization_license") get_organization_license

> Display a license

```python
def get_organization_license(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| licenseId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

license_id = 'licenseId'
collect['license_id'] = license_id


result = licenses_controller.get_organization_license(collect)

```


### <a name="update_organization_license"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.update_organization_license") update_organization_license

> Update a license

```python
def update_organization_license(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| licenseId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationLicense |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

license_id = 'licenseId'
collect['license_id'] = license_id

update_organization_license = UpdateOrganizationLicenseModel()
collect['update_organization_license'] = update_organization_license


result = licenses_controller.update_organization_license(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="link_aggregations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LinkAggregationsController") LinkAggregationsController

### Get controller instance

An instance of the ``` LinkAggregationsController ``` class can be accessed from the API Client.

```python
 link_aggregations_controller = client.link_aggregations
```

### <a name="get_network_switch_link_aggregations"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.get_network_switch_link_aggregations") get_network_switch_link_aggregations

> List link aggregation groups

```python
def get_network_switch_link_aggregations(self,
                                             network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = link_aggregations_controller.get_network_switch_link_aggregations(network_id)

```


### <a name="create_network_switch_link_aggregation"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.create_network_switch_link_aggregation") create_network_switch_link_aggregation

> Create a link aggregation group

```python
def create_network_switch_link_aggregation(self,
                                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchLinkAggregation |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_switch_link_aggregation = CreateNetworkSwitchLinkAggregationModel()
collect['create_network_switch_link_aggregation'] = create_network_switch_link_aggregation


result = link_aggregations_controller.create_network_switch_link_aggregation(collect)

```


### <a name="update_network_switch_link_aggregation"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.update_network_switch_link_aggregation") update_network_switch_link_aggregation

> Update a link aggregation group

```python
def update_network_switch_link_aggregation(self,
                                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| linkAggregationId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchLinkAggregation |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

link_aggregation_id = 'linkAggregationId'
collect['link_aggregation_id'] = link_aggregation_id

update_network_switch_link_aggregation = UpdateNetworkSwitchLinkAggregationModel()
collect['update_network_switch_link_aggregation'] = update_network_switch_link_aggregation


result = link_aggregations_controller.update_network_switch_link_aggregation(collect)

```


### <a name="delete_network_switch_link_aggregation"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.delete_network_switch_link_aggregation") delete_network_switch_link_aggregation

> Split a link aggregation group into separate ports

```python
def delete_network_switch_link_aggregation(self,
                                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| linkAggregationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

link_aggregation_id = 'linkAggregationId'
collect['link_aggregation_id'] = link_aggregation_id


link_aggregations_controller.delete_network_switch_link_aggregation(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mgdhcp_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGDHCPSettingsController") MGDHCPSettingsController

### Get controller instance

An instance of the ``` MGDHCPSettingsController ``` class can be accessed from the API Client.

```python
 mg_dhcp_settings_controller = client.mg_dhcp_settings
```

### <a name="get_network_cellular_gateway_settings_dhcp"></a>![Method: ](https://apidocs.io/img/method.png ".MGDHCPSettingsController.get_network_cellular_gateway_settings_dhcp") get_network_cellular_gateway_settings_dhcp

> List common DHCP settings of MGs

```python
def get_network_cellular_gateway_settings_dhcp(self,
                                                   network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mg_dhcp_settings_controller.get_network_cellular_gateway_settings_dhcp(network_id)

```


### <a name="update_network_cellular_gateway_settings_dhcp"></a>![Method: ](https://apidocs.io/img/method.png ".MGDHCPSettingsController.update_network_cellular_gateway_settings_dhcp") update_network_cellular_gateway_settings_dhcp

> Update common DHCP settings of MGs

```python
def update_network_cellular_gateway_settings_dhcp(self,
                                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsDhcp |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_cellular_gateway_settings_dhcp = UpdateNetworkCellularGatewaySettingsDhcpModel()
collect['update_network_cellular_gateway_settings_dhcp'] = update_network_cellular_gateway_settings_dhcp


result = mg_dhcp_settings_controller.update_network_cellular_gateway_settings_dhcp(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mglan_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGLANSettingsController") MGLANSettingsController

### Get controller instance

An instance of the ``` MGLANSettingsController ``` class can be accessed from the API Client.

```python
 mg_lan_settings_controller = client.mg_lan_settings
```

### <a name="get_device_cellular_gateway_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MGLANSettingsController.get_device_cellular_gateway_settings") get_device_cellular_gateway_settings

> Show the LAN Settings of a MG

```python
def get_device_cellular_gateway_settings(self,
                                             serial)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
serial = 'serial'

result = mg_lan_settings_controller.get_device_cellular_gateway_settings(serial)

```


### <a name="update_device_cellular_gateway_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MGLANSettingsController.update_device_cellular_gateway_settings") update_device_cellular_gateway_settings

> Update the LAN Settings for a single MG.

```python
def update_device_cellular_gateway_settings(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceCellularGatewaySettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

update_device_cellular_gateway_settings = UpdateDeviceCellularGatewaySettingsModel()
collect['update_device_cellular_gateway_settings'] = update_device_cellular_gateway_settings


result = mg_lan_settings_controller.update_device_cellular_gateway_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mg_connectivity_monitoring_destinations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGConnectivityMonitoringDestinationsController") MGConnectivityMonitoringDestinationsController

### Get controller instance

An instance of the ``` MGConnectivityMonitoringDestinationsController ``` class can be accessed from the API Client.

```python
 mg_connectivity_monitoring_destinations_controller = client.mg_connectivity_monitoring_destinations
```

### <a name="get_network_cellular_gateway_settings_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".MGConnectivityMonitoringDestinationsController.get_network_cellular_gateway_settings_connectivity_monitoring_destinations") get_network_cellular_gateway_settings_connectivity_monitoring_destinations

> Return the connectivity testing destinations for an MG network

```python
def get_network_cellular_gateway_settings_connectivity_monitoring_destinations(self,
                                                                                   network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mg_connectivity_monitoring_destinations_controller.get_network_cellular_gateway_settings_connectivity_monitoring_destinations(network_id)

```


### <a name="update_network_cellular_gateway_settings_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".MGConnectivityMonitoringDestinationsController.update_network_cellular_gateway_settings_connectivity_monitoring_destinations") update_network_cellular_gateway_settings_connectivity_monitoring_destinations

> Update the connectivity testing destinations for an MG network

```python
def update_network_cellular_gateway_settings_connectivity_monitoring_destinations(self,
                                                                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_cellular_gateway_settings_connectivity_monitoring_destinations = UpdateNetworkCellularGatewaySettingsConnectivityMonitoringDestinationsModel()
collect['update_network_cellular_gateway_settings_connectivity_monitoring_destinations'] = update_network_cellular_gateway_settings_connectivity_monitoring_destinations


result = mg_connectivity_monitoring_destinations_controller.update_network_cellular_gateway_settings_connectivity_monitoring_destinations(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mg_port_forwarding_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGPortForwardingRulesController") MGPortForwardingRulesController

### Get controller instance

An instance of the ``` MGPortForwardingRulesController ``` class can be accessed from the API Client.

```python
 mg_port_forwarding_rules_controller = client.mg_port_forwarding_rules
```

### <a name="get_device_cellular_gateway_settings_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MGPortForwardingRulesController.get_device_cellular_gateway_settings_port_forwarding_rules") get_device_cellular_gateway_settings_port_forwarding_rules

> Returns the port forwarding rules for a single MG.

```python
def get_device_cellular_gateway_settings_port_forwarding_rules(self,
                                                                   serial)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
serial = 'serial'

result = mg_port_forwarding_rules_controller.get_device_cellular_gateway_settings_port_forwarding_rules(serial)

```


### <a name="update_device_cellular_gateway_settings_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MGPortForwardingRulesController.update_device_cellular_gateway_settings_port_forwarding_rules") update_device_cellular_gateway_settings_port_forwarding_rules

> Updates the port forwarding rules for a single MG.

```python
def update_device_cellular_gateway_settings_port_forwarding_rules(self,
                                                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceCellularGatewaySettingsPortForwardingRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

update_device_cellular_gateway_settings_port_forwarding_rules = UpdateDeviceCellularGatewaySettingsPortForwardingRulesModel()
collect['update_device_cellular_gateway_settings_port_forwarding_rules'] = update_device_cellular_gateway_settings_port_forwarding_rules


result = mg_port_forwarding_rules_controller.update_device_cellular_gateway_settings_port_forwarding_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mg_subnet_pool_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGSubnetPoolSettingsController") MGSubnetPoolSettingsController

### Get controller instance

An instance of the ``` MGSubnetPoolSettingsController ``` class can be accessed from the API Client.

```python
 mg_subnet_pool_settings_controller = client.mg_subnet_pool_settings
```

### <a name="get_network_cellular_gateway_settings_subnet_pool"></a>![Method: ](https://apidocs.io/img/method.png ".MGSubnetPoolSettingsController.get_network_cellular_gateway_settings_subnet_pool") get_network_cellular_gateway_settings_subnet_pool

> Return the subnet pool and mask configured for MGs in the network.

```python
def get_network_cellular_gateway_settings_subnet_pool(self,
                                                          network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mg_subnet_pool_settings_controller.get_network_cellular_gateway_settings_subnet_pool(network_id)

```


### <a name="update_network_cellular_gateway_settings_subnet_pool"></a>![Method: ](https://apidocs.io/img/method.png ".MGSubnetPoolSettingsController.update_network_cellular_gateway_settings_subnet_pool") update_network_cellular_gateway_settings_subnet_pool

> Update the subnet pool and mask configuration for MGs in the network.

```python
def update_network_cellular_gateway_settings_subnet_pool(self,
                                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsSubnetPool |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_cellular_gateway_settings_subnet_pool = UpdateNetworkCellularGatewaySettingsSubnetPoolModel()
collect['update_network_cellular_gateway_settings_subnet_pool'] = update_network_cellular_gateway_settings_subnet_pool


result = mg_subnet_pool_settings_controller.update_network_cellular_gateway_settings_subnet_pool(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mg_uplink_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGUplinkSettingsController") MGUplinkSettingsController

### Get controller instance

An instance of the ``` MGUplinkSettingsController ``` class can be accessed from the API Client.

```python
 mg_uplink_settings_controller = client.mg_uplink_settings
```

### <a name="get_network_cellular_gateway_settings_uplink"></a>![Method: ](https://apidocs.io/img/method.png ".MGUplinkSettingsController.get_network_cellular_gateway_settings_uplink") get_network_cellular_gateway_settings_uplink

> Returns the uplink settings for your MG network.

```python
def get_network_cellular_gateway_settings_uplink(self,
                                                     network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mg_uplink_settings_controller.get_network_cellular_gateway_settings_uplink(network_id)

```


### <a name="update_network_cellular_gateway_settings_uplink"></a>![Method: ](https://apidocs.io/img/method.png ".MGUplinkSettingsController.update_network_cellular_gateway_settings_uplink") update_network_cellular_gateway_settings_uplink

> Updates the uplink settings for your MG network.

```python
def update_network_cellular_gateway_settings_uplink(self,
                                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsUplink |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_cellular_gateway_settings_uplink = UpdateNetworkCellularGatewaySettingsUplinkModel()
collect['update_network_cellular_gateway_settings_uplink'] = update_network_cellular_gateway_settings_uplink


result = mg_uplink_settings_controller.update_network_cellular_gateway_settings_uplink(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mrl3_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MRL3FirewallController") MRL3FirewallController

### Get controller instance

An instance of the ``` MRL3FirewallController ``` class can be accessed from the API Client.

```python
 mr_l_3_firewall_controller = client.mr_l_3_firewall
```

### <a name="get_network_ssid_l_3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MRL3FirewallController.get_network_ssid_l_3_firewall_rules") get_network_ssid_l_3_firewall_rules

> Return the L3 firewall rules for an SSID on an MR network

```python
def get_network_ssid_l_3_firewall_rules(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number


result = mr_l_3_firewall_controller.get_network_ssid_l_3_firewall_rules(collect)

```


### <a name="update_network_ssid_l_3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MRL3FirewallController.update_network_ssid_l_3_firewall_rules") update_network_ssid_l_3_firewall_rules

> Update the L3 firewall rules of an SSID on an MR network

```python
def update_network_ssid_l_3_firewall_rules(self,
                                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSsidL3FirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number

update_network_ssid_l_3_firewall_rules = UpdateNetworkSsidL3FirewallRulesModel()
collect['update_network_ssid_l_3_firewall_rules'] = update_network_ssid_l_3_firewall_rules


result = mr_l_3_firewall_controller.update_network_ssid_l_3_firewall_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mv_sense_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MVSenseController") MVSenseController

### Get controller instance

An instance of the ``` MVSenseController ``` class can be accessed from the API Client.

```python
 mv_sense_controller = client.mv_sense
```

### <a name="get_device_camera_analytics_live"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.get_device_camera_analytics_live") get_device_camera_analytics_live

> Returns live state from camera of analytics zones

```python
def get_device_camera_analytics_live(self,
                                         serial)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
serial = 'serial'

result = mv_sense_controller.get_device_camera_analytics_live(serial)

```


### <a name="get_device_camera_analytics_overview"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.get_device_camera_analytics_overview") get_device_camera_analytics_overview

> Returns an overview of aggregate analytics data for a timespan

```python
def get_device_camera_analytics_overview(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour. |
| objectType |  ``` Optional ```  | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 155.086356280412
collect['timespan'] = timespan

object_type = ObjectTypeEnum.PERSON
collect['object_type'] = object_type


result = mv_sense_controller.get_device_camera_analytics_overview(collect)

```


### <a name="get_device_camera_analytics_recent"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.get_device_camera_analytics_recent") get_device_camera_analytics_recent

> Returns most recent record for analytics zones

```python
def get_device_camera_analytics_recent(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| objectType |  ``` Optional ```  | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

object_type = ObjectTypeEnum.PERSON
collect['object_type'] = object_type


result = mv_sense_controller.get_device_camera_analytics_recent(collect)

```


### <a name="get_device_camera_analytics_zones"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.get_device_camera_analytics_zones") get_device_camera_analytics_zones

> Returns all configured analytic zones for this camera

```python
def get_device_camera_analytics_zones(self,
                                          serial)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
serial = 'serial'

result = mv_sense_controller.get_device_camera_analytics_zones(serial)

```


### <a name="get_device_camera_analytics_zone_history"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.get_device_camera_analytics_zone_history") get_device_camera_analytics_zone_history

> Return historical records for analytic zones

```python
def get_device_camera_analytics_zone_history(self,
                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| zoneId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 14 hours after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour. |
| resolution |  ``` Optional ```  | The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60. |
| objectType |  ``` Optional ```  | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

zone_id = 'zoneId'
collect['zone_id'] = zone_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 113.363183053845
collect['timespan'] = timespan

resolution = 113
collect['resolution'] = resolution

object_type = ObjectTypeEnum.PERSON
collect['object_type'] = object_type


result = mv_sense_controller.get_device_camera_analytics_zone_history(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mx11_nat_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MX11NATRulesController") MX11NATRulesController

### Get controller instance

An instance of the ``` MX11NATRulesController ``` class can be accessed from the API Client.

```python
 mx_1_1_nat_rules_controller = client.mx_1_1_nat_rules
```

### <a name="get_network_one_to_one_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX11NATRulesController.get_network_one_to_one_nat_rules") get_network_one_to_one_nat_rules

> Return the 1:1 NAT mapping rules for an MX network

```python
def get_network_one_to_one_nat_rules(self,
                                         network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_11_nat_rules_controller.get_network_one_to_one_nat_rules(network_id)

```


### <a name="update_network_one_to_one_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX11NATRulesController.update_network_one_to_one_nat_rules") update_network_one_to_one_nat_rules

> Set the 1:1 NAT mapping rules for an MX network

```python
def update_network_one_to_one_nat_rules(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkOneToOneNatRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_one_to_one_nat_rules = UpdateNetworkOneToOneNatRulesModel()
collect['update_network_one_to_one_nat_rules'] = update_network_one_to_one_nat_rules


result = mx_11_nat_rules_controller.update_network_one_to_one_nat_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mx1_many_nat_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MX1ManyNATRulesController") MX1ManyNATRulesController

### Get controller instance

An instance of the ``` MX1ManyNATRulesController ``` class can be accessed from the API Client.

```python
 mx_1_many_nat_rules_controller = client.mx_1_many_nat_rules
```

### <a name="get_network_one_to_many_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX1ManyNATRulesController.get_network_one_to_many_nat_rules") get_network_one_to_many_nat_rules

> Return the 1:Many NAT mapping rules for an MX network

```python
def get_network_one_to_many_nat_rules(self,
                                          network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_1_many_nat_rules_controller.get_network_one_to_many_nat_rules(network_id)

```


### <a name="update_network_one_to_many_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX1ManyNATRulesController.update_network_one_to_many_nat_rules") update_network_one_to_many_nat_rules

> Set the 1:Many NAT mapping rules for an MX network

```python
def update_network_one_to_many_nat_rules(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkOneToManyNatRules |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_one_to_many_nat_rules = UpdateNetworkOneToManyNatRulesModel()
collect['update_network_one_to_many_nat_rules'] = update_network_one_to_many_nat_rules


result = mx_1_many_nat_rules_controller.update_network_one_to_many_nat_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mxl3_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL3FirewallController") MXL3FirewallController

### Get controller instance

An instance of the ``` MXL3FirewallController ``` class can be accessed from the API Client.

```python
 mx_l_3_firewall_controller = client.mx_l_3_firewall
```

### <a name="get_network_l_3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL3FirewallController.get_network_l_3_firewall_rules") get_network_l_3_firewall_rules

> Return the L3 firewall rules for an MX network

```python
def get_network_l_3_firewall_rules(self,
                                       network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_l_3_firewall_controller.get_network_l_3_firewall_rules(network_id)

```


### <a name="update_network_l_3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL3FirewallController.update_network_l_3_firewall_rules") update_network_l_3_firewall_rules

> Update the L3 firewall rules of an MX network

```python
def update_network_l_3_firewall_rules(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkL3FirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_l_3_firewall_rules = UpdateNetworkL3FirewallRulesModel()
collect['update_network_l_3_firewall_rules'] = update_network_l_3_firewall_rules


result = mx_l_3_firewall_controller.update_network_l_3_firewall_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mxl7_application_categories_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL7ApplicationCategoriesController") MXL7ApplicationCategoriesController

### Get controller instance

An instance of the ``` MXL7ApplicationCategoriesController ``` class can be accessed from the API Client.

```python
 mx_l_7_application_categories_controller = client.mx_l_7_application_categories
```

### <a name="get_network_l_7_firewall_rules_application_categories"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7ApplicationCategoriesController.get_network_l_7_firewall_rules_application_categories") get_network_l_7_firewall_rules_application_categories

> Return the L7 firewall application categories and their associated applications for an MX network

```python
def get_network_l_7_firewall_rules_application_categories(self,
                                                              network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_l_7_application_categories_controller.get_network_l_7_firewall_rules_application_categories(network_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mxl7_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL7FirewallController") MXL7FirewallController

### Get controller instance

An instance of the ``` MXL7FirewallController ``` class can be accessed from the API Client.

```python
 mx_l_7_firewall_controller = client.mx_l_7_firewall
```

### <a name="get_network_l_7_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7FirewallController.get_network_l_7_firewall_rules") get_network_l_7_firewall_rules

> List the MX L7 firewall rules for an MX network

```python
def get_network_l_7_firewall_rules(self,
                                       network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_l_7_firewall_controller.get_network_l_7_firewall_rules(network_id)

```


### <a name="update_network_l_7_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7FirewallController.update_network_l_7_firewall_rules") update_network_l_7_firewall_rules

> Update the MX L7 firewall rules for an MX network

```python
def update_network_l_7_firewall_rules(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkL7FirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_l_7_firewall_rules = UpdateNetworkL7FirewallRulesModel()
collect['update_network_l_7_firewall_rules'] = update_network_l_7_firewall_rules


result = mx_l_7_firewall_controller.update_network_l_7_firewall_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mxvlan_ports_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXVLANPortsController") MXVLANPortsController

### Get controller instance

An instance of the ``` MXVLANPortsController ``` class can be accessed from the API Client.

```python
 mx_vlan_ports_controller = client.mx_vlan_ports
```

### <a name="get_network_appliance_ports"></a>![Method: ](https://apidocs.io/img/method.png ".MXVLANPortsController.get_network_appliance_ports") get_network_appliance_ports

> List per-port VLAN settings for all ports of a MX.

```python
def get_network_appliance_ports(self,
                                    network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_vlan_ports_controller.get_network_appliance_ports(network_id)

```


### <a name="get_network_appliance_port"></a>![Method: ](https://apidocs.io/img/method.png ".MXVLANPortsController.get_network_appliance_port") get_network_appliance_port

> Return per-port VLAN settings for a single MX port.

```python
def get_network_appliance_port(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appliancePortId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

appliance_port_id = 'appliancePortId'
collect['appliance_port_id'] = appliance_port_id


result = mx_vlan_ports_controller.get_network_appliance_port(collect)

```


### <a name="update_network_appliance_port"></a>![Method: ](https://apidocs.io/img/method.png ".MXVLANPortsController.update_network_appliance_port") update_network_appliance_port

> Update the per-port VLAN settings for a single MX port.

```python
def update_network_appliance_port(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appliancePortId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkAppliancePort |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

appliance_port_id = 'appliancePortId'
collect['appliance_port_id'] = appliance_port_id

update_network_appliance_port = UpdateNetworkAppliancePortModel()
collect['update_network_appliance_port'] = update_network_appliance_port


result = mx_vlan_ports_controller.update_network_appliance_port(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mxvpn_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXVPNFirewallController") MXVPNFirewallController

### Get controller instance

An instance of the ``` MXVPNFirewallController ``` class can be accessed from the API Client.

```python
 mx_vpn_firewall_controller = client.mx_vpn_firewall
```

### <a name="get_organization_vpn_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXVPNFirewallController.get_organization_vpn_firewall_rules") get_organization_vpn_firewall_rules

> Return the firewall rules for an organization's site-to-site VPN

```python
def get_organization_vpn_firewall_rules(self,
                                            organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = mx_vpn_firewall_controller.get_organization_vpn_firewall_rules(organization_id)

```


### <a name="update_organization_vpn_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXVPNFirewallController.update_organization_vpn_firewall_rules") update_organization_vpn_firewall_rules

> Update the firewall rules of an organization's site-to-site VPN

```python
def update_organization_vpn_firewall_rules(self,
                                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationVpnFirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

update_organization_vpn_firewall_rules = UpdateOrganizationVpnFirewallRulesModel()
collect['update_organization_vpn_firewall_rules'] = update_organization_vpn_firewall_rules


result = mx_vpn_firewall_controller.update_organization_vpn_firewall_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mx_cellular_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXCellularFirewallController") MXCellularFirewallController

### Get controller instance

An instance of the ``` MXCellularFirewallController ``` class can be accessed from the API Client.

```python
 mx_cellular_firewall_controller = client.mx_cellular_firewall
```

### <a name="get_network_cellular_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXCellularFirewallController.get_network_cellular_firewall_rules") get_network_cellular_firewall_rules

> Return the cellular firewall rules for an MX network

```python
def get_network_cellular_firewall_rules(self,
                                            network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_cellular_firewall_controller.get_network_cellular_firewall_rules(network_id)

```


### <a name="update_network_cellular_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXCellularFirewallController.update_network_cellular_firewall_rules") update_network_cellular_firewall_rules

> Update the cellular firewall rules of an MX network

```python
def update_network_cellular_firewall_rules(self,
                                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularFirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_cellular_firewall_rules = UpdateNetworkCellularFirewallRulesModel()
collect['update_network_cellular_firewall_rules'] = update_network_cellular_firewall_rules


result = mx_cellular_firewall_controller.update_network_cellular_firewall_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mx_inbound_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXInboundFirewallController") MXInboundFirewallController

### Get controller instance

An instance of the ``` MXInboundFirewallController ``` class can be accessed from the API Client.

```python
 mx_inbound_firewall_controller = client.mx_inbound_firewall
```

### <a name="get_network_appliance_firewall_inbound_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXInboundFirewallController.get_network_appliance_firewall_inbound_firewall_rules") get_network_appliance_firewall_inbound_firewall_rules

> Return the inbound firewall rules for an MX network

```python
def get_network_appliance_firewall_inbound_firewall_rules(self,
                                                              network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_inbound_firewall_controller.get_network_appliance_firewall_inbound_firewall_rules(network_id)

```


### <a name="update_network_appliance_firewall_inbound_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXInboundFirewallController.update_network_appliance_firewall_inbound_firewall_rules") update_network_appliance_firewall_inbound_firewall_rules

> Update the inbound firewall rules of an MX network

```python
def update_network_appliance_firewall_inbound_firewall_rules(self,
                                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkApplianceFirewallInboundFirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_appliance_firewall_inbound_firewall_rules = UpdateNetworkApplianceFirewallInboundFirewallRulesModel()
collect['update_network_appliance_firewall_inbound_firewall_rules'] = update_network_appliance_firewall_inbound_firewall_rules


result = mx_inbound_firewall_controller.update_network_appliance_firewall_inbound_firewall_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mx_port_forwarding_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXPortForwardingRulesController") MXPortForwardingRulesController

### Get controller instance

An instance of the ``` MXPortForwardingRulesController ``` class can be accessed from the API Client.

```python
 mx_port_forwarding_rules_controller = client.mx_port_forwarding_rules
```

### <a name="get_network_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXPortForwardingRulesController.get_network_port_forwarding_rules") get_network_port_forwarding_rules

> Return the port forwarding rules for an MX network

```python
def get_network_port_forwarding_rules(self,
                                          network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_port_forwarding_rules_controller.get_network_port_forwarding_rules(network_id)

```


### <a name="update_network_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXPortForwardingRulesController.update_network_port_forwarding_rules") update_network_port_forwarding_rules

> Update the port forwarding rules for an MX network

```python
def update_network_port_forwarding_rules(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkPortForwardingRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_port_forwarding_rules = UpdateNetworkPortForwardingRulesModel()
collect['update_network_port_forwarding_rules'] = update_network_port_forwarding_rules


result = mx_port_forwarding_rules_controller.update_network_port_forwarding_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mx_static_routes_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXStaticRoutesController") MXStaticRoutesController

### Get controller instance

An instance of the ``` MXStaticRoutesController ``` class can be accessed from the API Client.

```python
 mx_static_routes_controller = client.mx_static_routes
```

### <a name="get_network_static_routes"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.get_network_static_routes") get_network_static_routes

> List the static routes for an MX or teleworker network

```python
def get_network_static_routes(self,
                                  network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_static_routes_controller.get_network_static_routes(network_id)

```


### <a name="create_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.create_network_static_route") create_network_static_route

> Add a static route for an MX or teleworker network

```python
def create_network_static_route(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkStaticRoute |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_static_route = CreateNetworkStaticRouteModel()
collect['create_network_static_route'] = create_network_static_route


result = mx_static_routes_controller.create_network_static_route(collect)

```


### <a name="get_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.get_network_static_route") get_network_static_route

> Return a static route for an MX or teleworker network

```python
def get_network_static_route(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| srId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

sr_id = 'srId'
collect['sr_id'] = sr_id


result = mx_static_routes_controller.get_network_static_route(collect)

```


### <a name="update_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.update_network_static_route") update_network_static_route

> Update a static route for an MX or teleworker network

```python
def update_network_static_route(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| srId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkStaticRoute |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

sr_id = 'srId'
collect['sr_id'] = sr_id

update_network_static_route = UpdateNetworkStaticRouteModel()
collect['update_network_static_route'] = update_network_static_route


result = mx_static_routes_controller.update_network_static_route(collect)

```


### <a name="delete_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.delete_network_static_route") delete_network_static_route

> Delete a static route from an MX or teleworker network

```python
def delete_network_static_route(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| srId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

sr_id = 'srId'
collect['sr_id'] = sr_id


mx_static_routes_controller.delete_network_static_route(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mx_warm_spare_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXWarmSpareSettingsController") MXWarmSpareSettingsController

### Get controller instance

An instance of the ``` MXWarmSpareSettingsController ``` class can be accessed from the API Client.

```python
 mx_warm_spare_settings_controller = client.mx_warm_spare_settings
```

### <a name="swap_network_warmspare"></a>![Method: ](https://apidocs.io/img/method.png ".MXWarmSpareSettingsController.swap_network_warmspare") swap_network_warmspare

> Swap MX primary and warm spare appliances

```python
def swap_network_warmspare(self,
                               network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_warm_spare_settings_controller.swap_network_warmspare(network_id)

```


### <a name="get_network_warm_spare_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MXWarmSpareSettingsController.get_network_warm_spare_settings") get_network_warm_spare_settings

> Return MX warm spare settings

```python
def get_network_warm_spare_settings(self,
                                        network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_warm_spare_settings_controller.get_network_warm_spare_settings(network_id)

```


### <a name="update_network_warm_spare_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MXWarmSpareSettingsController.update_network_warm_spare_settings") update_network_warm_spare_settings

> Update MX warm spare settings

```python
def update_network_warm_spare_settings(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkWarmSpareSettings |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_warm_spare_settings = UpdateNetworkWarmSpareSettingsModel()
collect['update_network_warm_spare_settings'] = update_network_warm_spare_settings


result = mx_warm_spare_settings_controller.update_network_warm_spare_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="malware_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MalwareSettingsController") MalwareSettingsController

### Get controller instance

An instance of the ``` MalwareSettingsController ``` class can be accessed from the API Client.

```python
 malware_settings_controller = client.malware_settings
```

### <a name="get_network_security_malware_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MalwareSettingsController.get_network_security_malware_settings") get_network_security_malware_settings

> Returns all supported malware settings for an MX network

```python
def get_network_security_malware_settings(self,
                                              network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = malware_settings_controller.get_network_security_malware_settings(network_id)

```


### <a name="update_network_security_malware_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MalwareSettingsController.update_network_security_malware_settings") update_network_security_malware_settings

> Set the supported malware settings for an MX network

```python
def update_network_security_malware_settings(self,
                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSecurityMalwareSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_security_malware_settings = UpdateNetworkSecurityMalwareSettingsModel()
collect['update_network_security_malware_settings'] = update_network_security_malware_settings


result = malware_settings_controller.update_network_security_malware_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="management_interface_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ManagementInterfaceSettingsController") ManagementInterfaceSettingsController

### Get controller instance

An instance of the ``` ManagementInterfaceSettingsController ``` class can be accessed from the API Client.

```python
 management_interface_settings_controller = client.management_interface_settings
```

### <a name="get_network_device_management_interface_settings"></a>![Method: ](https://apidocs.io/img/method.png ".ManagementInterfaceSettingsController.get_network_device_management_interface_settings") get_network_device_management_interface_settings

> Return the management interface settings for a device

```python
def get_network_device_management_interface_settings(self,
                                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


result = management_interface_settings_controller.get_network_device_management_interface_settings(collect)

```


### <a name="update_network_device_management_interface_settings"></a>![Method: ](https://apidocs.io/img/method.png ".ManagementInterfaceSettingsController.update_network_device_management_interface_settings") update_network_device_management_interface_settings

> Update the management interface settings for a device

```python
def update_network_device_management_interface_settings(self,
                                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkDeviceManagementInterfaceSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

update_network_device_management_interface_settings = UpdateNetworkDeviceManagementInterfaceSettingsModel()
collect['update_network_device_management_interface_settings'] = update_network_device_management_interface_settings


result = management_interface_settings_controller.update_network_device_management_interface_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="meraki_auth_users_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MerakiAuthUsersController") MerakiAuthUsersController

### Get controller instance

An instance of the ``` MerakiAuthUsersController ``` class can be accessed from the API Client.

```python
 meraki_auth_users_controller = client.meraki_auth_users
```

### <a name="get_network_meraki_auth_users"></a>![Method: ](https://apidocs.io/img/method.png ".MerakiAuthUsersController.get_network_meraki_auth_users") get_network_meraki_auth_users

> List the splash or RADIUS users configured under Meraki Authentication for a network

```python
def get_network_meraki_auth_users(self,
                                      network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = meraki_auth_users_controller.get_network_meraki_auth_users(network_id)

```


### <a name="get_network_meraki_auth_user"></a>![Method: ](https://apidocs.io/img/method.png ".MerakiAuthUsersController.get_network_meraki_auth_user") get_network_meraki_auth_user

> Return the Meraki Auth splash or RADIUS user

```python
def get_network_meraki_auth_user(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| merakiAuthUserId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

meraki_auth_user_id = 'merakiAuthUserId'
collect['meraki_auth_user_id'] = meraki_auth_user_id


result = meraki_auth_users_controller.get_network_meraki_auth_user(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="monitored_media_servers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MonitoredMediaServersController") MonitoredMediaServersController

### Get controller instance

An instance of the ``` MonitoredMediaServersController ``` class can be accessed from the API Client.

```python
 monitored_media_servers_controller = client.monitored_media_servers
```

### <a name="get_organization_insight_monitored_media_servers"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.get_organization_insight_monitored_media_servers") get_organization_insight_monitored_media_servers

> List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.

```python
def get_organization_insight_monitored_media_servers(self,
                                                         organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = monitored_media_servers_controller.get_organization_insight_monitored_media_servers(organization_id)

```


### <a name="create_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.create_organization_insight_monitored_media_server") create_organization_insight_monitored_media_server

> Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.

```python
def create_organization_insight_monitored_media_server(self,
                                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationInsightMonitoredMediaServer |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_insight_monitored_media_server = CreateOrganizationInsightMonitoredMediaServerModel()
collect['create_organization_insight_monitored_media_server'] = create_organization_insight_monitored_media_server


result = monitored_media_servers_controller.create_organization_insight_monitored_media_server(collect)

```


### <a name="get_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.get_organization_insight_monitored_media_server") get_organization_insight_monitored_media_server

> Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.

```python
def get_organization_insight_monitored_media_server(self,
                                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| monitoredMediaServerId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

monitored_media_server_id = 'monitoredMediaServerId'
collect['monitored_media_server_id'] = monitored_media_server_id


result = monitored_media_servers_controller.get_organization_insight_monitored_media_server(collect)

```


### <a name="update_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.update_organization_insight_monitored_media_server") update_organization_insight_monitored_media_server

> Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.

```python
def update_organization_insight_monitored_media_server(self,
                                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| monitoredMediaServerId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationInsightMonitoredMediaServer |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

monitored_media_server_id = 'monitoredMediaServerId'
collect['monitored_media_server_id'] = monitored_media_server_id

update_organization_insight_monitored_media_server = UpdateOrganizationInsightMonitoredMediaServerModel()
collect['update_organization_insight_monitored_media_server'] = update_organization_insight_monitored_media_server


result = monitored_media_servers_controller.update_organization_insight_monitored_media_server(collect)

```


### <a name="delete_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.delete_organization_insight_monitored_media_server") delete_organization_insight_monitored_media_server

> Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.

```python
def delete_organization_insight_monitored_media_server(self,
                                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| monitoredMediaServerId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

monitored_media_server_id = 'monitoredMediaServerId'
collect['monitored_media_server_id'] = monitored_media_server_id


monitored_media_servers_controller.delete_organization_insight_monitored_media_server(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="named_tag_scope_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NamedTagScopeController") NamedTagScopeController

### Get controller instance

An instance of the ``` NamedTagScopeController ``` class can be accessed from the API Client.

```python
 named_tag_scope_controller = client.named_tag_scope
```

### <a name="get_network_sm_target_groups"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.get_network_sm_target_groups") get_network_sm_target_groups

> List the target groups in this network

```python
def get_network_sm_target_groups(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| withDetails |  ``` Optional ```  | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

with_details = True
collect['with_details'] = with_details


result = named_tag_scope_controller.get_network_sm_target_groups(collect)

```


### <a name="create_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.create_network_sm_target_group") create_network_sm_target_group

> Add a target group

```python
def create_network_sm_target_group(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmTargetGroup |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_sm_target_group = CreateNetworkSmTargetGroupModel()
collect['create_network_sm_target_group'] = create_network_sm_target_group


result = named_tag_scope_controller.create_network_sm_target_group(collect)

```


### <a name="get_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.get_network_sm_target_group") get_network_sm_target_group

> Return a target group

```python
def get_network_sm_target_group(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| targetGroupId |  ``` Required ```  | TODO: Add a parameter description |
| withDetails |  ``` Optional ```  | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

target_group_id = 'targetGroupId'
collect['target_group_id'] = target_group_id

with_details = True
collect['with_details'] = with_details


result = named_tag_scope_controller.get_network_sm_target_group(collect)

```


### <a name="update_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.update_network_sm_target_group") update_network_sm_target_group

> Update a target group

```python
def update_network_sm_target_group(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| targetGroupId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmTargetGroup |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

target_group_id = 'targetGroupId'
collect['target_group_id'] = target_group_id

update_network_sm_target_group = UpdateNetworkSmTargetGroupModel()
collect['update_network_sm_target_group'] = update_network_sm_target_group


result = named_tag_scope_controller.update_network_sm_target_group(collect)

```


### <a name="delete_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.delete_network_sm_target_group") delete_network_sm_target_group

> Delete a target group from a network

```python
def delete_network_sm_target_group(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| targetGroupId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

target_group_id = 'targetGroupId'
collect['target_group_id'] = target_group_id


named_tag_scope_controller.delete_network_sm_target_group(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="netflow_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NetflowSettingsController") NetflowSettingsController

### Get controller instance

An instance of the ``` NetflowSettingsController ``` class can be accessed from the API Client.

```python
 netflow_settings_controller = client.netflow_settings
```

### <a name="get_network_netflow_settings"></a>![Method: ](https://apidocs.io/img/method.png ".NetflowSettingsController.get_network_netflow_settings") get_network_netflow_settings

> Return the NetFlow traffic reporting settings for a network

```python
def get_network_netflow_settings(self,
                                     network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = netflow_settings_controller.get_network_netflow_settings(network_id)

```


### <a name="update_network_netflow_settings"></a>![Method: ](https://apidocs.io/img/method.png ".NetflowSettingsController.update_network_netflow_settings") update_network_netflow_settings

> Update the NetFlow traffic reporting settings for a network

```python
def update_network_netflow_settings(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork_netflow_Settings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_netflow_settings = UpdateNetworkNetflowSettingsModel()
collect['update_network_netflow_settings'] = update_network_netflow_settings


result = netflow_settings_controller.update_network_netflow_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="networks_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NetworksController") NetworksController

### Get controller instance

An instance of the ``` NetworksController ``` class can be accessed from the API Client.

```python
 networks_controller = client.networks
```

### <a name="get_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_network") get_network

> Return a network

```python
def get_network(self,
                    network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = networks_controller.get_network(network_id)

```


### <a name="update_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.update_network") update_network

> Update a network

```python
def update_network(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network = UpdateNetworkModel()
collect['update_network'] = update_network


result = networks_controller.update_network(collect)

```


### <a name="delete_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.delete_network") delete_network

> Delete a network

```python
def delete_network(self,
                       network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

networks_controller.delete_network(network_id)

```


### <a name="get_network_access_policies"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_network_access_policies") get_network_access_policies

> List the access policies for this network. Only valid for MS networks.

```python
def get_network_access_policies(self,
                                    network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = networks_controller.get_network_access_policies(network_id)

```


### <a name="get_network_air_marshal"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_network_air_marshal") get_network_air_marshal

> List Air Marshal scan results from a network

```python
def get_network_air_marshal(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

timespan = 204.858464945507
collect['timespan'] = timespan


result = networks_controller.get_network_air_marshal(collect)

```


### <a name="bind_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.bind_network") bind_network

> Bind a network to a template.

```python
def bind_network(self,
                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| bindNetwork |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

bind_network = BindNetworkModel()
collect['bind_network'] = bind_network


networks_controller.bind_network(collect)

```


### <a name="get_network_bluetooth_settings"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_network_bluetooth_settings") get_network_bluetooth_settings

> Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.

```python
def get_network_bluetooth_settings(self,
                                       network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = networks_controller.get_network_bluetooth_settings(network_id)

```


### <a name="update_network_bluetooth_settings"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.update_network_bluetooth_settings") update_network_bluetooth_settings

> Update the Bluetooth settings for a network. See the docs page for <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a>.

```python
def update_network_bluetooth_settings(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkBluetoothSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_bluetooth_settings = UpdateNetworkBluetoothSettingsModel()
collect['update_network_bluetooth_settings'] = update_network_bluetooth_settings


result = networks_controller.update_network_bluetooth_settings(collect)

```


### <a name="get_network_site_to_site_vpn"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_network_site_to_site_vpn") get_network_site_to_site_vpn

> Return the site-to-site VPN settings of a network. Only valid for MX networks.

```python
def get_network_site_to_site_vpn(self,
                                     network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = networks_controller.get_network_site_to_site_vpn(network_id)

```


### <a name="update_network_site_to_site_vpn"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.update_network_site_to_site_vpn") update_network_site_to_site_vpn

> Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

```python
def update_network_site_to_site_vpn(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSiteToSiteVpn |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_site_to_site_vpn = UpdateNetworkSiteToSiteVpnModel()
collect['update_network_site_to_site_vpn'] = update_network_site_to_site_vpn


result = networks_controller.update_network_site_to_site_vpn(collect)

```


### <a name="split_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.split_network") split_network

> Split a combined network into individual networks for each type of device

```python
def split_network(self,
                      network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = networks_controller.split_network(network_id)

```


### <a name="get_network_traffic"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_network_traffic") get_network_traffic

>     The traffic analysis data for this network.
>     <a href="https://documentation.meraki.com/MR/Monitoring_and_Reporting/Hostname_Visibility">Traffic Analysis with Hostname Visibility</a> must be enabled on the network.
> 

```python
def get_network_traffic(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 30 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. |
| deviceType |  ``` Optional ```  | Filter the data by device type: combined (default), wireless, switch, appliance.
    When using combined, for each rule the data will come from the device type with the most usage. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

timespan = 204.858464945507
collect['timespan'] = timespan

device_type = 'deviceType'
collect['device_type'] = device_type


result = networks_controller.get_network_traffic(collect)

```


### <a name="unbind_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.unbind_network") unbind_network

> Unbind a network from a template.

```python
def unbind_network(self,
                       network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

networks_controller.unbind_network(network_id)

```


### <a name="get_organization_networks"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_organization_networks") get_organization_networks

> List the networks in an organization

```python
def get_organization_networks(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| configTemplateId |  ``` Optional ```  | An optional parameter that is the ID of a config template. Will return all networks bound to that template. |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

config_template_id = 'configTemplateId'
collect['config_template_id'] = config_template_id


result = networks_controller.get_organization_networks(collect)

```


### <a name="create_organization_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.create_organization_network") create_organization_network

> Create a network

```python
def create_organization_network(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationNetwork |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_network = CreateOrganizationNetworkModel()
collect['create_organization_network'] = create_organization_network


result = networks_controller.create_organization_network(collect)

```


### <a name="combine_organization_networks"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.combine_organization_networks") combine_organization_networks

> Combine multiple networks into a single network

```python
def combine_organization_networks(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| combineOrganizationNetworks |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

combine_organization_networks = CombineOrganizationNetworksModel()
collect['combine_organization_networks'] = combine_organization_networks


result = networks_controller.combine_organization_networks(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="open_api_spec_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OpenAPISpecController") OpenAPISpecController

### Get controller instance

An instance of the ``` OpenAPISpecController ``` class can be accessed from the API Client.

```python
 open_api_spec_controller = client.open_api_spec
```

### <a name="get_organization_openapi_spec"></a>![Method: ](https://apidocs.io/img/method.png ".OpenAPISpecController.get_organization_openapi_spec") get_organization_openapi_spec

> Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON

```python
def get_organization_openapi_spec(self,
                                      organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = open_api_spec_controller.get_organization_openapi_spec(organization_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="organizations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OrganizationsController") OrganizationsController

### Get controller instance

An instance of the ``` OrganizationsController ``` class can be accessed from the API Client.

```python
 organizations_controller = client.organizations
```

### <a name="get_organizations"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organizations") get_organizations

> List the organizations that the user has privileges on

```python
def get_organizations(self)
```

#### Example Usage

```python

result = organizations_controller.get_organizations()

```


### <a name="create_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.create_organization") create_organization

> Create a new organization

```python
def create_organization(self,
                            create_organization)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| createOrganization |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
create_organization = CreateOrganizationModel()

result = organizations_controller.create_organization(create_organization)

```


### <a name="get_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization") get_organization

> Return an organization

```python
def get_organization(self,
                         organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = organizations_controller.get_organization(organization_id)

```


### <a name="update_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.update_organization") update_organization

> Update an organization

```python
def update_organization(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganization |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

update_organization = UpdateOrganizationModel()
collect['update_organization'] = update_organization


result = organizations_controller.update_organization(collect)

```


### <a name="delete_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.delete_organization") delete_organization

> Delete an organization

```python
def delete_organization(self,
                            organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

organizations_controller.delete_organization(organization_id)

```


### <a name="claim_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.claim_organization") claim_organization

> Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization's inventory.

```python
def claim_organization(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| claimOrganization |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

claim_organization = ClaimOrganizationModel()
collect['claim_organization'] = claim_organization


result = organizations_controller.claim_organization(collect)

```


### <a name="clone_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.clone_organization") clone_organization

> Create a new organization by cloning the addressed organization

```python
def clone_organization(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| cloneOrganization |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

clone_organization = CloneOrganizationModel()
collect['clone_organization'] = clone_organization


result = organizations_controller.clone_organization(collect)

```


### <a name="get_organization_device_statuses"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_device_statuses") get_organization_device_statuses

> List the status of every Meraki device in the organization

```python
def get_organization_device_statuses(self,
                                         organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = organizations_controller.get_organization_device_statuses(organization_id)

```


### <a name="get_organization_inventory"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_inventory") get_organization_inventory

> Return the inventory for an organization

```python
def get_organization_inventory(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| includeLicenseInfo |  ``` Optional ```  | When this parameter is true, each entity in the response will include the license expiration date of the device (if any). Only applies to organizations that support per-device licensing. Defaults to false. |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

include_license_info = True
collect['include_license_info'] = include_license_info


result = organizations_controller.get_organization_inventory(collect)

```


### <a name="get_organization_license_state"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_license_state") get_organization_license_state

> Return the license state for an organization

```python
def get_organization_license_state(self,
                                       organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = organizations_controller.get_organization_license_state(organization_id)

```


### <a name="get_organization_third_party_vpn_peers"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_third_party_vpn_peers") get_organization_third_party_vpn_peers

> Return the third party VPN peers for an organization

```python
def get_organization_third_party_vpn_peers(self,
                                               organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = organizations_controller.get_organization_third_party_vpn_peers(organization_id)

```


### <a name="update_organization_third_party_vpn_peers"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.update_organization_third_party_vpn_peers") update_organization_third_party_vpn_peers

> Update the third party VPN peers for an organization

```python
def update_organization_third_party_vpn_peers(self,
                                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationThirdPartyVPNPeers |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

update_organization_third_party_vpn_peers = UpdateOrganizationThirdPartyVPNPeersModel()
collect['update_organization_third_party_vpn_peers'] = update_organization_third_party_vpn_peers


result = organizations_controller.update_organization_third_party_vpn_peers(collect)

```


### <a name="get_organization_uplinks_loss_and_latency"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_uplinks_loss_and_latency") get_organization_uplinks_loss_and_latency

> Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

```python
def get_organization_uplinks_loss_and_latency(self,
                                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes. |
| uplink |  ``` Optional ```  | Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks. |
| ip |  ``` Optional ```  | Optional filter for a specific destination IP. Default will return all destination IPs. |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 204.858464945507
collect['timespan'] = timespan

uplink = UplinkEnum.WAN1
collect['uplink'] = uplink

ip = 'ip'
collect['ip'] = ip


result = organizations_controller.get_organization_uplinks_loss_and_latency(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="pii_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PIIController") PIIController

### Get controller instance

An instance of the ``` PIIController ``` class can be accessed from the API Client.

```python
 pii_controller = client.pii
```

### <a name="get_network_pii_pii_keys"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.get_network_pii_pii_keys") get_network_pii_pii_keys

> List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key "0" containing the applicable keys.
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/piiKeys
> ```

```python
def get_network_pii_pii_keys(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| username |  ``` Optional ```  | The username of a Systems Manager user |
| email |  ``` Optional ```  | The email of a network user account or a Systems Manager device |
| mac |  ``` Optional ```  | The MAC of a network client device or a Systems Manager device |
| serial |  ``` Optional ```  | The serial of a Systems Manager device |
| imei |  ``` Optional ```  | The IMEI of a Systems Manager device |
| bluetoothMac |  ``` Optional ```  | The MAC of a Bluetooth client |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

username = 'username'
collect['username'] = username

email = 'email'
collect['email'] = email

mac = 'mac'
collect['mac'] = mac

serial = 'serial'
collect['serial'] = serial

imei = 'imei'
collect['imei'] = imei

bluetooth_mac = 'bluetoothMac'
collect['bluetooth_mac'] = bluetooth_mac


result = pii_controller.get_network_pii_pii_keys(collect)

```


### <a name="get_network_pii_requests"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.get_network_pii_requests") get_network_pii_requests

> List the PII requests for this network or organization
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests
> ```

```python
def get_network_pii_requests(self,
                                 network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = pii_controller.get_network_pii_requests(network_id)

```


### <a name="create_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.create_network_pii_request") create_network_pii_request

> Submit a new delete or restrict processing PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests
> ```

```python
def create_network_pii_request(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkPiiRequest |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_pii_request = CreateNetworkPiiRequestModel()
collect['create_network_pii_request'] = create_network_pii_request


result = pii_controller.create_network_pii_request(collect)

```


### <a name="get_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.get_network_pii_request") get_network_pii_request

> Return a PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests/{requestId}
> ```

```python
def get_network_pii_request(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| requestId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

request_id = 'requestId'
collect['request_id'] = request_id


result = pii_controller.get_network_pii_request(collect)

```


### <a name="delete_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.delete_network_pii_request") delete_network_pii_request

> Delete a restrict processing PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests/{requestId}
> ```

```python
def delete_network_pii_request(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| requestId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

request_id = 'requestId'
collect['request_id'] = request_id


pii_controller.delete_network_pii_request(collect)

```


### <a name="get_network_pii_sm_devices_for_key"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.get_network_pii_sm_devices_for_key") get_network_pii_sm_devices_for_key

> Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/smDevicesForKey
> ```

```python
def get_network_pii_sm_devices_for_key(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| username |  ``` Optional ```  | The username of a Systems Manager user |
| email |  ``` Optional ```  | The email of a network user account or a Systems Manager device |
| mac |  ``` Optional ```  | The MAC of a network client device or a Systems Manager device |
| serial |  ``` Optional ```  | The serial of a Systems Manager device |
| imei |  ``` Optional ```  | The IMEI of a Systems Manager device |
| bluetoothMac |  ``` Optional ```  | The MAC of a Bluetooth client |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

username = 'username'
collect['username'] = username

email = 'email'
collect['email'] = email

mac = 'mac'
collect['mac'] = mac

serial = 'serial'
collect['serial'] = serial

imei = 'imei'
collect['imei'] = imei

bluetooth_mac = 'bluetoothMac'
collect['bluetooth_mac'] = bluetooth_mac


result = pii_controller.get_network_pii_sm_devices_for_key(collect)

```


### <a name="get_network_pii_sm_owners_for_key"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.get_network_pii_sm_owners_for_key") get_network_pii_sm_owners_for_key

> Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/smOwnersForKey
> ```

```python
def get_network_pii_sm_owners_for_key(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| username |  ``` Optional ```  | The username of a Systems Manager user |
| email |  ``` Optional ```  | The email of a network user account or a Systems Manager device |
| mac |  ``` Optional ```  | The MAC of a network client device or a Systems Manager device |
| serial |  ``` Optional ```  | The serial of a Systems Manager device |
| imei |  ``` Optional ```  | The IMEI of a Systems Manager device |
| bluetoothMac |  ``` Optional ```  | The MAC of a Bluetooth client |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

username = 'username'
collect['username'] = username

email = 'email'
collect['email'] = email

mac = 'mac'
collect['mac'] = mac

serial = 'serial'
collect['serial'] = serial

imei = 'imei'
collect['imei'] = imei

bluetooth_mac = 'bluetoothMac'
collect['bluetooth_mac'] = bluetooth_mac


result = pii_controller.get_network_pii_sm_owners_for_key(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="radio_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RadioSettingsController") RadioSettingsController

### Get controller instance

An instance of the ``` RadioSettingsController ``` class can be accessed from the API Client.

```python
 radio_settings_controller = client.radio_settings
```

### <a name="get_network_device_wireless_radio_settings"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.get_network_device_wireless_radio_settings") get_network_device_wireless_radio_settings

> Return the radio settings of a device

```python
def get_network_device_wireless_radio_settings(self,
                                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


result = radio_settings_controller.get_network_device_wireless_radio_settings(collect)

```


### <a name="update_network_device_wireless_radio_settings"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.update_network_device_wireless_radio_settings") update_network_device_wireless_radio_settings

> Update the radio settings of a device

```python
def update_network_device_wireless_radio_settings(self,
                                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkDeviceWirelessRadioSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

update_network_device_wireless_radio_settings = UpdateNetworkDeviceWirelessRadioSettingsModel()
collect['update_network_device_wireless_radio_settings'] = update_network_device_wireless_radio_settings


result = radio_settings_controller.update_network_device_wireless_radio_settings(collect)

```


### <a name="get_network_wireless_rf_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.get_network_wireless_rf_profiles") get_network_wireless_rf_profiles

> List the non-basic RF profiles for this network

```python
def get_network_wireless_rf_profiles(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| includeTemplateProfiles |  ``` Optional ```  | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template
    should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

include_template_profiles = False
collect['include_template_profiles'] = include_template_profiles


result = radio_settings_controller.get_network_wireless_rf_profiles(collect)

```


### <a name="create_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.create_network_wireless_rf_profile") create_network_wireless_rf_profile

> Creates new RF profile for this network

```python
def create_network_wireless_rf_profile(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkWirelessRfProfile |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_wireless_rf_profile = CreateNetworkWirelessRfProfileModel()
collect['create_network_wireless_rf_profile'] = create_network_wireless_rf_profile


result = radio_settings_controller.create_network_wireless_rf_profile(collect)

```


### <a name="update_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.update_network_wireless_rf_profile") update_network_wireless_rf_profile

> Updates specified RF profile for this network

```python
def update_network_wireless_rf_profile(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| rfProfileId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkWirelessRfProfile |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

rf_profile_id = 'rfProfileId'
collect['rf_profile_id'] = rf_profile_id

update_network_wireless_rf_profile = UpdateNetworkWirelessRfProfileModel()
collect['update_network_wireless_rf_profile'] = update_network_wireless_rf_profile


result = radio_settings_controller.update_network_wireless_rf_profile(collect)

```


### <a name="delete_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.delete_network_wireless_rf_profile") delete_network_wireless_rf_profile

> Delete a RF Profile

```python
def delete_network_wireless_rf_profile(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| rfProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

rf_profile_id = 'rfProfileId'
collect['rf_profile_id'] = rf_profile_id


radio_settings_controller.delete_network_wireless_rf_profile(collect)

```


### <a name="get_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.get_network_wireless_rf_profile") get_network_wireless_rf_profile

> Return a RF profile

```python
def get_network_wireless_rf_profile(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| rfProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

rf_profile_id = 'rfProfileId'
collect['rf_profile_id'] = rf_profile_id


result = radio_settings_controller.get_network_wireless_rf_profile(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="saml_roles_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SAMLRolesController") SAMLRolesController

### Get controller instance

An instance of the ``` SAMLRolesController ``` class can be accessed from the API Client.

```python
 saml_roles_controller = client.saml_roles
```

### <a name="get_organization_saml_roles"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.get_organization_saml_roles") get_organization_saml_roles

> List the SAML roles for this organization

```python
def get_organization_saml_roles(self,
                                    organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = saml_roles_controller.get_organization_saml_roles(organization_id)

```


### <a name="create_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.create_organization_saml_role") create_organization_saml_role

> Create a SAML role

```python
def create_organization_saml_role(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationSamlRole |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_saml_role = CreateOrganizationSamlRoleModel()
collect['create_organization_saml_role'] = create_organization_saml_role


result = saml_roles_controller.create_organization_saml_role(collect)

```


### <a name="get_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.get_organization_saml_role") get_organization_saml_role

> Return a SAML role

```python
def get_organization_saml_role(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| samlRoleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

saml_role_id = 'samlRoleId'
collect['saml_role_id'] = saml_role_id


result = saml_roles_controller.get_organization_saml_role(collect)

```


### <a name="update_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.update_organization_saml_role") update_organization_saml_role

> Update a SAML role

```python
def update_organization_saml_role(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| samlRoleId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSamlRole |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

saml_role_id = 'samlRoleId'
collect['saml_role_id'] = saml_role_id

update_organization_saml_role = UpdateOrganizationSamlRoleModel()
collect['update_organization_saml_role'] = update_organization_saml_role


result = saml_roles_controller.update_organization_saml_role(collect)

```


### <a name="delete_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.delete_organization_saml_role") delete_organization_saml_role

> Remove a SAML role

```python
def delete_organization_saml_role(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| samlRoleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

saml_role_id = 'samlRoleId'
collect['saml_role_id'] = saml_role_id


saml_roles_controller.delete_organization_saml_role(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="sm_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SMController") SMController

### Get controller instance

An instance of the ``` SMController ``` class can be accessed from the API Client.

```python
 sm_controller = client.sm
```

### <a name="create_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.create_network_sm_app_polaris") create_network_sm_app_polaris

> Create a new Polaris app

```python
def create_network_sm_app_polaris(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmAppPolaris |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_sm_app_polaris = CreateNetworkSmAppPolarisModel()
collect['create_network_sm_app_polaris'] = create_network_sm_app_polaris


result = sm_controller.create_network_sm_app_polaris(collect)

```


### <a name="get_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_app_polaris") get_network_sm_app_polaris

> Get details for a Cisco Polaris app if it exists

```python
def get_network_sm_app_polaris(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| bundleId |  ``` Optional ```  | The bundle ID of the app to be found, defaults to com.cisco.ciscosecurity.app |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

bundle_id = 'bundleId'
collect['bundle_id'] = bundle_id


result = sm_controller.get_network_sm_app_polaris(collect)

```


### <a name="update_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_app_polaris") update_network_sm_app_polaris

> Update an existing Polaris app

```python
def update_network_sm_app_polaris(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmAppPolaris |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

app_id = 'appId'
collect['app_id'] = app_id

update_network_sm_app_polaris = UpdateNetworkSmAppPolarisModel()
collect['update_network_sm_app_polaris'] = update_network_sm_app_polaris


result = sm_controller.update_network_sm_app_polaris(collect)

```


### <a name="delete_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.delete_network_sm_app_polaris") delete_network_sm_app_polaris

> Delete a Cisco Polaris app

```python
def delete_network_sm_app_polaris(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

app_id = 'appId'
collect['app_id'] = app_id


result = sm_controller.delete_network_sm_app_polaris(collect)

```


### <a name="create_network_sm_bypass_activation_lock_attempt"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.create_network_sm_bypass_activation_lock_attempt") create_network_sm_bypass_activation_lock_attempt

> Bypass activation lock attempt

```python
def create_network_sm_bypass_activation_lock_attempt(self,
                                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmBypassActivationLockAttempt |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_sm_bypass_activation_lock_attempt = CreateNetworkSmBypassActivationLockAttemptModel()
collect['create_network_sm_bypass_activation_lock_attempt'] = create_network_sm_bypass_activation_lock_attempt


result = sm_controller.create_network_sm_bypass_activation_lock_attempt(collect)

```


### <a name="get_network_sm_bypass_activation_lock_attempt"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_bypass_activation_lock_attempt") get_network_sm_bypass_activation_lock_attempt

> Bypass activation lock attempt status

```python
def get_network_sm_bypass_activation_lock_attempt(self,
                                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| attemptId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

attempt_id = 'attemptId'
collect['attempt_id'] = attempt_id


result = sm_controller.get_network_sm_bypass_activation_lock_attempt(collect)

```


### <a name="update_network_sm_device_fields"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_device_fields") update_network_sm_device_fields

> Modify the fields of a device

```python
def update_network_sm_device_fields(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDeviceFields |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_sm_device_fields = UpdateNetworkSmDeviceFieldsModel()
collect['update_network_sm_device_fields'] = update_network_sm_device_fields


result = sm_controller.update_network_sm_device_fields(collect)

```


### <a name="wipe_network_sm_device"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.wipe_network_sm_device") wipe_network_sm_device

> Wipe a device

```python
def wipe_network_sm_device(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| wipeNetworkSmDevice |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

wipe_network_sm_device = WipeNetworkSmDeviceModel()
collect['wipe_network_sm_device'] = wipe_network_sm_device


result = sm_controller.wipe_network_sm_device(collect)

```


### <a name="refresh_network_sm_device_details"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.refresh_network_sm_device_details") refresh_network_sm_device_details

> Refresh the details of a device

```python
def refresh_network_sm_device_details(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


sm_controller.refresh_network_sm_device_details(collect)

```


### <a name="get_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_devices") get_network_sm_devices

> List the devices enrolled in an SM network with various specified fields and filters

```python
def get_network_sm_devices(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| fields |  ``` Optional ```  | Additional fields that will be displayed for each device. Multiple fields can be passed in as comma separated values.
    The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,
    systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,
    ownerEmail, ownerUsername, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
    simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
    isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,
    hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion. |
| wifiMacs |  ``` Optional ```  | Filter devices by wifi mac(s). Multiple wifi macs can be passed in as comma separated values. |
| serials |  ``` Optional ```  | Filter devices by serial(s). Multiple serials can be passed in as comma separated values. |
| ids |  ``` Optional ```  | Filter devices by id(s). Multiple ids can be passed in as comma separated values. |
| scope |  ``` Optional ```  | Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values. |
| batchSize |  ``` Optional ```  | Number of devices to return, 1000 is the default as well as the max. |
| batchToken |  ``` Optional ```  | If the network has more devices than the batch size, a batch token will be returned
    as a part of the device list. To see the remainder of the devices, pass in the batchToken as a parameter in the next request.
    Requests made with the batchToken do not require additional parameters as the batchToken includes the parameters passed in
    with the original request. Additional parameters passed in with the batchToken will be ignored. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

fields = 'fields'
collect['fields'] = fields

wifi_macs = 'wifiMacs'
collect['wifi_macs'] = wifi_macs

serials = 'serials'
collect['serials'] = serials

ids = 'ids'
collect['ids'] = ids

scope = 'scope'
collect['scope'] = scope

batch_size = 41
collect['batch_size'] = batch_size

batch_token = 'batchToken'
collect['batch_token'] = batch_token


result = sm_controller.get_network_sm_devices(collect)

```


### <a name="checkin_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.checkin_network_sm_devices") checkin_network_sm_devices

> Force check-in a set of devices

```python
def checkin_network_sm_devices(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| checkinNetworkSmDevices |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

checkin_network_sm_devices = CheckinNetworkSmDevicesModel()
collect['checkin_network_sm_devices'] = checkin_network_sm_devices


result = sm_controller.checkin_network_sm_devices(collect)

```


### <a name="move_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.move_network_sm_devices") move_network_sm_devices

> Move a set of devices to a new network

```python
def move_network_sm_devices(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| moveNetworkSmDevices |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

move_network_sm_devices = MoveNetworkSmDevicesModel()
collect['move_network_sm_devices'] = move_network_sm_devices


result = sm_controller.move_network_sm_devices(collect)

```


### <a name="update_network_sm_devices_tags"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_devices_tags") update_network_sm_devices_tags

> Add, delete, or update the tags of a set of devices

```python
def update_network_sm_devices_tags(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDevicesTags |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_sm_devices_tags = UpdateNetworkSmDevicesTagsModel()
collect['update_network_sm_devices_tags'] = update_network_sm_devices_tags


result = sm_controller.update_network_sm_devices_tags(collect)

```


### <a name="unenroll_network_sm_device"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.unenroll_network_sm_device") unenroll_network_sm_device

> Unenroll a device

```python
def unenroll_network_sm_device(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.unenroll_network_sm_device(collect)

```


### <a name="get_network_sm_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_profiles") get_network_sm_profiles

> List all the profiles in the network

```python
def get_network_sm_profiles(self,
                                network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = sm_controller.get_network_sm_profiles(network_id)

```


### <a name="get_network_sm_user_device_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_user_device_profiles") get_network_sm_user_device_profiles

> Get the profiles associated with a user

```python
def get_network_sm_user_device_profiles(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| userId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

user_id = 'userId'
collect['user_id'] = user_id


result = sm_controller.get_network_sm_user_device_profiles(collect)

```


### <a name="get_network_sm_user_softwares"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_user_softwares") get_network_sm_user_softwares

> Get a list of softwares associated with a user

```python
def get_network_sm_user_softwares(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| userId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

user_id = 'userId'
collect['user_id'] = user_id


result = sm_controller.get_network_sm_user_softwares(collect)

```


### <a name="get_network_sm_users"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_users") get_network_sm_users

> List the owners in an SM network with various specified fields and filters

```python
def get_network_sm_users(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| ids |  ``` Optional ```  | Filter users by id(s). Multiple ids can be passed in as comma separated values. |
| usernames |  ``` Optional ```  | Filter users by username(s). Multiple usernames can be passed in as comma separated values. |
| emails |  ``` Optional ```  | Filter users by email(s). Multiple emails can be passed in as comma separated values. |
| scope |  ``` Optional ```  | Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags as comma separated values. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

ids = 'ids'
collect['ids'] = ids

usernames = 'usernames'
collect['usernames'] = usernames

emails = 'emails'
collect['emails'] = emails

scope = 'scope'
collect['scope'] = scope


result = sm_controller.get_network_sm_users(collect)

```


### <a name="get_network_sm_cellular_usage_history"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_cellular_usage_history") get_network_sm_cellular_usage_history

> Return the client's daily cellular data usage history. Usage data is in kilobytes.

```python
def get_network_sm_cellular_usage_history(self,
                                              options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_cellular_usage_history(collect)

```


### <a name="get_network_sm_certs"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_certs") get_network_sm_certs

> List the certs on a device

```python
def get_network_sm_certs(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_certs(collect)

```


### <a name="get_network_sm_device_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_device_profiles") get_network_sm_device_profiles

> Get the profiles associated with a device

```python
def get_network_sm_device_profiles(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_device_profiles(collect)

```


### <a name="get_network_sm_network_adapters"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_network_adapters") get_network_sm_network_adapters

> List the network adapters of a device

```python
def get_network_sm_network_adapters(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_network_adapters(collect)

```


### <a name="get_network_sm_restrictions"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_restrictions") get_network_sm_restrictions

> List the restrictions on a device

```python
def get_network_sm_restrictions(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_restrictions(collect)

```


### <a name="get_network_sm_security_centers"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_security_centers") get_network_sm_security_centers

> List the security centers on a device

```python
def get_network_sm_security_centers(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_security_centers(collect)

```


### <a name="get_network_sm_softwares"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_softwares") get_network_sm_softwares

> Get a list of softwares associated with a device

```python
def get_network_sm_softwares(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_softwares(collect)

```


### <a name="get_network_sm_wlan_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_wlan_lists") get_network_sm_wlan_lists

> List the saved SSID names on a device

```python
def get_network_sm_wlan_lists(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

device_id = 'deviceId'
collect['device_id'] = device_id


result = sm_controller.get_network_sm_wlan_lists(collect)

```


### <a name="lock_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.lock_network_sm_devices") lock_network_sm_devices

> Lock a set of devices

```python
def lock_network_sm_devices(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| lockNetworkSmDevices |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

lock_network_sm_devices = LockNetworkSmDevicesModel()
collect['lock_network_sm_devices'] = lock_network_sm_devices


result = sm_controller.lock_network_sm_devices(collect)

```


### <a name="get_network_sm_connectivity"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_connectivity") get_network_sm_connectivity

> Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

```python
def get_network_sm_connectivity(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 41
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = sm_controller.get_network_sm_connectivity(collect)

```


### <a name="get_network_sm_desktop_logs"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_desktop_logs") get_network_sm_desktop_logs

> Return historical records of various Systems Manager network connection details for desktop devices.

```python
def get_network_sm_desktop_logs(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 41
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = sm_controller.get_network_sm_desktop_logs(collect)

```


### <a name="get_network_sm_device_command_logs"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_device_command_logs") get_network_sm_device_command_logs

>     Return historical records of commands sent to Systems Manager devices.
>     <p>Note that this will include the name of the Dashboard user who initiated the command if it was generated
>     by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out
>     of any reports.</p>
> 

```python
def get_network_sm_device_command_logs(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 41
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = sm_controller.get_network_sm_device_command_logs(collect)

```


### <a name="get_network_sm_performance_history"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_performance_history") get_network_sm_performance_history

> Return historical records of various Systems Manager client metrics for desktop devices.

```python
def get_network_sm_performance_history(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 41
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = sm_controller.get_network_sm_performance_history(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="snmp_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SNMPSettingsController") SNMPSettingsController

### Get controller instance

An instance of the ``` SNMPSettingsController ``` class can be accessed from the API Client.

```python
 snmp_settings_controller = client.snmp_settings
```

### <a name="get_network_snmp_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.get_network_snmp_settings") get_network_snmp_settings

> Return the SNMP settings for a network

```python
def get_network_snmp_settings(self,
                                  network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = snmp_settings_controller.get_network_snmp_settings(network_id)

```


### <a name="update_network_snmp_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.update_network_snmp_settings") update_network_snmp_settings

> Update the SNMP settings for a network

```python
def update_network_snmp_settings(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSnmpSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_snmp_settings = UpdateNetworkSnmpSettingsModel()
collect['update_network_snmp_settings'] = update_network_snmp_settings


result = snmp_settings_controller.update_network_snmp_settings(collect)

```


### <a name="get_organization_snmp"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.get_organization_snmp") get_organization_snmp

> Return the SNMP settings for an organization

```python
def get_organization_snmp(self,
                              organization_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
organization_id = 'organizationId'

result = snmp_settings_controller.get_organization_snmp(organization_id)

```


### <a name="update_organization_snmp"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.update_organization_snmp") update_organization_snmp

> Update the SNMP settings for an organization

```python
def update_organization_snmp(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSnmp |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

update_organization_snmp = UpdateOrganizationSnmpModel()
collect['update_organization_snmp'] = update_organization_snmp


result = snmp_settings_controller.update_organization_snmp(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="ssids_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SsidsController") SsidsController

### Get controller instance

An instance of the ``` SsidsController ``` class can be accessed from the API Client.

```python
 ssids_controller = client.ssids
```

### <a name="get_network_device_wireless_status"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.get_network_device_wireless_status") get_network_device_wireless_status

> Return the SSID statuses of an access point

```python
def get_network_device_wireless_status(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial


result = ssids_controller.get_network_device_wireless_status(collect)

```


### <a name="get_network_ssids"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.get_network_ssids") get_network_ssids

> List the SSIDs in a network. Supports networks with access points or wireless-enabled security appliances and teleworker gateways.

```python
def get_network_ssids(self,
                          network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = ssids_controller.get_network_ssids(network_id)

```


### <a name="get_network_ssid"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.get_network_ssid") get_network_ssid

> Return a single SSID

```python
def get_network_ssid(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number


result = ssids_controller.get_network_ssid(collect)

```


### <a name="update_network_ssid"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.update_network_ssid") update_network_ssid

> Update the attributes of an SSID

```python
def update_network_ssid(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSsid |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number

update_network_ssid = UpdateNetworkSsidModel()
collect['update_network_ssid'] = update_network_ssid


result = ssids_controller.update_network_ssid(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="security_events_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SecurityEventsController") SecurityEventsController

### Get controller instance

An instance of the ``` SecurityEventsController ``` class can be accessed from the API Client.

```python
 security_events_controller = client.security_events
```

### <a name="get_network_client_security_events"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityEventsController.get_network_client_security_events") get_network_client_security_events

> List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client_security_events(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 791 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 791 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 254.630573610603
collect['timespan'] = timespan

per_page = 254
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = security_events_controller.get_network_client_security_events(collect)

```


### <a name="get_network_security_events"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityEventsController.get_network_security_events") get_network_security_events

> List the security events for a network

```python
def get_network_security_events(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 365 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 254.630573610603
collect['timespan'] = timespan

per_page = 254
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = security_events_controller.get_network_security_events(collect)

```


### <a name="get_organization_security_events"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityEventsController.get_organization_security_events") get_organization_security_events

> List the security events for an organization

```python
def get_organization_security_events(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 365 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 254.630573610603
collect['timespan'] = timespan

per_page = 254
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = security_events_controller.get_organization_security_events(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="splash_login_attempts_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SplashLoginAttemptsController") SplashLoginAttemptsController

### Get controller instance

An instance of the ``` SplashLoginAttemptsController ``` class can be accessed from the API Client.

```python
 splash_login_attempts_controller = client.splash_login_attempts
```

### <a name="get_network_splash_login_attempts"></a>![Method: ](https://apidocs.io/img/method.png ".SplashLoginAttemptsController.get_network_splash_login_attempts") get_network_splash_login_attempts

> List the splash login attempts for a network

```python
def get_network_splash_login_attempts(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| ssidNumber |  ``` Optional ```  | Only return the login attempts for the specified SSID |
| loginIdentifier |  ``` Optional ```  | The username, email, or phone number used during login |
| timespan |  ``` Optional ```  | The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

ssid_number = SsidNumberEnum.ENUM_0
collect['ssid_number'] = ssid_number

login_identifier = 'loginIdentifier'
collect['login_identifier'] = login_identifier

timespan = 254
collect['timespan'] = timespan


result = splash_login_attempts_controller.get_network_splash_login_attempts(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="splash_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SplashSettingsController") SplashSettingsController

### Get controller instance

An instance of the ``` SplashSettingsController ``` class can be accessed from the API Client.

```python
 splash_settings_controller = client.splash_settings
```

### <a name="get_network_ssids_plash_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SplashSettingsController.get_network_ssids_plash_settings") get_network_ssids_plash_settings

> Display the splash page settings for the given SSID

```python
def get_network_ssids_plash_settings(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number


result = splash_settings_controller.get_network_ssids_plash_settings(collect)

```


### <a name="update_network_ssids_plash_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SplashSettingsController.update_network_ssids_plash_settings") update_network_ssids_plash_settings

> Modify the splash page settings for the given SSID

```python
def update_network_ssids_plash_settings(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork_ssids_PlashSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number

update_network_ssids_plash_settings = UpdateNetworkSsidsPlashSettingsModel()
collect['update_network_ssids_plash_settings'] = update_network_ssids_plash_settings


result = splash_settings_controller.update_network_ssids_plash_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="switch_acls_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchAclsController") SwitchAclsController

### Get controller instance

An instance of the ``` SwitchAclsController ``` class can be accessed from the API Client.

```python
 switch_acls_controller = client.switch_acls
```

### <a name="get_network_switch_access_control_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchAclsController.get_network_switch_access_control_lists") get_network_switch_access_control_lists

> Return the access control lists for a MS network

```python
def get_network_switch_access_control_lists(self,
                                                network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_acls_controller.get_network_switch_access_control_lists(network_id)

```


### <a name="update_network_switch_access_control_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchAclsController.update_network_switch_access_control_lists") update_network_switch_access_control_lists

> Update the access control lists for a MS network

```python
def update_network_switch_access_control_lists(self,
                                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchAccessControlLists |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_access_control_lists = UpdateNetworkSwitchAccessControlListsModel()
collect['update_network_switch_access_control_lists'] = update_network_switch_access_control_lists


result = switch_acls_controller.update_network_switch_access_control_lists(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="switch_port_schedules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchPortSchedulesController") SwitchPortSchedulesController

### Get controller instance

An instance of the ``` SwitchPortSchedulesController ``` class can be accessed from the API Client.

```python
 switch_port_schedules_controller = client.switch_port_schedules
```

### <a name="get_network_switch_port_schedules"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.get_network_switch_port_schedules") get_network_switch_port_schedules

> List switch port schedules

```python
def get_network_switch_port_schedules(self,
                                          network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_port_schedules_controller.get_network_switch_port_schedules(network_id)

```


### <a name="create_network_switch_port_schedule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.create_network_switch_port_schedule") create_network_switch_port_schedule

> Add a switch port schedule

```python
def create_network_switch_port_schedule(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchPortSchedule |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_switch_port_schedule = CreateNetworkSwitchPortScheduleModel()
collect['create_network_switch_port_schedule'] = create_network_switch_port_schedule


result = switch_port_schedules_controller.create_network_switch_port_schedule(collect)

```


### <a name="delete_network_switch_port_schedule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.delete_network_switch_port_schedule") delete_network_switch_port_schedule

> Delete a switch port schedule

```python
def delete_network_switch_port_schedule(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| portScheduleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

port_schedule_id = 'portScheduleId'
collect['port_schedule_id'] = port_schedule_id


switch_port_schedules_controller.delete_network_switch_port_schedule(collect)

```


### <a name="update_network_switch_port_schedule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.update_network_switch_port_schedule") update_network_switch_port_schedule

> Update a switch port schedule

```python
def update_network_switch_port_schedule(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| portScheduleId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchPortSchedule |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

port_schedule_id = 'portScheduleId'
collect['port_schedule_id'] = port_schedule_id

update_network_switch_port_schedule = UpdateNetworkSwitchPortScheduleModel()
collect['update_network_switch_port_schedule'] = update_network_switch_port_schedule


result = switch_port_schedules_controller.update_network_switch_port_schedule(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="switch_ports_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchPortsController") SwitchPortsController

### Get controller instance

An instance of the ``` SwitchPortsController ``` class can be accessed from the API Client.

```python
 switch_ports_controller = client.switch_ports
```

### <a name="get_device_switch_port_statuses"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.get_device_switch_port_statuses") get_device_switch_port_statuses

> Return the status for all the ports of a switch

```python
def get_device_switch_port_statuses(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

t_0 = 't0'
collect['t_0'] = t_0

timespan = 254.630573610603
collect['timespan'] = timespan


result = switch_ports_controller.get_device_switch_port_statuses(collect)

```


### <a name="get_device_switch_port_statuses_packets"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.get_device_switch_port_statuses_packets") get_device_switch_port_statuses_packets

> Return the packet counters for all the ports of a switch

```python
def get_device_switch_port_statuses_packets(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 1 day from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

t_0 = 't0'
collect['t_0'] = t_0

timespan = 254.630573610603
collect['timespan'] = timespan


result = switch_ports_controller.get_device_switch_port_statuses_packets(collect)

```


### <a name="get_device_switch_ports"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.get_device_switch_ports") get_device_switch_ports

> List the switch ports for a switch

```python
def get_device_switch_ports(self,
                                serial)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
serial = 'serial'

result = switch_ports_controller.get_device_switch_ports(serial)

```


### <a name="get_device_switch_port"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.get_device_switch_port") get_device_switch_port

> Return a switch port

```python
def get_device_switch_port(self,
                               options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

number = 'number'
collect['number'] = number


result = switch_ports_controller.get_device_switch_port(collect)

```


### <a name="update_device_switch_port"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.update_device_switch_port") update_device_switch_port

> Update a switch port

```python
def update_device_switch_port(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceSwitchPort |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

number = 'number'
collect['number'] = number

update_device_switch_port = UpdateDeviceSwitchPortModel()
collect['update_device_switch_port'] = update_device_switch_port


result = switch_ports_controller.update_device_switch_port(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="switch_profiles_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchProfilesController") SwitchProfilesController

### Get controller instance

An instance of the ``` SwitchProfilesController ``` class can be accessed from the API Client.

```python
 switch_profiles_controller = client.switch_profiles
```

### <a name="get_organization_config_template_switch_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchProfilesController.get_organization_config_template_switch_profiles") get_organization_config_template_switch_profiles

> List the switch profiles for your switch template configuration

```python
def get_organization_config_template_switch_profiles(self,
                                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| configTemplateId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

config_template_id = 'configTemplateId'
collect['config_template_id'] = config_template_id


result = switch_profiles_controller.get_organization_config_template_switch_profiles(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="switch_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchSettingsController") SwitchSettingsController

### Get controller instance

An instance of the ``` SwitchSettingsController ``` class can be accessed from the API Client.

```python
 switch_settings_controller = client.switch_settings
```

### <a name="get_network_switch_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings") get_network_switch_settings

> Returns the switch network settings

```python
def get_network_switch_settings(self,
                                    network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings(network_id)

```


### <a name="update_network_switch_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings") update_network_switch_settings

> Update switch network settings

```python
def update_network_switch_settings(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings = UpdateNetworkSwitchSettingsModel()
collect['update_network_switch_settings'] = update_network_switch_settings


result = switch_settings_controller.update_network_switch_settings(collect)

```


### <a name="get_network_switch_settings_dhcp_server_policy"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_dhcp_server_policy") get_network_switch_settings_dhcp_server_policy

> Return the DHCP server policy

```python
def get_network_switch_settings_dhcp_server_policy(self,
                                                       network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_dhcp_server_policy(network_id)

```


### <a name="update_network_switch_settings_dhcp_server_policy"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_dhcp_server_policy") update_network_switch_settings_dhcp_server_policy

> Update the DHCP server policy

```python
def update_network_switch_settings_dhcp_server_policy(self,
                                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsDhcpServerPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings_dhcp_server_policy = UpdateNetworkSwitchSettingsDhcpServerPolicyModel()
collect['update_network_switch_settings_dhcp_server_policy'] = update_network_switch_settings_dhcp_server_policy


result = switch_settings_controller.update_network_switch_settings_dhcp_server_policy(collect)

```


### <a name="get_network_switch_settings_dscp_to_cos_mappings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_dscp_to_cos_mappings") get_network_switch_settings_dscp_to_cos_mappings

> Return the DSCP to CoS mappings

```python
def get_network_switch_settings_dscp_to_cos_mappings(self,
                                                         network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_dscp_to_cos_mappings(network_id)

```


### <a name="update_network_switch_settings_dscp_to_cos_mappings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_dscp_to_cos_mappings") update_network_switch_settings_dscp_to_cos_mappings

> Update the DSCP to CoS mappings

```python
def update_network_switch_settings_dscp_to_cos_mappings(self,
                                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsDscpToCosMappings |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings_dscp_to_cos_mappings = UpdateNetworkSwitchSettingsDscpToCosMappingsModel()
collect['update_network_switch_settings_dscp_to_cos_mappings'] = update_network_switch_settings_dscp_to_cos_mappings


result = switch_settings_controller.update_network_switch_settings_dscp_to_cos_mappings(collect)

```


### <a name="get_network_switch_settings_mtu"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_mtu") get_network_switch_settings_mtu

> Return the MTU configuration

```python
def get_network_switch_settings_mtu(self,
                                        network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_mtu(network_id)

```


### <a name="update_network_switch_settings_mtu"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_mtu") update_network_switch_settings_mtu

> Update the MTU configuration

```python
def update_network_switch_settings_mtu(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsMtu |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings_mtu = UpdateNetworkSwitchSettingsMtuModel()
collect['update_network_switch_settings_mtu'] = update_network_switch_settings_mtu


result = switch_settings_controller.update_network_switch_settings_mtu(collect)

```


### <a name="get_network_switch_settings_multicast"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_multicast") get_network_switch_settings_multicast

> Return Multicast settings for a network

```python
def get_network_switch_settings_multicast(self,
                                              network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_multicast(network_id)

```


### <a name="update_network_switch_settings_multicast"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_multicast") update_network_switch_settings_multicast

> Update multicast settings for a network

```python
def update_network_switch_settings_multicast(self,
                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsMulticast |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings_multicast = UpdateNetworkSwitchSettingsMulticastModel()
collect['update_network_switch_settings_multicast'] = update_network_switch_settings_multicast


result = switch_settings_controller.update_network_switch_settings_multicast(collect)

```


### <a name="get_network_switch_settings_qos_rules"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_qos_rules") get_network_switch_settings_qos_rules

> List quality of service rules

```python
def get_network_switch_settings_qos_rules(self,
                                              network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_qos_rules(network_id)

```


### <a name="create_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.create_network_switch_settings_qos_rule") create_network_switch_settings_qos_rule

> Add a quality of service rule

```python
def create_network_switch_settings_qos_rule(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchSettingsQosRule |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_switch_settings_qos_rule = CreateNetworkSwitchSettingsQosRuleModel()
collect['create_network_switch_settings_qos_rule'] = create_network_switch_settings_qos_rule


result = switch_settings_controller.create_network_switch_settings_qos_rule(collect)

```


### <a name="get_network_switch_settings_qos_rules_order"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_qos_rules_order") get_network_switch_settings_qos_rules_order

> Return the quality of service rule IDs by order in which they will be processed by the switch

```python
def get_network_switch_settings_qos_rules_order(self,
                                                    network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_qos_rules_order(network_id)

```


### <a name="update_network_switch_settings_qos_rules_order"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_qos_rules_order") update_network_switch_settings_qos_rules_order

> Update the order in which the rules should be processed by the switch

```python
def update_network_switch_settings_qos_rules_order(self,
                                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsQosRulesOrder |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings_qos_rules_order = UpdateNetworkSwitchSettingsQosRulesOrderModel()
collect['update_network_switch_settings_qos_rules_order'] = update_network_switch_settings_qos_rules_order


result = switch_settings_controller.update_network_switch_settings_qos_rules_order(collect)

```


### <a name="get_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_qos_rule") get_network_switch_settings_qos_rule

> Return a quality of service rule

```python
def get_network_switch_settings_qos_rule(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qosRuleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

qos_rule_id = 'qosRuleId'
collect['qos_rule_id'] = qos_rule_id


result = switch_settings_controller.get_network_switch_settings_qos_rule(collect)

```


### <a name="delete_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.delete_network_switch_settings_qos_rule") delete_network_switch_settings_qos_rule

> Delete a quality of service rule

```python
def delete_network_switch_settings_qos_rule(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qosRuleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

qos_rule_id = 'qosRuleId'
collect['qos_rule_id'] = qos_rule_id


switch_settings_controller.delete_network_switch_settings_qos_rule(collect)

```


### <a name="update_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_qos_rule") update_network_switch_settings_qos_rule

> Update a quality of service rule

```python
def update_network_switch_settings_qos_rule(self,
                                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qosRuleId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsQosRule |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

qos_rule_id = 'qosRuleId'
collect['qos_rule_id'] = qos_rule_id

update_network_switch_settings_qos_rule = UpdateNetworkSwitchSettingsQosRuleModel()
collect['update_network_switch_settings_qos_rule'] = update_network_switch_settings_qos_rule


result = switch_settings_controller.update_network_switch_settings_qos_rule(collect)

```


### <a name="get_network_switch_settings_storm_control"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_storm_control") get_network_switch_settings_storm_control

> Return the storm control configuration for a switch network

```python
def get_network_switch_settings_storm_control(self,
                                                  network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_storm_control(network_id)

```


### <a name="update_network_switch_settings_storm_control"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_storm_control") update_network_switch_settings_storm_control

> Update the storm control configuration for a switch network

```python
def update_network_switch_settings_storm_control(self,
                                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsStormControl |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings_storm_control = UpdateNetworkSwitchSettingsStormControlModel()
collect['update_network_switch_settings_storm_control'] = update_network_switch_settings_storm_control


result = switch_settings_controller.update_network_switch_settings_storm_control(collect)

```


### <a name="get_network_switch_settings_stp"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.get_network_switch_settings_stp") get_network_switch_settings_stp

> Returns STP settings

```python
def get_network_switch_settings_stp(self,
                                        network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_settings_controller.get_network_switch_settings_stp(network_id)

```


### <a name="update_network_switch_settings_stp"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.update_network_switch_settings_stp") update_network_switch_settings_stp

> Updates STP settings

```python
def update_network_switch_settings_stp(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsStp |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_switch_settings_stp = UpdateNetworkSwitchSettingsStpModel()
collect['update_network_switch_settings_stp'] = update_network_switch_settings_stp


result = switch_settings_controller.update_network_switch_settings_stp(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="switch_stacks_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchStacksController") SwitchStacksController

### Get controller instance

An instance of the ``` SwitchStacksController ``` class can be accessed from the API Client.

```python
 switch_stacks_controller = client.switch_stacks
```

### <a name="get_network_switch_stacks"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.get_network_switch_stacks") get_network_switch_stacks

> List the switch stacks in a network

```python
def get_network_switch_stacks(self,
                                  network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = switch_stacks_controller.get_network_switch_stacks(network_id)

```


### <a name="create_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.create_network_switch_stack") create_network_switch_stack

> Create a stack

```python
def create_network_switch_stack(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchStack |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_switch_stack = CreateNetworkSwitchStackModel()
collect['create_network_switch_stack'] = create_network_switch_stack


result = switch_stacks_controller.create_network_switch_stack(collect)

```


### <a name="get_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.get_network_switch_stack") get_network_switch_stack

> Show a switch stack

```python
def get_network_switch_stack(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

switch_stack_id = 'switchStackId'
collect['switch_stack_id'] = switch_stack_id


result = switch_stacks_controller.get_network_switch_stack(collect)

```


### <a name="delete_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.delete_network_switch_stack") delete_network_switch_stack

> Delete a stack

```python
def delete_network_switch_stack(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

switch_stack_id = 'switchStackId'
collect['switch_stack_id'] = switch_stack_id


switch_stacks_controller.delete_network_switch_stack(collect)

```


### <a name="add_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.add_network_switch_stack") add_network_switch_stack

> Add a switch to a stack

```python
def add_network_switch_stack(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |
| addNetworkSwitchStack |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

switch_stack_id = 'switchStackId'
collect['switch_stack_id'] = switch_stack_id

add_network_switch_stack = AddNetworkSwitchStackModel()
collect['add_network_switch_stack'] = add_network_switch_stack


result = switch_stacks_controller.add_network_switch_stack(collect)

```


### <a name="remove_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.remove_network_switch_stack") remove_network_switch_stack

> Remove a switch from a stack

```python
def remove_network_switch_stack(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |
| removeNetworkSwitchStack |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

switch_stack_id = 'switchStackId'
collect['switch_stack_id'] = switch_stack_id

remove_network_switch_stack = RemoveNetworkSwitchStackModel()
collect['remove_network_switch_stack'] = remove_network_switch_stack


result = switch_stacks_controller.remove_network_switch_stack(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="syslog_servers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SyslogServersController") SyslogServersController

### Get controller instance

An instance of the ``` SyslogServersController ``` class can be accessed from the API Client.

```python
 syslog_servers_controller = client.syslog_servers
```

### <a name="get_network_syslog_servers"></a>![Method: ](https://apidocs.io/img/method.png ".SyslogServersController.get_network_syslog_servers") get_network_syslog_servers

> List the syslog servers for a network

```python
def get_network_syslog_servers(self,
                                   network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = syslog_servers_controller.get_network_syslog_servers(network_id)

```


### <a name="update_network_syslog_servers"></a>![Method: ](https://apidocs.io/img/method.png ".SyslogServersController.update_network_syslog_servers") update_network_syslog_servers

> Update the syslog servers for a network

```python
def update_network_syslog_servers(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSyslogServers |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_syslog_servers = UpdateNetworkSyslogServersModel()
collect['update_network_syslog_servers'] = update_network_syslog_servers


result = syslog_servers_controller.update_network_syslog_servers(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="traffic_analysis_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TrafficAnalysisSettingsController") TrafficAnalysisSettingsController

### Get controller instance

An instance of the ``` TrafficAnalysisSettingsController ``` class can be accessed from the API Client.

```python
 traffic_analysis_settings_controller = client.traffic_analysis_settings
```

### <a name="get_network_traffic_analysis_settings"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficAnalysisSettingsController.get_network_traffic_analysis_settings") get_network_traffic_analysis_settings

> Return the traffic analysis settings for a network

```python
def get_network_traffic_analysis_settings(self,
                                              network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = traffic_analysis_settings_controller.get_network_traffic_analysis_settings(network_id)

```


### <a name="update_network_traffic_analysis_settings"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficAnalysisSettingsController.update_network_traffic_analysis_settings") update_network_traffic_analysis_settings

> Update the traffic analysis settings for a network

```python
def update_network_traffic_analysis_settings(self,
                                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkTrafficAnalysisSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_traffic_analysis_settings = UpdateNetworkTrafficAnalysisSettingsModel()
collect['update_network_traffic_analysis_settings'] = update_network_traffic_analysis_settings


result = traffic_analysis_settings_controller.update_network_traffic_analysis_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="traffic_shaping_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TrafficShapingController") TrafficShapingController

### Get controller instance

An instance of the ``` TrafficShapingController ``` class can be accessed from the API Client.

```python
 traffic_shaping_controller = client.traffic_shaping
```

### <a name="update_network_ssid_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.update_network_ssid_traffic_shaping") update_network_ssid_traffic_shaping

> Update the traffic shaping settings for an SSID on an MR network

```python
def update_network_ssid_traffic_shaping(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSsidTrafficShaping |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number

update_network_ssid_traffic_shaping = UpdateNetworkSsidTrafficShapingModel()
collect['update_network_ssid_traffic_shaping'] = update_network_ssid_traffic_shaping


result = traffic_shaping_controller.update_network_ssid_traffic_shaping(collect)

```


### <a name="get_network_ssid_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.get_network_ssid_traffic_shaping") get_network_ssid_traffic_shaping

> Display the traffic shaping settings for a SSID on an MR network

```python
def get_network_ssid_traffic_shaping(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

number = 'number'
collect['number'] = number


result = traffic_shaping_controller.get_network_ssid_traffic_shaping(collect)

```


### <a name="update_network_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.update_network_traffic_shaping") update_network_traffic_shaping

> Update the traffic shaping settings for an MX network

```python
def update_network_traffic_shaping(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkTrafficShaping |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_traffic_shaping = UpdateNetworkTrafficShapingModel()
collect['update_network_traffic_shaping'] = update_network_traffic_shaping


result = traffic_shaping_controller.update_network_traffic_shaping(collect)

```


### <a name="get_network_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.get_network_traffic_shaping") get_network_traffic_shaping

> Display the traffic shaping settings for an MX network

```python
def get_network_traffic_shaping(self,
                                    network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = traffic_shaping_controller.get_network_traffic_shaping(network_id)

```


### <a name="get_network_traffic_shaping_application_categories"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.get_network_traffic_shaping_application_categories") get_network_traffic_shaping_application_categories

> Returns the application categories for traffic shaping rules.

```python
def get_network_traffic_shaping_application_categories(self,
                                                           network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = traffic_shaping_controller.get_network_traffic_shaping_application_categories(network_id)

```


### <a name="get_network_traffic_shaping_dscp_tagging_options"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.get_network_traffic_shaping_dscp_tagging_options") get_network_traffic_shaping_dscp_tagging_options

> Returns the available DSCP tagging options for your traffic shaping rules.

```python
def get_network_traffic_shaping_dscp_tagging_options(self,
                                                         network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = traffic_shaping_controller.get_network_traffic_shaping_dscp_tagging_options(network_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="uplink_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".UplinkSettingsController") UplinkSettingsController

### Get controller instance

An instance of the ``` UplinkSettingsController ``` class can be accessed from the API Client.

```python
 uplink_settings_controller = client.uplink_settings
```

### <a name="get_network_uplink_settings"></a>![Method: ](https://apidocs.io/img/method.png ".UplinkSettingsController.get_network_uplink_settings") get_network_uplink_settings

> Returns the uplink settings for your MX network.

```python
def get_network_uplink_settings(self,
                                    network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = uplink_settings_controller.get_network_uplink_settings(network_id)

```


### <a name="update_network_uplink_settings"></a>![Method: ](https://apidocs.io/img/method.png ".UplinkSettingsController.update_network_uplink_settings") update_network_uplink_settings

> Updates the uplink settings for your MX network.

```python
def update_network_uplink_settings(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkUplinkSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_uplink_settings = UpdateNetworkUplinkSettingsModel()
collect['update_network_uplink_settings'] = update_network_uplink_settings


result = uplink_settings_controller.update_network_uplink_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="vlans_controller"></a>![Class: ](https://apidocs.io/img/class.png ".VlansController") VlansController

### Get controller instance

An instance of the ``` VlansController ``` class can be accessed from the API Client.

```python
 vlans_controller = client.vlans
```

### <a name="get_network_vlans"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.get_network_vlans") get_network_vlans

> List the VLANs for an MX network

```python
def get_network_vlans(self,
                          network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = vlans_controller.get_network_vlans(network_id)

```


### <a name="create_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.create_network_vlan") create_network_vlan

> Add a VLAN

```python
def create_network_vlan(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkVlan |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_vlan = CreateNetworkVlanModel()
collect['create_network_vlan'] = create_network_vlan


result = vlans_controller.create_network_vlan(collect)

```


### <a name="get_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.get_network_vlan") get_network_vlan

> Return a VLAN

```python
def get_network_vlan(self,
                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| vlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

vlan_id = 'vlanId'
collect['vlan_id'] = vlan_id


result = vlans_controller.get_network_vlan(collect)

```


### <a name="update_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.update_network_vlan") update_network_vlan

> Update a VLAN

```python
def update_network_vlan(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| vlanId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkVlan |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

vlan_id = 'vlanId'
collect['vlan_id'] = vlan_id

update_network_vlan = UpdateNetworkVlanModel()
collect['update_network_vlan'] = update_network_vlan


result = vlans_controller.update_network_vlan(collect)

```


### <a name="delete_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.delete_network_vlan") delete_network_vlan

> Delete a VLAN from a network

```python
def delete_network_vlan(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| vlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

vlan_id = 'vlanId'
collect['vlan_id'] = vlan_id


vlans_controller.delete_network_vlan(collect)

```


### <a name="get_network_vlans_enabled_state"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.get_network_vlans_enabled_state") get_network_vlans_enabled_state

> Returns the enabled status of VLANs for the network

```python
def get_network_vlans_enabled_state(self,
                                        network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = vlans_controller.get_network_vlans_enabled_state(network_id)

```


### <a name="update_network_vlans_enabled_state"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.update_network_vlans_enabled_state") update_network_vlans_enabled_state

> Enable/Disable VLANs for the given network

```python
def update_network_vlans_enabled_state(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork_vlans_EnabledState |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_vlans_enabled_state = UpdateNetworkVlansEnabledStateModel()
collect['update_network_vlans_enabled_state'] = update_network_vlans_enabled_state


result = vlans_controller.update_network_vlans_enabled_state(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="webhook_logs_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WebhookLogsController") WebhookLogsController

### Get controller instance

An instance of the ``` WebhookLogsController ``` class can be accessed from the API Client.

```python
 webhook_logs_controller = client.webhook_logs
```

### <a name="get_organization_webhook_logs"></a>![Method: ](https://apidocs.io/img/method.png ".WebhookLogsController.get_organization_webhook_logs") get_organization_webhook_logs

> Return the log of webhook POSTs sent

```python
def get_organization_webhook_logs(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 90 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 31 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| url |  ``` Optional ```  | The URL the webhook was sent to |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 91.1258555022654
collect['timespan'] = timespan

per_page = 91
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before

url = 'url'
collect['url'] = url


result = webhook_logs_controller.get_organization_webhook_logs(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="wireless_health_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WirelessHealthController") WirelessHealthController

### Get controller instance

An instance of the ``` WirelessHealthController ``` class can be accessed from the API Client.

```python
 wireless_health_controller = client.wireless_health
```

### <a name="get_network_clients_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_clients_connection_stats") get_network_clients_connection_stats

> Aggregated connectivity info for this network, grouped by clients

```python
def get_network_clients_connection_stats(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 91.1258555022654
collect['timespan'] = timespan

ssid = 91
collect['ssid'] = ssid

vlan = 91
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_clients_connection_stats(collect)

```


### <a name="get_network_clients_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_clients_latency_stats") get_network_clients_latency_stats

> Aggregated latency info for this network, grouped by clients

```python
def get_network_clients_latency_stats(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 91.1258555022654
collect['timespan'] = timespan

ssid = 91
collect['ssid'] = ssid

vlan = 91
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_clients_latency_stats(collect)

```


### <a name="get_network_client_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_client_connection_stats") get_network_client_connection_stats

> Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.

```python
def get_network_client_connection_stats(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 91.1258555022654
collect['timespan'] = timespan

ssid = 91
collect['ssid'] = ssid

vlan = 91
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_client_connection_stats(collect)

```


### <a name="get_network_client_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_client_latency_stats") get_network_client_latency_stats

> Aggregated latency info for a given client on this network. Clients are identified by their MAC.

```python
def get_network_client_latency_stats(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 91.1258555022654
collect['timespan'] = timespan

ssid = 91
collect['ssid'] = ssid

vlan = 91
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_client_latency_stats(collect)

```


### <a name="get_network_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_connection_stats") get_network_connection_stats

> Aggregated connectivity info for this network

```python
def get_network_connection_stats(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 91.1258555022654
collect['timespan'] = timespan

ssid = 91
collect['ssid'] = ssid

vlan = 91
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_connection_stats(collect)

```


### <a name="get_network_devices_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_devices_connection_stats") get_network_devices_connection_stats

> Aggregated connectivity info for this network, grouped by node

```python
def get_network_devices_connection_stats(self,
                                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 91.1258555022654
collect['timespan'] = timespan

ssid = 91
collect['ssid'] = ssid

vlan = 91
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_devices_connection_stats(collect)

```


### <a name="get_network_devices_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_devices_latency_stats") get_network_devices_latency_stats

> Aggregated latency info for this network, grouped by node

```python
def get_network_devices_latency_stats(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 49.4026822756988
collect['timespan'] = timespan

ssid = 49
collect['ssid'] = ssid

vlan = 49
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_devices_latency_stats(collect)

```


### <a name="get_network_device_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_device_connection_stats") get_network_device_connection_stats

> Aggregated connectivity info for a given AP on this network

```python
def get_network_device_connection_stats(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 49.4026822756988
collect['timespan'] = timespan

ssid = 49
collect['ssid'] = ssid

vlan = 49
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_device_connection_stats(collect)

```


### <a name="get_network_device_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_device_latency_stats") get_network_device_latency_stats

> Aggregated latency info for a given AP on this network

```python
def get_network_device_latency_stats(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 49.4026822756988
collect['timespan'] = timespan

ssid = 49
collect['ssid'] = ssid

vlan = 49
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_device_latency_stats(collect)

```


### <a name="get_network_failed_connections"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_failed_connections") get_network_failed_connections

> List of all failed client connection events on this network in a given time range

```python
def get_network_failed_connections(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| serial |  ``` Optional ```  | Filter by AP |
| clientId |  ``` Optional ```  | Filter by client MAC |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 49.4026822756988
collect['timespan'] = timespan

ssid = 49
collect['ssid'] = ssid

vlan = 49
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

serial = 'serial'
collect['serial'] = serial

client_id = 'clientId'
collect['client_id'] = client_id


result = wireless_health_controller.get_network_failed_connections(collect)

```


### <a name="get_network_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_latency_stats") get_network_latency_stats

> Aggregated latency info for this network

```python
def get_network_latency_stats(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t_0 = 't0'
collect['t_0'] = t_0

t_1 = 't1'
collect['t_1'] = t_1

timespan = 49.4026822756988
collect['timespan'] = timespan

ssid = 49
collect['ssid'] = ssid

vlan = 49
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_latency_stats(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="wireless_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WirelessSettingsController") WirelessSettingsController

### Get controller instance

An instance of the ``` WirelessSettingsController ``` class can be accessed from the API Client.

```python
 wireless_settings_controller = client.wireless_settings
```

### <a name="get_network_wireless_settings"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessSettingsController.get_network_wireless_settings") get_network_wireless_settings

> Return the wireless settings for a network

```python
def get_network_wireless_settings(self,
                                      network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = wireless_settings_controller.get_network_wireless_settings(network_id)

```


### <a name="update_network_wireless_settings"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessSettingsController.update_network_wireless_settings") update_network_wireless_settings

> Update the wireless settings for a network

```python
def update_network_wireless_settings(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkWirelessSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_wireless_settings = UpdateNetworkWirelessSettingsModel()
collect['update_network_wireless_settings'] = update_network_wireless_settings


result = wireless_settings_controller.update_network_wireless_settings(collect)

```


[Back to List of Controllers](#list_of_controllers)



