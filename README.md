# man 页

FreeBSD man 页。

当前来源：https://github.com/freebsd/freebsd-src

当前版本：bcb471cfb499f61d98abdc7bfd48bee0e229b02b

源代码路径：**share/man**

```sh
tar xvf src.txz usr/src/lib/libc/*.[23]    # 解压 man2，man3
mv usr/src/lib/libc libc          # 降低目录层级
rm -rf usr
find libc -name *.[23] > content.list    # 向 content.list 写入 man2，man3 路径
cat content.list | sed -e 's/libc\///' -e 's/\/.*$//' | uniq |sort > level1.list
```

本项目遵循 [BSD 2-Clause 许可证](LICENSE)。
