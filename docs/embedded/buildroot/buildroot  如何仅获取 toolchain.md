---
title: buildroot 如何仅获取 toolchain
date: 2024-08-29
categories:
  - embedded
tags:
  - buildroot
  - linux
---

# buildroot 如何仅获取 toolchain

> A more recent way to build just the toolchain, which can be used both within and outside of Buildroot, is documented in the [Buildroot manual](https://buildroot.org/downloads/manual/manual.html).

> Though `make toolchain` in Luca's answer does build the toolchain, it also places other host dependencies into `output/host/`, making it slightly more difficult to get a clean toolchain as compared to `make sdk` below, which produces a toolchain tarball in `output/images/`:

>> ### 6.1.3. Build an external toolchain with Buildroot
> 
>> The Buildroot internal toolchain option can be used to create an external toolchain. Here are a series of steps to build an internal toolchain and package it up for reuse by Buildroot itself (or other projects).
> 
>> Create a new Buildroot configuration, with the following details:
> 
>> - Select the appropriate **Target options** for your target CPU architecture
>> - In the **Toolchain** menu, keep the default of **Buildroot toolchain** for **Toolchain type**, and configure your toolchain as desired
>> - In the **System configuration** menu, select **None** as the **Init system** and **none** as **/bin/sh**
>> - In the **Target packages** menu, disable **BusyBox**
>> - In the **Filesystem images** menu, disable **tar the root filesystem**
> 
>> Then, we can trigger the build, and also ask Buildroot to generate a SDK. This will conveniently generate for us a tarball which contains our toolchain:
> 
>> ```
>> make sdk
>> ```
> 
>> This produces the SDK tarball in `$(O)/images`, with a name similar to `arm-buildroot-linux-uclibcgnueabi_sdk-buildroot.tar.gz`. Save this tarball, as it is now the toolchain that you can re-use as an external toolchain in other Buildroot projects.

# 参考

[Buildroot: install and build the toolchain only](https://stackoverflow.com/questions/44521150/buildroot-install-and-build-the-toolchain-only)
[Using the generated toolchain outside Buildroot](https://buildroot.org/downloads/manual/using-buildroot-toolchain.txt)