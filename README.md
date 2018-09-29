# BitCoin-PrivateKeys-Database
Implementation of Bitcoin Private keys Generator web with Django
使用Django搭建的一个比特币私钥“数据库”Web，私钥由range实时生成

运行环境python3+，不支持python2，因为python2的range不支持too long的大数
请安装好requirement.txt中的module后，在项目根路径下使用<python3 manage.py runserver>启动web服务

查询生成的比特币地址的余额，在KeyToAdd.py中定义了blockchain.info的免费API查询，在btc_api.py中定义了btc.com的免费API接口 

由于API查询的速度非常缓慢，目前默认！是将含有2000多万个比特币余额的地址放在了mysql的prikeys数据库中，如果使用数据库匹配生成的比特币地址，请在models迁移创建表后，导入比特币地址，然后将address字段添加索引

目前每页显示比特币私钥和地址是200个，网页反应在2～3秒，可以在views中修改显示数量， 在导航栏的"没有余额" 指的是整页200个地址都没有余额，如果其中有一个地址有的话会显示"此页可能有余额"，在地址的balance中会显示"可能有余额"。这是指地址在数据库中匹配到了。"可能"是指这个数据库并不是实时的，比特币地址的余额可能已经发生了变动！

注意：此Demo仅供娱乐，找到含有比特币余额的地址的概率几乎为0！

截图：
![image](https://github.com/isGuowang/BitCoin-PrivateKeys-Database/tree/master/screenshot/01.png)
