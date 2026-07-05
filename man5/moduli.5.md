# moduli.5

`moduli` — Diffie-Hellman 模数

## 名称

`moduli`

## 描述

**/etc/ssh/moduli** 文件包含供 sshd(8) 在 Diffie-Hellman 组交换密钥交换方法中使用的素数和生成元。

可以使用 [ssh-keygen(1)](../man1/ssh-keygen.1.md) 通过两步过程生成新的模数。第一步是 *候选生成*，使用 `ssh-keygen -G` 计算可能可用的数值。第二步是 *素性测试*，使用 `ssh-keygen -T` 提供高度保证，确认这些数值为素数并且在 Diffie-Hellman 操作中供 sshd(8) 使用是安全的。`moduli` 格式用作每一步的输出。

该文件由以换行符分隔的记录组成，每个模数一条记录，包含七个以空格分隔的字段。这些字段如下：

**0** 未知，未测试。

**2** “安全”素数；(p-1)/2 也是素数。

**4** Sophie Germain 素数；2p+1 也是素数。

**0x00** 未测试。

**0x01** 合数——非素数。

**0x02** 埃拉托斯特尼筛法。

**0x04** 概率性 Miller-Rabin 素性测试。

**timestamp** 模数上次处理的时间，格式为 YYYYMMDDHHMMSS。

**type** 指定素数模数内部结构的十进制数。支持的类型为：[ssh-keygen(1)](../man1/ssh-keygen.1.md) 最初生成的模数候选项为 Sophie Germain 素数（类型 4）。通过 [ssh-keygen(1)](../man1/ssh-keygen.1.md) 进一步素性测试后，产生可在 sshd(8) 中使用的安全素数模数（类型 2）。OpenSSH 不使用其他类型。

**tests** 十进制数，表示该数已经过的素性测试类型，以如下值的位掩码表示：[ssh-keygen(1)](../man1/ssh-keygen.1.md) 模数候选项生成使用埃拉托斯特尼筛法（标志 0x02）。随后的 [ssh-keygen(1)](../man1/ssh-keygen.1.md) 素性测试为 Miller-Rabin 测试（标志 0x04）。

**trials** 十进制数，表示已对该模数执行的素性测试次数。

**size** 十进制数，表示素数的位长度。

**generator** 用于该模数的推荐生成元（十六进制）。

**modulus** 模数本身（十六进制）。

执行 Diffie-Hellman 组交换时，sshd(8) 首先估计所需的模数大小，以产生足够的 Diffie-Hellman 输出来为选定的对称密码充分密钥化。然后 sshd(8) 从 **/etc/ssh/moduli** 中随机选择一个最符合大小要求的模数。

## 参见

[ssh-keygen(1)](../man1/ssh-keygen.1.md), sshd(8)

> “Diffie-Hellman Group Exchange for the Secure Shell (SSH) Transport Layer Protocol”, 2006.
