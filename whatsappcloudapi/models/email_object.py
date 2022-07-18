# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class EmailObject(object):

    """Implementation of the 'EmailObject' model.

    TODO: type model description here.

    Attributes:
        email (string): TODO: type description here.
        mtype (PersonalInformationTypeEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email": 'email',
        "mtype": 'type'
    }

    _optionals = [
        'email',
        'mtype',
    ]

    def __init__(self,
                 email=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the EmailObject class"""

        # Initialize members of the class
        if email is not APIHelper.SKIP:
            self.email = email 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(email,
                   mtype)
