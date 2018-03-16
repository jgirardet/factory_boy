# -*- coding: utf-8 -*-
# Copyright: See the LICENSE file.
"""factory_boy extensions for use with pony orm"""

from __future__ import unicode_literals

from . import base

try:
    from pony.orm import db_session
except ImportError as e:  # pragma: no cover
    raise e


class PonyFactory(base.Factory):
    """Factory for pony orm objects."""

    def __new__(cls, *args, **kwargs):
        cls.hello = "hello"
        return super().__new__(cls, *args, **kwargs)

    class Meta:
        abstract = True

    # @classmethod
    # def _build(cls, model_class, *args, **kwargs):
    #     return model_class(*args, **kwargs)

    @classmethod
    @db_session
    def _create(cls, model_class, *args, **kwargs):
        instance = model_class(*args, **kwargs)
        return instance