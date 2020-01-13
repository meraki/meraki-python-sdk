# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.mv_21_mv_71_model
import meraki_sdk.models.mv_12_mv_22_mv_72_model
import meraki_sdk.models.mv_32_model
import meraki_sdk.models.mv_12_we_model

class VideoSettingsModel(object):

    """Implementation of the 'VideoSettings' model.

    Video quality and resolution settings for all the camera models.

    Attributes:
        mv_21_mv_71 (MV21MV71Model): Quality and resolution for MV21/MV71
            camera models.
        mv_12_mv_22_mv_72 (MV12MV22MV72Model): Quality and resolution for
            MV12/MV22/MV72 camera models.
        mv_32 (MV32Model): Quality and resolution for MV32 camera models.
        mv_12_we (MV12WEModel): Quality and resolution for MV12WE camera
            models.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mv_21_mv_71":'MV21/MV71',
        "mv_12_mv_22_mv_72":'MV12/MV22/MV72',
        "mv_32":'MV32',
        "mv_12_we":'MV12WE'
    }

    def __init__(self,
                 mv_21_mv_71=None,
                 mv_12_mv_22_mv_72=None,
                 mv_32=None,
                 mv_12_we=None):
        """Constructor for the VideoSettingsModel class"""

        # Initialize members of the class
        self.mv_21_mv_71 = mv_21_mv_71
        self.mv_12_mv_22_mv_72 = mv_12_mv_22_mv_72
        self.mv_32 = mv_32
        self.mv_12_we = mv_12_we


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
        mv_21_mv_71 = meraki_sdk.models.mv_21_mv_71_model.MV21MV71Model.from_dictionary(dictionary.get('MV21/MV71')) if dictionary.get('MV21/MV71') else None
        mv_12_mv_22_mv_72 = meraki_sdk.models.mv_12_mv_22_mv_72_model.MV12MV22MV72Model.from_dictionary(dictionary.get('MV12/MV22/MV72')) if dictionary.get('MV12/MV22/MV72') else None
        mv_32 = meraki_sdk.models.mv_32_model.MV32Model.from_dictionary(dictionary.get('MV32')) if dictionary.get('MV32') else None
        mv_12_we = meraki_sdk.models.mv_12_we_model.MV12WEModel.from_dictionary(dictionary.get('MV12WE')) if dictionary.get('MV12WE') else None

        # Return an object of this model
        return cls(mv_21_mv_71,
                   mv_12_mv_22_mv_72,
                   mv_32,
                   mv_12_we)


