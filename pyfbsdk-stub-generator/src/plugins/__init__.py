from .plugin_base import PluginBaseClass


def GetDefaultPlugins():
    from .online_documentation import plugin_online_documentation
    from .manual_documentation import plugin_manual_docs
    from .fb_property import plugin_fbproperty
    from .dunder_methods import plugin_dunder_methods
    from .events import plugin_events
    from .enum import plugin_enum
    from .readonly_properties import plugin_readonly

    return [
        plugin_online_documentation.PluginOnlineDocumentation,
        plugin_manual_docs.PluginManualDocumentation,
        plugin_fbproperty.PluginFbProperty,
        plugin_dunder_methods.PluginDunderMethods,
        plugin_enum.PluginEnum,
        plugin_events.PluginEvents,
        plugin_readonly.PluginReadOnly,
    ]
