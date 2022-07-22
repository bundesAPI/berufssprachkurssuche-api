"""
    Arbeitsagentur Berufssprachkurssuche API

    Eine der größten Berufssprachförderungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** bd24f42e-ad0b-4005-b834-23bb6800dc6c  **ClientSecret:** 6776b89e-5728-4643-8cd5-c93aefb5314b   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsanbieter import (
    ResponseEmbeddedTermineInnerAngebotBildungsanbieter,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_bildungsart import (
    ResponseEmbeddedTermineInnerAngebotBildungsart,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_schulart import (
    ResponseEmbeddedTermineInnerAngebotSchulart,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_suchworte_inner import (
    ResponseEmbeddedTermineInnerAngebotSuchworteInner,
)
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot_systematiken_inner import (
    ResponseEmbeddedTermineInnerAngebotSystematikenInner,
)

from deutschland import berufssprachkurssuche

globals()[
    "ResponseEmbeddedTermineInnerAngebotBildungsanbieter"
] = ResponseEmbeddedTermineInnerAngebotBildungsanbieter
globals()[
    "ResponseEmbeddedTermineInnerAngebotBildungsart"
] = ResponseEmbeddedTermineInnerAngebotBildungsart
globals()[
    "ResponseEmbeddedTermineInnerAngebotSchulart"
] = ResponseEmbeddedTermineInnerAngebotSchulart
globals()[
    "ResponseEmbeddedTermineInnerAngebotSuchworteInner"
] = ResponseEmbeddedTermineInnerAngebotSuchworteInner
globals()[
    "ResponseEmbeddedTermineInnerAngebotSystematikenInner"
] = ResponseEmbeddedTermineInnerAngebotSystematikenInner
from deutschland.berufssprachkurssuche.model.response_embedded_termine_inner_angebot import (
    ResponseEmbeddedTermineInnerAngebot,
)


class TestResponseEmbeddedTermineInnerAngebot(unittest.TestCase):
    """ResponseEmbeddedTermineInnerAngebot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseEmbeddedTermineInnerAngebot(self):
        """Test ResponseEmbeddedTermineInnerAngebot"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseEmbeddedTermineInnerAngebot()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
