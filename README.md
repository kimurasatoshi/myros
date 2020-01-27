# 2019ロボットシステム学 課題 2 
# 概要  
体重と身長を入力してそこからBMIを出力するパッケージ  
体重と身長をrostopicとしてパブリッシュして別ノードでサブスクライブして，BMIを算出してパブリッシュする
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
`$ rosrun myros weight_height.py`  
端末３  
`$ rosrun myros bmi.py`
## YouTube
https://www.youtube.com/watch?v=DYvo__qwgD8



## LICENSE  
This repository is licensed under the BSD-3-Clause license, see LICENSE.
