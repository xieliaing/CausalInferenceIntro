# 因果推断：从概念到实践

![img](./chapters/data/img/brave-and-true.png)



本系列是 [Causal Inference for the Brave and True](https://zenodo.org/badge/latestdoi/255903310) 这本书 ![DOI](https://zenodo.org/badge/255903310.svg)的中文翻译版，由巴西Nubank的Staff Data Scientist [Matheus Facure](https://www.linkedin.com/in/matheus-facure-7b0099117/) 所著。该书用平实的语言和严谨的数学，以及实用的Python代码，结合经济学与社会学的策略评估和敏感性分析应用，对因果推断最新的概念、理论及实践进行了非常全面的介绍，既适合初学者入门，同时也适合技术管理专家回顾相关领域的整体知识。该书英文原版的Jupyter Notebooks可以由[该Github地址](https://github.com/matheusfacure/python-causality-handbook)获取。

本书主要基础是计量经济学，吸收了非常多学者，包括 [Joshua Angrist](https://economics.mit.edu/faculty/angrist), [Alberto Abadie](https://economics.mit.edu/faculty/abadie)，[Christopher Walters](https://www.econ.berkeley.edu/faculty/4678)，[Miguel Hernan](https://www.hsph.harvard.edu/miguel-hernan/) 和 [Jamie Robins](https://www.hsph.harvard.edu/james-robins/) 等，在这方面的最新研究，主要参考了以下资料：

* [Cross-Section Econometrics](https://www.aeaweb.org/conference/cont-ed/2017-webcasts)
* [Mastering Mostly Harmless Econometrics](https://www.aeaweb.org/conference/cont-ed/2020-webcasts)
* [Mostly Harmless Econometrics](https://www.mostlyharmlesseconometrics.com/)
* [Mastering 'Metrics](https://www.masteringmetrics.com/)
* [Causal Inference Book](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

这里非常感谢[Matheus Facure](https://www.linkedin.com/in/matheus-facure-7b0099117/)同意我翻译该书的中文译本。中文翻译版会在两个地方同步发布：

1. 方便国际读者的 [Github地址](https://github.com/xieliaing/CausalInferenceIntro)
2. 方便国内读者的 [Gitee地址](https://gitee.com/xieliaing/causal-inference-intro-gitee)


第一部分中文翻译版的进度按照如下时间线开展：

章节 | 名称 | 出稿日期 |
--- | --- | ---
1 |     第一章: 因果关系入门 |  2021-11-07 
2 |     第二章: 随机实验 |  2021-11-13 
3 |     第三章: 统计学回顾：最危险的公式|   2021-11-25 
4 |     第四章: 图因果模型|   2021-11-18 
5 |     第五章: 线性回归超常的有效性|  2021-12-05 
6 |     第六章: 分组和虚拟变量|  2021-12-12 
7 |     第七章: 混淆变量之外|  2021-12-19 
8 |     第八章: 工具变量|  2021-12-26 
9 |     第九章: 不服从与LATE效应|  2021-12-30
10 |    第十章: 匹配|  2022-01-10 
11 |    第十一章: 倾向性打分|   2022-01-22
12 |    第十二章: 双稳健估计|   2022-01-29 
13 |    第十三章: 面板数据和固定效应|   2022-2-13 
14 |    第十四章: 双重差分|   2022-02-20 
15 |    第十五章: 合成控制|   2022-02-27 
16 |    第十六章: 断点回归设计|   2022-03-06
17 |    第十七章: 预测模型|   2022-03-19
18 |    第十八章: 异质干预效应与个性化|   2022-03-26
19 |    第十九章: 评估因果模型|   2022-08-31
20 |    第二十章: 即插即用的估计量|   2022-10-10
21 |    第二十一章: 元学习器|   2022-11-15

该书遵守[MIT License](./LICENSE)。

## 本地运行指南 2026-03-02

### 安装 python 及相关程序

建议使用 **Python 3.10 ~ 3.12**。Windows 用户优先推荐安装 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)，也可以使用官方 Python。

此外建议安装：

- [Git](https://git-scm.com/)
- [VS Code](https://code.visualstudio.com/)（可选，但推荐）
- Jupyter（会在下方通过 `pip` 安装）

### 获取项目代码

```bash
git clone https://github.com/xieliaing/CausalInferenceIntro.git
cd CausalInferenceIntro
```

### 创建并激活虚拟环境（推荐）

#### 方案 A：使用 conda（推荐）

```bash
conda create -n causal-intro python=3.11 -y
conda activate causal-intro
```

#### 方案 B：使用 venv

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux：

```bash
source .venv/bin/activate
```

### 安装依赖

项目中的 Notebook 主要依赖如下（可先安装最小集合）：

```bash
pip install -U pip
pip install jupyter notebook jupyterlab numpy pandas scipy matplotlib seaborn scikit-learn statsmodels linearmodels graphviz
```

如果你需要运行翻译脚本 `AutoTranslateNotebooks.py`，再额外安装：

```bash
pip install nbformat googletrans==4.0.0-rc1
```

或者你可以直接使用如下命令安装本项目所需的依赖项：

```bash
pip install -r requirements.txt
```

### 启动并运行 Notebook

在仓库根目录运行：

```bash
jupyter lab
```

或：

```bash
jupyter notebook
```

然后在浏览器中打开 `chapters/` 目录，按顺序运行对应章节。

### 可选：运行翻译脚本

```bash
python AutoTranslateNotebooks.py "chapters/01 第一章-因果关系入门.ipynb" "chapters/01 第一章-因果关系入门_机器翻译.ipynb"
```

说明：

- 第 1 个参数是输入 Notebook
- 第 2 个参数是输出 Notebook
- 若出现翻译 API 报错，请稍后重试或更换网络环境

### 常见问题

1. **命令找不到（python / pip / jupyter）**
	- 请确认已激活虚拟环境，或将 Python 加入 PATH。

2. **PowerShell 无法激活 venv**
	- 可临时执行：
	```powershell
	Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
	```

3. **Notebook 打开后缺包报错**
	- 在当前环境补装缺失包，例如：
	```bash
	pip install <package_name>
	```

4. **图形模型相关章节绘图失败**
	- 请确认本机已安装 Graphviz 程序，并将其加入系统 PATH。