#!/usr/bin/env python

import os
import re
import sys
import json
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


class JupyterNotebook(object):
    """
    A simple Jupyter notebook class with some methods to operate on it.

    This should be mainly helpful for renumbering cell execution counters
    or for making them empty, or for deleting an entire section of the
    notebook (possibly containing subsections) specified by its initial
    MarkDown cell with some title in it.

    All methods but find_section_startend_indices() return self and can
    be chained.
    """
    def __init__(self, path):
        """
        Construct a notebook from a file in JSON format.
        """
        self.path = path
        with open(path) as f:
            self.nb = json.load(f)

    def save(self, path='', name_suffix=''):
        """
        Save to a notebook file (JSON).

        The order of fields inside a JSON object (a Python dict) might change.
        """
        msg = "Cannot accept `path` and `name_suffix` parameters together."
        assert not (path and name_suffix), msg

        if name_suffix:
            base, ext = os.path.splitext(self.path)
            path = base + name_suffix + ext
        with open(path or self.path, 'w') as f:
            json.dump(self.nb, f, indent=1)
        return self

    def renumber_cells(self, empty=False):
        """
        Renumber all cell execution counters from 1, or set empty.

        This can be useful as a last step before publishing a notebook.
        """
        cnt = 1
        for cell in self.nb['cells']:
            if cell["cell_type"] == "code":
                # set counter for input cell
                cell["execution_count"] = cnt if not empty else None
                # set counter for output cell(s?)
                for out in cell.get("outputs", []):
                    if "execution_count" in out:
                        out["execution_count"] = cnt if not empty else None
                cnt += 1
        return self

    def clear_cells_numbering(self):
        """
        Clear all cell execution counters.
        """
        self.renumber_cells(empty=True)
        return self

    def clear_all_output_cells(self):
        """
        Clear all output cells in notebook so people can rerun a clean version.
        """
        for cell in self.nb['cells']:
            if cell["cell_type"] == "code" and "outputs" in cell:
                cell["outputs"] = []
        return self

    def list_cells(self):
        """
        List beginning of all cells, mainly for debugging.
        """
        for i, cell in enumerate(self.nb['cells']):
            ct = cell["cell_type"]
            if "source" in cell and len(cell["source"]) > 0:
                src0 = cell["source"][0]
            else:
                srs0 = None
            print("{} {} {}".format(i, ct, src0))
        return self

    def find_section_startend_indices(self, title_pat):
        """
        Return start/end indices of first section with some desired title.

        Markdown titles start with a number of #. This method should delete
        subsections (more # at the start) until but not including the next
        section with the same number (or less) of # or (if not existing)
        the end of the notebook.

        Returns the indices betweem the first cell (included) and the last
        cell (not included) that have been removed, or (-1, -1) if nothing
        was found to be removed.
        """
        assert title_pat.startswith('#')

        start_level = re.search("^#+", title_pat).end()
        cells = self.nb['cells']

        # Find desired markdown cell or return.
        start = -1
        for i, cell in enumerate(cells):
            if cell["cell_type"] != "markdown":
                continue
            if re.match(title_pat, cell["source"][0]):
                start = i
                break
        if start == -1:
            return -1, -1

        # Find next markdown cell (same/higher level title) or end of notebook.
        end = -1
        for i, cell in enumerate(cells[start + 1:]):
            if cell["cell_type"] != "markdown":
                continue
            first_line = cell["source"][0]
            if first_line.startswith("#"):
                level = re.search("^#+", first_line).end()
                if level <= start_level:
                    end = start + i + 1
                    break
        if end == -1:
            end = len(cells) - 1

        return start, end

    def remove_section(self, title_pat):
        """
        Remove first section with some title until some next title or the end.

        Markdown titles start with a number of #. This method should delete
        subsections (more # at the start) until but not including the next
        section with the same number of # or (if not existing) the end of
        the notebook.

        Removes the section if found, else does nothing.
        """
        start, end = self.find_section_startend_indices(title_pat)
        if (start, end) != (-1, -1):
            del self.nb["cells"][start:end]

        return self

def remove_section(filepath, title_pat):
    path = os.path.join(PROJECT_DIRECTORY, filepath)
    nb = JupyterNotebook(path).remove_section(title_pat).save(path)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{ cookiecutter.json4s_version }}" == '-':
        remove_file("src/test/scala/TestJson.scala")
        remove_section("notebooks/tutorial.ipynb", "## Json4S")

    if "{{ cookiecutter.scalapb_compilerplugin_version }}" == '-':
        remove_file("src/test/scala/TestProtobuf.scala")
        remove_file("project/scalapb.sbt")
        remove_dir("src/main/protobuf")
        remove_section("notebooks/tutorial.ipynb", "## Protobuf")

    if "{{ cookiecutter.sbt_assembly_version }}" == '-':
        remove_file("project/assembly.sbt")
        remove_file("assembly.sbt")
