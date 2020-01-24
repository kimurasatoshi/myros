# 2019ロボットシステム学 課題 2 
# 概要  
mileで入力された数字を㎞になおす
## 手法  
### インストール手順
```
$ git clone https://github.com//myled.git
$ cd myled
$ make
$ sudo insmod myled.ko
$ sudo chmod 666 /dev/myled0
```    
## 実行
```
$ echo 1 > /dev/myled0
$ echo 2 > /dev/myled0
$ echo 3 > /dev/myled0
```  
## youtube
https://www.youtube.com/watch?v=W2laKTXbIjQ
