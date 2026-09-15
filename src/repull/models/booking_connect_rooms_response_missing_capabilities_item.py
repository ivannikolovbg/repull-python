from enum import Enum

class BookingConnectRoomsResponseMissingCapabilitiesItem(str, Enum):
    CONTENT = "content"
    MESSAGING = "messaging"
    RATES = "rates"
    RESERVATIONS = "reservations"

    def __str__(self) -> str:
        return str(self.value)
