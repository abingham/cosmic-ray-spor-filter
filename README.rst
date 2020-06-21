======================
cosmic-ray-spor-filter
======================

Spor-based filter for Cosmic Ray mutation testing.

The filter scans a Cosmic Ray session, looking for spor anchors attached to files in the session. If it finds an anchor
with the metadata `{mutate: False}`, then that mutation is marked as "skipped".

Example
=======

Assume you've got a directory structure like this::

  project_root/
      .spor/
         ...anchors...
      cr-session.sqlite
      src/
         ...project source...

If you run this command::

  cosmic-ray-spor-filter cr-session.sqlite

will look at each job scheduled in `cr-session.sqlite`. If the file referenced in job has an anchor in the `.spor`
directory *and* if that anchor has `{mutate: False}` in its metadata, then that job will be skipped.

