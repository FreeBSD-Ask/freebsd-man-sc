# config(5)

config — OpenSSL CONF 库配置文件

## 名称

config — OpenSSL CONF 库配置文件

## 描述

本页面记录 OpenSSL 配置文件的语法，由 NCONF_load(3) 及相关函数解析。此格式被许多 OpenSSL 命令使用，并用于初始化任何应用程序所使用的库。

第一部分描述配置文件的一般语法，后续各节描述各个模块的语义。其他模块在 fips_config(5) 和 x509v3_config(5) 中描述。定义 ASN.1 值的语法在 ASN1_generate_nconf(3) 中描述。

## 语法

配置文件由一系列行组成。空行和行中元素之间的空白无意义。注释以 `#` 字符开始；该行的其余部分被忽略。如果 `#` 是行中第一个非空格字符，则整行被忽略。

### 指令

两个指令可用于控制配置文件的解析：`.include` 和 `.pragma`。

为了与旧版本的 OpenSSL 兼容，指令后的等号将被忽略。旧版本会将其视为赋值，因此如果语义差异很重要，应谨慎处理。

文件可以使用 include 语法包含其他文件：

```sh
.include [=] pathname
```

如果 pathname 是简单文件名，则该文件直接在该点包含。被包含的文件可以包含指定其他文件的 `.include` 语句。如果 pathname 是目录，则该目录中所有具有 `.cnf` 或 `.conf` 扩展名的文件都将被包含。（这仅在具有 POSIX IO 支持的系统上可用。）在 pathname 中找到的任何子目录都将被忽略。同样，如果在扫描目录时打开的文件具有指定目录的 `.include` 指令，也会被忽略。

作为一般规则，pathname 应为绝对路径；可以通过下文描述的 abspath 和 includedir pragma 来强制执行。环境变量 `OPENSSL_CONF_INCLUDE`（如果存在）会被前置到所有相对路径名之前。如果 pathname 仍然是相对路径，则基于当前工作目录解释。

要要求所有文件包含都指定绝对路径，请使用以下指令：

```sh
.pragma [=] abspath:value
```

默认行为（值为 false 或 off）是允许相对路径。要要求所有 `.include` 路径名为绝对路径，请使用值 true 或 on。

在这些文件中，美元符号 `$` 用于引用变量，如下所述。但是，在某些平台上，通常将 `$` 视为符号名中的常规字符。可以使用以下指令支持此行为：

```sh
.pragma [=] dollarid:value
```

默认行为（值为 false 或 off）是将美元符号视为指示变量名；`foo$bar` 被解释为 `foo` 后跟变量 `bar` 的展开。如果 value 为 true 或 on，则 `foo$bar` 是一个七字符的单一名称，变量展开必须使用花括号或圆括号指定。

```sh
.pragma [=] includedir:value
```

如果在 `.include` 指令中指定了相对路径名，且 `OPENSSL_CONF_INCLUDE` 环境变量不存在，则 includedir pragma 的值（如果存在）会被前置到该路径名之前。

### 设置

配置文件分为多个节。一个节以方括号中的节名开始，在新节开始时或文件结束时结束。节名可以由字母数字字符和下划线组成。名称与方括号之间的空白被删除。

配置文件的第一节是特殊的，称为默认节。此节通常未命名，从文件开头跨越到第一个命名节。当查找名称时，首先在当前或命名节中查找，必要时再在默认节中查找。

环境被映射到名为 `ENV` 的节。

节内是一系列名称/值赋值，详见下文。提醒一下，此示例中显示的方括号是必需的，不是可选的：

```sh
[ section ]
name1 = This is value1
name2 = Another value
...
[ newsection ]
name1 = New value1
name3 = Value 3
```

名称可以包含任何字母数字字符以及一些标点符号，如 `.`、`,`、`;` 和 `_`。等号之前名称后的空白被忽略。

如果同一节中名称重复，则除最后一个值外的所有值都将被忽略。在某些情况下，例如证书 DN，同一字段可能出现多次。为了支持这一点，openssl-req(1) 等命令会忽略任何以句点开头的前导文本。例如：

```sh
1.OU = First OU
2.OU = Second OU
```

值由 `=` 字符后的字符串组成，直到行尾，去除任何前导和尾随空白。

值字符串会进行变量展开。文本 `$var` 或 `${var}` 插入当前节中命名变量的值。要使用其他节中的值，请使用 `$section::name` 或 `${section::name}`。通过使用 `$ENV::name`，将替换指定环境变量的值。

变量必须在其值被引用之前定义，否则会标记错误且文件不会加载。可以通过在使用变量之前在默认节中指定默认值来解决此问题。

`ENV` 节中的任何名称/值设置对配置文件可用，但不会传播到环境。

如果值最终超过 64k，则为错误。

可以通过在值周围使用单引号 `'` 或双引号 `"`，或在字符前使用反斜杠 `\` 来转义某些字符。通过使行的最后一个字符为 `\`，值字符串可以跨越多行。此外，还识别 `\n`、`\r`、`\b` 和 `\t` 序列。

上述适用于值的展开和转义规则也适用于 `.include` 指令的路径名。

## OpenSSL 库配置

以下各节使用非正式术语“模块”来指代 OpenSSL 功能的一部分。这与正式术语 FIPS 模块不同。

OpenSSL 配置在默认节中查找 `openssl_conf` 的值，并将其作为指定如何配置库中任何模块的节的名称。将任何模块保留在其默认配置中并不是错误。应用程序可以通过调用 CONF_modules_load_file() 等方式指定不同的名称。

OpenSSL 还会查找 `config_diagnostics` 的值。如果此值存在且具有非零数值，则传递给 CONF_modules_load() 的任何错误抑制标志将被忽略。这对于诊断配置错误很有用，但在生产环境中使用需要额外考虑。启用此选项后，配置错误将完全阻止对服务的访问。如果不启用此选项且存在配置错误，将允许访问但不会使用所需配置。

```sh
# 这些必须在默认节中
config_diagnostics = 1
openssl_conf = openssl_init

[openssl_init]
oid_section = oids
providers = providers
alg_section = evp_properties
ssl_conf = ssl_configuration
engines = engines
random = random

[oids]
... new oids here ...

[providers]
... provider stuff here ...

[evp_properties]
... EVP properties here ...

[ssl_configuration]
... SSL/TLS configuration properties here ...

[engines]
... engine properties here ...

[random]
... random properties here ...
```

各模块的语义描述如下。“在初始化节中”一语指由 `openssl_conf` 或其他名称（在上例中为 `openssl_init`）标识的节。以下示例假定使用上述配置来指定各个节。

### ASN.1 对象标识符配置

初始化节中的名称 `oid_section` 命名包含 OID 名称/值对的节。名称是短名称；值是可选的长名称后跟逗号和数值。虽然某些 OpenSSL 命令有自己指定 OID 的节，但此节使它们对所有命令和应用程序可用。

```sh
[oids]
shortName = a very long OID name, 1.2.3.4
newoid1 = 1.2.3.4.1
some_other_oid = 1.2.3.5
```

如果上述片段的完整配置位于文件 `example.cnf` 中，则以下命令行：

```sh
OPENSSL_CONF=example.cnf openssl asn1parse -genstr OID:1.2.3.4.1
```

将输出：

```sh
0:d=0  hl=2 l=  4 prim: OBJECT :newoid1
```

显示 OID“newoid1”已添加为“1.2.3.4.1”。

### Provider 配置

初始化节中的名称 `providers` 命名包含加密 provider 配置的节。此节中的名称/值赋值每个都命名一个 provider，并指向该 provider 的配置节。特定于 provider 的节用于指定如何加载模块、激活它以及设置其他参数。

在 provider 节内，以下名称具有意义：

`identity` 用于指定替代名称，覆盖 provider 列表中指定的默认名称。例如：

```sh
[providers]
foo = foo_provider

[foo_provider]
identity = my_fips_module
```

`module` 指定要加载的模块（通常是共享库）的路径名。

`activate` 如果存在并设置为 `yes`、`on`、`true` 或 `1` 之一，则关联的 provider 将被激活。相反，将此值设置为 `no`、`off`、`false` 或 `0` 将阻止 provider 被激活。设置可以以小写或大写形式给出。将 activate 设置为任何其他设置或省略设置值将导致错误。

`soft_load` 如果启用，通知库在激活请求的 provider 失败时清除错误堆栈。值为 `1`、`yes`、`true` 或 `on`（小写或大写）将激活此设置，而值为 `0`、`no`、`false` 或 `off`（同样小写或大写）将禁用此设置。任何其他值将产生错误。注意，如果未提供，此设置默认为 off。

节中的所有参数以及子节都提供给 provider。

#### 默认 provider 及其激活

如果没有显式激活任何 provider，则隐式激活默认 provider。详见 OSSL_PROVIDER-default(7)。

如果添加了一个节显式激活任何其他 provider，则很可能需要显式激活默认 provider，否则它将在 openssl 中变得不可用。这可能使系统远程不可用。

### EVP 配置

初始化节中的名称 `alg_section` 命名包含使用 EVP API 时的算法属性的节。

在算法属性节内，以下名称具有意义：

`default_properties` 该值可以是任何可作为 EVP_set_default_properties() 的属性查询字符串接受的值。

`fips_mode`（已弃用）该值是一个布尔值，可以是 `yes` 或 `no`。如果值为 `yes`，则完全等价于：

```sh
default_properties = fips=yes
```

如果值为 `no`，则什么也不发生。使用此名称已弃用，如果使用，它必须是节中唯一的名称。

### SSL 配置

初始化节中的名称 `ssl_conf` 命名包含 SSL/TLS 配置列表的节。与 provider 一样，此节中的每个名称都标识一个具有该名称配置的节。例如：

```sh
[ssl_configuration]
server = server_tls_config
client = client_tls_config
system_default = tls_system_default

[server_tls_config]
... configuration for SSL/TLS servers ...

[client_tls_config]
... configuration for SSL/TLS clients ...
```

配置名 `system_default` 具有特殊含义。如果存在，则在创建 `SSL_CTX` 对象时始终应用它。例如，要强制实施系统范围的最低 TLS 和 DTLS 协议版本：

```sh
[tls_system_default]
MinProtocol = TLSv1.2
MinProtocol = DTLSv1.2
```

最低 TLS 协议应用于基于 TLS 的 `SSL_CTX` 对象，最低 DTLS 协议应用于基于 DTLS 的对象。这同样适用于使用 `MaxProtocol` 设置的最大版本。

每个配置节由 SSL_CONF_cmd(3) 解析的名称/值对组成，SSL_CONF_cmd(3) 将由 SSL_CTX_config() 或 SSL_config() 适当调用。注意，配置节中初始句点之前的任何字符都将被忽略，以便同一命令可以多次使用。这可能对加载不同的密钥类型最有用，如下所示：

```sh
[server_tls_config]
RSA.Certificate = server-rsa.pem
ECDSA.Certificate = server-ecdsa.pem
```

### Engine 配置

初始化节中的名称 `engines` 命名包含 ENGINE 配置列表的节。与 provider 一样，此节中的每个名称都标识一个具有该 engine 配置的 engine。特定于 engine 的节用于指定如何加载 engine、激活它以及设置其他参数。

在 engine 节内，以下名称具有意义：

`engine_id` 用于指定替代名称，覆盖 engine 列表中指定的默认名称。如果存在，它必须排在首位。例如：

```sh
[engines]
foo = foo_engine

[foo_engine]
engine_id = myfoo
```

`dynamic_path` 这会从给定路径加载并添加一个 ENGINE。它等同于向动态 ENGINE 发送 ctrl `SO_PATH`（带路径参数），后跟值为 2 的 `LIST_ADD` 和 `LOAD`。如果这不是所需行为，则可以使用 ctrl 命令直接向动态 ENGINE 发送替代 ctrl。

`init` 指定是否初始化 ENGINE。如果值为 `0`，ENGINE 将不会被初始化；如果值为 `1`，将尝试立即初始化 ENGINE。如果 `init` 命令不存在，则会在其节中所有命令处理完毕后尝试初始化 ENGINE。

`default_algorithms` 这会使用函数 `ENGINE_set_default_string()` 设置 ENGINE 将提供的默认算法。

所有其他名称都被视为发送给 ENGINE 的 ctrl 命令的名称，值是随命令传递的参数。特殊值 `EMPTY` 表示命令不发送任何值。例如：

```sh
[engines]
foo = foo_engine

[foo_engine]
dynamic_path = /some/path/fooengine.so
some_ctrl = some_value
default_algorithms = ALL
other_ctrl = EMPTY
```

### 随机数配置

初始化节中的名称 `random` 命名包含随机数生成器设置的节。

在 random 节内，以下名称具有意义：

`random` 用于指定随机位生成器。例如：

```sh
[random]
random = CTR-DRBG
```

可用的随机位生成器有：

- `CTR-DRBG`
- `HASH-DRBG`
- `HMAC-DRBG`

`cipher` 指定 CTR-DRBG 随机位生成器将使用的密码。其他随机位生成器忽略此名称。默认值为 `AES-256-CTR`。

`digest` 指定 HASH-DRBG 或 HMAC-DRBG 随机位生成器将使用的摘要。其他随机位生成器忽略此名称。

`properties` 设置获取随机位生成器和任何底层算法时使用的属性查询。

`seed` 设置应使用的随机性源。默认情况下，将在 FIPS provider 之外使用 `SEED-SRC`。FIPS provider 使用回调从验证边界之外访问相同的随机性源。

`seed_properties` 设置获取随机性源时使用的属性查询。

`random_provider` 设置用于 RAND_bytes(3) 调用的 provider，而非内置熵源。它默认为“fips”。如果指定的 provider 未加载，将使用内置熵源。

## 实例

此示例展示如何使用引号和转义。

```sh
# 这是默认节。
HOME = /temp
configdir = $ENV::HOME/config

[ section_one ]
# 引号允许前导和尾随空白
any = " any variable name "
other = A string that can \
cover several lines \
by including \e \
characters
message = Hello World\n

[ section_two ]
greeting = $section_one::message
```

此示例展示如何安全地展开环境变量。在此示例中，变量 `tempfile` 旨在引用临时文件，环境变量 `TEMP` 或 `TMP`（如果存在）指定文件应放置的目录。由于如果变量不存在则检查默认节，因此可以将 `TMP` 默认设置为 `/tmp`，将 `TEMP` 默认设置为 `TMP`。

```sh
# 这两行必须在默认节中。
TMP = /tmp
TEMP = $ENV::TMP

# 这可以在任何地方使用
tmpfile = ${ENV::TEMP}/tmp.filename
```

此示例展示如何为应用程序 `sample` 强制实施 FIPS 模式。

```sh
sample = fips_config

[fips_config]
alg_section = evp_properties

[evp_properties]
default_properties = "fips=yes"
```

## 环境变量

`OPENSSL_CONF` 配置文件的路径，空字符串表示无。在 set-user-ID 和 set-group-ID 程序中被忽略。

`OPENSSL_ENGINES` engines 目录的路径。在 set-user-ID 和 set-group-ID 程序中被忽略。

`OPENSSL_MODULES` 包含 OpenSSL 模块（如 provider）的目录路径。在 set-user-ID 和 set-group-ID 程序中被忽略。

`OPENSSL_CONF_INCLUDE` 可选路径，前置到所有 `.include` 路径之前。

## 缺陷

无法使用八进制 `\nnn` 形式包含字符。字符串都以 null 终止，因此 null 不能构成值的一部分。

转义并不完全正确：如果要使用 `\n` 等序列，则同一行上不能使用任何引号转义。

一次只能打开和读取一个目录的限制可被视为一个错误，应该被修复。

## 历史

一个未文档化的 API，NCONF_WIN32()，使用了一组略有不同的解析规则，这些规则旨在为 Microsoft Windows 平台量身定制。具体来说，反斜杠字符不是转义字符，可在路径名中使用；仅识别双引号字符；注释以分号开始。此函数在 OpenSSL 3.0 中已弃用；使用该语法的配置文件的应用程序将不得不进行修改。

## 参见

openssl-x509(1), openssl-req(1), openssl-ca(1), openssl-fipsinstall(1), ASN1_generate_nconf(3), EVP_set_default_properties(3), CONF_modules_load(3), CONF_modules_load_file(3), RAND_bytes(3), fips_config(5), and x509v3_config(5).

## 版权

Copyright 2000-2025 The OpenSSL Project Authors. All Rights Reserved.

Licensed under the Apache License 2.0 (the "License"). You may not use this file except in compliance with the License. You can obtain a copy in the file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.
