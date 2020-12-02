# coding: utf-8

"""
    Bevragen Ingeschreven Personen

    API voor het bevragen van ingeschreven personen uit de basisregistratie personen (BRP), inclusief de registratie niet-ingezeten (RNI). Met deze API kun je personen zoeken en actuele gegevens over personen, kinderen, partners en ouders raadplegen.  Gegevens die er niet zijn of niet actueel zijn krijg je niet terug. Heeft een persoon bijvoorbeeld geen geldige nationaliteit, en alleen een beëindigd partnerschap, dan krijg je geen gegevens over nationaliteit en partner.  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/tree/v1.1.0/features) voor nadere toelichting.   # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class OverlijdenInOnderzoek(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'datum': 'bool',
        'land': 'bool',
        'plaats': 'bool',
        'datum_ingang_onderzoek': 'DatumOnvolledig'
    }

    attribute_map = {
        'datum': 'datum',
        'land': 'land',
        'plaats': 'plaats',
        'datum_ingang_onderzoek': 'datumIngangOnderzoek'
    }

    def __init__(self, datum=None, land=None, plaats=None, datum_ingang_onderzoek=None, local_vars_configuration=None):  # noqa: E501
        """OverlijdenInOnderzoek - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._datum = None
        self._land = None
        self._plaats = None
        self._datum_ingang_onderzoek = None
        self.discriminator = None

        if datum is not None:
            self.datum = datum
        if land is not None:
            self.land = land
        if plaats is not None:
            self.plaats = plaats
        if datum_ingang_onderzoek is not None:
            self.datum_ingang_onderzoek = datum_ingang_onderzoek

    @property
    def datum(self):
        """Gets the datum of this OverlijdenInOnderzoek.  # noqa: E501


        :return: The datum of this OverlijdenInOnderzoek.  # noqa: E501
        :rtype: bool
        """
        return self._datum

    @datum.setter
    def datum(self, datum):
        """Sets the datum of this OverlijdenInOnderzoek.


        :param datum: The datum of this OverlijdenInOnderzoek.  # noqa: E501
        :type: bool
        """

        self._datum = datum

    @property
    def land(self):
        """Gets the land of this OverlijdenInOnderzoek.  # noqa: E501


        :return: The land of this OverlijdenInOnderzoek.  # noqa: E501
        :rtype: bool
        """
        return self._land

    @land.setter
    def land(self, land):
        """Sets the land of this OverlijdenInOnderzoek.


        :param land: The land of this OverlijdenInOnderzoek.  # noqa: E501
        :type: bool
        """

        self._land = land

    @property
    def plaats(self):
        """Gets the plaats of this OverlijdenInOnderzoek.  # noqa: E501


        :return: The plaats of this OverlijdenInOnderzoek.  # noqa: E501
        :rtype: bool
        """
        return self._plaats

    @plaats.setter
    def plaats(self, plaats):
        """Sets the plaats of this OverlijdenInOnderzoek.


        :param plaats: The plaats of this OverlijdenInOnderzoek.  # noqa: E501
        :type: bool
        """

        self._plaats = plaats

    @property
    def datum_ingang_onderzoek(self):
        """Gets the datum_ingang_onderzoek of this OverlijdenInOnderzoek.  # noqa: E501


        :return: The datum_ingang_onderzoek of this OverlijdenInOnderzoek.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_ingang_onderzoek

    @datum_ingang_onderzoek.setter
    def datum_ingang_onderzoek(self, datum_ingang_onderzoek):
        """Sets the datum_ingang_onderzoek of this OverlijdenInOnderzoek.


        :param datum_ingang_onderzoek: The datum_ingang_onderzoek of this OverlijdenInOnderzoek.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_ingang_onderzoek = datum_ingang_onderzoek

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OverlijdenInOnderzoek):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OverlijdenInOnderzoek):
            return True

        return self.to_dict() != other.to_dict()
