from importlib import reload

from .plugin import PluginBaseClass


def GetDefaultPlugins():
    from .online_documentation import plugin_online_documentation
    from .manual_documentation import plugin_manual_docs

    reload(plugin_online_documentation)
    reload(plugin_manual_docs)

    return (
        plugin_online_documentation.PluginOnlineDocumentation,
        plugin_manual_docs.PluginManualDocumentation,
    )
