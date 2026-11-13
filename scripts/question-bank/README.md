# IELTS Path · 机考题库测试版

当前版本：剑桥雅思 21 Academic Test 1 的本机机考式练习。未发布、未接入正式应用或云端学习记录。

## 当前功能

- 听读各40道结构化题目：表格与摘要内嵌填空、单选、最多两项多选、判断、匹配。
- 三篇阅读原文与题目分栏独立滚动；高亮、笔记、题号跳转、待检查标记、完成状态。
- 写作两任务独立作文区与字数统计，Task 1保留原书图表；口语题卡、本地录音与文字复盘。
- 可暂停、重置的本科倒计时；交卷核对原始正确题数，支持继续订正。音频可回放，属于练习模式。
- 自动保存当前浏览器草稿、JSON导出。首次从上一版草稿恢复答案和写说文本；不覆盖正式站点数据。
- 资料分类脚本可按册数、文件类型、A/G标识生成索引；没有明确标识的内容保留待核对状态。

## 重建预览

需要 Python 3.9+、`pypdf`、`Pillow` 和 Poppler 的 `pdftoppm`（在 PATH 中）。源 PDF 与音频由使用者在本机提供，不包含在仓库中。

```sh
python3 -m pip install pypdf Pillow
python3 scripts/question-bank/build_preview.py \
  --pdf '/path/to/剑桥雅思21（A类）(1).pdf' \
  --audio-dir '/path/to/剑21音频' \
  --source-root '/path/to/剑4-19原书+解析+音频' \
  --source-root '/path/to/剑20完整' \
  --source-root '/path/to/剑21完整版'
python3 -m http.server 5184 --bind 127.0.0.1 --directory work/question-preview
```

访问 http://127.0.0.1:5184/ 。音频目录须包含 `Test1-Part1.mp3` 至 `Test1-Part4.mp3`。PDF版本须与当前题页映射一致：Test 1位于物理第11–32页、听读答案位于第118–119页、写作图表位于第30页。其他版本必须重新校准页码。

所有生成文件进入已被Git忽略的 `work/question-preview/`；原文件保持原位。生成过程不读取或上传浏览器学习记录。

## 文件说明

- `computer-preview.html`：当前机考式界面。
- `prepare_computer_test.py`：从原书提取三篇阅读，生成结构化题组并裁出写作图表。
- `answer-keys.json`：与原书核对后的Test 1听读答案，供本地练习判分。
- `classify.py`：只读扫描输入目录，生成分类索引。
- `build_preview.py`：完整重建入口。
- `preview.html`：最初的原书图片预览模板，作为历史参考，不是当前入口。

## 保存与限制

当前草稿键为 `ielts-path-c21-a-t1-computer-v2`；旧版为 `ielts-path-c21-a-t1-preview-v1`。录音仅在当前页面提供回听和下载，不包含在JSON中。导出暂不支持再导入。

本版答案随本地页面数据提供，不能作为独立诊断。仅核对听读原始题数，不预测雅思分数、不自动评分写说、尚未提取详细解析。其他册尚未结构化。

接入正式站点前需配置受保护媒体存储、用户隔离记录与支持40题的保存接口，不能直接复用体验题的20答案/5分限制。保留现有站点身份和私有访问范围。

已验证：JavaScript语法；80题编号与填空编号完整；全对/全空白、多选顺序及重复判分；浏览器表格填写恢复、跨Part题号跳转、多选最多两项、判断题状态和桌面分栏。麦克风录制未实测。
