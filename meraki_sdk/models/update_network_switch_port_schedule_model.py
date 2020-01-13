# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.port_schedule_model

class UpdateNetworkSwitchPortScheduleModel(object):

    """Implementation of the 'updateNetworkSwitchPortSchedule' model.

    TODO: type model description here.

    Attributes:
        name (string): The name for your port schedule.
        port_schedule (PortScheduleModel): The schedule for switch port
            scheduling. Schedules are applied to days of the week.     When
            it's empty, default schedule with all days of a week are
            configured.     Any unspecified day in the schedule is added as a
            default schedule configuration of the day.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "port_schedule":'portSchedule'
    }

    def __init__(self,
                 name=None,
                 port_schedule=None):
        """Constructor for the UpdateNetworkSwitchPortScheduleModel class"""

        # Initialize members of the class
        self.name = name
        self.port_schedule = port_schedule


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get('name')
        port_schedule = meraki_sdk.models.port_schedule_model.PortScheduleModel.from_dictionary(dictionary.get('portSchedule')) if dictionary.get('portSchedule') else None

        # Return an object of this model
        return cls(name,
                   port_schedule)


