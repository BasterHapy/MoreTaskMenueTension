# 这是一个基于官方任务菜单扩展示例项目的扩展
主要解决不同终端环境来实现`pyside6-designer`读取**任务菜单扩展**

## 官网demo
[任务菜单扩展示例](https://doc.qt.io/qtforpython-6/examples/example_designer_taskmenuextension.html)

## 怎么使用
看看你的终端环境 如果是目前支持`cmd`、`bash`、`powershell`(可以在vscode终端的右侧看到)

在运行`pyside6-designer`之前，运行对应的`pyside_designer_plugins`脚本

| 终端环境 | 对应文件 |
| ----- | ----- |
| cmd | scripts\pyside_designer_plugins.bat |
| bash | scripts/pyside_designer_plugins.sh |
| powershell | scripts\pyside_designer_plugins.ps1 |

运行示例
```bash
# bash
source scripts/pyside_designer_plugins.sh
```
```cmd
# cmd
scritps\pyside_designer_plugins.bat
```
```powershell
#powershell
 .\scritps\pyside_designer_plugins.ps1
```