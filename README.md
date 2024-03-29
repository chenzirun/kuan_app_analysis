# 分析酷安6000款App, 找到良心软件
**摘要**
1.分析动机:如今移动互联网越来越发达, 每个人的对于App的依赖越来越大, 于是App的对于我们的生活的影响也越来越大. 有需求就有生产, 各类App层出不穷, 自然而然也产生了优劣之分, 而我们肯定愿意去使用那些良心的佳软来满足我们的各种需求. 平常我们发掘好软件的渠道无外乎来自于朋友推荐和网络媒体信息流的推荐, 这种方法比较**低效**.于是本文做了这样一个分析.
2.分析方法: 首先爬取著名的搞机爱好者重度使用的应用下载市场[酷安网]上的6000余款App, 并将爬取结果转存为csv格式的文件. 利用Python的数据分析包pandas, numpy来进行数据的清洗, 分析. 最后利用pyecharts, matplotlib等数据可视化软件将数据转化为图标的形式, 更加清晰直观的呈现分析结果.

## 1. 总体情况
先看一下表格的情况

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/1.png)

*我们主要从总体和功能分类这两个维度对App的下载量, 评分, 还有体积等指标进行进行分析*
### 1.1 下载量  的排名
> 首先来看一下 App 的下载量情况，很多时候我们下载一个 App ，下载量是一个非常重要的参考指标，由于绝大多数 App 的下载量都相对较少，直方图无法看出趋势，所以我们择将数据进行分段，离散化为柱状图，绘图工具采用的是 Pyecharts。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/App%20%E4%B8%8B%E8%BD%BD%E6%95%B0%E9%87%8F%E5%8C%BA%E9%97%B4%E5%88%86%E5%B8%83.png)

可以看到多达 5117 款（占总数 85%）App 的下载量不到 10 万， 而下载量超过 500 万的仅有 20 款，开发一个要想盈利的 App ，用户下载量尤为重要，从这一点来看，大部分 App 的处境都比较尴尬，至少是在酷安平台上。

> 接下来，我们看看 **下载量最多的** 20 款 App 是哪些：

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/%E4%B8%8B%E8%BD%BD%E9%87%8F-Top20%E7%9A%84App.png)

可以看到，这里「酷安」App 以 5000 万+ 次的下载量遥遥领先，是第二名微信 2700 万下载量的近两倍，这么巨大的优势也很容易理解，毕竟是自家的 App，如果你手机上没有「酷安」，说明你还不算是一个真正的「搞机爱好者」，从图中我们还可以看出以下几点信息：

TOP 20 款 App 中，很多都是 装机必备，算是比较大众型的 App。

右侧 App 评分图中可以看到仅有 5 款 App 评分超过了 4 分（5 分制），绝大多数的评分都不到 3 分，甚至到不到 2 分，到底是因为这些 App 开发者做不出好 App 还是根本不想做出来？

相较于其他 App，RE 管理器、绿色守护 这几款非常突出，其中 RE 管理器在如此高的下载量下，仍然能够得到 4.8 分（最高分）并且体积只有几 M，实属难得，什么是「良心 App」，这类就是。

### 1.2 评分排名
> 接下来，我们看看 App 的总体得分情况。这里，将得分分为了以下 4 个区间段，并且为不同分数定义了相应的等级。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/App%20%E5%BE%97%E5%88%86%E5%8C%BA%E9%97%B4%E5%88%86%E5%B8%83.png)

可以发现这么几点有意思的现象：

3 分以下的软件非常少，只占不到 10%，而之前下载量最多的 20 款 APP 中，微信、QQ、淘宝、支付宝等大多数软件的得分都不到 3 分，这就有点尴尬了。
中品也就是中等得分的 App 数量最多。
4 分以上的 高分 APP 数量占了近一半（46%），可能是这些 App 的确还不错，也可能是由于评分数量过少，为了优中选优，后续有必要设置一定筛选门槛。

接下来，我们看看评分最高的 20 款 App 有哪些，很多时候我们下载 App 都是跟着「哪个评分高，下载哪个」这种感觉走。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/%E5%BE%97%E5%88%86-Top20%E7%9A%84App.png)

可以看到，评分最高的 20 个 App，它们都得到了 4.8 分 ，包括：RE 管理器（再次出现）、Pure 轻雨图标包等，还有一些不太常见，可能这些都是不错的 App，不过我们还需要结合看一下下载量，它们的下载量都在 1 万以上，有了一定的下载量，评分才算比较可靠，我们就能放心的下载下来体验一下了。

经过上面的总体分析，我们大致发现了一些不错的 App ，但还不够，所以接下来将进行细分并设置一定筛选条件。

## 2.对App进行功能分类, 筛选出各个分类下的优质App
> 按照 App 功能和日常使用场景，将 App 分为以下 9 大类别，然后 从每个类别中筛选出 20 款最棒的 App。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/3.png)

为了尽可能找出最好的 App，这里不妨设置 3 个条件：

· 评分不低于 4 分
· 下载量不低于 1 万
· 设置一个总分评价指标（总分 = 下载量 * 评分），再标准化为满分 1000 分，作为 App 的排名参照指标。
经过评选之后，我们依次得到了各个类别下分数最高的 20 款 App，这些 App 大部分的确是良心软件。

### 2.1 系统工具
系统工具包括了：输入法、文件管理 、系统清理、桌面、插件、锁屏等。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category1:%20%E7%B3%BB%E7%BB%9F%E5%B7%A5%E5%85%B7%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

可以看到，第一名是大名鼎鼎的老牌文件管理器「RE 管理器」，仅有 5 M 大小的它除了具备普通文件管理器的各项功能以外，最大的特点是能够卸载手机自带的 App，不过需要 Root。

「ES 文件浏览器」的文件分析器功能非常强大，能够有效清理臃肿的手机空间。

「一个木函」这款 App 就比较牛逼了，正如它的软件介绍「拥有很多，不如有我」所说，打开它你能发现它提供了好几十项实用功能，比如：翻译、以图搜图、快递查询、制作表情包等等。

再往下的「Super SU」、「存储空间清理」、「镧」、「MT 管理器」、「My Android Tools」都力荐，总之，这份榜单上的 App 可以说都值得进入你的手机 App 使用名单。

### 2.2 社交聊天

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category2:%20%E7%A4%BE%E4%BA%A4%E8%81%8A%E5%A4%A9%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

社交聊天类中， 「Share 微博客户端」位居第一，作为一款第三方客户端 App，它自然有比官方版本好的地方，比如相比正版 70M 的体积，它只有其十分之一大小，也几乎没有广告，还有额外强大的诸多功能，如果你爱刷微博，那么不妨尝试下这款「Share」。

「即刻」这款 App 也相当不错，再往下还能看到前阵子很火的「子弹短信」，宣称将要取代微信，看来短期内应该是做不到了。

你可能会发现，这份社交榜单上没有出现「知乎」、「豆瓣」、「简书」这类常见的 App，是因为它们的评分都比较低，分别只有 2.9分、3.5分和 2.9 分，自然进入不了这份名单，如果你一定想用它们，推荐去使用它们的第三方客户端或者历史版本。

### 2.3 资讯阅读

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category3:%20%E8%B5%84%E8%AE%AF%E9%98%85%E8%AF%BB%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

可以看到，在资讯阅读类中，「静读天下」牢牢占据了第一名，我之前专门写过一篇文章介绍它：安卓最强阅读器。

同类别中的「多看阅读」、「追书神器」、「微信读书」也都进入了榜单。

另外，如果你经常为不知道去哪里下载电子书而头疼，那不妨试一下「搜书大师」、「老子搜书」。


### 2.4 文档写作
我们时常需要在手机上写作、做备忘录，那么自然需要好的文档写作类 App

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category4:%20%E6%96%87%E6%A1%A3%E5%86%99%E4%BD%9C%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

「印象笔记」就不用多说了，我觉得最好用的学习总结类 App，免费版一般也够用，但是推荐订阅会员，遇到双十一、周年庆这种日子，会有 6折优惠，一年不到 100 块还是很划算了。

如果你喜欢使用 Markdown 写作，那么「纯纯写作」这款精巧的 App 应该会很适合你。

体积不到 3M 却拥有云备份、生成长图、中英文自动空格等数十项功能，即使这样，仍然保持了蕴繁于简的设计风格，这大概就是两三个月之内，下载量就从两三万飙升了十倍的原因，而这款 App 的背后是一位 牺牲了几年的业余时间不断开发和更新的大佬，值得敬佩。


### 2.5 影音娱乐

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category5:%20%E5%BD%B1%E9%9F%B3%E5%A8%B1%E4%B9%90%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

接下来是影音娱乐版块，网易家的「网易云音乐」毫无压力地占据头名，难得的大厂精品。

如果你爱玩游戏，那么 「Adobe AIR」应该尝试一下。

如果你很文艺，那么应该会喜欢「VUE」这款短视频拍摄 App，创作好以后发到朋友圈绝对能装逼。

最后一位的「海贝音乐」很赞，最近发现它有一个强大的功能是结合百度网盘使用，它能够自动识别音频文件然后播放。


### 2.6 通讯网络
下面到了通讯网络类别，这个类别主要包括：浏览器、通讯录、通知、邮箱等小类。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category6:%20%E9%80%9A%E8%AE%AF%E7%BD%91%E7%BB%9C%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

浏览器，我们每个人手机上都有，用的也五花八门，有些人就用手机自带的浏览器，有些人用 Chrome、火狐这类大牌浏览器。

不过你会发现榜单上的前三位你可能听都没听过，但是它们真的很牛逼，用「极简高效、清爽极速」来形容再适合不过，其中 「Via 」和 「X 浏览器」 体积不到 1M ，真正的「麻雀虽小、五脏俱全」，强烈推荐。


### 2.7 摄影图片
拍照修图也是我们常用的功能。

也许你有自己的图片管理软件，但是这里要强烈推荐第一名「快图浏览」这款 App，只有 3M 大小的它，能够瞬间发现和加载上万张图片，如果你是拍照狂魔，用它打开再多的照片也能秒开，另外还拥有隐藏私密照片、自动备份百度网盘等功能。它是我使用时间最久的 App 之一。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category7:%20%E6%91%84%E5%BD%B1%E5%9B%BE%E7%89%87%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)


### 2.8 出行交通购物
这个类别中，排名第一的居然是 12306，一提起它，就会想起那一张张奇葩的验证码。不过这里的 App 不是官网的 ，而是第三方开发的。最牛逼的功能应该就是「抢票了」，如果你还在靠发朋友圈来抢票的话，那不妨试一下它。

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category8:%20%E4%BA%A4%E9%80%9A%E8%B4%AD%E7%89%A9%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

### 2.9 Xposed 插件

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category9:%20Xposed%20%E6%A8%A1%E5%9D%97%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

这个类别是 Xposed，很多人应该不太熟悉，但是一提微信上的抢红包、防撤回功能，应该很多人就知道了。这些牛逼又不同寻常的功能就用到了 Xposed 框架里的各种模块功能。这个框架由国外著名的 XDA 手机论坛，你经常听到的一些所谓由 XDA 大神破解的软件，就是来自这个论坛。

简单地说就是，安装了 Xposed 这个框架之后，就可以在里面安装一些好玩有趣的插件，有了这些插件，你的手机就能实现更多更大的功能。比如：能够去除广告、破解 App 付费功能、杀死耗电的自启动进程、虚拟手机定位等功能。

不过使用这个框架和这些插件需要刷机、ROOT，门槛有点高。

### 2.10 实用工具

![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/category10:%20%E5%AE%9E%E7%94%A8%E5%B7%A5%E5%85%B7%20%E8%BD%AF%E4%BB%B6%E7%B2%BE%E9%80%89.png)

这里排名靠前的一个木函, 是一个轻量级的多功能的App, 能处理图片,文字等等. 像天气, 浏览器, 遥控器, 壁纸等等软件都在实用工具的行列


## 3. 小结

本文使用 Python的pandas, numpy, pyecharts, matplotlib等等工具分析了酷安网的 6000 款 App.
由于网页版的 App 数量比 App 中的少，所以还有很多好用的 App 没有包括进来，比如 Chrome 、MX player、Snapseed 等，建议使用酷安 App，那里有更多好玩的东西。
通过这篇文章，我们完成一个项目从抓取到分析的过程，文中涉及了很多精品佳软，如有兴趣可以去尝试下载体验一下，为了更方便你，我这里也收集好了 24 款精品 App。
![avatar](https://github.com/missLH/kuan_app_analysis/blob/master/%E9%85%B7%E5%AE%896000%E6%AC%BEapp%E5%88%86%E6%9E%90%2C%E6%89%BE%E5%88%B0%E8%89%AF%E5%BF%83%E4%BD%B3%E8%BD%AF/2.png)
