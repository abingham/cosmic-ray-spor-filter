import subprocess
from cosmic_ray_spor_filter.filter import _line_and_col_to_offset
from cosmic_ray.work_db import WorkDB, use_db
from cosmic_ray.work_item import WorkerOutcome
from io import StringIO


conf = """[cosmic-ray]
module-path = "test.py"
python-version = ""
timeout = 10
excluded-modules = []
test-command = "python -m unittest discover tests"
execution-engine.name = "local"

[cosmic-ray.cloning]
method = 'copy'
commands = []
"""

source_code = """def foo(x):
    if x > 2:
        return x + 3
    else:
        return x - 5
"""


def test_e2e(tmp_path):
    """Basic end-to-end test.
    """
    def run(cmd, *args, **kwargs):
        subprocess.run(cmd.split(),
                       cwd=tmp_path,
                       *args, **kwargs)

    (tmp_path / "test.conf").write_text(conf)
    (tmp_path / "test.py").write_text(source_code)
    run("cosmic-ray init test.conf test.sqlite")
    run("spor init")
    run("spor add test.py 21 1 5", input=b'{"mutate": false}')
    run('cosmic-ray-spor-filter test.sqlite')

    with use_db((tmp_path / 'test.sqlite'), WorkDB.Mode.open) as db:
        skipped = [i for i, r in db.completed_work_items if r.worker_outcome == WorkerOutcome.SKIPPED]

    # We expect *some* skipped tests, though we can't be 100% how many since potentially
    # new operators will be added that create new skippable work items.
    assert len(skipped) > 0

    # Make sure each skipped entry falls in the expected range
    for item in skipped:
        assert _line_and_col_to_offset(source_code.split('\n'), *item.start_pos) == 20
        assert _line_and_col_to_offset(source_code.split('\n'), *item.end_pos) == 21
