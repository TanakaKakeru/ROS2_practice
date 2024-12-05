import rclpy        #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

### ヘッダの下にTalkerというクラスを作成 ###
class Talker(Node):   #ヘッダの下にTalkerというクラスを作成
    def __init__(self): #Nodeというクラスの機能を受け継いだクラスにな
        super().__init__("takler") #Nodeのオブジェクトとしての初期化
        self.pub = self.create_publisher(Int16, "countup", 10)  #selfはオブジェクトのこと
        self.create_timer(0.5, self.cb)  #ここでタイマーをしかける。
        self.n = 0   #オブジェクトにひとつパブリッシャと変数をもたせる。

    def cb(self):  #コールバックのメソッド
        msg = Int16()
        msg.data = self.n   #属性には必ずselfをつける
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)