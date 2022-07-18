# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from whatsappcloudapi.api_helper import APIHelper
from whatsappcloudapi.configuration import Server
from whatsappcloudapi.controllers.base_controller import BaseController
from whatsappcloudapi.models.get_business_profile_id_response import GetBusinessProfileIDResponse
from whatsappcloudapi.models.success_response import SuccessResponse


class BusinessProfilesController(BaseController):

    """A Controller to access Endpoints in the whatsappcloudapi API."""
    def __init__(self, config, auth_managers):
        super(BusinessProfilesController, self).__init__(config, auth_managers)

    def get_business_profile_id(self,
                                phone_number_id,
                                fields=None):
        """Does a GET request to /{Phone-Number-ID}/whatsapp_business_profile.

        Use this endpoint to retrieve your business’ profile. This business
        profile is visible to consumers in the chat thread next to the profile
        photo. The profile information will contain a business profile ID
        which you can use to make API calls.

        Args:
            phone_number_id (string): TODO: type description here.
            fields (string, optional): Here you can specify what you want to
                know from your business as a comma separated list of fields.
                Available fields include: id, about, messaging_product,
                address, description, vertical, email, websites,
                profile_picture_url

        Returns:
            GetBusinessProfileIDResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/{Phone-Number-ID}/whatsapp_business_profile'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'Phone-Number-ID': {'value': phone_number_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'fields': fields
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetBusinessProfileIDResponse.from_dictionary)

        return decoded

    def update_business_profile(self,
                                phone_number_id,
                                body):
        """Does a POST request to /{Phone-Number-ID}/whatsapp_business_profile.

        Use this endpoint to update your business’ profile information such as
        the business description, email or address.

        Args:
            phone_number_id (string): TODO: type description here.
            body (UpdateBusinessProfileRequest): TODO: type description here.

        Returns:
            SuccessResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/{Phone-Number-ID}/whatsapp_business_profile'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'Phone-Number-ID': {'value': phone_number_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, SuccessResponse.from_dictionary)

        return decoded
