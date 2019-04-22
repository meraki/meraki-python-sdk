# Getting started

The Cisco Meraki Dashboard API is a modern REST API based on the [OpenAPI](https://swagger.io/docs/specification/about/) specification.

## What can the API be used for?
The Dashboard API can be used for many purposes. It’s meant to be an open-ended tool. Here are some examples of use cases:

* Add new organizations, admins, networks, devices, VLANs, and more
* Configure networks at scale
* Automatically on-board and off-board new employees’ teleworker setups
* Build your own dashboard for store managers, field techs, or unique use cases

## Enabling the Dashboard API
1. Begin by logging into [Meraki Dashboard](https://dashboard.meraki.com) and navigating to **Organization > Settings**

2. Locate the section titled **Dashboard API access** and select **Enable Access**, then **Save** your changes

3. After enabling the API, choose your username at the top-right of the Meraki Dashboard and select **my profile**

4. Locate the section titled **Dashboard API access** and select **Generate new API key**

*Note: The API key is associated with a Dashboard administrator account. You can generate, revoke, and regenerate your API key on your profile.*

**Keep your API key safe as it provides authentication to all of your organizations with the API enabled. If your API key is shared, you can regenerate your API key at any time. This will revoke the existing API key.**

Copy and store your API key in a safe place. Dashboard does not store API keys in plaintext for security reasons, so this is the only time you will be able to record it. If you lose or forget your API key, you will have to revoke it and generate a new one.

Every request must specify an API key via a request header.

The API key must be specified in the URL header. The API will return a 404 (rather than a 403) in response to a request with a missing or incorrect API key in order to prevent leaking the existence of resources to unauthorized users.

`X-Cisco-Meraki-API-Key: <secret key>`

Read more about API [authorization](../api/#/python/getting-started/authorizing-your-client)


## Versioning
Once an API version is released, we will make only backwards-compatible changes to it. Backwards-compatible changes include:

* Adding new API resources

* Adding new optional request parameters to existing API methods

* Adding new properties to existing API responses

* Changing the order of properties in existing API responses

## Rate Limit
* The Dashboard API is limited to **5 calls per second**, per organization.
* A burst of 5 additional calls are allowed in the first second, so a maximum of 15 calls in the first 2 seconds.
* The rate limiting technique is based off of the [token bucket model](https://en.wikipedia.org/wiki/Token_bucket).
* An error with a `429` status code will be returned when the rate limit has been exceeded.
* Expect to backoff for 1 - 2 seconds if the limit has been exceeded. You may have to wait potentially longer if a large number of requests were made within this timeframe.


## Additional Details
Identifiers in the API are opaque strings. A `{networkId}`, for example, might be the string “126043”, whereas an `{orderId}` might contain characters, such as “4S1234567”. Client applications must not try to parse them as numbers. Even identifiers that look like numbers might be too long to encode without loss of precision in Javascript, where the only numeric type is IEEE 754 floating point.

Verbs in the API follow the usual REST conventions:

`GET` returns the value of a resource or a list of resources, depending on whether an identifier is specified. For example, a `GET` of `/v0/organizations` returns a list of organizations, whereas a `GET` of `/v0/organizations/{organizationId}` returns a particular organization.

`POST` adds a new resource, as in a `POST` to `/v0/organizations/{organizationId}/admins`, or performs some other non-idempotent change.

`PUT` updates a resource. `PUTs` are idempotent; they update a resource, creating it first if it does not already exist. A `PUT` should specify all the fields of a resource; the API will revert omitted fields to their default value.

`DELETE` removes a resource.


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

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Meraki-Python&projectName=meraki)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Meraki-Python&projectName=meraki)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Meraki-Python&projectName=meraki)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from meraki.meraki import Meraki
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Meraki-Python&libraryName=meraki.meraki&projectName=meraki&className=Meraki)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Meraki-Python&libraryName=meraki.meraki&projectName=meraki&className=Meraki)


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

client = Meraki(x_cisco_meraki_api_key)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [AdminsController](#admins_controller)
* [AlertSettingsController](#alert_settings_controller)
* [MVSenseController](#mv_sense_controller)
* [APIUsageController](#api_usage_controller)
* [BluetoothClientsController](#bluetooth_clients_controller)
* [NetworksController](#networks_controller)
* [CamerasController](#cameras_controller)
* [ClientsController](#clients_controller)
* [ConfigTemplatesController](#config_templates_controller)
* [DevicesController](#devices_controller)
* [MXCellularFirewallController](#mx_cellular_firewall_controller)
* [MXL3FirewallController](#mxl3_firewall_controller)
* [MXL7ApplicationCategoriesController](#mxl7_application_categories_controller)
* [MXL7FirewallController](#mxl7_firewall_controller)
* [MXVPNFirewallController](#mxvpn_firewall_controller)
* [MRL3FirewallController](#mrl3_firewall_controller)
* [GroupPoliciesController](#group_policies_controller)
* [HTTPServersController](#http_servers_controller)
* [MerakiAuthUsersController](#meraki_auth_users_controller)
* [OrganizationsController](#organizations_controller)
* [PIIController](#pii_controller)
* [SAMLRolesController](#saml_roles_controller)
* [ClientSecurityEventsController](#client_security_events_controller)
* [MalwareSettingsController](#malware_settings_controller)
* [NamedTagScopeController](#named_tag_scope_controller)
* [SMController](#sm_controller)
* [SplashLoginAttemptsController](#splash_login_attempts_controller)
* [SplashSettingsController](#splash_settings_controller)
* [SsidsController](#ssids_controller)
* [SwitchSettingsController](#switch_settings_controller)
* [SwitchPortsController](#switch_ports_controller)
* [SwitchStacksController](#switch_stacks_controller)
* [SyslogServersController](#syslog_servers_controller)
* [ContentFilteringCategoriesController](#content_filtering_categories_controller)
* [ContentFilteringRulesController](#content_filtering_rules_controller)
* [FirewalledServicesController](#firewalled_services_controller)
* [MX1ManyNATRulesController](#mx1_many_nat_rules_controller)
* [MX11NATRulesController](#mx11_nat_rules_controller)
* [MXPortForwardingRulesController](#mx_port_forwarding_rules_controller)
* [StaticRoutesController](#static_routes_controller)
* [UplinkSettingsController](#uplink_settings_controller)
* [VlansController](#vlans_controller)
* [WirelessHealthController](#wireless_health_controller)

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


### <a name="create_organization_admins"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.create_organization_admins") create_organization_admins

> Create a new dashboard administrator

```python
def create_organization_admins(self,
                                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationAdmins |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_admins = CreateOrganizationAdminsModel()
collect['create_organization_admins'] = create_organization_admins


result = admins_controller.create_organization_admins(collect)

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

## <a name="mv_sense_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MVSenseController") MVSenseController

### Get controller instance

An instance of the ``` MVSenseController ``` class can be accessed from the API Client.

```python
 mv_sense_controller = client.mv_sense
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


### <a name="get_device_camera_analytics_recent"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.get_device_camera_analytics_recent") get_device_camera_analytics_recent

> Returns most recent record for analytics zones

```python
def get_device_camera_analytics_recent(self,
                                           serial)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
serial = 'serial'

result = mv_sense_controller.get_device_camera_analytics_recent(serial)

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



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

timespan = 245
collect['timespan'] = timespan


result = mv_sense_controller.get_device_camera_analytics_overview(collect)

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



#### Example Usage

```python
collect = {}

serial = 'serial'
collect['serial'] = serial

zone_id = 'zoneId'
collect['zone_id'] = zone_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

timespan = 81
collect['timespan'] = timespan

resolution = 81
collect['resolution'] = resolution


result = mv_sense_controller.get_device_camera_analytics_zone_history(collect)

```


[Back to List of Controllers](#list_of_controllers)

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



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

timespan = 81
collect['timespan'] = timespan

per_page = 81
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


result = api_usage_controller.get_organization_api_requests(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="bluetooth_clients_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BluetoothClientsController") BluetoothClientsController

### Get controller instance

An instance of the ``` BluetoothClientsController ``` class can be accessed from the API Client.

```python
 bluetooth_clients_controller = client.bluetooth_clients
```

### <a name="get_network_bluetooth_client"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothClientsController.get_network_bluetooth_client") get_network_bluetooth_client

> Return a Bluetooth client

```python
def get_network_bluetooth_client(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| includeConnectivityHistory |  ``` Optional ```  | Include the connectivity history for this client |
| connectivityHistoryTimespan |  ``` Optional ```  | The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

include_connectivity_history = 'includeConnectivityHistory'
collect['include_connectivity_history'] = include_connectivity_history

connectivity_history_timespan = 'connectivityHistoryTimespan'
collect['connectivity_history_timespan'] = connectivity_history_timespan


result = bluetooth_clients_controller.get_network_bluetooth_client(collect)

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
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| timespan |  ``` Optional ```  | The timespan, in seconds, used to look back from now for bluetooth clients |
| includeConnectivityHistory |  ``` Optional ```  | Include the connectivity history for this client |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

per_page = 81
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before

timespan = 'timespan'
collect['timespan'] = timespan

include_connectivity_history = 'includeConnectivityHistory'
collect['include_connectivity_history'] = include_connectivity_history


result = bluetooth_clients_controller.get_network_bluetooth_clients(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="networks_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NetworksController") NetworksController

### Get controller instance

An instance of the ``` NetworksController ``` class can be accessed from the API Client.

```python
 networks_controller = client.networks
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


### <a name="create_organization_networks"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.create_organization_networks") create_organization_networks

> Create a network

```python
def create_organization_networks(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationNetworks |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_networks = CreateOrganizationNetworksModel()
collect['create_organization_networks'] = create_organization_networks


result = networks_controller.create_organization_networks(collect)

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


result = networks_controller.bind_network(collect)

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

result = networks_controller.unbind_network(network_id)

```


### <a name="get_network_traffic"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.get_network_traffic") get_network_traffic

> The traffic analysis data for this network.
> <a href="https://documentation.meraki.com/MR/Monitoring_and_Reporting/Hostname_Visibility">Traffic Analysis with Hostname Visibility</a> must be enabled on the network.
> 

```python
def get_network_traffic(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| timespan |  ``` Required ```  | The timespan for the data. Must be an integer representing a duration in seconds between two hours and one month. (Mandatory.) |
| deviceType |  ``` Optional ```  | Filter the data by device type: combined (default), wireless, switch, appliance. When using combined, for each rule the data will come from the device type with the most usage. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

timespan = 'timespan'
collect['timespan'] = timespan

device_type = 'deviceType'
collect['device_type'] = device_type


result = networks_controller.get_network_traffic(collect)

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

t0 = 't0'
collect['t0'] = t0

timespan = 81
collect['timespan'] = timespan


result = networks_controller.get_network_air_marshal(collect)

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
| updateNetworkSiteToSiteVpn |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_site_to_site_vpn = UpdateNetworkSiteToSiteVpnModel()
collect['update_network_site_to_site_vpn'] = update_network_site_to_site_vpn


result = networks_controller.update_network_site_to_site_vpn(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="cameras_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CamerasController") CamerasController

### Get controller instance

An instance of the ``` CamerasController ``` class can be accessed from the API Client.

```python
 cameras_controller = client.cameras
```

### <a name="get_network_camera_video_link"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.get_network_camera_video_link") get_network_camera_video_link

> Returns video link for the specified camera. If a timestamp supplied, it links to that time.

```python
def get_network_camera_video_link(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| timestamp |  ``` Optional ```  | The video link will start at this timestamp. The timestamp is in UNIX Epoch time (milliseconds). |



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


### <a name="snapshot_network_camera"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.snapshot_network_camera") snapshot_network_camera

> Generate a snapshot of what the camera sees at the specified time and return a link to that image.

```python
def snapshot_network_camera(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| snapshotNetworkCamera |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

snapshot_network_camera = SnapshotNetworkCameraModel()
collect['snapshot_network_camera'] = snapshot_network_camera


result = cameras_controller.snapshot_network_camera(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="clients_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ClientsController") ClientsController

### Get controller instance

An instance of the ``` ClientsController ``` class can be accessed from the API Client.

```python
 clients_controller = client.clients
```

### <a name="get_network_client"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client") get_network_client

> Return the client associated with the given identifier. This endpoint will lookup by client ID or either the MAC or IP depending on whether the network uses Track-by-IP.

```python
def get_network_client(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| idOrMacOrIp |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id_or_mac_or_ip = 'idOrMacOrIp'
collect['id_or_mac_or_ip'] = id_or_mac_or_ip


result = clients_controller.get_network_client(collect)

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
| provisionNetworkClients |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

provision_network_clients = ProvisionNetworkClientsModel()
collect['provision_network_clients'] = provision_network_clients


result = clients_controller.provision_network_clients(collect)

```


### <a name="get_network_client_usage_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_usage_history") get_network_client_usage_history

> Return the client's daily usage history. Usage data is in kilobytes.

```python
def get_network_client_usage_history(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| idOrMacOrIp |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id_or_mac_or_ip = 'idOrMacOrIp'
collect['id_or_mac_or_ip'] = id_or_mac_or_ip


result = clients_controller.get_network_client_usage_history(collect)

```


### <a name="get_network_client_policy"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_policy") get_network_client_policy

> Return the policy assigned to a client on the network.

```python
def get_network_client_policy(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| mac |  ``` Required ```  | TODO: Add a parameter description |
| timespan |  ``` Optional ```  | The timespan for which clients will be fetched. Must be in seconds and less than or equal to a month (2592000 seconds). |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

mac = 'mac'
collect['mac'] = mac

timespan = 'timespan'
collect['timespan'] = timespan


result = clients_controller.get_network_client_policy(collect)

```


### <a name="update_network_client_policy"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.update_network_client_policy") update_network_client_policy

> Update the policy assigned to a client on the network.

```python
def update_network_client_policy(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| mac |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkClientPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

mac = 'mac'
collect['mac'] = mac

update_network_client_policy = UpdateNetworkClientPolicyModel()
collect['update_network_client_policy'] = update_network_client_policy


result = clients_controller.update_network_client_policy(collect)

```


### <a name="get_network_client_splash_authorization_status"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_splash_authorization_status") get_network_client_splash_authorization_status

> Return the splash authorization for a client, for each SSID they've associated with through splash.

```python
def get_network_client_splash_authorization_status(self,
                                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| mac |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

id = 'id'
collect['id'] = id

mac = 'mac'
collect['mac'] = mac


result = clients_controller.get_network_client_splash_authorization_status(collect)

```


### <a name="update_network_client_splash_authorization_status"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.update_network_client_splash_authorization_status") update_network_client_splash_authorization_status

> Update a client's splash authorization.

```python
def update_network_client_splash_authorization_status(self,
                                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| mac |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkClientSplashAuthorizationStatus |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

id = 'id'
collect['id'] = id

mac = 'mac'
collect['mac'] = mac

update_network_client_splash_authorization_status = UpdateNetworkClientSplashAuthorizationStatusModel()
collect['update_network_client_splash_authorization_status'] = update_network_client_splash_authorization_status


result = clients_controller.update_network_client_splash_authorization_status(collect)

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

t0 = 't0'
collect['t0'] = t0

timespan = 81
collect['timespan'] = timespan


result = clients_controller.get_device_clients(collect)

```


### <a name="get_network_client_traffic_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_traffic_history") get_network_client_traffic_history

> Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page.

```python
def get_network_client_traffic_history(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| idOrMacOrIp |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id_or_mac_or_ip = 'idOrMacOrIp'
collect['id_or_mac_or_ip'] = id_or_mac_or_ip

per_page = 81
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = clients_controller.get_network_client_traffic_history(collect)

```


### <a name="get_network_client_events"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_events") get_network_client_events

> Return the events associated with this client

```python
def get_network_client_events(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| idOrMacOrIp |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 100. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id_or_mac_or_ip = 'idOrMacOrIp'
collect['id_or_mac_or_ip'] = id_or_mac_or_ip

per_page = 81
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = clients_controller.get_network_client_events(collect)

```


### <a name="get_network_client_latency_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.get_network_client_latency_history") get_network_client_latency_history

> Return the latency history for a client. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.

```python
def get_network_client_latency_history(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| idOrMacOrIp |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 791 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 791 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day. |
| resolution |  ``` Optional ```  | The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id_or_mac_or_ip = 'idOrMacOrIp'
collect['id_or_mac_or_ip'] = id_or_mac_or_ip

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

timespan = 173
collect['timespan'] = timespan

resolution = 173
collect['resolution'] = resolution


result = clients_controller.get_network_client_latency_history(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

id = 'id'
collect['id'] = id


config_templates_controller.delete_organization_config_template(collect)

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

timespan = 'timespan'
collect['timespan'] = timespan


result = devices_controller.get_network_device_lldp_cdp(collect)

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
| claimNetworkDevices |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

claim_network_devices = ClaimNetworkDevicesModel()
collect['claim_network_devices'] = claim_network_devices


result = devices_controller.claim_network_devices(collect)

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


result = devices_controller.remove_network_device(collect)

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

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

timespan = 173
collect['timespan'] = timespan

resolution = 173
collect['resolution'] = resolution

uplink = 'uplink'
collect['uplink'] = uplink


result = devices_controller.get_network_device_loss_and_latency_history(collect)

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


### <a name="blink_leds_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.blink_leds_network_device") blink_leds_network_device

> Blink the LEDs on a device

```python
def blink_leds_network_device(self,
                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| blinkLedsNetworkDevice |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

serial = 'serial'
collect['serial'] = serial

blink_leds_network_device = BlinkLedsNetworkDeviceModel()
collect['blink_leds_network_device'] = blink_leds_network_device


result = devices_controller.blink_leds_network_device(collect)

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

## <a name="mxl3_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL3FirewallController") MXL3FirewallController

### Get controller instance

An instance of the ``` MXL3FirewallController ``` class can be accessed from the API Client.

```python
 mx_l3_firewall_controller = client.mx_l3_firewall
```

### <a name="get_network_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL3FirewallController.get_network_l3_firewall_rules") get_network_l3_firewall_rules

> Return the L3 firewall rules for an MX network

```python
def get_network_l3_firewall_rules(self,
                                      network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_l3_firewall_controller.get_network_l3_firewall_rules(network_id)

```


### <a name="update_network_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL3FirewallController.update_network_l3_firewall_rules") update_network_l3_firewall_rules

> Update the L3 firewall rules of an MX network

```python
def update_network_l3_firewall_rules(self,
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

update_network_l3_firewall_rules = UpdateNetworkL3FirewallRulesModel()
collect['update_network_l3_firewall_rules'] = update_network_l3_firewall_rules


result = mx_l3_firewall_controller.update_network_l3_firewall_rules(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mxl7_application_categories_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL7ApplicationCategoriesController") MXL7ApplicationCategoriesController

### Get controller instance

An instance of the ``` MXL7ApplicationCategoriesController ``` class can be accessed from the API Client.

```python
 mx_l7_application_categories_controller = client.mx_l7_application_categories
```

### <a name="get_network_l7_firewall_rules_application_categories"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7ApplicationCategoriesController.get_network_l7_firewall_rules_application_categories") get_network_l7_firewall_rules_application_categories

> Return the L7 firewall application categories and their associated applications for an MX network

```python
def get_network_l7_firewall_rules_application_categories(self,
                                                             network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_l7_application_categories_controller.get_network_l7_firewall_rules_application_categories(network_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="mxl7_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL7FirewallController") MXL7FirewallController

### Get controller instance

An instance of the ``` MXL7FirewallController ``` class can be accessed from the API Client.

```python
 mx_l7_firewall_controller = client.mx_l7_firewall
```

### <a name="get_network_l7_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7FirewallController.get_network_l7_firewall_rules") get_network_l7_firewall_rules

> List the MX L7 firewall rules for an MX network

```python
def get_network_l7_firewall_rules(self,
                                      network_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
network_id = 'networkId'

result = mx_l7_firewall_controller.get_network_l7_firewall_rules(network_id)

```


### <a name="update_network_l7_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7FirewallController.update_network_l7_firewall_rules") update_network_l7_firewall_rules

> Update the MX L7 firewall rules for an MX network

```python
def update_network_l7_firewall_rules(self,
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

update_network_l7_firewall_rules = UpdateNetworkL7FirewallRulesModel()
collect['update_network_l7_firewall_rules'] = update_network_l7_firewall_rules


result = mx_l7_firewall_controller.update_network_l7_firewall_rules(collect)

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

## <a name="mrl3_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MRL3FirewallController") MRL3FirewallController

### Get controller instance

An instance of the ``` MRL3FirewallController ``` class can be accessed from the API Client.

```python
 mr_l3_firewall_controller = client.mr_l3_firewall
```

### <a name="get_network_ssid_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MRL3FirewallController.get_network_ssid_l3_firewall_rules") get_network_ssid_l3_firewall_rules

> Return the L3 firewall rules for an SSID on an MR network

```python
def get_network_ssid_l3_firewall_rules(self,
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


result = mr_l3_firewall_controller.get_network_ssid_l3_firewall_rules(collect)

```


### <a name="update_network_ssid_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MRL3FirewallController.update_network_ssid_l3_firewall_rules") update_network_ssid_l3_firewall_rules

> Update the L3 firewall rules of an SSID on an MR network

```python
def update_network_ssid_l3_firewall_rules(self,
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

update_network_ssid_l3_firewall_rules = UpdateNetworkSsidL3FirewallRulesModel()
collect['update_network_ssid_l3_firewall_rules'] = update_network_ssid_l3_firewall_rules


result = mr_l3_firewall_controller.update_network_ssid_l3_firewall_rules(collect)

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


### <a name="create_network_group_policies"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.create_network_group_policies") create_network_group_policies

> Create a group policy

```python
def create_network_group_policies(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkGroupPolicies |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_group_policies = CreateNetworkGroupPoliciesModel()
collect['create_network_group_policies'] = create_network_group_policies


result = group_policies_controller.create_network_group_policies(collect)

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


### <a name="create_network_http_servers"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.create_network_http_servers") create_network_http_servers

> Add an HTTP server

```python
def create_network_http_servers(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkHttpServers |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_http_servers = CreateNetworkHttpServersModel()
collect['create_network_http_servers'] = create_network_http_servers


result = http_servers_controller.create_network_http_servers(collect)

```


### <a name="get_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.get_network_http_server") get_network_http_server

> Return an HTTP server

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

> Delete an HTTP server

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


### <a name="create_network_http_servers_webhook_tests"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.create_network_http_servers_webhook_tests") create_network_http_servers_webhook_tests

> Send a test webhook

```python
def create_network_http_servers_webhook_tests(self,
                                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkHttpServersWebhookTests |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_http_servers_webhook_tests = CreateNetworkHttpServersWebhookTestsModel()
collect['create_network_http_servers_webhook_tests'] = create_network_http_servers_webhook_tests


result = http_servers_controller.create_network_http_servers_webhook_tests(collect)

```


### <a name="get_network_http_servers_webhook_test"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.get_network_http_servers_webhook_test") get_network_http_servers_webhook_test

> Return the status of a webhook test

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = meraki_auth_users_controller.get_network_meraki_auth_user(collect)

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


### <a name="create_organizations"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.create_organizations") create_organizations

> Create a new organization

```python
def create_organizations(self,
                             create_organizations=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| createOrganizations |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
create_organizations = CreateOrganizationsModel()

result = organizations_controller.create_organizations(create_organizations)

```


### <a name="get_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization") get_organization

> Return an organization

```python
def get_organization(self,
                         id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'

result = organizations_controller.get_organization(id)

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
| id |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganization |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

id = 'id'
collect['id'] = id

update_organization = UpdateOrganizationModel()
collect['update_organization'] = update_organization


result = organizations_controller.update_organization(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |
| cloneOrganization |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

id = 'id'
collect['id'] = id

clone_organization = CloneOrganizationModel()
collect['clone_organization'] = clone_organization


result = organizations_controller.clone_organization(collect)

```


### <a name="get_organization_license_state"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_license_state") get_organization_license_state

> Return the license state for an organization

```python
def get_organization_license_state(self,
                                       id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'

result = organizations_controller.get_organization_license_state(id)

```


### <a name="get_organization_inventory"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_inventory") get_organization_inventory

> Return the inventory for an organization

```python
def get_organization_inventory(self,
                                   id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'

result = organizations_controller.get_organization_inventory(id)

```


### <a name="get_organization_device_statuses"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_device_statuses") get_organization_device_statuses

> List the status of every Meraki device in the organization

```python
def get_organization_device_statuses(self,
                                         id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'

result = organizations_controller.get_organization_device_statuses(id)

```


### <a name="get_organization_snmp"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_snmp") get_organization_snmp

> Return the SNMP settings for an organization

```python
def get_organization_snmp(self,
                              id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'

result = organizations_controller.get_organization_snmp(id)

```


### <a name="update_organization_snmp"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.update_organization_snmp") update_organization_snmp

> Update the SNMP settings for an organization

```python
def update_organization_snmp(self,
                                 options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSnmp |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

id = 'id'
collect['id'] = id

update_organization_snmp = UpdateOrganizationSnmpModel()
collect['update_organization_snmp'] = update_organization_snmp


result = organizations_controller.update_organization_snmp(collect)

```


### <a name="claim_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.claim_organization") claim_organization

> Claim a device, license key, or order into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization's inventory. These three types of claims are mutually exclusive and cannot be performed in one request.

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


### <a name="get_organization_uplinks_loss_and_latency"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.get_organization_uplinks_loss_and_latency") get_organization_uplinks_loss_and_latency

> Return the uplink loss and latency for every MX in the organization from 2 - 7 minutes ago

```python
def get_organization_uplinks_loss_and_latency(self,
                                                  options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| uplink |  ``` Optional ```  | Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks. |
| ip |  ``` Optional ```  | Optional filter for a specific destination IP. Default will return all destination IPs. |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

uplink = 'uplink'
collect['uplink'] = uplink

ip = 'ip'
collect['ip'] = ip


result = organizations_controller.get_organization_uplinks_loss_and_latency(collect)

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


### <a name="create_network_pii_requests"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.create_network_pii_requests") create_network_pii_requests

> Submit a new delete or restrict processing PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests
> ```

```python
def create_network_pii_requests(self,
                                    options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkPiiRequests |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_pii_requests = CreateNetworkPiiRequestsModel()
collect['create_network_pii_requests'] = create_network_pii_requests


result = pii_controller.create_network_pii_requests(collect)

```


### <a name="get_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.get_network_pii_request") get_network_pii_request

> Return a PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests/{id}
> ```

```python
def get_network_pii_request(self,
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


result = pii_controller.get_network_pii_request(collect)

```


### <a name="delete_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.delete_network_pii_request") delete_network_pii_request

> Delete a restrict processing PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests/{id}
> ```

```python
def delete_network_pii_request(self,
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


pii_controller.delete_network_pii_request(collect)

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


### <a name="create_organization_saml_roles"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.create_organization_saml_roles") create_organization_saml_roles

> Create a SAML role

```python
def create_organization_saml_roles(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationSamlRoles |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

create_organization_saml_roles = CreateOrganizationSamlRolesModel()
collect['create_organization_saml_roles'] = create_organization_saml_roles


result = saml_roles_controller.create_organization_saml_roles(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

id = 'id'
collect['id'] = id


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
| id |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSamlRole |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

id = 'id'
collect['id'] = id

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

organization_id = 'organizationId'
collect['organization_id'] = organization_id

id = 'id'
collect['id'] = id


saml_roles_controller.delete_organization_saml_role(collect)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="client_security_events_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ClientSecurityEventsController") ClientSecurityEventsController

### Get controller instance

An instance of the ``` ClientSecurityEventsController ``` class can be accessed from the API Client.

```python
 client_security_events_controller = client.client_security_events
```

### <a name="get_network_client_security_events"></a>![Method: ](https://apidocs.io/img/method.png ".ClientSecurityEventsController.get_network_client_security_events") get_network_client_security_events

> List the security events

```python
def get_network_client_security_events(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Required ```  | The number of entries per page returned. Acceptable range is 3 - 1000. |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 791 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 791 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

client_id = 'clientId'
collect['client_id'] = client_id

per_page = 223
collect['per_page'] = per_page

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

timespan = 223
collect['timespan'] = timespan

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = client_security_events_controller.get_network_client_security_events(collect)

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

with_details = 'withDetails'
collect['with_details'] = with_details


result = named_tag_scope_controller.get_network_sm_target_groups(collect)

```


### <a name="create_network_sm_target_groups"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.create_network_sm_target_groups") create_network_sm_target_groups

> Add a target group

```python
def create_network_sm_target_groups(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmTargetGroups |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_sm_target_groups = CreateNetworkSmTargetGroupsModel()
collect['create_network_sm_target_groups'] = create_network_sm_target_groups


result = named_tag_scope_controller.create_network_sm_target_groups(collect)

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
| withDetails |  ``` Optional ```  | Boolean indicating if the the ids of devices or users scoped by the target group should be included in the response |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

target_group_id = 'targetGroupId'
collect['target_group_id'] = target_group_id

with_details = 'withDetails'
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

## <a name="sm_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SMController") SMController

### Get controller instance

An instance of the ``` SMController ``` class can be accessed from the API Client.

```python
 sm_controller = client.sm
```

### <a name="create_network_sm_profile_clarity"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.create_network_sm_profile_clarity") create_network_sm_profile_clarity

> Create a new profile containing a Cisco Clarity payload

```python
def create_network_sm_profile_clarity(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmProfileClarity |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

create_network_sm_profile_clarity = CreateNetworkSmProfileClarityModel()
collect['create_network_sm_profile_clarity'] = create_network_sm_profile_clarity


result = sm_controller.create_network_sm_profile_clarity(collect)

```


### <a name="update_network_sm_profile_clarity"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_profile_clarity") update_network_sm_profile_clarity

> Update an existing profile containing a Cisco Clarity payload

```python
def update_network_sm_profile_clarity(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmProfileClarity |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id

update_network_sm_profile_clarity = UpdateNetworkSmProfileClarityModel()
collect['update_network_sm_profile_clarity'] = update_network_sm_profile_clarity


result = sm_controller.update_network_sm_profile_clarity(collect)

```


### <a name="add_network_sm_profile_clarity"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.add_network_sm_profile_clarity") add_network_sm_profile_clarity

> Add a Cisco Clarity payload to an existing profile

```python
def add_network_sm_profile_clarity(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |
| addNetworkSmProfileClarity |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id

add_network_sm_profile_clarity = AddNetworkSmProfileClarityModel()
collect['add_network_sm_profile_clarity'] = add_network_sm_profile_clarity


result = sm_controller.add_network_sm_profile_clarity(collect)

```


### <a name="get_network_sm_profile_clarity"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_profile_clarity") get_network_sm_profile_clarity

> Get details for a Cisco Clarity payload

```python
def get_network_sm_profile_clarity(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id


result = sm_controller.get_network_sm_profile_clarity(collect)

```


### <a name="delete_network_sm_profile_clarity"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.delete_network_sm_profile_clarity") delete_network_sm_profile_clarity

> Delete a Cisco Clarity payload. Deletes the entire profile if it's empty after removing the payload.

```python
def delete_network_sm_profile_clarity(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id


sm_controller.delete_network_sm_profile_clarity(collect)

```


### <a name="create_network_sm_profile_umbrella"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.create_network_sm_profile_umbrella") create_network_sm_profile_umbrella

> Create a new profile containing a Cisco Umbrella payload

```python
def create_network_sm_profile_umbrella(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmProfileUmbrella |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

create_network_sm_profile_umbrella = CreateNetworkSmProfileUmbrellaModel()
collect['create_network_sm_profile_umbrella'] = create_network_sm_profile_umbrella


result = sm_controller.create_network_sm_profile_umbrella(collect)

```


### <a name="update_network_sm_profile_umbrella"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_profile_umbrella") update_network_sm_profile_umbrella

> Update an existing profile containing a Cisco Umbrella payload

```python
def update_network_sm_profile_umbrella(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmProfileUmbrella |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id

update_network_sm_profile_umbrella = UpdateNetworkSmProfileUmbrellaModel()
collect['update_network_sm_profile_umbrella'] = update_network_sm_profile_umbrella


result = sm_controller.update_network_sm_profile_umbrella(collect)

```


### <a name="add_network_sm_profile_umbrella"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.add_network_sm_profile_umbrella") add_network_sm_profile_umbrella

> Add a Cisco Umbrella payload to an existing profile

```python
def add_network_sm_profile_umbrella(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |
| addNetworkSmProfileUmbrella |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id

add_network_sm_profile_umbrella = AddNetworkSmProfileUmbrellaModel()
collect['add_network_sm_profile_umbrella'] = add_network_sm_profile_umbrella


result = sm_controller.add_network_sm_profile_umbrella(collect)

```


### <a name="get_network_sm_profile_umbrella"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.get_network_sm_profile_umbrella") get_network_sm_profile_umbrella

> Get details for a Cisco Umbrella payload

```python
def get_network_sm_profile_umbrella(self,
                                        options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id


result = sm_controller.get_network_sm_profile_umbrella(collect)

```


### <a name="delete_network_sm_profile_umbrella"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.delete_network_sm_profile_umbrella") delete_network_sm_profile_umbrella

> Delete a Cisco Umbrella payload. Deletes the entire profile if it's empty after removing the payload

```python
def delete_network_sm_profile_umbrella(self,
                                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| profileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

profile_id = 'profileId'
collect['profile_id'] = profile_id


sm_controller.delete_network_sm_profile_umbrella(collect)

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
| createNetworkSmAppPolaris |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
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

network_id = 'network_id'
collect['network_id'] = network_id

bundle_id = 'bundleId'
collect['bundle_id'] = bundle_id


result = sm_controller.get_network_sm_app_polaris(collect)

```


### <a name="update_network_sm_app_polari"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_app_polari") update_network_sm_app_polari

> Update an existing Polaris app

```python
def update_network_sm_app_polari(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmAppPolari |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

app_id = 'appId'
collect['app_id'] = app_id

update_network_sm_app_polari = UpdateNetworkSmAppPolariModel()
collect['update_network_sm_app_polari'] = update_network_sm_app_polari


result = sm_controller.update_network_sm_app_polari(collect)

```


### <a name="delete_network_sm_app_polari"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.delete_network_sm_app_polari") delete_network_sm_app_polari

> Delete a Cisco Polaris app

```python
def delete_network_sm_app_polari(self,
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

network_id = 'network_id'
collect['network_id'] = network_id

app_id = 'appId'
collect['app_id'] = app_id


sm_controller.delete_network_sm_app_polari(collect)

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
| batchToken |  ``` Optional ```  | On networks with more than 1000 devices, the device list will be limited to 1000 devices per query.
      If there are more devices to be seen, a batch token will be returned as a part of the device list. To see the remainder of
      the devices, pass in the batchToken as a parameter in the next request. Requests made with the batchToken do not require
      additional parameters as the batchToken includes the parameters passed in with the original request. Additional parameters
      passed in with the batchToken will be ignored. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
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

batch_token = 'batchToken'
collect['batch_token'] = batch_token


result = sm_controller.get_network_sm_devices(collect)

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
| usernames |  ``` Optional ```  | Filter users by username(s). Multiple usernames can be passed in as comma separated values. |
| emails |  ``` Optional ```  | Filter users by email(s). Multiple emails can be passed in as comma separated values. |
| ids |  ``` Optional ```  | Filter users by id(s). Multiple ids can be passed in as comma separated values. |
| scope |  ``` Optional ```  | Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

usernames = 'usernames'
collect['usernames'] = usernames

emails = 'emails'
collect['emails'] = emails

ids = 'ids'
collect['ids'] = ids

scope = 'scope'
collect['scope'] = scope


result = sm_controller.get_network_sm_users(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_user_device_profiles(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_device_profiles(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_user_softwares(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_softwares(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_network_adapters(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_wlan_lists(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_security_centers(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_restrictions(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_certs(collect)

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
| updateNetworkSmDevicesTags |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

update_network_sm_devices_tags = UpdateNetworkSmDevicesTagsModel()
collect['update_network_sm_devices_tags'] = update_network_sm_devices_tags


result = sm_controller.update_network_sm_devices_tags(collect)

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
| updateNetworkSmDeviceFields |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

update_network_sm_device_fields = UpdateNetworkSmDeviceFieldsModel()
collect['update_network_sm_device_fields'] = update_network_sm_device_fields


result = sm_controller.update_network_sm_device_fields(collect)

```


### <a name="update_network_sm_devices_lock"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_devices_lock") update_network_sm_devices_lock

> Lock a set of devices

```python
def update_network_sm_devices_lock(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDevicesLock |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

update_network_sm_devices_lock = UpdateNetworkSmDevicesLockModel()
collect['update_network_sm_devices_lock'] = update_network_sm_devices_lock


result = sm_controller.update_network_sm_devices_lock(collect)

```


### <a name="update_network_sm_device_wipe"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_device_wipe") update_network_sm_device_wipe

> Wipe a device

```python
def update_network_sm_device_wipe(self,
                                      options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDeviceWipe |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

update_network_sm_device_wipe = UpdateNetworkSmDeviceWipeModel()
collect['update_network_sm_device_wipe'] = update_network_sm_device_wipe


result = sm_controller.update_network_sm_device_wipe(collect)

```


### <a name="update_network_sm_devices_checkin"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_devices_checkin") update_network_sm_devices_checkin

> Force check-in a set of devices

```python
def update_network_sm_devices_checkin(self,
                                          options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDevicesCheckin |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

update_network_sm_devices_checkin = UpdateNetworkSmDevicesCheckinModel()
collect['update_network_sm_devices_checkin'] = update_network_sm_devices_checkin


result = sm_controller.update_network_sm_devices_checkin(collect)

```


### <a name="update_network_sm_devices_move"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.update_network_sm_devices_move") update_network_sm_devices_move

> Move a set of devices to a new network

```python
def update_network_sm_devices_move(self,
                                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDevicesMove |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

update_network_sm_devices_move = UpdateNetworkSmDevicesMoveModel()
collect['update_network_sm_devices_move'] = update_network_sm_devices_move


result = sm_controller.update_network_sm_devices_move(collect)

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

network_id = 'network_id'
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
network_id = 'network_id'

result = sm_controller.get_network_sm_profiles(network_id)

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
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id


result = sm_controller.get_network_sm_cellular_usage_history(collect)

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
| perPage |  ``` Optional ```  | The number of entries per page returned |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 'perPage'
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = sm_controller.get_network_sm_performance_history(collect)

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
| perPage |  ``` Optional ```  | The number of entries per page returned |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 'perPage'
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
| perPage |  ``` Optional ```  | The number of entries per page returned |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 'perPage'
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = sm_controller.get_network_sm_device_command_logs(collect)

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
| perPage |  ``` Optional ```  | The number of entries per page returned |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, next or prev page in the HTTP Link header should define it. |



#### Example Usage

```python
collect = {}

network_id = 'network_id'
collect['network_id'] = network_id

id = 'id'
collect['id'] = id

per_page = 'perPage'
collect['per_page'] = per_page

starting_after = 'startingAfter'
collect['starting_after'] = starting_after

ending_before = 'endingBefore'
collect['ending_before'] = ending_before


result = sm_controller.get_network_sm_connectivity(collect)

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
| id |  ``` Required ```  | TODO: Add a parameter description |
| ssidNumber |  ``` Optional ```  | Only return the login attempts for the specified SSID |
| loginIdentifier |  ``` Optional ```  | The username, email, or phone number used during login |
| timespan |  ``` Optional ```  | The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months |



#### Example Usage

```python
collect = {}

id = 'id'
collect['id'] = id

ssid_number = 'ssidNumber'
collect['ssid_number'] = ssid_number

login_identifier = 'loginIdentifier'
collect['login_identifier'] = login_identifier

timespan = 'timespan'
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

## <a name="ssids_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SsidsController") SsidsController

### Get controller instance

An instance of the ``` SsidsController ``` class can be accessed from the API Client.

```python
 ssids_controller = client.ssids
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


[Back to List of Controllers](#list_of_controllers)

## <a name="switch_ports_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchPortsController") SwitchPortsController

### Get controller instance

An instance of the ``` SwitchPortsController ``` class can be accessed from the API Client.

```python
 switch_ports_controller = client.switch_ports
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


### <a name="create_network_switch_stacks"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.create_network_switch_stacks") create_network_switch_stacks

> Create a stack

```python
def create_network_switch_stacks(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchStacks |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_switch_stacks = CreateNetworkSwitchStacksModel()
collect['create_network_switch_stacks'] = create_network_switch_stacks


result = switch_stacks_controller.create_network_switch_stacks(collect)

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
| networkID |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |
| removeNetworkSwitchStack |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkID'
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
| updateNetworkSyslogServers |  ``` Optional ```  | TODO: Add a parameter description |



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
| updateNetworkFirewalledService |  ``` Optional ```  | TODO: Add a parameter description |



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

result = mx1_many_nat_rules_controller.get_network_one_to_many_nat_rules(network_id)

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
| updateNetworkOneToManyNatRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

update_network_one_to_many_nat_rules = UpdateNetworkOneToManyNatRulesModel()
collect['update_network_one_to_many_nat_rules'] = update_network_one_to_many_nat_rules


result = mx1_many_nat_rules_controller.update_network_one_to_many_nat_rules(collect)

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

result = mx11_nat_rules_controller.get_network_one_to_one_nat_rules(network_id)

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


result = mx11_nat_rules_controller.update_network_one_to_one_nat_rules(collect)

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

## <a name="static_routes_controller"></a>![Class: ](https://apidocs.io/img/class.png ".StaticRoutesController") StaticRoutesController

### Get controller instance

An instance of the ``` StaticRoutesController ``` class can be accessed from the API Client.

```python
 static_routes_controller = client.static_routes
```

### <a name="get_network_static_routes"></a>![Method: ](https://apidocs.io/img/method.png ".StaticRoutesController.get_network_static_routes") get_network_static_routes

> List the static routes for this network

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

result = static_routes_controller.get_network_static_routes(network_id)

```


### <a name="create_network_static_routes"></a>![Method: ](https://apidocs.io/img/method.png ".StaticRoutesController.create_network_static_routes") create_network_static_routes

> Add a static route

```python
def create_network_static_routes(self,
                                     options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkStaticRoutes |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_static_routes = CreateNetworkStaticRoutesModel()
collect['create_network_static_routes'] = create_network_static_routes


result = static_routes_controller.create_network_static_routes(collect)

```


### <a name="get_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".StaticRoutesController.get_network_static_route") get_network_static_route

> Return a static route

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


result = static_routes_controller.get_network_static_route(collect)

```


### <a name="update_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".StaticRoutesController.update_network_static_route") update_network_static_route

> Update a static route

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


result = static_routes_controller.update_network_static_route(collect)

```


### <a name="delete_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".StaticRoutesController.delete_network_static_route") delete_network_static_route

> Delete a static route from a network

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


static_routes_controller.delete_network_static_route(collect)

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

> List the VLANs for this network

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


### <a name="create_network_vlans"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.create_network_vlans") create_network_vlans

> Add a VLAN

```python
def create_network_vlans(self,
                             options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetwork_vlans |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

create_network_vlans = CreateNetworkVlansModel()
collect['create_network_vlans'] = create_network_vlans


result = vlans_controller.create_network_vlans(collect)

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

## <a name="wireless_health_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WirelessHealthController") WirelessHealthController

### Get controller instance

An instance of the ``` WirelessHealthController ``` class can be accessed from the API Client.

```python
 wireless_health_controller = client.wireless_health
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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_devices_connection_stats(collect)

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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
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

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_device_connection_stats(collect)

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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_clients_connection_stats(collect)

```


### <a name="get_network_client_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_client_connection_stats") get_network_client_connection_stats

> Aggregated connectivity info for a given client on this network

```python
def get_network_client_connection_stats(self,
                                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
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

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag


result = wireless_health_controller.get_network_client_connection_stats(collect)

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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_latency_stats(collect)

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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_devices_latency_stats(collect)

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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
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

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_device_latency_stats(collect)

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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_clients_latency_stats(collect)

```


### <a name="get_network_client_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.get_network_client_latency_stats") get_network_client_latency_stats

> Aggregated latency info for a given client on this network

```python
def get_network_client_latency_stats(self,
                                         options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
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

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

fields = 'fields'
collect['fields'] = fields


result = wireless_health_controller.get_network_client_latency_stats(collect)

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
| t0 |  ``` Optional ```  | Start of the requested time range in seconds since epoch (Required) |
| t1 |  ``` Optional ```  | End of the requested time range in seconds since epoch (Required) |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| serial |  ``` Optional ```  | Filter by AP |
| clientId |  ``` Optional ```  | Filter by client |



#### Example Usage

```python
collect = {}

network_id = 'networkId'
collect['network_id'] = network_id

t0 = 't0'
collect['t0'] = t0

t1 = 't1'
collect['t1'] = t1

ssid = 'ssid'
collect['ssid'] = ssid

vlan = 'vlan'
collect['vlan'] = vlan

ap_tag = 'apTag'
collect['ap_tag'] = ap_tag

serial = 'serial'
collect['serial'] = serial

client_id = 'clientId'
collect['client_id'] = client_id


result = wireless_health_controller.get_network_failed_connections(collect)

```


[Back to List of Controllers](#list_of_controllers)



