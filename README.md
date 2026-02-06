# Video Generator Configuration

Configuration module for the AI Video Generation system. Contains style definitions, effect presets, transition settings, and configuration management utilities.

## Features

- **Extended Style Library**: Presets for Music Videos, Documentaries, Podcasts, and Artistic styles.
- **Scene Effects**: Definitions for visual effects like motion blur, vignetting, film grain, etc.
- **Transition Library**: Configuration for video transitions (cuts, fades, wipes).
- **Configuration Management**: `VideoConfig` dataclass and `ConfigManager` for handling settings.

## Usage

```python
from video_gen_config import ConfigManager

manager = ConfigManager()
config = manager.get_preset("music_video_standard")
print(config.style_preset)
```

**Note**: This module may depend on `STYLE_MAP` and `SCENE_THEMES` expected to be present in the execution environment (e.g. from `ai_video_generator`).
