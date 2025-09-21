# Change Log

## [2026.1.0]

- The stubs are now avaliable as a PyPI package [motionbuilder-stubs](https://pypi.org/project/motionbuilder-stubs/)
- Reorganized the GitHub repository, the generator is now in a subfolder 'pyfbsdk-stub-generator'

## [2026.0.0]

### Generator:
- This is no longer a package on PyPI. Pip install the package using the git repository url instead.
- Threading is now used when parsing the online documentation

### Stubs:
- Added manually typed stubs: 
    - pyfbsdk_additions.pyi
    - callbackframework.pyi
- `callbackframework.FBEventSource` now have typed arguments
- Tabs are now used instead of spaces _(for a reduced file size)_
- Enums now have the metaclass `EnumMeta`
- Enums now have their correct int values
- Functions returning `None` are now typed as `-> None`
- Improved types for `FBPropertyList`'s
- Multiple type fixes


## [2025.0.0] - 2024-04-07
- Support for MotionBuilder 2025
- All arguments are now marked as positional only
- Fixed type for `FBModelPath3D.PathEndCapStyle`

## [1.0.2] - 2023-08-13

- Fixed setter types for `FBPropertyAnimatable` properties
- `FBModel.Parent` type is now an optional `FBModel`