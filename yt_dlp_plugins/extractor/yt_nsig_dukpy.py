import dukpy
from yt_dlp.extractor.youtube import YoutubeIE

class Youtube_NsigDukpyIE(YoutubeIE, plugin_name='NSigDukpy'):
    def _extract_n_function_from_code(self, jsi, func_code):
        args, func_body = func_code
        def extract_nsig(s):
            jscode = f'var decrypt_nsig=function({", ".join(args)}) {{ {func_body} }};decrypt_nsig({s!r});'
            result = dukpy.evaljs(jscode)
            self.write_debug(f'Executing nsig via dukpy, n = {s}, result = {result}')
            if result.startswith('enhanced_except_') or result.endswith(s):
                raise Exception('Signature function returned an exception')

            return result
        return extract_nsig

__all__ = []
