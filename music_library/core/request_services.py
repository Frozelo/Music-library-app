from typing import Any


def get_params_from_kwargs(id_type: str, **kwargs) -> Any:
    return kwargs.get(id_type)