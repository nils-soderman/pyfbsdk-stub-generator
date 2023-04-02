from .plugin import PluginBaseClass

def GetDefaultPlugins():
    from .online_documentation import PluginOnlineDocumentation
    from .manual_documentation import PluginManualDocs

    return (
        PluginOnlineDocumentation,
        # PluginManualDocs
    )
