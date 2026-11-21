from enum import IntEnum

class UpdateVrboListingBookingSettingsBodyMaxMonthsBeforeBooking(IntEnum):
    VALUE_6 = 6
    VALUE_9 = 9
    VALUE_12 = 12
    VALUE_18 = 18
    VALUE_24 = 24

    def __str__(self) -> str:
        return str(self.value)
