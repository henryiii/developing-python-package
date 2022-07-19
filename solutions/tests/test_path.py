import example_package

import pytest
import contextlib
import io
from pathlib import Path


def test_no_write(monkeypatch):
    out = io.StringIO()
    monkeypatch.setattr(Path, "open", lambda _1, _2: contextlib.nullcontext(out))
    local = Path("never_written.txt")
    example_package.write_a_file(local)
    assert not local.exists()
    assert out.getvalue() == "Hello from write_a_file"


def test_tmp_write(tmp_path):
    tmp_file = tmp_path / "autoremove.txt"
    example_package.write_a_file(tmp_file)
    assert tmp_file.read_text() == "Hello from write_a_file"
