## Jetson orin nano super 學習紀錄
##
## 書籍
# 邊緣AI - 使用 NVIDIA Jetson Orin Nano 開發具備深度學習、電腦視覺與生成式AI 功能的 ROS2 機器人
CAVEDU 出版之 Jetson Orin 系列單板電腦書籍範例與相關資源

## 作者
* 曾吉弘博士，CAVEDU教育團隊技術總監、MIT CSAIL訪問學者、國立台灣科技大學資訊工程學系助理教授(兼任)、[NVIDIA DLI大使白金級](https://www.nvidia.com/en-us/training/instructor-directory/bio/?instructorId=0038Z00002pvnqVQAQ)
* 郭俊廷，CAVEDU教育團隊資深講師、NVIDIA Jetson AI Specialist
* 楊子賢，CAVEDU教育團隊資深講師、NVIDIA Jetson AI Specialist
<img src="https://github.com/cavedunissin/edgeai_jetson_orin/blob/main/pics/ros2_cover.jpg" width="200" alt="book cover">

##
* [GITHUB](https://github.com/cavedunissin/edgeai_jetson_orin)
##
###遠端連線
* [Jetson Nano - 遠端連線](https://hackmd.io/@Yungger/Jetson-Nano-Remote)
* [解決nvidia Jetson無法遠端VNC問題](https://youyouyou.pixnet.net/blog/post/119567170)
### vnc client
* [Download TightVNC](https://www.tightvnc.com/download.php)
     * [here](https://www.tightvnc.com/download/2.8.85/tightvnc-2.8.85-gpl-setup-64bit.msi)
### vnc server
* [How to Install and Configure VNC on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04)
### vino setting:
```
 export DISPLAY=:0
 gsettings set org.gnome.Vino prompt-enabled false
 gsettings set org.gnome.Vino require-encryption false
 gsettings set org.gnome.Vino authentication-methods "['vnc']"
 gsettings set org.gnome.Vino lock-screen-on-disconnect false
 gsettings set org.gnome.Vino vnc-password $(echo -n "x123456789x"|base64)
```
## 參考
```
sudo python benchnark.py --all --csv_fite_path ortn_nano_ptm.c --nodel_dir /home/crossin/Desktop/res/benchmarking/model_engines/
```
* [Nvidia jetson系列VNC、VScode、中文輸入法，常用套件安裝大全](https://medium.com/@EricChou711/nvidia-jetson%E7%B3%BB%E5%88%97vnc-vscode-%E4%B8%AD%E6%96%87%E8%BC%B8%E5%85%A5%E6%B3%95-%E5%B8%B8%E7%94%A8%E5%A5%97%E4%BB%B6%E5%AE%89%E8%A3%9D%E5%A4%A7%E5%85%A8-4b36e49438ba)
* [技術教學文-NVIDIA® Jetson Orin Nano™ 開發者套件 如何升級“Super” 模式](https://blog.cavedu.com/2025/02/14/nvidia-jetson-orin-nano-super/)
* [RAG AI](https://www.ragie.ai/multimodal?utm_source=substack&utm_medium=email)
* [第三章：深度學習結合視覺辨識應用](https://github.com/cavedunissin/edgeai_jetson_orin/blob/main/ch03/ch03.md?fbclid=IwY2xjawK_O0pleHRuA2FlbQIxMABicmlkETFkNElTdGRGVERKVHNNYnhmAR6RzS_VVJOgEgTlntWJx7vsZrC_mKcGKM0cLChZN5-Cly0n9vIDRjWn1AbXgw_aem_sCkKS3sz1KUh8CO-miyhFQ)
* ai-class01 123456
