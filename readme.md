# 微信小程序小区心愿地图
## 框架
- wepy 1.6.0 
- weui-wxss 1.1.1
## 开发方式
#### 安装（更新） wepy 命令行工具。
```console
npm install wepy-cli -g
```
#### clone 项目
```
    git clone  https://github.com/cfc2018/wx-cdWant.git
    cd wx-cdWant
    npm install
```

#### 开发实时编译

```console
wepy build --watch
```
#### 安装微信调试工具
https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html?t=1515507318

#### 设置微信调试工具

1. 使用`微信开发者工具`新建项目，本地开发选择`dist`目录。

2. `微信开发者工具`-->项目-->关闭ES6转ES5。<font style="color:red">重要：漏掉此项会运行报错。</font>

3. `微信开发者工具`-->项目-->关闭上传代码时样式自动补全 <font style="color:red">重要：某些情况下漏掉此项会也会运行报错。</font>

4. `微信开发者工具`-->项目-->关闭代码压缩上传 <font style="color:red">重要：开启后，会导致真机computed, props.sync 等等属性失效。[#270](https://github.com/wepyjs/wepy/issues/270)</font>

5. 项目根目录运行`wepy build --watch`，开启实时编译。

   ​

![img](https://image.ibb.co/jFQE46/20180109225526.png)