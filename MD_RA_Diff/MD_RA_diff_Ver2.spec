# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['MD_RA_diff_Ver2.py'],
             pathex=['C:\\Users\\party\\Desktop\\Works\\Ray-GitHub\\MD_RA_Diff'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MD_RA_diff_Ver2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
