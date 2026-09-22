"""Minimal smoke test for video-gen-config (stdlib + numpy)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from video_gen_config import VideoConfig, ConfigManager


def test_config_defaults_and_roundtrip():
    cfg = VideoConfig()
    assert cfg.fps == 30
    assert cfg.style_preset == "cinematic"
    d = cfg.to_dict()
    assert d["fps"] == 30 and d["image_width"] == 1920
    cfg2 = VideoConfig.from_dict(d)
    assert cfg2 == cfg


def test_config_manager_presets():
    mgr = ConfigManager()
    presets = mgr.list_presets()
    assert len(presets) > 0
    cfg = mgr.get_preset(presets[0])
    assert isinstance(cfg, VideoConfig)
    assert len(mgr.list_styles()) > 0
    assert isinstance(mgr.list_themes(), list)  # theme map ships empty


def test_custom_config():
    mgr = ConfigManager()
    cfg = mgr.create_custom_config(fps=60, style_preset="anime")
    assert cfg.fps == 60
    assert cfg.style_preset == "anime"
