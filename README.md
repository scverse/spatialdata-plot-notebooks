# spatialdata-plot-notebooks

Executable notebooks demonstrating [spatialdata-plot] on real spatial-omics
datasets. Rendered into the [spatialdata-plot documentation][docs] as a
gallery.

[spatialdata-plot]: https://github.com/scverse/spatialdata-plot
[docs]: https://spatialdata.scverse.org/projects/plot/en/latest/

## Layout

```
tutorials/   # end-to-end workflows on real datasets (Visium, Xenium, MERFISH, ...)
examples/    # short, focused notebooks demonstrating one feature at a time
```

Each notebook is committed **with outputs** so the `spatialdata-plot` docs build
performs no execution. Outputs are kept fresh by a scheduled CI job that
re-executes every notebook against the latest `spatialdata-plot` release.

## Running notebooks locally

```bash
git clone https://github.com/scverse/spatialdata-plot-notebooks.git
cd spatialdata-plot-notebooks
pip install -e ".[exec]"
jupyter lab
```

The `exec` extra pulls `spatialdata-plot`, `squidpy` (for dataset loaders),
and `jupyter`. Datasets are fetched on first run via each library's built-in
caching (`pooch`), then re-used across runs.

## Contributing a notebook

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version:

1. Add `tutorials/<topic>.ipynb` (workflow) or `examples/<group>/<topic>.ipynb`
   (focused).
2. Re-execute end-to-end and commit with outputs.
3. Add the notebook to `tutorials/index.md` or `examples/index.md`.
4. Open a PR — `lint.yaml` checks structure; `execute.yaml` re-runs notebooks
   on the PR.

## Datasets and attribution

Notebooks use public datasets distributed via `squidpy.datasets` and
`spatialdata.datasets`. Per-dataset citations live in the markdown header of
each notebook; please follow the same convention when contributing.

## License

BSD-3-Clause. See [LICENSE](LICENSE).
