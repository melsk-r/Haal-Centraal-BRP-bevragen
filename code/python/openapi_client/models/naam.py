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


class Naam(object):
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
        'geslachtsnaam': 'str',
        'voorletters': 'str',
        'voornamen': 'str',
        'voorvoegsel': 'str',
        'aanduiding_naamgebruik': 'NaamgebruikEnum',
        'adellijke_titel_predikaat': 'Waardetabel',
        'in_onderzoek': 'NaamInOnderzoek'
    }

    attribute_map = {
        'geslachtsnaam': 'geslachtsnaam',
        'voorletters': 'voorletters',
        'voornamen': 'voornamen',
        'voorvoegsel': 'voorvoegsel',
        'aanduiding_naamgebruik': 'aanduidingNaamgebruik',
        'adellijke_titel_predikaat': 'adellijkeTitelPredikaat',
        'in_onderzoek': 'inOnderzoek'
    }

    def __init__(self, geslachtsnaam=None, voorletters=None, voornamen=None, voorvoegsel=None, aanduiding_naamgebruik=None, adellijke_titel_predikaat=None, in_onderzoek=None, local_vars_configuration=None):  # noqa: E501
        """Naam - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geslachtsnaam = None
        self._voorletters = None
        self._voornamen = None
        self._voorvoegsel = None
        self._aanduiding_naamgebruik = None
        self._adellijke_titel_predikaat = None
        self._in_onderzoek = None
        self.discriminator = None

        if geslachtsnaam is not None:
            self.geslachtsnaam = geslachtsnaam
        if voorletters is not None:
            self.voorletters = voorletters
        if voornamen is not None:
            self.voornamen = voornamen
        if voorvoegsel is not None:
            self.voorvoegsel = voorvoegsel
        if aanduiding_naamgebruik is not None:
            self.aanduiding_naamgebruik = aanduiding_naamgebruik
        if adellijke_titel_predikaat is not None:
            self.adellijke_titel_predikaat = adellijke_titel_predikaat
        if in_onderzoek is not None:
            self.in_onderzoek = in_onderzoek

    @property
    def geslachtsnaam(self):
        """Gets the geslachtsnaam of this Naam.  # noqa: E501

        De achternaam van een persoon.   # noqa: E501

        :return: The geslachtsnaam of this Naam.  # noqa: E501
        :rtype: str
        """
        return self._geslachtsnaam

    @geslachtsnaam.setter
    def geslachtsnaam(self, geslachtsnaam):
        """Sets the geslachtsnaam of this Naam.

        De achternaam van een persoon.   # noqa: E501

        :param geslachtsnaam: The geslachtsnaam of this Naam.  # noqa: E501
        :type: str
        """

        self._geslachtsnaam = geslachtsnaam

    @property
    def voorletters(self):
        """Gets the voorletters of this Naam.  # noqa: E501

        De voorletters van de persoon, afgeleid van de voornamen.   # noqa: E501

        :return: The voorletters of this Naam.  # noqa: E501
        :rtype: str
        """
        return self._voorletters

    @voorletters.setter
    def voorletters(self, voorletters):
        """Sets the voorletters of this Naam.

        De voorletters van de persoon, afgeleid van de voornamen.   # noqa: E501

        :param voorletters: The voorletters of this Naam.  # noqa: E501
        :type: str
        """

        self._voorletters = voorletters

    @property
    def voornamen(self):
        """Gets the voornamen of this Naam.  # noqa: E501

        De verzameling namen voor de geslachtsnaam, gescheiden door spaties.   # noqa: E501

        :return: The voornamen of this Naam.  # noqa: E501
        :rtype: str
        """
        return self._voornamen

    @voornamen.setter
    def voornamen(self, voornamen):
        """Sets the voornamen of this Naam.

        De verzameling namen voor de geslachtsnaam, gescheiden door spaties.   # noqa: E501

        :param voornamen: The voornamen of this Naam.  # noqa: E501
        :type: str
        """

        self._voornamen = voornamen

    @property
    def voorvoegsel(self):
        """Gets the voorvoegsel of this Naam.  # noqa: E501


        :return: The voorvoegsel of this Naam.  # noqa: E501
        :rtype: str
        """
        return self._voorvoegsel

    @voorvoegsel.setter
    def voorvoegsel(self, voorvoegsel):
        """Sets the voorvoegsel of this Naam.


        :param voorvoegsel: The voorvoegsel of this Naam.  # noqa: E501
        :type: str
        """

        self._voorvoegsel = voorvoegsel

    @property
    def aanduiding_naamgebruik(self):
        """Gets the aanduiding_naamgebruik of this Naam.  # noqa: E501


        :return: The aanduiding_naamgebruik of this Naam.  # noqa: E501
        :rtype: NaamgebruikEnum
        """
        return self._aanduiding_naamgebruik

    @aanduiding_naamgebruik.setter
    def aanduiding_naamgebruik(self, aanduiding_naamgebruik):
        """Sets the aanduiding_naamgebruik of this Naam.


        :param aanduiding_naamgebruik: The aanduiding_naamgebruik of this Naam.  # noqa: E501
        :type: NaamgebruikEnum
        """

        self._aanduiding_naamgebruik = aanduiding_naamgebruik

    @property
    def adellijke_titel_predikaat(self):
        """Gets the adellijke_titel_predikaat of this Naam.  # noqa: E501


        :return: The adellijke_titel_predikaat of this Naam.  # noqa: E501
        :rtype: Waardetabel
        """
        return self._adellijke_titel_predikaat

    @adellijke_titel_predikaat.setter
    def adellijke_titel_predikaat(self, adellijke_titel_predikaat):
        """Sets the adellijke_titel_predikaat of this Naam.


        :param adellijke_titel_predikaat: The adellijke_titel_predikaat of this Naam.  # noqa: E501
        :type: Waardetabel
        """

        self._adellijke_titel_predikaat = adellijke_titel_predikaat

    @property
    def in_onderzoek(self):
        """Gets the in_onderzoek of this Naam.  # noqa: E501


        :return: The in_onderzoek of this Naam.  # noqa: E501
        :rtype: NaamInOnderzoek
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek):
        """Sets the in_onderzoek of this Naam.


        :param in_onderzoek: The in_onderzoek of this Naam.  # noqa: E501
        :type: NaamInOnderzoek
        """

        self._in_onderzoek = in_onderzoek

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
        if not isinstance(other, Naam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Naam):
            return True

        return self.to_dict() != other.to_dict()
