"""Classical music detection and title parsing (premium).

Public API:
    is_classical(title) -> bool
    parse_classical(title) -> TrackData | None
    extract_catalogue_ids(text) -> list[CatalogueMatch]
    extract_key(text) -> str | None

The test suite in tests/ doubles as the title-format corpus — every symbol
or key variant added to the parser must come with a case there. Run with:

    uv run pytest src/swingmusic/premium/classical/tests
"""

from swingmusic.premium.classical.catalogue import (
    SYMBOLS,
    CatalogueMatch,
    CatalogueSymbol,
    extract_catalogue_ids,
)
from swingmusic.premium.classical.keys import extract_key
from swingmusic.premium.classical.parser import (
    TrackData,
    is_classical,
    parse_classical,
)

__all__ = [
    "SYMBOLS",
    "CatalogueMatch",
    "CatalogueSymbol",
    "TrackData",
    "extract_catalogue_ids",
    "extract_key",
    "is_classical",
    "parse_classical",
]
