# elf.5

`elf` — ELF 可执行二进制文件格式

## 名称

`elf`

## 概要

`#include <elf.h>`

## 描述

头文件

`#include <elf.h>`

定义了 ELF 可执行二进制文件的格式。这些文件包括普通可执行文件、可重定位目标文件、core 文件和共享库。

使用 ELF 文件格式的可执行文件由一个 ELF 头开始，其后是程序头表或节头表，或两者兼有。ELF 头始终位于文件的零偏移处。程序头表和节头表在文件中的偏移量由 ELF 头定义。这两个表描述了文件其余的具体内容。

仅希望处理本机架构 ELF 二进制文件的应用程序应在其源代码中包含

`#include <elf.h>`

这些应用程序应通过通用名称 “Elf_xxx” 引用所有类型和结构，通过 “ELF_xxx” 引用宏。以这种方式编写的应用程序可以在任何架构上编译，无论主机是 32 位还是 64 位。

如果应用程序需要处理未知架构的 ELF 文件，则需要同时包含

`#include <sys/elf32.h>`

和

`#include <sys/elf64.h>`

而不是

`#include <elf.h>`

此外，所有类型和结构需要通过 “Elf32_xxx” 或 “Elf64_xxx” 来标识。宏需要通过 “ELF32_xxx” 或 “ELF64_xxx” 来标识。

无论系统架构如何，它始终会包含

`#include <sys/elf_common.h>`

以及

`#include <sys/elf_generic.h>`

这些头文件将上述头描述为 C 结构，并包含动态节、重定位节和符号表的结构。

32 位架构使用以下类型：

```sh
Elf32_Addr	Unsigned 32-bit program address
Elf32_Half	Unsigned 16-bit field
Elf32_Lword	Unsigned 64-bit field
Elf32_Off	Unsigned 32-bit file offset
Elf32_Sword	Signed 32-bit field or integer
Elf32_Word	Unsigned 32-bit field or integer
```

64 位架构使用以下类型：

```sh
Elf64_Addr	Unsigned 64-bit program address
Elf64_Half	Unsigned 16-bit field
Elf64_Lword	Unsigned 64-bit field
Elf64_Off	Unsigned 64-bit file offset
Elf64_Sword	Signed 32-bit field
Elf64_Sxword	Signed 64-bit field or integer
Elf64_Word	Unsigned 32-bit field
Elf64_Xword	Unsigned 64-bit field or integer
```

文件格式定义的所有数据结构遵循相关类的“自然”大小和对齐准则。必要时，数据结构包含显式填充，以确保 4 字节对象的 4 字节对齐，强制结构大小为 4 的倍数等。

ELF 头由 Elf32_Ehdr 或 Elf64_Ehdr 类型描述：

```sh
typedef struct {
        unsigned char   e_ident[EI_NIDENT];
        Elf32_Half      e_type;
        Elf32_Half      e_machine;
        Elf32_Word      e_version;
        Elf32_Addr      e_entry;
        Elf32_Off       e_phoff;
        Elf32_Off       e_shoff;
        Elf32_Word      e_flags;
        Elf32_Half      e_ehsize;
        Elf32_Half      e_phentsize;
        Elf32_Half      e_phnum;
        Elf32_Half      e_shentsize;
        Elf32_Half      e_shnum;
        Elf32_Half      e_shstrndx;
} Elf32_Ehdr;
```

```sh
typedef struct {
	unsigned char   e_ident[EI_NIDENT];
	Elf64_Half      e_type;
	Elf64_Half      e_machine;
	Elf64_Word      e_version;
	Elf64_Addr      e_entry;
	Elf64_Off       e_phoff;
	Elf64_Off       e_shoff;
	Elf64_Word      e_flags;
	Elf64_Half      e_ehsize;
	Elf64_Half      e_phentsize;
	Elf64_Half      e_phnum;
	Elf64_Half      e_shentsize;
	Elf64_Half      e_shnum;
	Elf64_Half      e_shstrndx;
} Elf64_Ehdr;
```

各字段含义如下：

**`ELFCLASSNONE`** 此类无效。
**`ELFCLASS32`** 定义 32 位架构。支持文件和虚拟地址空间最大为 4 GB 的机器。
**`ELFCLASS64`** 定义 64 位架构。

**`ELFDATANONE`** 未知数据格式。
**`ELFDATA2LSB`** 二进制补码，小端序。
**`ELFDATA2MSB`** 二进制补码，大端序。

**`EV_NONE`** 无效版本。
**`EV_CURRENT`** 当前版本。

**`ELFOSABI_SYSV`** UNIX System V ABI。
**`ELFOSABI_HPUX`** HP-UX 操作系统 ABI。
**`ELFOSABI_NETBSD`** NetBSD 操作系统 ABI。
**`ELFOSABI_LINUX`** GNU/Linux 操作系统 ABI。
**`ELFOSABI_HURD`** GNU/Hurd 操作系统 ABI。
**`ELFOSABI_86OPEN`** 86Open 通用 IA32 ABI。
**`ELFOSABI_SOLARIS`** Solaris 操作系统 ABI。
**`ELFOSABI_MONTEREY`** Monterey 项目 ABI。
**`ELFOSABI_IRIX`** IRIX 操作系统 ABI。
**`ELFOSABI_FREEBSD`** FreeBSD 操作系统 ABI。
**`ELFOSABI_TRU64`** TRU64 UNIX 操作系统 ABI。
**`ELFOSABI_ARM`** ARM 架构 ABI。
**`ELFOSABI_STANDALONE`** 独立（嵌入式）ABI。

**`EI_MAG0`** 魔数的第一个字节。必须填充为 **ELFMAG0。**
**`EI_MAG1`** 魔数的第二个字节。必须填充为 **ELFMAG1。**
**`EI_MAG2`** 魔数的第三个字节。必须填充为 **ELFMAG2。**
**`EI_MAG3`** 魔数的第四个字节。必须填充为 **ELFMAG3。**
**`EI_CLASS`** 第五个字节标识此二进制文件的架构：
**`EI_DATA`** 第六个字节指定文件中处理器特定数据的数据编码。目前支持以下编码：
**`EI_VERSION`** ELF 规范的版本号：
**`EI_OSABI`** 此字节标识目标对象所针对的操作系统和 ABI。其他 ELF 结构中的某些字段具有平台特定含义的标志和值；这些字段的解释由此字节的值决定。目前定义了以下值：
**`EI_ABIVERSION`** 此字节标识目标对象所针对的 ABI 版本。此字段用于区分 ABI 的不兼容版本。此版本号的解释取决于 EI_OSABI 字段标识的 ABI。符合本规范的应用程序使用值 0。
**`EI_PAD`** 填充开始处。这些字节保留并设为零。读取它们的程序应忽略它们。如果当前未使用的字节被赋予含义，EI_PAD 的值在未来会发生变化。
**`EI_BRAND`** 架构标识的开始。
**`EI_NIDENT`** e_ident 数组的大小。

**`ET_NONE`** 未知类型。
**`ET_REL`** 可重定位文件。
**`ET_EXEC`** 可执行文件。
**`ET_DYN`** 共享对象。
**`ET_CORE`** core 文件。

**`EM_NONE`** 未知机器。
**`EM_M32`** AT&T WE 32100。
**`EM_SPARC`** Sun Microsystems SPARC。
**`EM_386`** Intel 80386。
**`EM_68K`** Motorola 68000。
**`EM_88K`** Motorola 88000。
**`EM_486`** Intel 80486。
**`EM_860`** Intel 80860。
**`EM_MIPS`** MIPS RS3000（仅大端序）。
**`EM_MIPS_RS4_BE`** MIPS RS4000（仅大端序）。
**`EM_SPARC64`** SPARC v9 64 位非官方。
**`EM_PARISC`** HPPA。
**`EM_PPC`** PowerPC。
**`EM_ALPHA`** Compaq [DEC] Alpha。

**`EV_NONE`** 无效版本
**`EV_CURRENT`** 当前版本

**`e_ident`** 此字节数组指定如何解释文件，独立于处理器或文件其余内容。在此数组中，一切都由宏命名，这些宏以 **EI_** 前缀开始，可能包含以 **ELF** 前缀开始的值。定义了以下宏：
**`e_type`** 此结构成员标识目标文件类型：
**`e_machine`** 此成员指定单个文件所需的架构：
**`e_version`** 此成员标识文件版本：
**`e_entry`** 此成员给出系统首次转移控制权的虚拟地址，从而启动进程。如果文件没有关联的入口点，此成员为零。
**`e_phoff`** 此成员保存程序头表在文件中的字节偏移量。如果文件没有程序头表，此成员为零。
**`e_shoff`** 此成员保存节头表在文件中的字节偏移量。如果文件没有节头表，此成员为零。
**`e_flags`** 此成员保存与文件关联的处理器特定标志。标志名称采用 EF_`machine_flag' 形式。目前未定义任何标志。
**`e_ehsize`** 此成员保存 ELF 头的字节大小。
**`e_phentsize`** 此成员保存文件程序头表中一个条目的字节大小；所有条目大小相同。
**`e_phnum`** 此成员保存程序头表中的条目数。如果文件使用扩展程序头编号，则 **e_phnum** 成员将包含值 `PN_XNUM`，而程序头表的实际条目数将存储在索引为 `SHN_UNDEF` 的节头的 **sh_info** 成员中。**e_phentsize** 与程序头表条目数的乘积即为程序头表的字节大小。如果文件没有程序头，**e_phnum** 为零。
**`e_shentsize`** 此成员保存一个节头的字节大小。节头是节头表中的一个条目；所有条目大小相同。
**`e_shnum`** 此成员保存节头表中的条目数。如果文件使用扩展节编号，则 **e_shnum** 成员将为零，实际的节数将存储在索引为 `SHN_UNDEF` 的节头的 **sh_size** 成员中。如果文件没有节头表，ELF 头的 **e_shnum** 和 **e_shoff** 字段都为零。**e_shentsize** 与文件中节数的乘积即为节头表的字节大小。
**`e_shstrndx`** 此成员保存与节名字符串表关联的条目的节头表索引。如果使用扩展节编号，此字段将保存值 **SHN_XINDEX**，实际的节头表索引将存在于索引为 `SHN_UNDEF` 的节头条目的 **sh_link** 字段中。如果文件没有节名字符串表，此成员为 **SHN_UNDEF。**

可执行文件或共享目标文件的程序头表是一个结构数组，每个结构描述一个段或系统为执行程序而需要准备的其他信息。目标文件 *段* 包含一个或多个 *节。* 程序头仅对可执行文件和共享目标文件有意义。文件通过 ELF 头的 **e_phentsize** 和 **e_phnum** 成员指定自身的程序头大小。与 Elf 可执行头一样，程序头根据架构也有不同版本：

```sh
typedef struct {
        Elf32_Word      p_type;
        Elf32_Off       p_offset;
        Elf32_Addr      p_vaddr;
        Elf32_Addr      p_paddr;
        Elf32_Word      p_filesz;
        Elf32_Word      p_memsz;
        Elf32_Word      p_flags;
        Elf32_Word      p_align;
} Elf32_Phdr;
```

```sh
typedef struct {
        Elf64_Word      p_type;
        Elf64_Word      p_flags;
        Elf64_Off       p_offset;
        Elf64_Addr      p_vaddr;
        Elf64_Addr      p_paddr;
        Elf64_Xword     p_filesz;
        Elf64_Xword     p_memsz;
        Elf64_Xword     p_align;
} Elf64_Phdr;
```

32 位和 64 位程序头的主要区别仅在于 **p_flags** 成员在整个结构中的位置。

**`PT_NULL`** 该数组元素未使用，其他成员的值未定义。这使程序头可以包含被忽略的条目。
**`PT_LOAD`** 该数组元素指定一个可加载段，由 **p_filesz** 和 **p_memsz** 描述。文件中的字节被映射到内存段的开头。如果段的内存大小（**p_memsz**）大于文件大小（**p_filesz**），则“额外”字节定义为持有值 0，并跟随在段的已初始化区域之后。文件大小不能大于内存大小。程序头表中的可加载段条目按 **p_vaddr** 成员升序排列。
**`PT_DYNAMIC`** 该数组元素指定动态链接信息。
**`PT_INTERP`** 该数组元素指定一个以 null 结尾的路径名的位置和大小，该路径名作为解释器调用。此段类型仅对可执行文件有意义（尽管可能出现在共享对象中）。但是，它在文件中出现的次数不能超过一次。如果存在，它必须位于任何可加载段条目之前。
**`PT_NOTE`** 该数组元素指定辅助信息的位置和大小。
**`PT_SHLIB`** 此段类型已保留，但语义未指定。包含此类型数组元素的程序不符合 ABI。
**`PT_PHDR`** 该数组元素（如果存在）指定程序头表本身在文件和程序内存映像中的位置和大小。此段类型在文件中出现的次数不能超过一次。此外，它只有在程序头表是程序内存映像的一部分时才可能出现。如果存在，它必须位于任何可加载段条目之前。
**`PT_LOPROC`** 此值到 **PT_HIPROC**（含）保留用于处理器特定的语义。
**`PT_HIPROC`** 此值到 **PT_LOPROC**（含）保留用于处理器特定的语义。

**`PF_X`** 可执行段。
**`PF_W`** 可写段。
**`PF_R`** 可读段。

**`p_type`** Phdr 结构的此成员说明此数组元素描述的段类型或如何解释数组元素的信息。
**`p_offset`** 此成员保存段的第一个字节在文件中距文件开头的偏移量。
**`p_vaddr`** 此成员保存段的第一个字节在内存中的虚拟地址。
**`p_paddr`** 在物理寻址相关的系统上，此成员保留用于段的物理地址。在 BSD 下不使用此成员，必须为零。
**`p_filesz`** 此成员保存段的文件映像中的字节数。可以为零。
**`p_memsz`** 此成员保存段的内存映像中的字节数。可以为零。
**`p_flags`** 此成员保存与段相关的标志：文本段通常具有标志 **PF_X** 和 **PF_R。** 数据段通常具有 **PF_X、** **PF_W** 和 **PF_R。**
**`p_align`** 此成员保存段在内存和文件中对齐的值。可加载进程段的 **p_vaddr** 和 **p_offset** 值必须按页大小取模相等。值零和一表示不需要对齐。否则，**p_align** 应为 2 的正整数幂，且 **p_vaddr** 应等于 **p_offset** 模 **p_align。**

文件的节头表用于定位文件的所有节。节头表是 Elf32_Shdr 或 Elf64_Shdr 结构的数组。ELF 头的 **e_shoff** 成员给出从文件开头到节头表的字节偏移量。**e_shnum** 保存节头表包含的条目数。**e_shentsize** 保存每个条目的字节大小。

节头表索引是此数组的下标。一些节头表索引是保留的。目标文件没有这些特殊索引对应的节：

**`SHN_UNDEF`** 此值标记未定义、缺失、不相关或无意义的节引用。例如，相对于节号 **SHN_UNDEF** “定义”的符号是未定义符号。
**`SHN_LORESERVE`** 此值指定保留索引范围的下界。
**`SHN_LOPROC`** 此值到 **SHN_HIPROC**（含）保留用于处理器特定的语义。
**`SHN_HIPROC`** 此值到 **SHN_LOPROC**（含）保留用于处理器特定的语义。
**`SHN_ABS`** 此值为相应引用指定绝对值。例如，相对于节号 **SHN_ABS** 定义的符号具有绝对值，不受重定位影响。
**`SHN_COMMON`** 相对于此节定义的符号是公共符号，如 FORTRAN COMMON 或未分配的 C 外部变量。
**`SHN_HIRESERVE`** 此值指定保留索引范围的上界。系统保留 **SHN_LORESERVE** 到 **SHN_HIRESERVE**（含）之间的索引。节头表不包含保留索引的条目。

节头具有以下结构：

```sh
typedef struct {
	Elf32_Word      sh_name;
	Elf32_Word      sh_type;
	Elf32_Word      sh_flags;
	Elf32_Addr      sh_addr;
	Elf32_Off       sh_offset;
	Elf32_Word      sh_size;
	Elf32_Word      sh_link;
	Elf32_Word      sh_info;
	Elf32_Word      sh_addralign;
	Elf32_Word      sh_entsize;
} Elf32_Shdr;
```

```sh
typedef struct {
	Elf64_Word      sh_name;
	Elf64_Word      sh_type;
	Elf64_Xword     sh_flags;
	Elf64_Addr      sh_addr;
	Elf64_Off       sh_offset;
	Elf64_Xword     sh_size;
	Elf64_Word      sh_link;
	Elf64_Word      sh_info;
	Elf64_Xword     sh_addralign;
	Elf64_Xword     sh_entsize;
} Elf64_Shdr;
```

**`SHT_NULL`** 此值将节头标记为非活动状态。它没有关联的节。节头的其他成员值未定义。
**`SHT_PROGBITS`** 此节保存由程序定义的信息，其格式和含义完全由程序决定。
**`SHT_SYMTAB`** 此节保存符号表。通常，**SHT_SYMTAB** 提供用于链接编辑的符号，但也可用于动态链接。作为完整的符号表，它可能包含许多动态链接不需要的符号。目标文件还可包含一个 **SHN_DYNSYM** 节。
**`SHT_STRTAB`** 此节保存字符串表。一个目标文件可以有多个字符串表节。
**`SHT_RELA`** 此节保存带显式加数的重定位条目，例如 32 位类目标文件的 **Elf32_Rela** 类型。一个目标文件可以有多个重定位节。
**`SHT_HASH`** 此节保存符号哈希表。所有参与动态链接的目标文件必须包含符号哈希表。一个目标文件只能有一个哈希表。
**`SHT_DYNAMIC`** 此节保存动态链接信息。一个目标文件只能有一个动态节。
**`SHT_NOTE`** 此节保存以某种方式标记文件的信息。
**`SHT_NOBITS`** 此类型的节在文件中不占用空间，但在其他方面类似于 **SHN_PROGBITS。** 尽管此节不包含字节，**sh_offset** 成员仍包含概念上的文件偏移量。
**`SHT_REL`** 此节保存不带显式加数的重定位偏移量，例如 32 位类目标文件的 **Elf32_Rel** 类型。一个目标文件可以有多个重定位节。
**`SHT_SHLIB`** 此节已保留，但语义未指定。
**`SHT_DYNSYM`** 此节保存最小化的动态链接符号集。目标文件还可包含一个 **SHN_SYMTAB** 节。
**`SHT_LOPROC`** 此值到 **SHT_HIPROC**（含）保留用于处理器特定的语义。
**`SHT_HIPROC`** 此值到 **SHT_LOPROC**（含）保留用于处理器特定的语义。
**`SHT_LOUSER`** 此值指定为应用程序保留的索引范围的下界。
**`SHT_HIUSER`** 此值指定为应用程序保留的索引范围的上界。**SHT_LOUSER** 到 **SHT_HIUSER** 之间的节类型可被应用程序使用，不会与当前或未来系统定义的节类型冲突。

**`SHF_WRITE`** 此节包含在进程执行期间应可写的数据。
**`SHF_ALLOC`** 此节在进程执行期间占用内存。某些控制节不驻留在目标文件的内存映像中。对于这些节，此属性为关闭。
**`SHF_EXECINSTR`** 此节包含可执行的机器指令。
**`SHF_MASKPROC`** 此掩码中包含的所有位保留用于处理器特定的语义。
**`SHF_COMPRESSED`** 节数据已压缩。

**`sh_name`** 此成员指定节名称。其值是节头字符串表节的索引，给出一个以 null 结尾的字符串的位置。
**`sh_type`** 此成员对节的内容和语义进行分类。
**`sh_flags`** 节支持描述杂项属性的一位标志。如果 **sh_flags** 中某标志位被设置，则该属性对此节为“开”。否则，该属性为“关”或不适用。未定义的属性设为零。
**`sh_addr`** 如果节将出现在进程的内存映像中，此成员保存节第一个字节应驻留的地址。否则，该成员为零。
**`sh_offset`** 此成员的值保存从文件开头到节中第一个字节的字节偏移量。一种节类型 **SHT_NOBITS** 在文件中不占用空间，其 **sh_offset** 成员定位的是文件中概念上的放置位置。
**`sh_size`** 此成员保存节的字节大小。除非节类型为 **SHT_NOBITS**，否则该节在文件中占用 **sh_size** 字节。**SHT_NOBITS** 类型的节可以具有非零大小，但在文件中不占用空间。
**`sh_link`** 此成员保存一个节头表索引链接，其解释取决于节类型。
**`sh_info`** 此成员保存额外信息，其解释取决于节类型。
**`sh_addralign`** 某些节有地址对齐约束。如果某节持有双字，系统必须确保整个节的双字对齐。即 **sh_addr** 的值必须与 **sh_addralign** 的值取模为零。只允许零和 2 的正整数幂。值零或一表示该节没有对齐约束。
**`sh_entsize`** 某些节持有固定大小条目的表，如符号表。对于此类节，此成员给出每个条目的字节大小。如果节不持有固定大小条目的表，此成员为零。

各节保存程序和控制信息：

**.bss** （Block Started by Symbol）此节保存有助于程序内存映像的未初始化数据。根据定义，系统在程序开始运行时将数据初始化为零。此节类型为 **SHT_NOBITS。** 属性类型为 **SHF_ALLOC** 和 **SHF_WRITE。**
**.comment** 此节保存版本控制信息。此节类型为 **SHT_PROGBITS。** 不使用任何属性类型。
**.ctors** 此遗留节保存指向初始化例程的指针，这些例程在调用主程序入口点之前执行。此节类型为 **SHT_PROGBITS。** 使用的属性为 **SHF_ALLOC。**
**.data** 此节保存有助于程序内存映像的已初始化数据。此节类型为 **SHT_PROGBITS。** 属性类型为 **SHF_ALLOC** 和 **SHF_WRITE。**
**.data1** 此节保存有助于程序内存映像的已初始化数据。此节类型为 **SHT_PROGBITS。** 属性类型为 **SHF_ALLOC** 和 **SHF_WRITE。**
**.debug** 此节保存用于符号调试的信息。内容未指定。此节类型为 **SHT_PROGBITS。** 不使用任何属性类型。
**.dtors** 此遗留节保存指向终止例程的指针，在程序正常退出时执行。此节类型为 **SHT_PROGBITS。** 使用的属性为 **SHF_ALLOC。**
**.dynamic** 此节保存动态链接信息。该节的属性将包括 **SHF_ALLOC** 位。是否设置 **SHF_WRITE** 位取决于处理器。此节类型为 **SHT_DYNAMIC。** 参见上述属性。
**.dynstr** 此节保存动态链接所需的字符串，最常见的是表示与符号表条目关联的名称的字符串。此节类型为 **SHT_STRTAB。** 使用的属性类型为 **SHF_ALLOC。**
**.dynsym** 此节保存动态链接符号表。此节类型为 **SHT_DYNSYM。** 使用的属性为 **SHF_ALLOC。**
**.fini** 此遗留节保存有助于进程终止代码的可执行指令。当程序正常退出时，系统安排执行此节中的代码。此节类型为 **SHT_PROGBITS。** 使用的属性为 **SHF_ALLOC** 和 **SHF_EXECINSTR。**
**.fini_array** 此节保存指向终止例程的指针。当程序正常退出时，rtld(1) 执行此节引用的代码。此节类型为 **SHT_FINI_ARRAY。** 使用的属性为 **SHF_ALLOC。** 关于初始化和终止代码如何被调用，参见 `NT_FREEBSD_NOINIT_TAG`（下文）的描述。
**.got** 此节保存全局偏移表。此节类型为 **SHT_PROGBITS。** 属性取决于处理器。
**.hash** 此节保存符号哈希表。此节类型为 **SHT_HASH。** 使用的属性为 **SHF_ALLOC。**
**.init** 此遗留节保存有助于进程初始化代码的可执行指令。当程序开始运行时，系统在调用主程序入口点之前安排执行此节中的代码。此节类型为 **SHT_PROGBITS。** 使用的属性为 **SHF_ALLOC** 和 **SHF_EXECINSTR。**
**.init_array** 此节保存指向初始化例程的指针。当程序开始运行时，rtld(1) 在调用程序入口点之前执行此节引用的代码。此节类型为 **SHT_INIT_ARRAY。** 使用的属性为 **SHF_ALLOC。** 关于初始化和终止代码如何被调用，参见 `NT_FREEBSD_NOINIT_TAG`（下文）的描述。
**.interp** 此节保存程序解释器的路径名。如果文件有包含此节的可加载段，则该节的属性将包括 **SHF_ALLOC** 位。否则，该位为关闭。此节类型为 **SHT_PROGBITS。**
**.line** 此节保存用于符号调试的行号信息，描述程序源代码与机器代码之间的对应关系。内容未指定。此节类型为 **SHT_PROGBITS。** 不使用任何属性类型。
**.note** 此节保存以下文所述“Note Section”格式存储的信息。此节类型为 **SHT_NOTE。** 不使用任何属性类型。
**.plt** 此节保存过程链接表。此节类型为 **SHT_PROGBITS。** 属性取决于处理器。
**.relNAME** 此节保存下文所述的重定位信息。如果文件有包含重定位的可加载段，则该节的属性将包括 **SHF_ALLOC** 位。否则，该位为关闭。按照约定，“NAME”由重定位所应用的节提供。因此，**.text** 的重定位节通常命名为 **.rel.text。** 此节类型为 **SHT_REL。**
**.relaNAME** 此节保存下文所述的重定位信息。如果文件有包含重定位的可加载段，则该节的属性将包括 **SHF_ALLOC** 位。否则，该位为关闭。按照约定，“NAME”由重定位所应用的节提供。因此，**.text** 的重定位节通常命名为 **.rela.text。** 此节类型为 **SHT_RELA。**
**.rodata** 此节保存只读数据，通常有助于进程映像中的不可写段。此节类型为 **SHT_PROGBITS。** 使用的属性为 **SHF_ALLOC。**
**.rodata1** 此节保存只读数据，通常有助于进程映像中的不可写段。此节类型为 **SHT_PROGBITS。** 使用的属性为 **SHF_ALLOC。**
**.shstrtab** 此节保存节名称。此节类型为 **SHT_STRTAB。** 不使用任何属性类型。
**.strtab** 此节保存字符串，最常见的是表示与符号表条目关联的名称的字符串。如果文件有包含符号字符串表的可加载段，则该节的属性将包括 **SHF_ALLOC** 位。否则，该位为关闭。此节类型为 **SHT_STRTAB。**
**.symtab** 此节保存符号表。如果文件有包含符号表的可加载段，则该节的属性将包括 **SHF_ALLOC** 位。否则，该位为关闭。此节类型为 **SHT_SYMTAB。**
**.text** 此节保存程序的“文本”或可执行指令。此节类型为 **SHT_PROGBITS。** 使用的属性为 **SHF_ALLOC** 和 **SHF_EXECINSTR。**
**.jcr** 此节保存关于必须注册的 Java 类的信息。它已过时，为 FreeBSD 15 或更高版本创建的二进制文件不处理它。
**.eh_frame** 此节保存用于 C++ 异常处理的信息。

设置了 `SHF_COMPRESSED` 标志的节包含节数据的压缩副本。压缩的节数据以 `Elf64_Chdr` 或 `Elf32_Chdr` 结构开头，该结构编码了压缩算法和未压缩数据的某些特征。

```sh
typedef struct {
	Elf32_Word    ch_type;
	Elf32_Word    ch_size;
	Elf32_Word    ch_addralign;
} Elf32_Chdr;
```

```sh
typedef struct {
	Elf64_Word    ch_type;
	Elf64_Word    ch_reserved;
	Elf64_Xword   ch_size;
	Elf64_Xword   ch_addralign;
} Elf64_Chdr;
```

**`ch_type`** 使用的压缩算法。值 `ELFCOMPRESS_ZLIB` 表示数据使用 zlib(3) 压缩。值 `ELFCOMPRESS_ZSTD` 表示数据使用 Zstandard 压缩。
**`ch_size`** 未压缩节数据的字节大小。这对应于包含未压缩数据的节头的 **sh_size** 字段。
**`ch_addralign`** 未压缩节数据的地址对齐。这对应于包含未压缩数据的节头的 **sh_addralign** 字段。

字符串表节保存以 null 结尾的字符序列，通常称为字符串。目标文件使用这些字符串表示符号和节名称。通过字符串表节的索引来引用字符串。第一个字节（索引为零）定义为持有 null 字符。类似地，字符串表的最后一个字节定义为持有 null 字符，确保所有字符串以 null 结尾。

目标文件的符号表保存定位和重定位程序符号定义及引用所需的信息。符号表索引是此数组的下标。

```sh
typedef struct {
	Elf32_Word      st_name;
	Elf32_Addr      st_value;
	Elf32_Word      st_size;
	unsigned char   st_info;
	unsigned char   st_other;
	Elf32_Half      st_shndx;
} Elf32_Sym;
```

```sh
typedef struct {
	Elf64_Word      st_name;
	unsigned char   st_info;
	unsigned char   st_other;
	Elf64_Half      st_shndx;
	Elf64_Addr      st_value;
	Elf64_Xword     st_size;
} Elf64_Sym;
```

**`STT_NOTYPE`** 符号类型未定义。
**`STT_OBJECT`** 该符号与数据对象关联。
**`STT_FUNC`** 该符号与函数或其他可执行代码关联。
**`STT_SECTION`** 该符号与节关联。此类型的符号表条目主要用于重定位，通常具有 **STB_LOCAL** 绑定。
**`STT_FILE`** 按照约定，符号名称给出与目标文件关联的源文件名称。文件符号具有 **STB_LOCAL** 绑定，其节索引为 **SHN_ABS，** 如果存在，它位于文件其他 **STB_LOCAL** 符号之前。
**`STT_LOPROC`** 此值到 **STT_HIPROC**（含）保留用于处理器特定的语义。
**`STT_HIPROC`** 此值到 **STT_LOPROC**（含）保留用于处理器特定的语义。

**Xo** Fn ELF32_ST_BIND info Xc 或 Fn ELF64_ST_BIND info 从 st_info 值中提取绑定。
**Xo** Fn ELF64_ST_TYPE info Xc 或 Fn ELF32_ST_TYPE info 从 st_info 值中提取类型。
**Xo** Fn ELF32_ST_INFO bind type Xc 或 Fn ELF64_ST_INFO bind type 将绑定和类型转换为 st_info 值。

**`STB_LOCAL`** 局部符号在包含其定义的目标文件之外不可见。同名局部符号可以存在于多个文件中而不会相互干扰。
**`STB_GLOBAL`** 全局符号对所有正在合并的目标文件可见。一个文件对全局符号的定义将满足另一个文件对同一符号的未定义引用。
**`STB_WEAK`** 弱符号类似于全局符号，但其定义优先级较低。
**`STB_LOPROC`** 此值到 **STB_HIPROC**（含）保留用于处理器特定的语义。
**`STB_HIPROC`** 此值到 **STB_LOPROC**（含）保留用于处理器特定的语义。有用于打包和解包绑定与类型字段的宏：

**`st_name`** 此成员保存目标文件符号字符串表的索引，该表持有符号名称的字符表示。如果值非零，它表示给出符号名称的字符串表索引。否则，符号表没有名称。
**`st_value`** 此成员给出关联符号的值。
**`st_size`** 许多符号有关联的大小。如果符号没有大小或大小未知，此成员为零。
**`st_info`** 此成员指定符号的类型和绑定属性：
**`st_other`** 此成员当前为零，没有定义的含义。
**`st_shndx`** 每个符号表条目都“定义”于某个节。此成员保存相关的节头表索引。

重定位是将符号引用与符号定义连接的过程。可重定位文件必须包含描述如何修改其节内容的信息，从而允许可执行文件和共享目标文件为进程的程序映像持有正确信息。重定位条目即是这些数据。

不需要加数的重定位结构：

```sh
typedef struct {
	Elf32_Addr      r_offset;
	Elf32_Word      r_info;
} Elf32_Rel;
```

```sh
typedef struct {
	Elf64_Addr      r_offset;
	Elf64_Xword     r_info;
} Elf64_Rel;
```

需要加数的重定位结构：

```sh
typedef struct {
	Elf32_Addr      r_offset;
	Elf32_Word      r_info;
	Elf32_Sword     r_addend;
} Elf32_Rela;
```

```sh
typedef struct {
	Elf64_Addr      r_offset;
	Elf64_Xword     r_info;
	Elf64_Sxword    r_addend;
} Elf64_Rela;
```

**`r_offset`** 此成员给出应用重定位操作的位置。对于可重定位文件，该值是从节开头到受重定位影响的存储单元的字节偏移量。对于可执行文件或共享对象，该值是受重定位影响的存储单元的虚拟地址。
**`r_info`** 此成员同时给出进行重定位所依据的符号表索引和要应用的重定位类型。重定位类型取决于处理器。当文本提及重定位条目的重定位类型或符号表索引时，是指分别对条目的 **r_info** 成员应用 **ELF_[32|64]_R_TYPE** 或 **ELF[32|64]_R_SYM** 的结果。
**`r_addend`** 此成员指定用于计算存储到可重定位字段的值的常数加数。

### Note 节

ELF note 节由以下格式的条目组成：

| 字段 | 大小 | 描述 |
| --- | --- | --- |
| `namesz` | 32 位 | 名称大小 |
| `descsz` | 32 位 | 描述大小 |
| `type` | 32 位 | 依赖于操作系统的 note 类型 |
| `name` | `namesz` | 以 null 结尾的发起者名称 |
| `desc` | `descsz` | 依赖于操作系统的 note 数据 |

`name` 和 `desc` 字段经过填充以确保 4 字节对齐。`namesz` 和 `descsz` 指定未填充时的长度。

FreeBSD 定义了以下 ELF note 类型（`desc` 的相应解释如下）

**NT_FREEBSD_FCTL_ASLR_DISABLE** （值：0x01）请求不执行地址随机化（ASLR）。参见 [security(7)](../man7/security.7.md)。

**NT_FREEBSD_FCTL_PROTMAX_DISABLE** （值：0x02）请求 mmap(2) 调用不要将 PROT_MAX 设置为 `prot` 参数的初始值。

**NT_FREEBSD_FCTL_STKGAP_DISABLE** （值：0x04）禁用栈间隙。

**NT_FREEBSD_FCTL_WXNEEDED** （值：0x08）指示该二进制文件需要同时可写和可执行的映射。

**NT_FREEBSD_FCTL_LA48** （值：0x10）在 amd64 上请求 48 位线性地址空间。

**NT_FREEBSD_FCTL_LA57** （值：0x40）在 amd64 上接受 57 位线性地址空间。

**`NT_FREEBSD_ABI_TAG`** （值：1）以 32 位整数形式指示 OS ABI 版本，包含预期的 ABI 版本（即 `__FreeBSD_version`）

**`NT_FREEBSD_NOINIT_TAG`** （值：2）指示 C 启动代码不调用初始化例程，因此 rtld(1) 必须这样做。`desc` 被忽略。

**`NT_FREEBSD_ARCH_TAG`** （值：3）包含可执行文件构建时所用的 MACHINE_ARCH。

**`NT_FREEBSD_FEATURE_CTL`** （值：4）包含要启用的缓解措施和功能的位掩码：

## 参见

as(1), gdb(1) (`ports/devel/gdb`), [ld(1)](../man1/ld.1.md), objdump(1), [readelf(1)](../man1/readelf.1.md), execve(2), zlib(3), [ar(5)](ar.5.md), [core(5)](core.5.md)

> Hewlett Packard, *Elf-64 Object File Format*.

> Santa Cruz Operation, *System V Application Binary Interface*.

> Unix System Laboratories, "Object Files", *Executable and Linking Format (ELF)*.

## 历史

ELF 头文件出现于 FreeBSD 2.2.6。ELF 本身首次出现于 AT&T System V UNIX。ELF 格式是一项采用的标准。

## 作者

本手册页由 Jeroen Ruigrok van der Werven <asmodai@FreeBSD.org> 编写，灵感来自 BSDi 的 BSD/OS `elf` 手册页。
