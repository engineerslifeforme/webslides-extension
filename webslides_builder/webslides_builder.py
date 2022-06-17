from os import path
from typing import Any, Dict, Iterator, Set, Tuple
import shutil
from pathlib import Path

from docutils.io import StringOutput
from docutils.nodes import Node
from sphinx.builders import Builder
from sphinx.util.osutil import ensuredir, os_path

from .webslides_writer import WebslidesWriter, WebslidesTranslator

class WebslidesBuilder(Builder):
    name = 'webslides'
    default_translator_class = WebslidesTranslator
    out_suffix = '.html'

    def get_outdated_docs(self) -> Iterator[str]:
        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                yield docname
                continue
            targetname = path.join(self.outdir, docname + self.out_suffix)
            try:
                targetmtime = path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = path.getmtime(self.env.doc2path(docname))
                if srcmtime > targetmtime:
                    yield docname
            except OSError:
                # source doesn't exist anymore
                pass

    def prepare_writing(self, docnames: Set[str]) -> None:
        self.writer = WebslidesWriter(self)

    def write_doc(self, docname: str, doctree: Node) -> None:
        self.current_docname = docname
        self.secnumbers = self.env.toc_secnumbers.get(docname, {})
        destination = StringOutput(encoding='utf-8')
        self.writer.write(doctree, destination)
        outfilename = path.join(self.outdir, os_path(docname) + self.out_suffix)
        ensuredir(path.dirname(outfilename))
        try:
            with open(outfilename, 'w', encoding='utf-8') as f:
                f.write(self.writer.output)
        except OSError as err:
            logger.warning(__("error writing file %s: %s"), outfilename, err)
        static_dir_destination = Path(self.outdir) / 'static'
        if not static_dir_destination.exists():
            source_dir = Path(self.srcdir) / '_static'
            shutil.copytree(source_dir, static_dir_destination)

    def get_target_uri(self, docname: str, typ: str = None) -> str:
        return ''
