# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [("C:/Users/Alex/AppData/Local/Programs/Python/Python39/Lib/site-packages/streamlit/runtime", "./streamlit/runtime"),
         ("C:/Users/Alex/OneDrive/Projects/st_exe/client.py", "."),
         ("C:/Users/Alex/OneDrive/Projects/st_exe/test_app_no_menu.py", ".")
        ]
datas += collect_data_files("streamlit")
datas += copy_metadata("streamlit")


block_cipher = None


a = Analysis(
    ["run.py", "test_app_no_menu.py", "client.py"],
    pathex=["."],
    binaries=[],
    datas=datas,
    hiddenimports=["streamlit", "streamlit_extras" , "streamlit_modal", "streamlit.components.v1", "streamlit_extras.chart_container", "streamlit_extras.altex", "streamlit_extras.colored_header", "pyarrow.vendored.version"],
    hookspath=["./hooks"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
