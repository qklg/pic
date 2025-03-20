---
title: '将我博客的图片都转换成avif'
date: 2024-03-07 16:56:22
tags: []
published: true
hideInList: false
feature: 
isTop: false
---
1 avif的好处
=================
avif最大的好处就是更高的压缩性，从而省流量和存储
我的博客已经是纯静态化的了，主要的大头是图片，变小可以更加快的打开博客
之前的png格式的，现在转换成avif，大小只有原来21%
![](https://s3.qklg.net/img/202403071657600.png)
![](https://s3.qklg.net/img/202403071657238.png)

压缩性比webp更加好

2主流浏览器已经支持
=================
Microsoft Edge在从2024年1月开始的121版本也开始支持了
其他的浏览器safari和firefox也早就支持了
chrome的话早在2020年的chrome85就支持了

具体支持度可以看这个
<https://caniuse.com/?search=avif>

3用ffmpeg转换
=================
```
 for %%i in ("D:\blog\png\*.png") do ffmpeg -i "%%i" -c:v av1 -strict experimental -b:v 0 -crf 30 "D:\blog\avif\%%~ni.avif"
```

将我D:\blog\png下的png文件全转成了avif

4更多
=================
如果你想更加了解avif的话
<https://blog.cloudflare.com/generate-avif-images-with-image-resizing>
<https://developer.aliyun.com/article/1147111>



