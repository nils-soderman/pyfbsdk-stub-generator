from . import table_of_contents, requests_cache, parser


class Documentation:
    def __init__(self, module_name: str, version: int, use_cache: bool = False) -> None:
        self.module_name = module_name
        self.version = version
        self.use_cache = use_cache

        self.table_of_contents = table_of_contents.get_table_of_contents_python(module_name,
                                                                                version,
                                                                                use_cache)

    def parse_page(self, name: str) -> parser.ParsedPage | None:
        if url := self.table_of_contents.get(name):
            html = requests_cache.get_request(url, use_cache=self.use_cache)
            return parser.parse_page(name, html, url)

        return None
