from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_class_loader import JavaLangClassLoader
    from ..models.org_springframework_beans_factory_bean_factory import OrgSpringframeworkBeansFactoryBeanFactory
    from ..models.org_springframework_beans_factory_config_autowire_capable_bean_factory import (
        OrgSpringframeworkBeansFactoryConfigAutowireCapableBeanFactory,
    )
    from ..models.org_springframework_core_env_environment import OrgSpringframeworkCoreEnvEnvironment


T = TypeVar("T", bound="OrgSpringframeworkContextApplicationContext")


@_attrs_define
class OrgSpringframeworkContextApplicationContext:
    """
    Attributes:
        application_name (str | Unset):
        autowire_capable_bean_factory (OrgSpringframeworkBeansFactoryConfigAutowireCapableBeanFactory | Unset):
        bean_definition_count (int | Unset):
        bean_definition_names (list[str] | Unset):
        class_loader (JavaLangClassLoader | Unset):
        display_name (str | Unset):
        environment (OrgSpringframeworkCoreEnvEnvironment | Unset):
        id (str | Unset):
        parent (OrgSpringframeworkContextApplicationContext | Unset):
        parent_bean_factory (OrgSpringframeworkBeansFactoryBeanFactory | Unset):
        startup_date (int | Unset):
    """

    application_name: str | Unset = UNSET
    autowire_capable_bean_factory: OrgSpringframeworkBeansFactoryConfigAutowireCapableBeanFactory | Unset = UNSET
    bean_definition_count: int | Unset = UNSET
    bean_definition_names: list[str] | Unset = UNSET
    class_loader: JavaLangClassLoader | Unset = UNSET
    display_name: str | Unset = UNSET
    environment: OrgSpringframeworkCoreEnvEnvironment | Unset = UNSET
    id: str | Unset = UNSET
    parent: OrgSpringframeworkContextApplicationContext | Unset = UNSET
    parent_bean_factory: OrgSpringframeworkBeansFactoryBeanFactory | Unset = UNSET
    startup_date: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        autowire_capable_bean_factory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.autowire_capable_bean_factory, Unset):
            autowire_capable_bean_factory = self.autowire_capable_bean_factory.to_dict()

        bean_definition_count = self.bean_definition_count

        bean_definition_names: list[str] | Unset = UNSET
        if not isinstance(self.bean_definition_names, Unset):
            bean_definition_names = self.bean_definition_names

        class_loader: dict[str, Any] | Unset = UNSET
        if not isinstance(self.class_loader, Unset):
            class_loader = self.class_loader.to_dict()

        display_name = self.display_name

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        id = self.id

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        parent_bean_factory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_bean_factory, Unset):
            parent_bean_factory = self.parent_bean_factory.to_dict()

        startup_date = self.startup_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if autowire_capable_bean_factory is not UNSET:
            field_dict["autowireCapableBeanFactory"] = autowire_capable_bean_factory
        if bean_definition_count is not UNSET:
            field_dict["beanDefinitionCount"] = bean_definition_count
        if bean_definition_names is not UNSET:
            field_dict["beanDefinitionNames"] = bean_definition_names
        if class_loader is not UNSET:
            field_dict["classLoader"] = class_loader
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if id is not UNSET:
            field_dict["id"] = id
        if parent is not UNSET:
            field_dict["parent"] = parent
        if parent_bean_factory is not UNSET:
            field_dict["parentBeanFactory"] = parent_bean_factory
        if startup_date is not UNSET:
            field_dict["startupDate"] = startup_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_class_loader import JavaLangClassLoader  # noqa: PLC0415
        from ..models.org_springframework_beans_factory_bean_factory import OrgSpringframeworkBeansFactoryBeanFactory  # noqa: PLC0415
        from ..models.org_springframework_beans_factory_config_autowire_capable_bean_factory import (
            OrgSpringframeworkBeansFactoryConfigAutowireCapableBeanFactory,  # noqa: PLC0415
        )
        from ..models.org_springframework_core_env_environment import OrgSpringframeworkCoreEnvEnvironment  # noqa: PLC0415

        d = dict(src_dict)
        application_name = d.pop("applicationName", UNSET)

        _autowire_capable_bean_factory = d.pop("autowireCapableBeanFactory", UNSET)
        autowire_capable_bean_factory: OrgSpringframeworkBeansFactoryConfigAutowireCapableBeanFactory | Unset
        if isinstance(_autowire_capable_bean_factory, Unset):
            autowire_capable_bean_factory = UNSET
        else:
            autowire_capable_bean_factory = OrgSpringframeworkBeansFactoryConfigAutowireCapableBeanFactory.from_dict(
                _autowire_capable_bean_factory
            )

        bean_definition_count = d.pop("beanDefinitionCount", UNSET)

        bean_definition_names = cast(list[str], d.pop("beanDefinitionNames", UNSET))

        _class_loader = d.pop("classLoader", UNSET)
        class_loader: JavaLangClassLoader | Unset
        if isinstance(_class_loader, Unset):
            class_loader = UNSET
        else:
            class_loader = JavaLangClassLoader.from_dict(_class_loader)

        display_name = d.pop("displayName", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: OrgSpringframeworkCoreEnvEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = OrgSpringframeworkCoreEnvEnvironment.from_dict(_environment)

        id = d.pop("id", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: OrgSpringframeworkContextApplicationContext | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = OrgSpringframeworkContextApplicationContext.from_dict(_parent)

        _parent_bean_factory = d.pop("parentBeanFactory", UNSET)
        parent_bean_factory: OrgSpringframeworkBeansFactoryBeanFactory | Unset
        if isinstance(_parent_bean_factory, Unset):
            parent_bean_factory = UNSET
        else:
            parent_bean_factory = OrgSpringframeworkBeansFactoryBeanFactory.from_dict(_parent_bean_factory)

        startup_date = d.pop("startupDate", UNSET)

        org_springframework_context_application_context = cls(
            application_name=application_name,
            autowire_capable_bean_factory=autowire_capable_bean_factory,
            bean_definition_count=bean_definition_count,
            bean_definition_names=bean_definition_names,
            class_loader=class_loader,
            display_name=display_name,
            environment=environment,
            id=id,
            parent=parent,
            parent_bean_factory=parent_bean_factory,
            startup_date=startup_date,
        )

        org_springframework_context_application_context.additional_properties = d
        return org_springframework_context_application_context

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
