from .plugin_base import PluginBaseClass


def get_default_plugins():
    from .dunder_methods import plugin_dunder_methods
    from .enum import plugin_enum
    from .events import plugin_events
    from .fb_property import plugin_fbproperty
    from .manual_documentation import plugin_manual_docs
    from .online_documentation import plugin_online_documentation
    from .pyfbsdk_imports import plugins_pyfbsdk_imports
    from .readonly_properties import plugin_readonly

    return [
        plugin_dunder_methods.PluginDunderMethods,
        plugin_enum.PluginEnum,
        plugin_events.PluginEvents,
        plugin_fbproperty.PluginFbProperty,
        plugin_manual_docs.PluginManualDocumentation,
        plugin_online_documentation.PluginOnlineDocumentation,
        plugin_readonly.PluginReadOnly,
        plugins_pyfbsdk_imports.PluginPyfbsdkImports,
    ]
