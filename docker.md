* [在NVIDIA Jetson NANO 上使用 Docker Container 部署視覺應用](https://grady1006.medium.com/%E9%82%8A%E7%B7%A3ai%E7%B3%BB%E5%88%97-%E5%9C%A8nvidia-jetson-nano-%E4%B8%8A%E4%BD%BF%E7%94%A8-docker-container-%E9%83%A8%E7%BD%B2%E8%A6%96%E8%A6%BA%E6%87%89%E7%94%A8-1719b2062f15)
## Step0：確認你的JetPack SDK版本
```
jetson_release
```
## Step1：確認系統預先安裝好的Docker Container
```
sudo dpkg --get-selections | grep nvidia | grep container
