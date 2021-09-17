from django.core.exceptions import ValidationError


def validate_is_digits(value: str):
    if not value.isdigit():
        raise ValidationError(
            '%(value)s is not phone number.',
            params={'value': value},
        )
