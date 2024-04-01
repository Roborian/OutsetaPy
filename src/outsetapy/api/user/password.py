from outsetapy.util.request import Request
from outsetapy.util.store import Store
from outsetapy.models.wrappers.validation_error import ValidationError


class Password:
    def __init__(self, store: Store):
        self.store = store

    async def update(self, existing_password: str, new_password: str) -> None:
        request = (
            Request(self.store, "profile/password")
            .authenticate_as_user()
            .with_body(
                {"ExistingPassword": existing_password, "NewPassword": new_password}
            )
        )
        response = await request.put()

        if response.status == 400:
            raise ValidationError(response.json())
        elif response.ok:
            return None
        else:
            raise Exception(response)
