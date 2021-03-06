# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.aanduiding_bij_huisnummer_enum import AanduidingBijHuisnummerEnum
from openapi_client.model.aanduiding_bijzonder_nederlanderschap_enum import AanduidingBijzonderNederlanderschapEnum
from openapi_client.model.aangaan_huwelijk_partnerschap import AangaanHuwelijkPartnerschap
from openapi_client.model.aangaan_huwelijk_partnerschap_in_onderzoek import AangaanHuwelijkPartnerschapInOnderzoek
from openapi_client.model.adres import Adres
from openapi_client.model.bad_request_foutbericht import BadRequestFoutbericht
from openapi_client.model.bad_request_foutbericht_all_of import BadRequestFoutberichtAllOf
from openapi_client.model.datum_onvolledig import DatumOnvolledig
from openapi_client.model.foutbericht import Foutbericht
from openapi_client.model.geboorte import Geboorte
from openapi_client.model.geboorte_all_of import GeboorteAllOf
from openapi_client.model.geboorte_in_onderzoek import GeboorteInOnderzoek
from openapi_client.model.geboortedatum import Geboortedatum
from openapi_client.model.geslacht_enum import GeslachtEnum
from openapi_client.model.gezagsverhouding import Gezagsverhouding
from openapi_client.model.gezagsverhouding_in_onderzoek import GezagsverhoudingInOnderzoek
from openapi_client.model.hal_collection_links import HalCollectionLinks
from openapi_client.model.hal_link import HalLink
from openapi_client.model.indicatie_gezag_minderjarige_enum import IndicatieGezagMinderjarigeEnum
from openapi_client.model.ingeschreven_persoon import IngeschrevenPersoon
from openapi_client.model.ingeschreven_persoon_embedded import IngeschrevenPersoonEmbedded
from openapi_client.model.ingeschreven_persoon_hal import IngeschrevenPersoonHal
from openapi_client.model.ingeschreven_persoon_hal_all_of import IngeschrevenPersoonHalAllOf
from openapi_client.model.ingeschreven_persoon_hal_basis import IngeschrevenPersoonHalBasis
from openapi_client.model.ingeschreven_persoon_hal_basis_all_of import IngeschrevenPersoonHalBasisAllOf
from openapi_client.model.ingeschreven_persoon_hal_collectie import IngeschrevenPersoonHalCollectie
from openapi_client.model.ingeschreven_persoon_hal_collectie_embedded import IngeschrevenPersoonHalCollectieEmbedded
from openapi_client.model.ingeschreven_persoon_links import IngeschrevenPersoonLinks
from openapi_client.model.invalid_params import InvalidParams
from openapi_client.model.kiesrecht import Kiesrecht
from openapi_client.model.kind import Kind
from openapi_client.model.kind_hal_basis import KindHalBasis
from openapi_client.model.kind_hal_basis_all_of import KindHalBasisAllOf
from openapi_client.model.kind_hal_collectie import KindHalCollectie
from openapi_client.model.kind_hal_collectie_embedded import KindHalCollectieEmbedded
from openapi_client.model.kind_in_onderzoek import KindInOnderzoek
from openapi_client.model.kind_links import KindLinks
from openapi_client.model.naam import Naam
from openapi_client.model.naam_in_onderzoek import NaamInOnderzoek
from openapi_client.model.naam_persoon import NaamPersoon
from openapi_client.model.naam_persoon_all_of import NaamPersoonAllOf
from openapi_client.model.naam_persoon_in_onderzoek import NaamPersoonInOnderzoek
from openapi_client.model.naam_persoon_in_onderzoek_all_of import NaamPersoonInOnderzoekAllOf
from openapi_client.model.naamgebruik_enum import NaamgebruikEnum
from openapi_client.model.nationaliteit import Nationaliteit
from openapi_client.model.nationaliteit_in_onderzoek import NationaliteitInOnderzoek
from openapi_client.model.opschorting_bijhouding import OpschortingBijhouding
from openapi_client.model.ouder import Ouder
from openapi_client.model.ouder_aanduiding_enum import OuderAanduidingEnum
from openapi_client.model.ouder_hal_basis import OuderHalBasis
from openapi_client.model.ouder_hal_basis_all_of import OuderHalBasisAllOf
from openapi_client.model.ouder_hal_collectie import OuderHalCollectie
from openapi_client.model.ouder_hal_collectie_embedded import OuderHalCollectieEmbedded
from openapi_client.model.ouder_in_onderzoek import OuderInOnderzoek
from openapi_client.model.ouder_links import OuderLinks
from openapi_client.model.overlijden import Overlijden
from openapi_client.model.overlijden_in_onderzoek import OverlijdenInOnderzoek
from openapi_client.model.partner import Partner
from openapi_client.model.partner_hal_basis import PartnerHalBasis
from openapi_client.model.partner_hal_basis_all_of import PartnerHalBasisAllOf
from openapi_client.model.partner_hal_collectie import PartnerHalCollectie
from openapi_client.model.partner_hal_collectie_embedded import PartnerHalCollectieEmbedded
from openapi_client.model.partner_in_onderzoek import PartnerInOnderzoek
from openapi_client.model.partner_links import PartnerLinks
from openapi_client.model.persoon_in_onderzoek import PersoonInOnderzoek
from openapi_client.model.reden_opschorting_bijhouding_enum import RedenOpschortingBijhoudingEnum
from openapi_client.model.soort_adres_enum import SoortAdresEnum
from openapi_client.model.soort_verbintenis_enum import SoortVerbintenisEnum
from openapi_client.model.verblijfplaats import Verblijfplaats
from openapi_client.model.verblijfplaats_all_of import VerblijfplaatsAllOf
from openapi_client.model.verblijfplaats_in_onderzoek import VerblijfplaatsInOnderzoek
from openapi_client.model.verblijfstitel import Verblijfstitel
from openapi_client.model.verblijfstitel_in_onderzoek import VerblijfstitelInOnderzoek
from openapi_client.model.waardetabel import Waardetabel
