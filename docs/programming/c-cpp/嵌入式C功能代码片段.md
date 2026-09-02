---
title: 嵌入式C功能代码片段
date: 2025-09-12
categories:
  - programming
tags:
  - c-cpp
---

# 嵌入式C功能代码片段

## 1.快速获取结构体成员大小及偏移量
获取结构体成员大小及偏移量的方式有多种。最简便的方式：
```C
#include <stdio.h>

// 获取结构体成员大小
#define  GET_MEMBER_SIZE(type, member)   sizeof(((type*)0)->member)

// 获取结构体成员偏移量
#define  GET_MEMBER_OFFSET(type, member)  ((size_t)(&(((type*)0)->member)))

typedefstruct _test_struct0
{
char x;
char y;
char z;
}test_struct0;

typedefstruct _test_struct1
{
char a;
char c;
 short b;
int d;
 test_struct0 e;
}test_struct1;

int main(int arc, char *argv[])
{
printf("GET_MEMBER_SIZE(test_struct1, a) = %ld\n", GET_MEMBER_SIZE(test_struct1, a));
    printf("GET_MEMBER_SIZE(test_struct1, c) = %ld\n", GET_MEMBER_SIZE(test_struct1, c));
printf("GET_MEMBER_SIZE(test_struct1, b) = %ld\n", GET_MEMBER_SIZE(test_struct1, b));
printf("GET_MEMBER_SIZE(test_struct1, d) = %ld\n", GET_MEMBER_SIZE(test_struct1, d));
    printf("GET_MEMBER_SIZE(test_struct1, e) = %ld\n", GET_MEMBER_SIZE(test_struct1, e));
    printf("test_struct1 size = %ld\n", sizeof(test_struct1));

printf("GET_MEMBER_OFFSET(a): %ld\n", GET_MEMBER_OFFSET(test_struct1, a));
printf("GET_MEMBER_OFFSET(c): %ld\n", GET_MEMBER_OFFSET(test_struct1, c));
printf("GET_MEMBER_OFFSET(b): %ld\n", GET_MEMBER_OFFSET(test_struct1, b));
printf("GET_MEMBER_OFFSET(d): %ld\n", GET_MEMBER_OFFSET(test_struct1, d));
printf("GET_MEMBER_OFFSET(e): %ld\n", GET_MEMBER_OFFSET(test_struct1, e));

return0;
}
```

## 2. 获取CPU温度
应用可以定时获取CPU的温度，比如程序异常崩溃时，我们可能需要分析多方面原因，CPU温度就是其中之一。

```C
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define CPU_TEMP_FILE0 "/sys/devices/virtual/thermal/thermal_zone0/temp"

struct cpu_temperature
{
int integer_part;
int decimal_part;
};

typedefstruct cpu_temperature cpu_temperature_t;

cpu_temperature_t get_cpu_temperature(const char *_cpu_temp_file)
{
 FILE *fp = NULL;
cpu_temperature_t cpu_temperature = {0};
int temp = 0;

 fp = fopen(_cpu_temp_file, "r");
if (NULL == fp)
 {
printf("fopen file error\n");
return cpu_temperature;
 }

fscanf(fp, "%d", &temp);
 cpu_temperature.integer_part = temp / 1000;
 cpu_temperature.decimal_part = temp % 1000 / 100;

 fclose(fp);

return cpu_temperature;
}


int main(int arc, char *argv[])
{
cpu_temperature_t cpu_temperature = {0};

 cpu_temperature = get_cpu_temperature(CPU_TEMP_FILE0);
printf("cpu_temperature = %d.%d ℃\n", cpu_temperature.integer_part, cpu_temperature.decimal_part);
return0;
}
```

## 3. 获取文件大小
有时候我们需要获取某个文件的大小，比如如果需要发送文件里的内容，则需要知道文件的大小。

```C
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>

long get_file_size(const char *_file_name)
{
    FILE * fp = fopen(_file_name, "r");
    if (NULL == fp)
    {
        printf("fopen error\n");
        return-1;
    }

    fseek(fp, 0L, SEEK_END);
    long size = ftell(fp);
    fclose(fp);

    return size;
}

int main()
{
    #define FILE_NAME  "./get_file_size"
    long file_size = get_file_size(FILE_NAME);
    printf("file_size = %ld\n", file_size);

    return0;
}
```

## 4. 获取时间戳
系统时间戳很常用，比如log输出时，可以附带时间戳数据，方便分析。

```C
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/time.h>
#include <time.h>

long long get_sys_time_ms(void)
{
    longlong time_ms = 0;
    struct timeval sys_current_time;

    gettimeofday(&sys_current_time, NULL);
    time_ms = ((longlong)sys_current_time.tv_sec*1000000 + sys_current_time.tv_usec) / 1000;

    return time_ms;
}

int main(int arc, char *argv[])
{
longlong cur_sys_time = get_sys_time_ms();

    printf("cur_sys_time = %lld ms\n", cur_sys_time);

return0;
}
```

## 5. 获取MAC

```C
#include <stdio.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>

int get_netif_mac(const char *_ifr_name, uint8_t *_mac)
{
int32_t    ret = -1;
    struct ifreq   m_ifreq;
    int32_t    sock = 0;

    sock = socket(AF_INET, SOCK_STREAM, 0);
if (sock < 0)
 {
printf("socket err\r\n");
goto err;
 }

    strcpy(m_ifreq.ifr_name, _ifr_name);

    ret = ioctl(sock,SIOCGIFHWADDR, &m_ifreq);
if (ret < 0)
 {
printf("ioctl err:%d\r\n",ret);
goto err;
 }

    snprintf((char *)_mac, 32, "%02x%02x%02x%02x%02x%02x", (uint8_t)m_ifreq.ifr_hwaddr.sa_data[0],
                                                     (uint8_t)m_ifreq.ifr_hwaddr.sa_data[1],
                                                     (uint8_t)m_ifreq.ifr_hwaddr.sa_data[2],
                                                     (uint8_t)m_ifreq.ifr_hwaddr.sa_data[3],
                                                     (uint8_t)m_ifreq.ifr_hwaddr.sa_data[4],
                                                     (uint8_t)m_ifreq.ifr_hwaddr.sa_data[5]);

    return0;
err:
return-1;
}


int main(int argc, char **argv)
{
    char mac_str[32] = {0};
    get_netif_mac("wlan1", mac_str);
    printf("mac = %s\n", mac_str);

    return0;
}
```
## 6、获取IP
```C
#include <stdio.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>

int get_local_ip(const char *_ifr_name, char *_ip)
{
int ret = -1;
    int sockfd;
    struct sockaddr_in sin;
    struct ifreq ifr;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (-1 == sockfd)
    {
        printf("socket error\n");
        return ret;
    }

    strncpy(ifr.ifr_name, _ifr_name, IFNAMSIZ);
    ifr.ifr_name[IFNAMSIZ - 1] = 0;

    if (ioctl(sockfd, SIOCGIFADDR, &ifr) < 0)
    {
        printf("ioctl error\n");
        close(sockfd);
        return ret;
    }

    memcpy(&sin, &ifr.ifr_addr, sizeof(sin));
    int ip_len = snprintf(_ip, 32, "%s", inet_ntoa(sin.sin_addr));

    close(sockfd);
 ret = ip_len;

return ret;
}

int main(int argc, char **argv)
{
    char ip_str[32] = {0};
    get_local_ip("wlan1", ip_str);
    printf("ip = %s\n", ip_str);

    return0;
}
```

## 7. 文件操作
文件操作平时用得很多，为了方便使用，可以自己根据实际需要再封装一层：

代码：

```C
#include <stdio.h>

static int file_opt_write(const char *filename, void *ptr, int size)
{
    FILE *fp;
    size_t num;

    fp = fopen(filename, "wb");
    if(NULL == fp)
    {
        printf("open %s file error!\n", filename);
        return-1;
    }

    num = fwrite(ptr, 1, size, fp);
    if(num != size)
    {
        fclose(fp);
        printf("write %s file error!\n", filename);
        return-1;
    }

    fclose(fp);

    return num;
}

static int file_opt_read(const char *filename, void *ptr, int size)
{
    FILE *fp;
    size_t num;

    fp = fopen(filename, "rb");
    if(NULL == fp)
    {
        printf("open %s file error!\n", filename);
        return-1;
    }

    num = fread(ptr, 1, size, fp);
    if(num != size)
    {
        fclose(fp);
        printf("write %s file error!\n", filename);

        return-1;
    }
    fclose(fp);

    return num;
}

typedefstruct _test_struct
{
char a;
char c;
 short b;
int d;
}test_struct;

int main(int arc, char *argv[])
{
    #define FILE_NAME  "./test_file"

    test_struct write_data = {0};
    write_data.a = 1;
    write_data.b = 2;
    write_data.c = 3;
    write_data.d = 4;
    printf("write_data.a = %d\n", write_data.a);
    printf("write_data.b = %d\n", write_data.b);
    printf("write_data.c = %d\n", write_data.c);
    printf("write_data.d = %d\n", write_data.d);
    file_opt_write(FILE_NAME, (test_struct*)&write_data, sizeof(test_struct));

    test_struct read_data = {0};
    file_opt_read(FILE_NAME, (test_struct*)&read_data, sizeof(test_struct));
    printf("read_data.a = %d\n", read_data.a);
    printf("read_data.b = %d\n", read_data.b);
    printf("read_data.c = %d\n", read_data.c);
    printf("read_data.d = %d\n", read_data.d);

return0;
}
```

## 8. 进度条
有时候，加上进度条可以比较方便知道当前的下载进度、写入文件的进度等。

代码：

```C
#include <stdio.h>
#include <string.h>
#include <unistd.h>

typedefstruct _progress
{
    int cur_size;
    int sum_size;
}progress_t;

void progress_bar(progress_t *progress_data)
{
    int percentage = 0;
    int cnt = 0;
    char proc[102];

    memset(proc, '\0', sizeof(proc));

    percentage = (int)(progress_data->cur_size * 100 / progress_data->sum_size);
    printf("percentage = %d %%\n", percentage);

    if (percentage <= 100)
    {
        while (cnt <= percentage)
        {
            printf("[%-100s] [%d%%]\r", proc, cnt);
            fflush(stdout);
            proc[cnt] = '#';
            usleep(100000);
            cnt++;
        }

    }
    printf("\n");
}

int main(int arc, char *argv[])
{
    progress_t progress_test = {0};

    progress_test.cur_size = 65;
    progress_test.sum_size = 100;
    progress_bar(&progress_test);

    return0;
}
```

## 9.日志输出
日志输出常常需要带一些格式。最简单的方式如：

```C
#include <stdio.h>

#define LOG_D(fmt, args...) do\
                            {\
                                printf("<<File:%s  Line:%d  Function:%s>> ", __FILE__, __LINE__, __FUNCTION__);\
                                printf(fmt, ##args);\
                            }while(0)

int main(int arc, char *argv[])
{
    char ch = 'a';
    char str[10] = "ZhengN";
    float float_val = 10.10;
    int num = 88;
    double double_val = 10.123456;
    LOG_D("字符为 %c \n", ch);
    LOG_D("字符串为 %s \n" , str);
    LOG_D("浮点数为 %f \n", float_val);
    LOG_D("整数为 %d\n" , num);
    LOG_D("双精度值为 %lf \n", double_val);
    LOG_D("八进制值为 %o \n", num);
    LOG_D("十六进制值为 %x \n", num);

return0;
}
```

## 10.后台运行生成core文件
方便大家使用corefile文件定位bug。

```C

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>

#define SHELL_CMD_CONF_CORE_FILE    "echo /var/core-%e-%p-%t > /proc/sys/kernel/core_pattern"
#define SHELL_CMD_DEL_CORE_FILE     "rm -f /var/core*"

static int enable_core_dump(void)
{
    int ret = -1;
    int resource = RLIMIT_CORE;
    struct rlimit rlim;

    rlim.rlim_cur = 1 ? RLIM_INFINITY : 0;
    rlim.rlim_max = 1 ? RLIM_INFINITY : 0;

    system(SHELL_CMD_DEL_CORE_FILE);

    if (0 != setrlimit(resource, &rlim))
    {
        printf("setrlimit error!\n");
        return-1;
    }
    else
    {
        system(SHELL_CMD_CONF_CORE_FILE);
        printf("SHELL_CMD_CONF_CORE_FILE\n");
        return0;
    }

    return ret;
}

int main(int argc, char **argv)
{
    enable_core_dump();

    printf("==================segmentation fault test==================\n");

    int *p = NULL;
    *p = 1234;

    return0;
}
```

## 参考
[实用的嵌入式C功能代码片段，开发更高效~](https://mp.weixin.qq.com/s/1K8CR85cyDqVb37tNlGqMw)