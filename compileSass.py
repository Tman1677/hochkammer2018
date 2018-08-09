#!/usr/bin/env python
import sass
import os
sass.compile(dirname=('bootstrap-4.1.3/scss', 'css-min'), output_style='compressed')
sass.compile(dirname=('scss', 'css-min'), output_style='compressed')
