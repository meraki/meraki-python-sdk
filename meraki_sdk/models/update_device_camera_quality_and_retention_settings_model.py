# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateDeviceCameraQualityAndRetentionSettingsModel(object):

    """Implementation of the 'updateDeviceCameraQualityAndRetentionSettings' model.

    TODO: type model description here.

    Attributes:
        profile_id (string): The ID of a quality and retention profile to
            assign to the camera. The profile's settings will override all of
            the per-camera quality and retention settings. If the value of
            this parameter is null, any existing profile will be unassigned
            from the camera.
        motion_based_retention_enabled (bool): Boolean indicating if
            motion-based retention is enabled(true) or disabled(false) on the
            camera
        audio_recording_enabled (bool): Boolean indicating if audio recording
            is enabled(true) or disabled(false) on the camera
        restricted_bandwidth_mode_enabled (bool): Boolean indicating if
            restricted bandwidth is enabled(true) or disabled(false) on the
            camera
        quality (QualityEnum): Quality of the camera. Can be one of
            'Standard', 'High' or 'Enhanced'. Not all qualities are supported
            by every camera model.
        resolution (ResolutionEnum): Resolution of the camera. Can be one of
            '1280x720', '1920x1080', '1080x1080' or '2058x2058'. Not all
            resolutions are supported by every camera model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "profile_id":'profileId',
        "motion_based_retention_enabled":'motionBasedRetentionEnabled',
        "audio_recording_enabled":'audioRecordingEnabled',
        "restricted_bandwidth_mode_enabled":'restrictedBandwidthModeEnabled',
        "quality":'quality',
        "resolution":'resolution'
    }

    def __init__(self,
                 profile_id=None,
                 motion_based_retention_enabled=None,
                 audio_recording_enabled=None,
                 restricted_bandwidth_mode_enabled=None,
                 quality=None,
                 resolution=None):
        """Constructor for the UpdateDeviceCameraQualityAndRetentionSettingsModel class"""

        # Initialize members of the class
        self.profile_id = profile_id
        self.motion_based_retention_enabled = motion_based_retention_enabled
        self.audio_recording_enabled = audio_recording_enabled
        self.restricted_bandwidth_mode_enabled = restricted_bandwidth_mode_enabled
        self.quality = quality
        self.resolution = resolution


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
        profile_id = dictionary.get('profileId')
        motion_based_retention_enabled = dictionary.get('motionBasedRetentionEnabled')
        audio_recording_enabled = dictionary.get('audioRecordingEnabled')
        restricted_bandwidth_mode_enabled = dictionary.get('restrictedBandwidthModeEnabled')
        quality = dictionary.get('quality')
        resolution = dictionary.get('resolution')

        # Return an object of this model
        return cls(profile_id,
                   motion_based_retention_enabled,
                   audio_recording_enabled,
                   restricted_bandwidth_mode_enabled,
                   quality,
                   resolution)


