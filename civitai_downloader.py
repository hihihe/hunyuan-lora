import argparse
import os
import warnings
warnings.filterwarnings('ignore')

def download_from_civitai(url, folder="models/loras", name=None, 
                         token="07d88b0075ca90f7807366ed6bdb426c", 
                         base_path="/data3/ComfyUI"):
    """从Civitai下载模型文件
    
    Args:
        url: Civitai下载链接
        folder: 保存的目标文件夹 (默认: models/loras)
        name: 文件名，如果为None则从URL中提取
        token: Civitai API token
        base_path: ComfyUI的基础路径
    """
    if name is None:
        # 从URL中提取文件名
        name = url.split('/')[-1].split('?')[0]
        if not name.endswith('.safetensors'):
            name += '.safetensors'
    
    model_url = f"{url}&token={token}"
    save_path = f"{base_path}/{folder}/{name}"
    
    # 确保目标文件夹存在
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # 使用wget下载文件
    os.system(f'wget -O "{save_path}" "{model_url}"')
    print(f"文件： {name}")
    print("下载完成✅")

def main():
    parser = argparse.ArgumentParser(description='从Civitai下载模型文件的工具')
    # 位置参数
    parser.add_argument('url', help='Civitai下载链接')
    parser.add_argument('name', nargs='?', default=None, help='文件名 (可选，默认从URL提取)')
    
    # 可选参数
    parser.add_argument('-f', '--folder', default="models/loras", 
                       help='保存的目标文件夹 (默认: models/loras)')
    parser.add_argument('-t', '--token', default="07d88b0075ca90f780ed6bdb426c", 
                       help='Civitai API token')
    parser.add_argument('-b', '--base-path', default="/data3/ComfyUI", 
                       help='ComfyUI的基础路径')
    
    args = parser.parse_args()
    
    if args.name and not args.name.endswith('.safetensors'):
        print("错误: 文件名必须以.safetensors结尾")
        return
    
    try:
        download_from_civitai(
            url=args.url,
            folder=args.folder,
            name=args.name,
            token=args.token,
            base_path=args.base_path
        )
    except Exception as e:
        print(f"下载过程中发生错误: {str(e)}")

if __name__ == "__main__":
    main() 