import os
from optparse import OptionParser


# 火山引擎对象存储工具
tosutil = './tosutil'


# 原始config文件
origin_tosutil_config = './.tosutilconfig'


def download(url_path, output_dir, config_file):
    
    # 创建存储点
    os.makedirs(output_dir, exist_ok=True)

    
    # 下载文件
    download_cli = f"""
    
    {tosutil} cp -r {url_path} {output_dir} -conf {config_file}
    
    """

    os.system(download_cli)


def config(config_file=None, endpoint=None, region=None, access_key_id=None, secret_access_key=None, token=None):
    
    # 拷贝一份原始config文件，然后基于该文件进行更新
    if not os.path.exists(config_file):
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        os.system(f"cp {origin_tosutil_config} {config_file}")

    # 更新配置文件
    update_conf_cli = f"""
    
    {tosutil} config -conf={config_file} -e={endpoint} -re={region} -i={access_key_id} -k={secret_access_key}
    
    """

    if token:
       update_conf_cli += f" -t {token}"

    os.system(update_conf_cli)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--i', dest='url_path', help="tos路径")
    parser.add_option('--o', dest='output_dir', help="存储点")
    parser.add_option('--c', dest='config_file', help="存放的配置文件")
    #parser.add_option('--new', dest='isnew_config', action_store='true', help="是否为新创建的配置文件")
    parser.add_option('--e', dest='endpoint', default=None, help="Endpoint")
    parser.add_option('--re', dest='region', default=None, help="Region")
    parser.add_option('--ak', dest='access_key_id', default=None,  help=" Access Key ID")
    parser.add_option('--sk', dest='secret_access_key', default=None, help="Secret Access Key")
    parser.add_option('--t', dest='token', default=None, help="Token")

    options, args = parser.parse_args()

    if any((options.endpoint, options.region, options.access_key_id, options.secret_access_key)):
        config(
            config_file=options.config_file, 
            endpoint=options.endpoint, 
            region=options.region, 
            access_key_id=options.access_key_id, 
            secret_access_key=options.secret_access_key, 
            token=options.token
            )
    
    download(
            url_path=options.url_path, 
            output_dir=options.output_dir, 
            config_file=options.config_file
            )
