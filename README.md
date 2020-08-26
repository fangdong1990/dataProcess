# 数据收集脚本

### `CpuMemPlot.py`数据收集-shell脚本

```shell
# 每10秒收集一下数据，将数据写入cpu_mem_data文件，将脚本写入cpu_mem_collect.sh 

echo "while Ture; do top -m 3 -n 1 >> /data/local/tmp/cpu_mem_data; sleep 10; done" > /data/local/tmp/cpu_mem_collect.sh 
chmod +x ./cpu_mem_collect.sh   # 改为可执行文件
./cpu_mem_collect.sh &          # 后台执行

```

