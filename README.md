# yt-nsig-dukpy

## Description

A yt-dlp plugin to use `duktape` js engine to execute nsig code in place of built-in `jsinterp`.

## Usage

Install the plugin.

```
pip install .
```

With the plugin installed, `yt-dlp` automatically uses `dukpy` as python binding to `duktape` js engine to execute nsig function.

To revert back using built-in `jsinterp`:

```
pip uninstall yt-nsig-dukpy
```

## Performance comparison

See [benchmark](BENCHMARK.md)

tl,dr: about 221× speedup against built-in `jsinterp`.
