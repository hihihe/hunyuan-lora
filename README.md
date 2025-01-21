# Civitai模型下载工具

这是一个用于从Civitai下载模型文件的命令行工具。支持下载Loras、Checkpoints等模型文件。

## 功能特点

- 支持直接从Civitai链接下载模型
- 自动提取文件名（也可手动指定）
- 自动创建目标文件夹
- 支持自定义保存路径
- 内置默认token，无需配置即可使用

## 使用方法

### 基础用法

最简单的使用方式，只需提供Civitai下载链接：

    python civitai_downloader.py "https://civitai.com/api/download/models/1274571"

### 指定文件名

如果想自定义保存的文件名：

    python civitai_downloader.py "https://civitai.com/api/download/models/1274571" "Lisa_62.safetensors"

### 高级选项

脚本支持以下可选参数：

- `-f, --folder`: 指定保存文件夹（默认: models/loras）
- `-t, --token`: 自定义Civitai API token
- `-b, --base-path`: 指定基础路径（默认: /data3/ComfyUI）

例如：

    # 保存到不同文件夹
    python civitai_downloader.py "https://civitai.com/api/download/models/1274571" -f "models/checkpoints"

    # 使用自定义token
    python civitai_downloader.py "https://civitai.com/api/download/models/1274571" -t "你的token"

    # 指定基础路径
    python civitai_downloader.py "https://civitai.com/api/download/models/1274571" -b "/path/to/comfyui"

## 默认配置

- 默认保存路径：`/data3/ComfyUI/models/loras/`
- 默认token已内置，一般情况下无需修改
- 文件名如未指定，将自动从下载链接中提取
- 所有下载的文件都会自动添加.safetensors后缀（如果没有的话）

## 注意事项

- 确保有足够的磁盘空间
- 确保有稳定的网络连接
- 文件名必须以.safetensors结尾
- 下载完成后会显示✅标记 