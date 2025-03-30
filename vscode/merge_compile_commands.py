#!/usr/bin/env python3

import os
import json
import glob
from pathlib import Path

def merge_compile_commands():
    """
    合并所有包中的compile_commands.json文件到工作区根目录
    """
    workspace_dir = os.getcwd()
    print(f"工作区目录: {workspace_dir}")
    
    # 创建输出目录
    output_dir = os.path.join(workspace_dir, "compile_output")
    os.makedirs(output_dir, exist_ok=True)
    
    # 查找所有编译命令文件
    compile_commands_files = glob.glob(os.path.join(workspace_dir, "build/*/compile_commands.json"))
    print(f"找到 {len(compile_commands_files)} 个编译命令文件")
    
    # 合并所有编译命令
    all_commands = []
    for file_path in compile_commands_files:
        package_name = file_path.split('/')[-2]
        print(f"处理包: {package_name}")
        
        try:
            with open(file_path, 'r') as f:
                commands = json.load(f)
                
            # 为每个命令创建一个单独的输出文件
            for cmd in commands:
                # 修复文件路径为绝对路径
                if not os.path.isabs(cmd.get('file', '')):
                    cmd['file'] = os.path.abspath(os.path.join(os.path.dirname(file_path), cmd['file']))
                
                # 更新编译目录为工作区根目录
                cmd['directory'] = workspace_dir
                
                # 保存到输出文件
                file_basename = os.path.basename(cmd.get('file', 'unknown'))
                output_file = os.path.join(output_dir, f"{package_name}_{file_basename}.json")
                with open(output_file, 'w') as f:
                    json.dump([cmd], f, indent=2)
                
                all_commands.append(cmd)
                
        except Exception as e:
            print(f"处理 {file_path} 时出错: {e}")
    
    # 保存合并后的编译命令到根目录
    combined_path = os.path.join(workspace_dir, "compile_commands.json")
    with open(combined_path, 'w') as f:
        json.dump(all_commands, f, indent=2)
    
    print(f"合并完成! 总共 {len(all_commands)} 条编译命令")
    print(f"合并的编译命令保存到: {combined_path}")
    print(f"单独的编译命令保存到: {output_dir}")

if __name__ == "__main__":
    merge_compile_commands()