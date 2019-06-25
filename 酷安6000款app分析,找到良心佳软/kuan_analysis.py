# -*- coding: utf-8 -*-
# @Date    : 2019-06-19
# @Author  : czr

import pandas as pd
import numpy as np
from pyecharts import Bar, Grid, configure
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 配置pd
# 小数精度显示设置
pd.set_option('precision', 1)

# 配置matplotlib绘图风格
plt.style.use('ggplot')
# 颜色
colors = '#000000'
colorline = '#CC2824'
# 字体
my_font = font_manager.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
fontsize_title = 20
fontsize_text = 10

# 配置pyecharts绘图风格
configure(global_theme='dark')  # 设置 pyecharts 绘图主题
# pyecharts 图表选项设置
legend_text_size = 16,  # 图例文字大小
legend_text_color = '#aaa'  # 图例文字颜色

# 数据清洗部分
# 读取数据
data = pd.read_csv('kuan.csv')
# 增加一行
data['score_total'] = data['score'] * data['download']
# 下载量分布
bins = [0, 10, 100, 500, 10000]
group_names = ['<10晚', '10-100万', '100-500万', '>500万']
dl_fenbu = pd.cut(data['download'], bins, labels=group_names)
dl_fenbu = dl_fenbu.value_counts()
# 得分分布
bins = [0, 3, 4, 4.5, 5]
group_names = ['<=3分', '中品(3-4分)', '良品(4-4.5分)', '精品(4.5-5分)']
score_fenbu = pd.cut(data.score, bins, labels=group_names)
score_fenbu = score_fenbu.value_counts()


# 1.分析下载量
def analysis_download(df):
    # 画图
    bar = Bar('App 下载数量区间分布', '绝大部分App下载量低于10万')
    bar.add(
        'App数量(个)',
        list(df.index),
        list(df.values),
        is_label_show=True,
    )
    bar.render('下载量分布.html')


# 2. 分析得分
def analysis_score(df):
    # 画图
    bar = Bar('App 得分区间分布', '相当一部分App都在4分以上')
    bar.add(
        'App数量(个)',
        list(df.index),
        list(df.values),
        is_label_show=True,
    )
    bar.render('得分分布.html')


# 3.下载量top20的总分,评分和下载量
# 中文无法显示在pd.plot中
def analysis_top20(df):
    # 下载量top20
    d_t20 = df.sort_values(by='download', ascending=False)[:20][::-1]
    d_t20 = d_t20[['name', 'download', 'score', 'score_total']].reset_index(drop=True).set_index(d_t20.name)
    return d_t20


# 4.评分top20 的总分,评分和下载量
def analysis_tops20(df):
    d_ts20 = df.sort_values(by=['score','download'], ascending=False)[:20]
    d_ts20 = d_ts20[['name', 'download', 'score', 'score_total']].reset_index(drop=True).set_index(d_ts20.name)[::-1]
    return d_ts20


# 5.分类情况
def analysis_category(df, n):
    # 关键词
    dic = {
        1: '文件|系统|清理|输入法|安全|辅助|桌面|插件|锁屏',
        2: '社交|聊天|微博|论坛',
        3: '阅读|新闻|小说|科普',
        4: '文档|记事本',
        5: '视频|音乐|播放器|直播|电台',
        6: '浏览器|通讯录|流量|通知|邮箱|WiFi',
        7: '拍照|美图|图库',
        8: '导航|地图|旅游|酒店|车|购',
        9: 'Xposed|xposed',
        10: '酷友作品'
    }
    # 先筛选
    df = df[(df.download > 1) & (df.score >= 4)]
    col = data['score_total']
    # score_total 标准化为 0-1000 分
    data['score_total'] = (col - col.min()) / (col.max() - col.min()) * 1000

    category = dic[n]
    d_c = df[df.tags.str.contains(category)].sort_values(by='score_total', ascending=False)[:20]
    d_c = d_c[['name', 'score_total', 'score', 'download']].set_index(d_c.name)[::-1]
    return d_c


# 画图
def draw_ssd(df, str):
    fig = plt.figure(figsize=(18, 16), dpi=100)
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)

    y1 = 'score_total'
    y2 = 'score'
    y3 = 'download'

    df.plot(
        ax=ax1,
        y=y1,
        kind='barh',
        color='#C44B37',
        subplots=True,  # 设置子图
        sharey=True,  # 共享y轴
        # xlim = (0,5.5),
        fontsize=11,
        rot=30,
    )

    df.plot(
        ax=ax2,
        y=y2,
        kind='barh',
        color='#2EC7C9',
        subplots=True,
        sharey=True,
        xlim=(0, 5.3),
        fontsize=11,
    )
    ax2.vlines(4, 0, 1, transform=ax2.get_xaxis_transform(), colors='r', ls='--')
    df.plot(
        ax=ax3,
        y=y3,
        kind='barh',
        color='#2EC7C9',
        subplots=True,
        sharey=True,
        fontsize=11,
    )

    for y, x in enumerate(list(df[y1].values)):
        ax1.text(x, y, '%s' %
                 round(x, 0), ha='left',va= 'center', color=colors,fontsize=12)
    for y, x in enumerate(list(df[y2].values)):
        ax2.text(x, y, '%s' %
                 round(x, 1), ha='left',va= 'center', color=colors,fontsize=12)
    for y, x in enumerate(list(df[y3].values)):
        ax3.text(x, y , '%s' %
                 round(x, 1), ha='left',va= 'center', color=colors,fontsize=12)

    ax1.legend(loc='lower right')  # 更改图例位置
    ax2.legend(loc='lower right')  # 更改图例位置
    ax3.legend(loc='lower right')  # 更改图例位置
    # 设置总标题
    fig.suptitle(str, fontsize=25)

    plt.savefig(f'{str}.png', dpi=300)

    #plt.show()




if __name__ == '__main__':
    data = data
    # 下载量
    analysis_download(dl_fenbu)
    # 得分分布
    analysis_score(score_fenbu)
    # 下载top_20
    draw_ssd(analysis_top20(data), '下载量-Top20的App')
    # 评分top20
    draw_ssd(analysis_tops20(data), '得分-Top20的App')
    # 分类
    cgs = {
         1 : '系统工具',
         2 : '社交聊天',
         3 : '资讯阅读',
         4 : '文档写作',
         5 : '影音娱乐',
         6 : '通讯网络',
         7 : '摄影图片',
         8 : '交通购物',
         9 : 'Xposed 模块',
         10 : '实用工具',
    }

    for k, v in cgs.items():
        draw_ssd(analysis_category(data, k), 'category{}: {} 软件精选'.format(k, v))