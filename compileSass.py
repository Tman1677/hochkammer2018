import sass
import os
sass.compile(dirname=('bootstrap-4.1.3/scss', 'css-min/bootstrap'), output_style='compressed')
sass.compile(dirname=('scss', 'css-min'), output_style='compressed')
os.remove('css-min/bootstrap/bootstrap-grid.css')
os.remove('css-min/bootstrap/bootstrap-reboot.css')