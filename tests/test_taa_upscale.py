import pytest
from render import taa_upscale as mod

CASES = [
    ("reproject_add", "m.reproject((0.2, 0.3), (0.1, -0.1)) == approx((0.3, 0.2))"),
    ("reproject_zero", "m.reproject((0.2, 0.3), (0.0, 0.0)) == approx((0.2, 0.3))"),
    ("halton_mid", "m.jitter(3, 2) == approx(0.5)"),
    ("halton_zero", "m.jitter(0, 2) == approx(0.0)"),
    ("history_short", "m.history_length(0.016, 60) == approx(0.96)"),
    ("history_zero", "m.history_length(0.0, 60) == approx(0.0)"),
    ("threshold_scale", "m.depth_threshold(10.0) == approx(1.0)"),
    ("motion_sum", "m.object_motion((1.0, 0.0), (0.0, 1.0)) == (1.0, 1.0)"),
    ("mask_value", "m.reactive_mask(0.5) == approx(0.5)"),
    ("sharpen_value", "m.sharpen_after(1.0, 2.0) == approx(2.0)"),
    ("resize_true", "m.reset_resize(1280, 1920) is True"),
    ("resize_false", "m.reset_resize(1920, 1920) is False"),
    ("clip_high", "m.clip_luminance(10.0, 4.0) == approx(4.0)"),
    ("clip_low", "m.clip_luminance(2.0, 4.0) == approx(2.0)"),
    ("stereo_right", "m.stereo_history(1) == 1")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
