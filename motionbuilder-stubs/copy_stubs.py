""" 
Build script to copy the latest stubs from 'generated-stub-files/' to 'src/'
"""

import os
import shutil

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    PLUGIN_NAME = "copy-stubs"

    def initialize(self, version, build_data):
        package_version = self.metadata.version
        package_version_major = package_version.partition(".")[0]

        target_dir = os.path.join(self.root, "src")

        root_dir = os.path.abspath(self.root)
        generated_files_dir = os.path.join(os.path.dirname(root_dir), "generated-stub-files")

        if not os.path.exists(generated_files_dir):
            if os.path.exists(target_dir):
                # If src/ directory exists but not the generated-stub-files we're building from src tar.gz
                # In this case this build script should not do anything
                return

            raise FileNotFoundError(f"Directory {generated_files_dir} does not exist.")

        source_dir = os.path.join(generated_files_dir, f"motionbuilder-{package_version_major}")
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Directory {source_dir} does not exist.")

        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)

        shutil.copytree(source_dir, target_dir)
