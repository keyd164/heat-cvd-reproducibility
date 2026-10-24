# Heat CVD reproducibility

本公有仓库分别提供关键代码包和数据包，对应2026年10月23日作者修订版本；过程文件未上传。

- [代码包](heat-cvd-code.zip)：模型、条件转换、统计比较、绘图和上游气候处理代码；包含依赖、运行说明及分析口径。
- [数据包](heat-cvd-data.zip)：历史分析面板、自然强迫年度暴露、SSP三模型年度输入、当前图表源数据及数值基准。
- [文件清单与SHA256](FILE_MANIFEST.json)；[压缩包SHA256](SHA256SUMS)。

## 使用

```sh
git clone https://github.com/keyd164/heat-cvd-reproducibility.git
cd heat-cvd-reproducibility
unzip -o heat-cvd-code.zip
unzip -o heat-cvd-data.zip
python -m pip install -r requirements.txt
python code/verify_package.py
Rscript -e 'install.packages("fixest", repos="https://cloud.r-project.org")'
Rscript code/fit_models.R
python code/derive_results.py
```

两个包解压到同一目录后，代码在 `code/`，数据在 `data/`；完整README和数据字典随包提供。解压会将此分发说明替换为完整运行说明。新结果写入Git忽略的 `results/`。

打包后已从输入复现四模型、三个结局主模型、现有lead诊断、历史/自然强迫/SSP汇总及Holm比较，并验证独立ZIP解压和干净Git克隆中的校验。Figure5所有时期比较统一为2041–2060与2081–2100。

本次没有重新进行2000次bootstrap或从全球日尺度网格端到端重算。已报告bootstrap区间作为标记清楚的参考数据提供；原始大规模NetCDF、栅格、草稿、聊天记录、审稿快照、缓存和临时输出均未上传。原历史数据保留GBD2021导出标签；GBD2023引用依据作者报告的数值核对，不表示新下载的2023导出。第三方数据仍遵循原提供方条款。
