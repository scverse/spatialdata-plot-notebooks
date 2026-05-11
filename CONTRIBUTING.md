# Contributing

Thanks for contributing a notebook to the `spatialdata-plot` gallery.

## Setup

```bash
git clone https://github.com/scverse/spatialdata-plot-notebooks.git
cd spatialdata-plot-notebooks
pip install -e ".[exec,dev]"
pre-commit install
```

## Adding a notebook

1. Decide the type:
   - **`tutorials/<topic>.ipynb`** — end-to-end workflow on a real dataset
     (Visium, Xenium, MERFISH, …). Focuses on a complete analysis story.
   - **`examples/<group>/<topic>.ipynb`** — short, single-feature notebook
     (e.g., `examples/customization/outlines.ipynb`). Focuses on one technique.

2. Start the notebook with a markdown cell containing:
   - A title (`# ...`).
   - 2-3 sentences on what the reader will learn.
   - A dataset citation when applicable.

3. Use `squidpy.datasets.*` or `spatialdata.datasets.*` for data — never raw
   URLs. Both libraries cache via `pooch`, so first-run downloads are cheap on
   re-runs.

4. Re-execute the notebook end-to-end (Restart Kernel & Run All) and commit
   with outputs. The `spatialdata-plot` docs build performs no execution; what
   you commit is what users see rendered.

5. Add the notebook to the appropriate `index.md` so it appears in the gallery
   toctree.

6. Open a PR. CI will:
   - Lint structure and code (`lint.yaml`).
   - Re-execute the notebook against the latest `spatialdata-plot` release
     and diff outputs (`execute.yaml`).

## Updating an existing notebook

Edit, re-execute, commit. CI catches output drift on the next scheduled run if
you forget.

## What not to commit

- Raw datasets (use `squidpy.datasets` / `spatialdata.datasets`).
- Notebooks larger than ~5 MB after execution — open an issue first; we may
  need git-lfs or a downsampled variant.
- Cells that depend on local files outside the repo.

## Questions

Open an issue or ping in [scverse Zulip](https://scverse.zulipchat.com).
