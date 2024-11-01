import os


if __name__ == '__main__':
    # 配置文件未产生/需要更新配置文件，下载文件的示例
    os.system(f"python ~/software/tosutil/tosutil_download.py\
            --i tos://skyseq-product-tos/0012v00002ONfrfAAD/JYTK-20241021-L-01-2024-10-240923 \
            --o ./test/ \
            --c ./tosutil_ssh_key_passwod/.20241031_tosutilconfig \
            --e https://tos-cn-shanghai.volces.com \
            --re cn-shanghai \
            --ak AKLTMWFlNTdjOGNjMjVhNGI1ZDkyODU1OTYzYzk3MDA2Mzk \
            --sk TnpnNE1qYzNaRFJqWVRJME5ERm1PVGc0TURJeU16TXhNamcyWlRJeU5UWQ=="
            )
    # 已有配置文件，下载文件的示例
    os.system(f"python ~/software/tosutil/tosutil_download.py \
            --i tos://skyseq-product-tos/0012v00002ONfrfAAD/JYTK-20241025-L-01-2024-10-310113 \
            --o ./test/ \
            --c ./tosutil_ssh_key_passwod/.20241031_tosutilconfig "
            )
