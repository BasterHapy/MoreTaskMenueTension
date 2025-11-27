# This is an extension based on the official Task Menu Extension example project  
It primarily addresses how to enable `pyside6-designer` to load **task menu extensions** across different terminal environments.

[简体中文](./README.cn.md)
## Official Demo  
[Task Menu Extension Example](https://doc.qt.io/qtforpython-6/examples/example_designer_taskmenuextension.html)

## How to Use  
Check your terminal environment. Currently supported terminals include `cmd`, `bash`, and `PowerShell` (you can see which one you're using in the top-right corner of the VS Code terminal).

Before running `pyside6-designer`, execute the corresponding `pyside_designer_plugins` script for your terminal:

| Terminal Environment | Corresponding File |
|----------------------|--------------------|
| cmd                  | `scripts\pyside_designer_plugins.bat` |
| bash                 | `scripts/pyside_designer_plugins.sh` |
| PowerShell           | `scripts\pyside_designer_plugins.ps1` |

### Usage Examples

```bash
# bash
source scripts/pyside_designer_plugins.sh
```

```cmd
# cmd
scripts\pyside_designer_plugins.bat
```

```powershell
# PowerShell
.\scripts\pyside_designer_plugins.ps1
```