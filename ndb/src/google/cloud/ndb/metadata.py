# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Access datastore metadata."""

from google.cloud.ndb import model


__all__ = [
    "EntityGroup",
    "get_entity_group_version",
    "get_kinds",
    "get_namespaces",
    "get_properties_of_kind",
    "get_representations_of_kind",
    "Kind",
    "Namespace",
    "Property",
]


class _BaseMetadata(model.Model):
    """Base class for all metadata models."""

    _use_cache = False
    _use_memcache = False

    KIND_NAME = ""

    def __new__(cls, *args, **kwargs):
        if cls is _BaseMetadata:
            raise TypeError("This base class cannot be instantiated")
        return model.Model(*args, **kwargs)

    @classmethod
    def _get_kind(cls):
        """Kind name override."""
        return cls.KIND_NAME


class Namespace(_BaseMetadata):
    """Model for __namespace__ metadata query results."""

    KIND_NAME = "__namespace__"
    EMPTY_NAMESPACE_ID = 1

    @property
    def namespace_name(self):
        """Return the namespace name specified by this entity's key."""
        return self.key_to_namespace(self.key)

    @classmethod
    def key_for_namespace(cls, namespace):
        """Return the Key for a namespace.

    Args:
        namespace (str): A string giving the namespace whose key is requested.

    Returns:
        key.Key: The Key for the namespace.
    """
        if namespace:
            return model.Key(cls.KIND_NAME, namespace)
        else:
            return model.Key(cls.KIND_NAME, cls.EMPTY_NAMESPACE_ID)

    @classmethod
    def key_to_namespace(cls, key):
        """Return the namespace specified by a given __namespace__ key.

    Args:
        key (key.Key): key whose name is requested.

    Returns:
        str: The namespace specified by key.
    """
        return key.string_id() or ""


class Kind(_BaseMetadata):
    """Model for __kind__ metadata query results."""

    KIND_NAME = "__kind__"

    @property
    def kind_name(self):
        """Return the kind name specified by this entity's key."""
        return self.key_to_kind(self.key)

    @classmethod
    def key_for_kind(cls, kind):
        """Return the __kind__ key for kind.

    Args:
        kind (Kind): kind whose key is requested.

    Returns:
        key.Key: key for kind.
    """
        return model.Key(cls.KIND_NAME, kind)

    @classmethod
    def key_to_kind(cls, key):
        """Return the kind specified by a given __kind__ key.

    Args:
        key (key.Key): key whose name is requested.

    Returns:
        Kind: The kind specified by key.
    """
        return key.id()


class Property(_BaseMetadata):
    """Model for __property__ metadata query results."""

    KIND_NAME = "__property__"

    @property
    def property_name(self):
        """Return the property name specified by this entity's key."""
        return self.key_to_property(self.key)

    @property
    def kind_name(self):
        """Return the kind name specified by this entity's key."""
        return self.key_to_kind(self.key)

    property_representation = model.StringProperty(repeated=True)

    @classmethod
    def key_for_kind(cls, kind):
        """Return the __property__ key for kind.

    Args:
        kind (Kind): kind whose key is requested.

    Returns:
        key.Key: The parent key for __property__ keys of kind.
    """
        return model.Key(Kind.KIND_NAME, kind)

    @classmethod
    def key_for_property(cls, kind, property):
        """Return the __property__ key for property of kind.

    Args:
        kind (Kind): kind whose key is requested.
        property (Property): property whose key is requested.

    Returns:
        key.Key: The key for property of kind.
    """
        return model.Key(Kind.KIND_NAME, kind, Property.KIND_NAME, property)

    @classmethod
    def key_to_kind(cls, key):
        """Return the kind specified by a given __property__ key.

    Args:
        key (key.Key): key whose kind name is requested.

    Returns:
        Kind: The kind specified by key.
    """
        if key.kind() == Kind.KIND_NAME:
            return key.id()
        else:
            return key.parent().id()

    @classmethod
    def key_to_property(cls, key):
        """Return the property specified by a given __property__ key.

    Args:
        key (key.Key): key whose property name is requested.

    Returns:
        Property: property specified by key, or None if the key specified only a
            kind.
    """
        if key.kind() == Kind.KIND_NAME:
            return None
        else:
            return key.id()


class EntityGroup(_BaseMetadata):
    """Model for __entity_group__ metadata (available in HR datastore only).

  This metadata contains a numeric __version__ property that is guaranteed
  to increase on every change to the entity group. The version may increase
  even in the absence of user-visible changes to the entity group. The
  __entity_group__ entity may not exist if the entity group was never
  written to.
  """

    KIND_NAME = "__entity_group__"
    ID = 1

    version = model.IntegerProperty(name="__version__")

    @classmethod
    def key_for_entity_group(cls, key):
        """Return the key for the entity group containing key.

    Args:
        key (key.Key): a key for an entity group whose __entity_group__ key you want.

    Returns:
        key.Key: The __entity_group__ key for the entity group containing key.
    """
        return model.Key(cls.KIND_NAME, cls.ID, parent=key.root())


def get_entity_group_version(*args, **kwargs):
    """Need query for this"""
    raise NotImplementedError


def get_kinds(*args, **kwargs):
    """Need query for this"""
    raise NotImplementedError


def get_namespaces(*args, **kwargs):
    """Need query for this"""
    raise NotImplementedError


def get_properties_of_kind(*args, **kwargs):
    """Need query for this"""
    raise NotImplementedError


def get_representations_of_kind(*args, **kwargs):
    """Need query for this"""
    raise NotImplementedError
