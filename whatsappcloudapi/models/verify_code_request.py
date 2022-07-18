# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class VerifyCodeRequest(object):

    """Implementation of the 'VerifyCodeRequest' model.

    TODO: type model description here.

    Attributes:
        code (string): The code you received after calling
            FROM_PHONE_NUMBER_ID/request_code.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code'
    }

    def __init__(self,
                 code=None):
        """Constructor for the VerifyCodeRequest class"""

        # Initialize members of the class
        self.code = code 

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

        code = dictionary.get("code") if dictionary.get("code") else None
        # Return an object of this model
        return cls(code)
