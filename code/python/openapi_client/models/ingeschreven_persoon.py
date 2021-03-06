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


class IngeschrevenPersoon(object):
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
        'burgerservicenummer': 'str',
        'geheimhouding_persoonsgegevens': 'bool',
        'geslachtsaanduiding': 'GeslachtEnum',
        'leeftijd': 'int',
        'datum_eerste_inschrijving_gba': 'DatumOnvolledig',
        'kiesrecht': 'Kiesrecht',
        'naam': 'NaamPersoon',
        'in_onderzoek': 'PersoonInOnderzoek',
        'nationaliteiten': 'list[Nationaliteit]',
        'geboorte': 'Geboorte',
        'opschorting_bijhouding': 'OpschortingBijhouding',
        'overlijden': 'Overlijden',
        'verblijfplaats': 'Verblijfplaats',
        'gezagsverhouding': 'Gezagsverhouding',
        'verblijfstitel': 'Verblijfstitel',
        'reisdocumentnummers': 'list[str]'
    }

    attribute_map = {
        'burgerservicenummer': 'burgerservicenummer',
        'geheimhouding_persoonsgegevens': 'geheimhoudingPersoonsgegevens',
        'geslachtsaanduiding': 'geslachtsaanduiding',
        'leeftijd': 'leeftijd',
        'datum_eerste_inschrijving_gba': 'datumEersteInschrijvingGBA',
        'kiesrecht': 'kiesrecht',
        'naam': 'naam',
        'in_onderzoek': 'inOnderzoek',
        'nationaliteiten': 'nationaliteiten',
        'geboorte': 'geboorte',
        'opschorting_bijhouding': 'opschortingBijhouding',
        'overlijden': 'overlijden',
        'verblijfplaats': 'verblijfplaats',
        'gezagsverhouding': 'gezagsverhouding',
        'verblijfstitel': 'verblijfstitel',
        'reisdocumentnummers': 'reisdocumentnummers'
    }

    def __init__(self, burgerservicenummer=None, geheimhouding_persoonsgegevens=None, geslachtsaanduiding=None, leeftijd=None, datum_eerste_inschrijving_gba=None, kiesrecht=None, naam=None, in_onderzoek=None, nationaliteiten=None, geboorte=None, opschorting_bijhouding=None, overlijden=None, verblijfplaats=None, gezagsverhouding=None, verblijfstitel=None, reisdocumentnummers=None, local_vars_configuration=None):  # noqa: E501
        """IngeschrevenPersoon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._burgerservicenummer = None
        self._geheimhouding_persoonsgegevens = None
        self._geslachtsaanduiding = None
        self._leeftijd = None
        self._datum_eerste_inschrijving_gba = None
        self._kiesrecht = None
        self._naam = None
        self._in_onderzoek = None
        self._nationaliteiten = None
        self._geboorte = None
        self._opschorting_bijhouding = None
        self._overlijden = None
        self._verblijfplaats = None
        self._gezagsverhouding = None
        self._verblijfstitel = None
        self._reisdocumentnummers = None
        self.discriminator = None

        if burgerservicenummer is not None:
            self.burgerservicenummer = burgerservicenummer
        if geheimhouding_persoonsgegevens is not None:
            self.geheimhouding_persoonsgegevens = geheimhouding_persoonsgegevens
        if geslachtsaanduiding is not None:
            self.geslachtsaanduiding = geslachtsaanduiding
        if leeftijd is not None:
            self.leeftijd = leeftijd
        if datum_eerste_inschrijving_gba is not None:
            self.datum_eerste_inschrijving_gba = datum_eerste_inschrijving_gba
        if kiesrecht is not None:
            self.kiesrecht = kiesrecht
        if naam is not None:
            self.naam = naam
        if in_onderzoek is not None:
            self.in_onderzoek = in_onderzoek
        if nationaliteiten is not None:
            self.nationaliteiten = nationaliteiten
        if geboorte is not None:
            self.geboorte = geboorte
        if opschorting_bijhouding is not None:
            self.opschorting_bijhouding = opschorting_bijhouding
        if overlijden is not None:
            self.overlijden = overlijden
        if verblijfplaats is not None:
            self.verblijfplaats = verblijfplaats
        if gezagsverhouding is not None:
            self.gezagsverhouding = gezagsverhouding
        if verblijfstitel is not None:
            self.verblijfstitel = verblijfstitel
        if reisdocumentnummers is not None:
            self.reisdocumentnummers = reisdocumentnummers

    @property
    def burgerservicenummer(self):
        """Gets the burgerservicenummer of this IngeschrevenPersoon.  # noqa: E501


        :return: The burgerservicenummer of this IngeschrevenPersoon.  # noqa: E501
        :rtype: str
        """
        return self._burgerservicenummer

    @burgerservicenummer.setter
    def burgerservicenummer(self, burgerservicenummer):
        """Sets the burgerservicenummer of this IngeschrevenPersoon.


        :param burgerservicenummer: The burgerservicenummer of this IngeschrevenPersoon.  # noqa: E501
        :type: str
        """

        self._burgerservicenummer = burgerservicenummer

    @property
    def geheimhouding_persoonsgegevens(self):
        """Gets the geheimhouding_persoonsgegevens of this IngeschrevenPersoon.  # noqa: E501

        Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen.   # noqa: E501

        :return: The geheimhouding_persoonsgegevens of this IngeschrevenPersoon.  # noqa: E501
        :rtype: bool
        """
        return self._geheimhouding_persoonsgegevens

    @geheimhouding_persoonsgegevens.setter
    def geheimhouding_persoonsgegevens(self, geheimhouding_persoonsgegevens):
        """Sets the geheimhouding_persoonsgegevens of this IngeschrevenPersoon.

        Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen.   # noqa: E501

        :param geheimhouding_persoonsgegevens: The geheimhouding_persoonsgegevens of this IngeschrevenPersoon.  # noqa: E501
        :type: bool
        """

        self._geheimhouding_persoonsgegevens = geheimhouding_persoonsgegevens

    @property
    def geslachtsaanduiding(self):
        """Gets the geslachtsaanduiding of this IngeschrevenPersoon.  # noqa: E501


        :return: The geslachtsaanduiding of this IngeschrevenPersoon.  # noqa: E501
        :rtype: GeslachtEnum
        """
        return self._geslachtsaanduiding

    @geslachtsaanduiding.setter
    def geslachtsaanduiding(self, geslachtsaanduiding):
        """Sets the geslachtsaanduiding of this IngeschrevenPersoon.


        :param geslachtsaanduiding: The geslachtsaanduiding of this IngeschrevenPersoon.  # noqa: E501
        :type: GeslachtEnum
        """

        self._geslachtsaanduiding = geslachtsaanduiding

    @property
    def leeftijd(self):
        """Gets the leeftijd of this IngeschrevenPersoon.  # noqa: E501

        Leeftijd in jaren op het moment van bevragen.   # noqa: E501

        :return: The leeftijd of this IngeschrevenPersoon.  # noqa: E501
        :rtype: int
        """
        return self._leeftijd

    @leeftijd.setter
    def leeftijd(self, leeftijd):
        """Sets the leeftijd of this IngeschrevenPersoon.

        Leeftijd in jaren op het moment van bevragen.   # noqa: E501

        :param leeftijd: The leeftijd of this IngeschrevenPersoon.  # noqa: E501
        :type: int
        """

        self._leeftijd = leeftijd

    @property
    def datum_eerste_inschrijving_gba(self):
        """Gets the datum_eerste_inschrijving_gba of this IngeschrevenPersoon.  # noqa: E501


        :return: The datum_eerste_inschrijving_gba of this IngeschrevenPersoon.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_eerste_inschrijving_gba

    @datum_eerste_inschrijving_gba.setter
    def datum_eerste_inschrijving_gba(self, datum_eerste_inschrijving_gba):
        """Sets the datum_eerste_inschrijving_gba of this IngeschrevenPersoon.


        :param datum_eerste_inschrijving_gba: The datum_eerste_inschrijving_gba of this IngeschrevenPersoon.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_eerste_inschrijving_gba = datum_eerste_inschrijving_gba

    @property
    def kiesrecht(self):
        """Gets the kiesrecht of this IngeschrevenPersoon.  # noqa: E501


        :return: The kiesrecht of this IngeschrevenPersoon.  # noqa: E501
        :rtype: Kiesrecht
        """
        return self._kiesrecht

    @kiesrecht.setter
    def kiesrecht(self, kiesrecht):
        """Sets the kiesrecht of this IngeschrevenPersoon.


        :param kiesrecht: The kiesrecht of this IngeschrevenPersoon.  # noqa: E501
        :type: Kiesrecht
        """

        self._kiesrecht = kiesrecht

    @property
    def naam(self):
        """Gets the naam of this IngeschrevenPersoon.  # noqa: E501


        :return: The naam of this IngeschrevenPersoon.  # noqa: E501
        :rtype: NaamPersoon
        """
        return self._naam

    @naam.setter
    def naam(self, naam):
        """Sets the naam of this IngeschrevenPersoon.


        :param naam: The naam of this IngeschrevenPersoon.  # noqa: E501
        :type: NaamPersoon
        """

        self._naam = naam

    @property
    def in_onderzoek(self):
        """Gets the in_onderzoek of this IngeschrevenPersoon.  # noqa: E501


        :return: The in_onderzoek of this IngeschrevenPersoon.  # noqa: E501
        :rtype: PersoonInOnderzoek
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek):
        """Sets the in_onderzoek of this IngeschrevenPersoon.


        :param in_onderzoek: The in_onderzoek of this IngeschrevenPersoon.  # noqa: E501
        :type: PersoonInOnderzoek
        """

        self._in_onderzoek = in_onderzoek

    @property
    def nationaliteiten(self):
        """Gets the nationaliteiten of this IngeschrevenPersoon.  # noqa: E501


        :return: The nationaliteiten of this IngeschrevenPersoon.  # noqa: E501
        :rtype: list[Nationaliteit]
        """
        return self._nationaliteiten

    @nationaliteiten.setter
    def nationaliteiten(self, nationaliteiten):
        """Sets the nationaliteiten of this IngeschrevenPersoon.


        :param nationaliteiten: The nationaliteiten of this IngeschrevenPersoon.  # noqa: E501
        :type: list[Nationaliteit]
        """

        self._nationaliteiten = nationaliteiten

    @property
    def geboorte(self):
        """Gets the geboorte of this IngeschrevenPersoon.  # noqa: E501


        :return: The geboorte of this IngeschrevenPersoon.  # noqa: E501
        :rtype: Geboorte
        """
        return self._geboorte

    @geboorte.setter
    def geboorte(self, geboorte):
        """Sets the geboorte of this IngeschrevenPersoon.


        :param geboorte: The geboorte of this IngeschrevenPersoon.  # noqa: E501
        :type: Geboorte
        """

        self._geboorte = geboorte

    @property
    def opschorting_bijhouding(self):
        """Gets the opschorting_bijhouding of this IngeschrevenPersoon.  # noqa: E501


        :return: The opschorting_bijhouding of this IngeschrevenPersoon.  # noqa: E501
        :rtype: OpschortingBijhouding
        """
        return self._opschorting_bijhouding

    @opschorting_bijhouding.setter
    def opschorting_bijhouding(self, opschorting_bijhouding):
        """Sets the opschorting_bijhouding of this IngeschrevenPersoon.


        :param opschorting_bijhouding: The opschorting_bijhouding of this IngeschrevenPersoon.  # noqa: E501
        :type: OpschortingBijhouding
        """

        self._opschorting_bijhouding = opschorting_bijhouding

    @property
    def overlijden(self):
        """Gets the overlijden of this IngeschrevenPersoon.  # noqa: E501


        :return: The overlijden of this IngeschrevenPersoon.  # noqa: E501
        :rtype: Overlijden
        """
        return self._overlijden

    @overlijden.setter
    def overlijden(self, overlijden):
        """Sets the overlijden of this IngeschrevenPersoon.


        :param overlijden: The overlijden of this IngeschrevenPersoon.  # noqa: E501
        :type: Overlijden
        """

        self._overlijden = overlijden

    @property
    def verblijfplaats(self):
        """Gets the verblijfplaats of this IngeschrevenPersoon.  # noqa: E501


        :return: The verblijfplaats of this IngeschrevenPersoon.  # noqa: E501
        :rtype: Verblijfplaats
        """
        return self._verblijfplaats

    @verblijfplaats.setter
    def verblijfplaats(self, verblijfplaats):
        """Sets the verblijfplaats of this IngeschrevenPersoon.


        :param verblijfplaats: The verblijfplaats of this IngeschrevenPersoon.  # noqa: E501
        :type: Verblijfplaats
        """

        self._verblijfplaats = verblijfplaats

    @property
    def gezagsverhouding(self):
        """Gets the gezagsverhouding of this IngeschrevenPersoon.  # noqa: E501


        :return: The gezagsverhouding of this IngeschrevenPersoon.  # noqa: E501
        :rtype: Gezagsverhouding
        """
        return self._gezagsverhouding

    @gezagsverhouding.setter
    def gezagsverhouding(self, gezagsverhouding):
        """Sets the gezagsverhouding of this IngeschrevenPersoon.


        :param gezagsverhouding: The gezagsverhouding of this IngeschrevenPersoon.  # noqa: E501
        :type: Gezagsverhouding
        """

        self._gezagsverhouding = gezagsverhouding

    @property
    def verblijfstitel(self):
        """Gets the verblijfstitel of this IngeschrevenPersoon.  # noqa: E501


        :return: The verblijfstitel of this IngeschrevenPersoon.  # noqa: E501
        :rtype: Verblijfstitel
        """
        return self._verblijfstitel

    @verblijfstitel.setter
    def verblijfstitel(self, verblijfstitel):
        """Sets the verblijfstitel of this IngeschrevenPersoon.


        :param verblijfstitel: The verblijfstitel of this IngeschrevenPersoon.  # noqa: E501
        :type: Verblijfstitel
        """

        self._verblijfstitel = verblijfstitel

    @property
    def reisdocumentnummers(self):
        """Gets the reisdocumentnummers of this IngeschrevenPersoon.  # noqa: E501


        :return: The reisdocumentnummers of this IngeschrevenPersoon.  # noqa: E501
        :rtype: list[str]
        """
        return self._reisdocumentnummers

    @reisdocumentnummers.setter
    def reisdocumentnummers(self, reisdocumentnummers):
        """Sets the reisdocumentnummers of this IngeschrevenPersoon.


        :param reisdocumentnummers: The reisdocumentnummers of this IngeschrevenPersoon.  # noqa: E501
        :type: list[str]
        """

        self._reisdocumentnummers = reisdocumentnummers

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
        if not isinstance(other, IngeschrevenPersoon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngeschrevenPersoon):
            return True

        return self.to_dict() != other.to_dict()
