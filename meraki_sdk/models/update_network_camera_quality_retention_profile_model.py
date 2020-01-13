# -*- coding: utf-8 -*-

"""
    meraki_sdk

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki_sdk.models.video_settings_model

class UpdateNetworkCameraQualityRetentionProfileModel(object):

    """Implementation of the 'updateNetworkCameraQualityRetentionProfile' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the new profile. Must be unique.
        motion_based_retention_enabled (bool): Deletes footage older than 3
            days in which no motion was detected. Can be either true or false.
            Defaults to false.
        restricted_bandwidth_mode_enabled (bool): Disable features that
            require additional bandwidth such as Motion Recap. Can be either
            true or false. Defaults to false.
        audio_recording_enabled (bool): Whether or not to record audio. Can be
            either true or false. Defaults to false.
        cloud_archive_enabled (bool): Create redundant video backup using
            Cloud Archive. Can be either true or false. Defaults to false.
        schedule_id (string): Schedule for which this camera will record
            video, or 'null' to always record.
        max_retention_days (int): The maximum number of days for which the
            data will be stored, or 'null' to keep data until storage space
            runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8,
            9, 10, 14, 30, 60, 90] days
        video_settings (VideoSettingsModel): Video quality and resolution
            settings for all the camera models.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "motion_based_retention_enabled":'motionBasedRetentionEnabled',
        "restricted_bandwidth_mode_enabled":'restrictedBandwidthModeEnabled',
        "audio_recording_enabled":'audioRecordingEnabled',
        "cloud_archive_enabled":'cloudArchiveEnabled',
        "schedule_id":'scheduleId',
        "max_retention_days":'maxRetentionDays',
        "video_settings":'videoSettings'
    }

    def __init__(self,
                 name=None,
                 motion_based_retention_enabled=None,
                 restricted_bandwidth_mode_enabled=None,
                 audio_recording_enabled=None,
                 cloud_archive_enabled=None,
                 schedule_id=None,
                 max_retention_days=None,
                 video_settings=None):
        """Constructor for the UpdateNetworkCameraQualityRetentionProfileModel class"""

        # Initialize members of the class
        self.name = name
        self.motion_based_retention_enabled = motion_based_retention_enabled
        self.restricted_bandwidth_mode_enabled = restricted_bandwidth_mode_enabled
        self.audio_recording_enabled = audio_recording_enabled
        self.cloud_archive_enabled = cloud_archive_enabled
        self.schedule_id = schedule_id
        self.max_retention_days = max_retention_days
        self.video_settings = video_settings


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
        motion_based_retention_enabled = dictionary.get('motionBasedRetentionEnabled')
        restricted_bandwidth_mode_enabled = dictionary.get('restrictedBandwidthModeEnabled')
        audio_recording_enabled = dictionary.get('audioRecordingEnabled')
        cloud_archive_enabled = dictionary.get('cloudArchiveEnabled')
        schedule_id = dictionary.get('scheduleId')
        max_retention_days = dictionary.get('maxRetentionDays')
        video_settings = meraki_sdk.models.video_settings_model.VideoSettingsModel.from_dictionary(dictionary.get('videoSettings')) if dictionary.get('videoSettings') else None

        # Return an object of this model
        return cls(name,
                   motion_based_retention_enabled,
                   restricted_bandwidth_mode_enabled,
                   audio_recording_enabled,
                   cloud_archive_enabled,
                   schedule_id,
                   max_retention_days,
                   video_settings)


