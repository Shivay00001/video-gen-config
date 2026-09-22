"""
Video Generator Configuration and Enhancement System
Extended features, effects, and customization options
"""

import json
from typing import Dict, List
from dataclasses import dataclass, asdict
import numpy as np

# ============================================================================
# EXTENDED STYLE LIBRARY (No LLM)
# ============================================================================

EXTENDED_STYLES = {
    # Music Video Styles
    "music_video_pop": {
        "prompt": "professional music video scene, vibrant colors, dynamic composition, studio lighting, 4k cinematic",
        "negative": "amateur, low quality, static, boring",
        "effects": ["color_vibrance", "motion_blur"],
        "transition_speed": "medium"
    },
    "music_video_rock": {
        "prompt": "energetic rock concert scene, stage lights, dramatic atmosphere, intense energy, professional cinematography",
        "negative": "calm, peaceful, soft, low quality",
        "effects": ["high_contrast", "vignette"],
        "transition_speed": "fast"
    },
    "music_video_electronic": {
        "prompt": "futuristic electronic music scene, neon lights, digital aesthetics, cyberpunk atmosphere, 4k",
        "negative": "organic, natural, vintage, low quality",
        "effects": ["glow", "chromatic_aberration"],
        "transition_speed": "fast"
    },
    
    # Narrative Styles
    "documentary": {
        "prompt": "documentary style scene, realistic photography, natural lighting, authentic atmosphere, professional",
        "negative": "artistic, stylized, fake, low quality",
        "effects": ["subtle_grain", "slight_desaturation"],
        "transition_speed": "slow"
    },
    "storytelling": {
        "prompt": "cinematic storytelling scene, emotional atmosphere, beautiful composition, film photography",
        "negative": "snapshot, amateur, low quality",
        "effects": ["film_grain", "letterbox"],
        "transition_speed": "medium"
    },
    
    # Podcast/Talk Styles
    "podcast_minimal": {
        "prompt": "minimal abstract background, soft gradients, professional clean design, modern aesthetic",
        "negative": "busy, cluttered, distracting, low quality",
        "effects": ["subtle_motion"],
        "transition_speed": "slow"
    },
    "podcast_dynamic": {
        "prompt": "dynamic visual background, flowing shapes, energetic atmosphere, modern design",
        "negative": "static, boring, plain, low quality",
        "effects": ["flowing_motion", "color_shift"],
        "transition_speed": "medium"
    },
    
    # Artistic Styles
    "anime": {
        "prompt": "anime art style scene, vibrant colors, beautiful illustration, studio quality animation",
        "negative": "realistic, photographic, low quality, blurry",
        "effects": ["cel_shading", "enhanced_saturation"],
        "transition_speed": "medium"
    },
    "watercolor": {
        "prompt": "watercolor painting scene, soft colors, artistic brush strokes, dreamy atmosphere",
        "negative": "photorealistic, harsh, digital, low quality",
        "effects": ["soft_edges", "texture_overlay"],
        "transition_speed": "slow"
    },
    "oil_painting": {
        "prompt": "oil painting scene, rich colors, textured brush strokes, classical art style",
        "negative": "digital, flat, modern, low quality",
        "effects": ["paint_texture", "dramatic_lighting"],
        "transition_speed": "slow"
    }
}

# Base style map merged with EXTENDED_STYLES in ConfigManager.
# (Was referenced but never defined; empty by default so existing styles work.)
STYLE_MAP = {}

# Scene theme prompt variations, keyed by theme name (e.g. "nature").
# (Was referenced but never defined; empty by default.)
SCENE_THEMES = {}


# ============================================================================
# SCENE EFFECT PRESETS
# ============================================================================

SCENE_EFFECTS = {
    "color_vibrance": {
        "type": "color_adjustment",
        "saturation": 1.3,
        "vibrance": 1.2
    },
    "motion_blur": {
        "type": "motion",
        "blur_amount": 0.3,
        "direction": "horizontal"
    },
    "high_contrast": {
        "type": "color_adjustment",
        "contrast": 1.4,
        "brightness": 1.05
    },
    "vignette": {
        "type": "overlay",
        "strength": 0.4,
        "feather": 0.6
    },
    "glow": {
        "type": "effect",
        "intensity": 0.3,
        "threshold": 0.7
    },
    "chromatic_aberration": {
        "type": "effect",
        "offset": 3,
        "strength": 0.2
    },
    "film_grain": {
        "type": "texture",
        "intensity": 0.15,
        "size": 1
    },
    "letterbox": {
        "type": "overlay",
        "ratio": 2.35,
        "color": "black"
    }
}


# ============================================================================
# TRANSITION LIBRARY
# ============================================================================

TRANSITIONS = {
    "cut": {
        "duration": 0.0,
        "type": "instant"
    },
    "fade": {
        "duration": 0.5,
        "type": "crossfade"
    },
    "dissolve": {
        "duration": 0.8,
        "type": "crossfade"
    },
    "wipe_left": {
        "duration": 0.6,
        "type": "directional",
        "direction": "left"
    },
    "wipe_right": {
        "duration": 0.6,
        "type": "directional",
        "direction": "right"
    },
    "zoom_in": {
        "duration": 0.7,
        "type": "scale",
        "start_scale": 1.0,
        "end_scale": 1.5
    },
    "zoom_out": {
        "duration": 0.7,
        "type": "scale",
        "start_scale": 1.5,
        "end_scale": 1.0
    }
}


# ============================================================================
# PROMPT TEMPLATES BY CONTENT TYPE
# ============================================================================

CONTENT_TEMPLATES = {
    "song_verse": [
        "intimate close-up scene, {emotion} atmosphere, soft focus, {style}",
        "personal moment scene, {emotion} mood, beautiful lighting, {style}",
        "reflective scene, {emotion} feeling, artistic composition, {style}"
    ],
    "song_chorus": [
        "epic wide shot, {emotion} energy, dynamic composition, {style}",
        "powerful scene, {emotion} atmosphere, cinematic scale, {style}",
        "grand visual, {emotion} mood, impressive composition, {style}"
    ],
    "song_bridge": [
        "transitional scene, {emotion} shift, creative composition, {style}",
        "unique perspective, {emotion} change, artistic vision, {style}",
        "contrasting scene, {emotion} evolution, dynamic framing, {style}"
    ],
    "narration_intro": [
        "establishing shot, {emotion} tone, cinematic opening, {style}",
        "introductory scene, {emotion} atmosphere, professional framing, {style}"
    ],
    "narration_body": [
        "supportive visual, {emotion} mood, clear composition, {style}",
        "contextual scene, {emotion} atmosphere, informative framing, {style}"
    ],
    "narration_conclusion": [
        "closing scene, {emotion} resolution, memorable composition, {style}",
        "final visual, {emotion} conclusion, impactful framing, {style}"
    ]
}


# ============================================================================
# ENHANCED CONFIGURATION CLASS
# ============================================================================

@dataclass
class VideoConfig:
    """Complete video generation configuration"""
    # Style settings
    style_preset: str = "cinematic"
    theme: str = "nature"
    custom_style: Dict = None
    
    # Scene settings
    segment_duration: float = 3.0
    min_segment_duration: float = 2.0
    max_segment_duration: float = 5.0
    
    # Image generation
    image_width: int = 1920
    image_height: int = 1080
    inference_steps: int = 20
    guidance_scale: float = 7.5
    
    # Video settings
    fps: int = 30
    bitrate: str = "8000k"
    codec: str = "libx264"
    
    # Effects
    enable_effects: bool = True
    effect_strength: float = 1.0
    
    # Transitions
    transition_mode: str = "auto"  # auto, sync_to_beat, smooth
    
    # Audio sync
    beat_sync: bool = True
    energy_reactive: bool = True
    
    # Subtitles
    subtitle_style: Dict = None
    
    # Advanced
    seed: int = None
    use_cache: bool = True
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)
    
    @classmethod
    def from_json(cls, path: str):
        with open(path, 'r') as f:
            return cls.from_dict(json.load(f))
    
    def save(self, path: str):
        with open(path, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)


# ============================================================================
# PRESET CONFIGURATIONS
# ============================================================================

PRESET_CONFIGS = {
    "music_video_standard": VideoConfig(
        style_preset="music_video_pop",
        theme="urban",
        segment_duration=2.5,
        fps=30,
        beat_sync=True,
        energy_reactive=True
    ),
    
    "podcast_episode": VideoConfig(
        style_preset="podcast_dynamic",
        theme="abstract",
        segment_duration=5.0,
        fps=24,
        beat_sync=False,
        energy_reactive=False
    ),
    
    "documentary": VideoConfig(
        style_preset="documentary",
        theme="nature",
        segment_duration=4.0,
        fps=24,
        beat_sync=False,
        energy_reactive=True
    ),
    
    "lyric_video": VideoConfig(
        style_preset="music_video_pop",
        theme="abstract",
        segment_duration=3.0,
        fps=30,
        beat_sync=True,
        subtitle_style={
            "fontsize": 60,
            "color": "white",
            "stroke_color": "black",
            "stroke_width": 3
        }
    ),
    
    "cinematic_narrative": VideoConfig(
        style_preset="storytelling",
        theme="cinematic",
        segment_duration=3.5,
        image_width=2560,
        image_height=1440,
        fps=24,
        inference_steps=30
    )
}


# ============================================================================
# CONFIGURATION MANAGER
# ============================================================================

class ConfigManager:
    """Manages video generation configurations"""
    
    def __init__(self):
        self.presets = PRESET_CONFIGS
        self.styles = {**STYLE_MAP, **EXTENDED_STYLES}
        self.themes = SCENE_THEMES
        self.effects = SCENE_EFFECTS
        self.transitions = TRANSITIONS
    
    def get_preset(self, name: str) -> VideoConfig:
        """Get preset configuration"""
        if name not in self.presets:
            raise ValueError(f"Preset '{name}' not found. Available: {list(self.presets.keys())}")
        return self.presets[name]
    
    def list_presets(self) -> List[str]:
        """List available presets"""
        return list(self.presets.keys())
    
    def list_styles(self) -> List[str]:
        """List available styles"""
        return list(self.styles.keys())
    
    def list_themes(self) -> List[str]:
        """List available themes"""
        return list(self.themes.keys())
    
    def get_style(self, name: str) -> Dict:
        """Get style configuration"""
        return self.styles.get(name, self.styles["happy"])
    
    def get_theme_prompts(self, name: str) -> List[str]:
        """Get theme prompt variations"""
        return self.themes.get(name, self.themes["nature"])
    
    def create_custom_config(self, base_preset: str = "music_video_standard",
                           **kwargs) -> VideoConfig:
        """Create custom configuration from preset"""
        config = self.get_preset(base_preset)
        
        # Update with custom values
        for key, value in kwargs.items():
            if hasattr(config, key):
                setattr(config, key, value)
        
        return config
    
    def export_preset(self, config: VideoConfig, name: str, path: str):
        """Export configuration as preset"""
        preset_data = {
            "name": name,
            "description": f"Custom preset: {name}",
            "config": config.to_dict()
        }
        
        with open(path, 'w') as f:
            json.dump(preset_data, f, indent=2)
    
    def import_preset(self, path: str) -> VideoConfig:
        """Import configuration preset"""
        with open(path, 'r') as f:
            preset_data = json.load(f)
        
        return VideoConfig.from_dict(preset_data['config'])


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

def example_usage():
    """Example usage of configuration system"""
    
    manager = ConfigManager()
    
    # List available options
    print("Available presets:", manager.list_presets())
    print("Available styles:", manager.list_styles())
    print("Available themes:", manager.list_themes())
    
    # Use preset
    config = manager.get_preset("music_video_standard")
    print(f"\nMusic video config: {config}")
    
    # Create custom config
    custom = manager.create_custom_config(
        base_preset="podcast_episode",
        segment_duration=4.0,
        theme="urban",
        fps=60
    )
    print(f"\nCustom config: {custom}")
    
    # Save and load
    config.save("my_config.json")
    loaded = VideoConfig.from_json("my_config.json")
    print(f"\nLoaded config: {loaded}")
    
    # Export as preset
    manager.export_preset(custom, "my_preset", "my_preset.json")


# ============================================================================
# EXAMPLE CONFIGURATION FILES
# ============================================================================

EXAMPLE_MUSIC_VIDEO_CONFIG = """
{
  "style_preset": "music_video_pop",
  "theme": "urban",
  "segment_duration": 2.5,
  "image_width": 1920,
  "image_height": 1080,
  "inference_steps": 25,
  "fps": 30,
  "beat_sync": true,
  "energy_reactive": true,
  "enable_effects": true,
  "transition_mode": "sync_to_beat"
}
"""

EXAMPLE_PODCAST_CONFIG = """
{
  "style_preset": "podcast_minimal",
  "theme": "abstract",
  "segment_duration": 8.0,
  "image_width": 1920,
  "image_height": 1080,
  "inference_steps": 15,
  "fps": 24,
  "beat_sync": false,
  "energy_reactive": false,
  "enable_effects": true,
  "transition_mode": "smooth",
  "subtitle_style": {
    "fontsize": 50,
    "color": "white",
    "position": "bottom"
  }
}
"""

EXAMPLE_DOCUMENTARY_CONFIG = """
{
  "style_preset": "documentary",
  "theme": "nature",
  "segment_duration": 4.0,
  "image_width": 3840,
  "image_height": 2160,
  "inference_steps": 30,
  "fps": 24,
  "beat_sync": false,
  "energy_reactive": true,
  "enable_effects": true,
  "transition_mode": "smooth",
  "bitrate": "20000k"
}
"""


if __name__ == "__main__":
    example_usage()
