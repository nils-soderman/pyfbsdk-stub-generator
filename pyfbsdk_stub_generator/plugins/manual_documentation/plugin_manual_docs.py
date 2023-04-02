from ..plugin import PluginBaseClass

class PluginManualDocs(PluginBaseClass):
    ...



def _PatchFromManualDocumentation(self):
        """
        Patch the StubClasses & StubFunctions based on the 'manual_documentation.py' file.
        """
        def _ParseManualDocumentation(Doc: str):
            # Remove tabs
            if "\n" in Doc:
                Doc = Doc.replace("\t", TAB_CHARACTER)
                Doc = Doc.replace("    ", TAB_CHARACTER)
                Lines = Doc.split("\n")
                Num = min(x.count(TAB_CHARACTER, 0, len(x) - len(x.lstrip())) for x in Lines[1:] if x)
                NewDoc = ""
                for Line in Lines:
                    if Num and Line.startswith(TAB_CHARACTER * Num):
                        Line = Line.partition(TAB_CHARACTER * Num)[2]
                    NewDoc += f"{Line}\n"
                Doc = NewDoc

            return Doc

        def _GetTypeHintString(TypeHint):
            if IS_PYTHON_39 and isinstance(TypeHint, typing._UnionGenericAlias):  # pylint: disable=protected-access
                return typing.get_args(TypeHint)[0].__name__
            if inspect.isclass(TypeHint):
                return TypeHint.__name__
            return str(TypeHint)

        def _PatchFunction(Function: StubFunction, DocumentedFunction: FunctionType):
            if DocumentedFunction.__doc__:
                Function.DocString = _ParseManualDocumentation(DocumentedFunction.__doc__)
            TypeHints = typing.get_type_hints(DocumentedFunction)
            StubParameters = Function.GetParameters()
            DocumentedSignature = inspect.signature(DocumentedFunction)

            for i, ParameterName in enumerate(DocumentedSignature.parameters):
                StubParam = StubParameters[i]
                Parameter = DocumentedSignature.parameters[ParameterName]
                StubParam.Name = ParameterName

                TypeHint = TypeHints.get(ParameterName)
                if TypeHint:
                    StubParam.Type = _GetTypeHintString(TypeHint)

                # Default values
                if Parameter.default is not inspect._empty:  # pylint: disable=protected-access
                    if "pyfbsdk" in str(type(Parameter.default)):
                        StubParam.DefaultValue = f"{type(Parameter.default).__name__}.{Parameter.default}"
                    else:
                        StubParam.DefaultValue = str(Parameter.default)

            if "return" in TypeHints:
                Function.ReturnType = _GetTypeHintString(TypeHints["return"])

        # Patch classes
        for Name, Object in inspect.getmembers(manualDoc, inspect.isclass):
            TypeHints = typing.get_type_hints(Object, localns = locals())
            StubClassRef = self.GetClassByName(Name)
            ClassMembers = dict(inspect.getmembers(Object))
            if StubClassRef:
                if Object.__doc__:
                    StubClassRef.DocString = _ParseManualDocumentation(Object.__doc__)

                # Patch properties
                for ClassMemberName, TypeHint in TypeHints.items():
                    StubPropertyRef = StubClassRef.GetPropertyByName(ClassMemberName)
                    if StubPropertyRef:
                        # Set type hint & doc string
                        StubPropertyRef.Type = _GetTypeHintString(TypeHint)
                        DocString = ClassMembers.get(f"{ClassMemberName}__doc__")
                        if DocString:
                            StubPropertyRef.DocString = _ParseManualDocumentation(DocString)

                PatchedStubFunctions = []
                for FunctionName, Function in inspect.getmembers(Object, inspect.isfunction):
                    bOverloadedFunction = re.search(r"_\d+$", Function.__name__)
                    if bOverloadedFunction:
                        FunctionName = FunctionName.rpartition("_")[0]
                    StubFunctionReferences = StubClassRef.GetFunctionsByName(FunctionName)
                    if StubFunctionReferences:
                        StubFunc = StubFunctionReferences[0]
                        if len(StubFunctionReferences) > 1:
                            Matches = [x for x in StubFunctionReferences if x not in PatchedStubFunctions and len(x.GetParameters()) == len(inspect.signature(Function).parameters)]
                            if not Matches:
                                continue
                            StubFunc = Matches[0]
                        _PatchFunction(StubFunc, Function)

                        PatchedStubFunctions.append(StubFunc)

        # Patch functions
        for Name, Object in inspect.getmembers(manualDoc, inspect.isfunction):
            StubFunctionRef = self.GetFunctionsByName(Name)
            if StubFunctionRef:
                _PatchFunction(StubFunctionRef[0], Object)
