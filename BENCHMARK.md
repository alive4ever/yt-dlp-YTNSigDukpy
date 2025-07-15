# Performance comparison between dukpy and built in interpreter

## dukpy performance against built-in interpreter

Benchmark script.

```python
import dukpy
import json
from yt_dlp import jsinterp
nsig_cache = '.cache/yt-dlp/youtube-nsig/69b31e11-main.json'
with open(nsig_cache, 'r') as file:
    nsig_cache_dict = json.load(file)
test_signature = 'abcdefghijklmn'
args, func_body = nsig_cache_dict['data']
nsig_code = f"var decrypt_nsig = function({ ', '.join(args)}) {{ { func_body } }}; decrypt_nsig( {test_signature!r} );"
get_ipython().run_line_magic('timeit', 'dukpy.evaljs(nsig_code)')
jsi = jsinterp.JSInterpreter(nsig_code)
get_ipython().run_line_magic('timeit', "jsi.call_function('decrypt_nsig', test_signature)")
```

## Result

```
# dukpy
8.28 ms ± 1.05 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
# jsinterp
1.83 s ± 173 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

About 221× speedup.

