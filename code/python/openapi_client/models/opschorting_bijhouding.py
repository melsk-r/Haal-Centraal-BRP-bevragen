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


class OpschortingBijhouding(object):
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
        'reden': 'RedenOpschortingBijhoudingEnum',
        'datum': 'DatumOnvolledig'
    }

    attribute_map = {
        'reden': 'reden',
        'datum': 'datum'
    }

    def __init__(self, reden=None, datum=None, local_vars_configuration=None):  # noqa: E501
        """OpschortingBijhouding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reden = None
        self._datum = None
        self.discriminator = None

        if reden is not None:
            self.reden = reden
        if datum is not None:
            self.datum = datum

    @property
    def reden(self):
        """Gets the reden of this OpschortingBijhouding.  # noqa: E501


        :return: The reden of this OpschortingBijhouding.  # noqa: E501
        :rtype: RedenOpschortingBijhoudingEnum
        """
        return self._reden

    @reden.setter
    def reden(self, reden):
        """Sets the reden of this OpschortingBijhouding.


        :param reden: The reden of this OpschortingBijhouding.  # noqa: E501
        :type: RedenOpschortingBijhoudingEnum
        """

        self._reden = reden

    @property
    def datum(self):
        """Gets the datum of this OpschortingBijhouding.  # noqa: E501


        :return: The datum of this OpschortingBijhouding.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum

    @datum.setter
    def datum(self, datum):
        """Sets the datum of this OpschortingBijhouding.


        :param datum: The datum of this OpschortingBijhouding.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum = datum

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
        if not isinstance(other, OpschortingBijhouding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpschortingBijhouding):
            return True

        return self.to_dict() != other.to_dict()
