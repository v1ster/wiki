---
title: linux Fan driver
date: 2024-10-15
categories:
  - embedded
tags:
  - hardware
  - linux
---

# Linux fan driver

```
+	fan0: fan {
+		compatible = "gpio-fan";
+		pinctrl-names = "default";
+		pinctrl-0 = <&pinctrl_fan>;
+		gpio-fan,speed-map = <0     0
+				      13000 1>;
+		gpios = <&gpio5 4 GPIO_ACTIVE_HIGH>;
+		#cooling-cells = <2>;
+	};
+
+	thermal-zones {
+		soc-thermal {
+			trips {
+				active1: trip2 {
+					temperature = <60000>;
+					hysteresis = <2000>;
+					type = "active";
+				};
+			};
+
+			cooling-maps {
+				map1 {
+					trip = <&active1>;
+					cooling-device = <&fan0 1 THERMAL_NO_LIMIT>;
+				};
+			};
+		};
+	};

```

## 参考

[imx8mp-phyboard-pollux-rdk.dts.patch](https://lore.kernel.org/imx/20240924-wip-y-moog-phytec-de-phyboard-pollux-fan-v1-1-9ea6ec43f27b@phytec.de/T/)  
[rk3399 linux 风扇调试](https://blog.csdn.net/qq_32645109/article/details/121398978)  
[Rockchip RK3399 - GPIO&PWM风扇调试](https://www.cnblogs.com/zyly/p/17718920.html)  
