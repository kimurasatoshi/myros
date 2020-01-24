# 2019ロボットシステム学 課題 2 
# 概要  
mileで入力された数字を㎞になおす  
mileをPublishして、それをSubscribeしてkmに変換するパッケージ  
## 手法  
### インストール手順
```
$ cd ~/catkin_ws/src/
$ https://github.com/kimurasatoshi/myros.git
$ cd ../
$ catkin_make
```    
## 実行  
端末１  
`$ roscore`  
端末２  
`$ rosrun myros number.py`  
端末３  
`$ rosrun myros sub.py`
## YouTube
https://www.youtube.com/watch?v=g-EkdhKf1Po
