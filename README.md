# pairwise-taa-upscale

快速转身和细密条纹时画面拖影、鬼影、边缘闪烁：TAA 只用上一帧颜色；抖动序列固定；历史长度按帧数；深度阈值用固定值；运动矢量只算相机；透明物体不写 reactive mask；锐化在 TAA 前；分辨率切换不重置历史；HDR 亮度参与权重；VR 双眼历史共享。render/taa_upscale.py 是核心，tests/test_taa_upscale.py 15个红。要修的是：邻帧重投影；Halton 抖动；时间自适应历史；深度/法线阈值；物体运动矢量；reactive mask；后置锐化；分辨率切换重置；亮度裁剪；双眼独立历史。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
