# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.monday_model
import meraki_sdk.models.tuesday_model
import meraki_sdk.models.wednesday_model
import meraki_sdk.models.thursday_model
import meraki_sdk.models.friday_model
import meraki_sdk.models.saturday_model
import meraki_sdk.models.sunday_model

class PortScheduleModel(object):

    """Implementation of the 'PortSchedule' model.

    The schedule for switch port scheduling. Schedules are applied to days of
    the week.
        When it's empty, default schedule with all days of a week are
        configured.
        Any unspecified day in the schedule is added as a default schedule
        configuration of the day.

    Attributes:
        monday (MondayModel): The schedule object for Monday.
        tuesday (TuesdayModel): The schedule object for Tuesday.
        wednesday (WednesdayModel): The schedule object for Wednesday.
        thursday (ThursdayModel): The schedule object for Thursday.
        friday (FridayModel): The schedule object for Friday.
        saturday (SaturdayModel): The schedule object for Saturday.
        sunday (SundayModel): The schedule object for Sunday.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "monday":'monday',
        "tuesday":'tuesday',
        "wednesday":'wednesday',
        "thursday":'thursday',
        "friday":'friday',
        "saturday":'saturday',
        "sunday":'sunday'
    }

    def __init__(self,
                 monday=None,
                 tuesday=None,
                 wednesday=None,
                 thursday=None,
                 friday=None,
                 saturday=None,
                 sunday=None):
        """Constructor for the PortScheduleModel class"""

        # Initialize members of the class
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday


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
        monday = meraki_sdk.models.monday_model.MondayModel.from_dictionary(dictionary.get('monday')) if dictionary.get('monday') else None
        tuesday = meraki_sdk.models.tuesday_model.TuesdayModel.from_dictionary(dictionary.get('tuesday')) if dictionary.get('tuesday') else None
        wednesday = meraki_sdk.models.wednesday_model.WednesdayModel.from_dictionary(dictionary.get('wednesday')) if dictionary.get('wednesday') else None
        thursday = meraki_sdk.models.thursday_model.ThursdayModel.from_dictionary(dictionary.get('thursday')) if dictionary.get('thursday') else None
        friday = meraki_sdk.models.friday_model.FridayModel.from_dictionary(dictionary.get('friday')) if dictionary.get('friday') else None
        saturday = meraki_sdk.models.saturday_model.SaturdayModel.from_dictionary(dictionary.get('saturday')) if dictionary.get('saturday') else None
        sunday = meraki_sdk.models.sunday_model.SundayModel.from_dictionary(dictionary.get('sunday')) if dictionary.get('sunday') else None

        # Return an object of this model
        return cls(monday,
                   tuesday,
                   wednesday,
                   thursday,
                   friday,
                   saturday,
                   sunday)


