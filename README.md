# list build dependencies for srpm

## how to use

```
$ ./list-srpm-builddeps.py [-t target_cpu] SPECFILE
```

### target cpus

Currently x86_64 and aarch64 are supported. Default target is x86_64.

### example

Show build dependencies for x86_64.

```
$ ./list-srpm-builddeps.py ~/tmp/shim/shim.spec
efi-filesystem
efi-srpm-macros >= 3-2
pesign >= 0.112-20.fc27
shim-unsigned-ia32 = 15-1.el8+7
shim-unsigned-x64 = 15-1.el8+7
```

Show build dependencies for aarch64.

```
$ ./list-srpm-builddeps.py ~/tmp/shim/shim.spec -t aarch64
efi-filesystem
efi-srpm-macros >= 3-2
pesign >= 0.112-20.fc27
shim-unsigned-aarch64 = 15-1.el8+7
```

