# 数据收集脚本

### `CpuMemPlot.py`数据收集-shell脚本

```shell
# 每10秒收集一下数据，将数据写入cpu_mem_data文件，将脚本写入cpu_mem_collect.sh 

echo "while Ture; do top -m 3 -n 1 >> /data/local/tmp/cpu_mem_data; sleep 10; done" > /data/local/tmp/cpu_mem_collect.sh 
chmod +x ./cpu_mem_collect.sh   # 改为可执行文件
./cpu_mem_collect.sh &          # 后台执行

```

### `faceImageQulity.py` 统计图片质量分配概率

根据logcat输出的文件，筛选人脸质量数据，然后调用方法统计



### `base64_get_image.py`将base64数据转化为图片



### `url_get_image.py`根据url获取人脸图片

根据人脸照片的存放路径，获取人脸图像并且保存到本地指定地点



### `csv_data_create.py`解决jemter压测的数据依赖