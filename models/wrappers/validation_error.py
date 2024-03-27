from typing import Generic, List, TypeVar

T = TypeVar('T')

class ValidationError(Generic[T]):
    def __init__(self, ErrorMessage: str, EntityValidationErrors: List['EntityValidationError[T]']):
        self.ErrorMessage = ErrorMessage
        self.EntityValidationErrors = EntityValidationErrors

class EntityValidationError(Generic[T]):
    def __init__(self, Entity: T, TypeName: str, ValidationErrors: List['ErrorDetail']):
        self.Entity = Entity
        self.TypeName = TypeName
        self.ValidationErrors = ValidationErrors

class ErrorDetail:
    def __init__(self, ErrorCode: str, ErrorMessage: str, PropertyName: str):
        self.ErrorCode = ErrorCode
        self.ErrorMessage = ErrorMessage
        self.PropertyName = PropertyName