# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.custom_pie_chart_item_model

class UpdateNetworkTrafficAnalysisSettingsModel(object):

    """Implementation of the 'updateNetworkTrafficAnalysisSettings' model.

    TODO: type model description here.

    Attributes:
        mode (ModeEnum): The traffic analysis mode for the network. Can be one
            of 'disabled' (do not collect traffic types),     'basic' (collect
            generic traffic categories), or 'detailed' (collect destination
            hostnames).
        custom_pie_chart_items (list of CustomPieChartItemModel): The list of
            items that make up the custom pie chart for traffic reporting.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mode":'mode',
        "custom_pie_chart_items":'customPieChartItems'
    }

    def __init__(self,
                 mode=None,
                 custom_pie_chart_items=None):
        """Constructor for the UpdateNetworkTrafficAnalysisSettingsModel class"""

        # Initialize members of the class
        self.mode = mode
        self.custom_pie_chart_items = custom_pie_chart_items


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
        mode = dictionary.get('mode')
        custom_pie_chart_items = None
        if dictionary.get('customPieChartItems') != None:
            custom_pie_chart_items = list()
            for structure in dictionary.get('customPieChartItems'):
                custom_pie_chart_items.append(meraki.models.custom_pie_chart_item_model.CustomPieChartItemModel.from_dictionary(structure))

        # Return an object of this model
        return cls(mode,
                   custom_pie_chart_items)


