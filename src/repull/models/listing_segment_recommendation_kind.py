from enum import Enum

class ListingSegmentRecommendationKind(str, Enum):
    LOW_DNA_COVERAGE = "low_dna_coverage"
    MY_SEGMENT = "my_segment"
    NO_GEO = "no_geo"
    NO_MARKET_SIGNAL = "no_market_signal"
    SEGMENT_NOT_FOUND = "segment_not_found"
    SELF_NOT_SCORED = "self_not_scored"
    TIER_UPLIFT = "tier_uplift"

    def __str__(self) -> str:
        return str(self.value)
