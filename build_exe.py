import os
import PyInstaller.__main__

print("开始打包应用程序...")

PyInstaller.__main__.run([
    'timer.py',
    '--onefile',
    '--noconsole',
    '--name=ScreenTimer',
    '--icon=NONE',
    '--add-data=README.md;.'
])

print("打包完成！")
print("可执行文件位于 dist 文件夹中")
