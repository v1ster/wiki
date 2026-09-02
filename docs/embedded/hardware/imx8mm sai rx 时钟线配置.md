---
title: imx8mm sai rx 时钟线配置
date: 2024-08-09
categories:
  - embedded
tags:
  - hardware
  - kernel
---

# imx8mm sai rx 时钟线配置

```
For future reference, here is the summary of what these device tree properties do to the fsl-sai configuration:  
为了供将来参考，以下总结了这些设备树属性对 fsl-sai 配置的作用：

* Adding no synchronization properties results in the default configuration which is Rx synchronized with Tx   
* 不添加同步属性会导致默认配置，即 Rx 与 Tx 同步

* Adding **fsl,sai-synchronous-rx** results with Tx being synchronized with Rx   
* 添加**fsl,sai-synchronous-rx**结果，Tx 与 Rx 同步

*Adding **fsl,sai-asynchronous** clears synchronization bits for both Tx and Rx, thus operating on their timing.  
*添加**fsl,sai-asynchronous**会清除 Tx 和 Rx 的同步位，从而按其时序进行操作。

* Adding both **fsl,sai-synchronous-rx**  and **fsl,sai-asynchronous** ends up in an error as they are mutually exclusive  
* 同时添加**fsl,sai-synchronous-rx**和**fsl,sai-asynchronous**最终会出现错误，因为它们是互斥的
```

## 例子

```
&sai3 {

    pinctrl-names = "default";

    pinctrl-0 = <&pinctrl_sai3>;

    assigned-clocks = <&clk IMX8MM_CLK_SAI3_SRC>,

                    <&clk IMX8MM_CLK_SAI3_DIV>;

    assigned-clock-parents = <&clk IMX8MM_AUDIO_PLL1_OUT>;

    assigned-clock-rates = <0>,<24576000>;

    fsl,sai-synchronous-rx;

    status = "okay";

};
```

# 参考

- [How to Sync SAI RX to TX?](https://community.nxp.com/t5/i-MX-Processors/How-to-Sync-SAI-RX-to-TX/m-p/1564654#M198362) 
- [fsl-sai.txt](https://www.kernel.org/doc/Documentation/devicetree/bindings/sound/fsl-sai.txt)
