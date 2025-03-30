# vscode-ros2-clang
## 介绍
这是使用vscode进行ros2的智能补全与一键编译的vscode设置文件，使用该文件编译之后会生成compile_outputs文件供clangd进行解析，在较为复杂依赖的工程中能够叫好的实现跨功能包解析工作。
## 使用方法
1. 安装clang clangd python三个插件
2. 安装cmake等插件(推荐)
3. 将vscode文件夹复制到ros2工作空间中，重命名为`.vscode`，重启vscode
## 参考工作
https://github.com/homalozoa/vscode_ros2_config
