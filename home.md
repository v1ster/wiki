--------------------------------------------------------------------------

```dataviewjs
// 修改其中的时间，可以输出当前离倒计时的时间差。
const setTime = new Date("2022/10/1 18:38:00");
const nowTime = new Date();
const restSec = nowTime.getTime() - setTime.getTime();
const day = parseInt(restSec / (60*60*24*1000));

const str =  day + "天 ^_^"

dv.paragraph(str);

```

# Tags

```dataviewjs
// 生成所有的标签且以 | 分割，修改时只需要修改 join(" | ") 里面的内容。
dv.paragraph(
  dv.pages("").file.tags.distinct().map(t => {return `[${t}](${t})`}).array().join(" | ")
)
```

# List

```dataview
table tags, date, categories
from "docs" 
sort date DESC
```

```dataviewjs
// 只要在任务后边加上时间（格式为 2020-01-01 ，就会在显示所有的任务的同时对应生成对应的倒计时之差
dv.paragraph(
  dv.pages("").file.tasks.array().map(t => {
   const reg = /\d{4}\-\d{2}\-\d{2}/;
 var d = t.text.match(reg);
 if (d != null) {
   var date = Date.parse(d);
   return `- ${t.text} -- ${Math.round((date - Date.now()) / 86400000)}天`
 };
 return `- ${t.text}`;
  }).join("\n")
)

```
```dataviewjs

```


# Category

```dataviewjs
// 基于文件夹聚类所有的标签。
for (let group of dv.pages("").filter(p => p.file.folder != "").groupBy(p => p.file.folder.split("/")[0])) {
  dv.paragraph(`## ${group.key}`);
  dv.paragraph(
    dv.pages(`"${group.key}"`).file.tags.distinct().map(t => {return `[${t}](${t})`}).array().sort().join(" | "));
}
```
