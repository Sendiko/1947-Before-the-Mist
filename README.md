# 1947 Before the Mist

An in-progress Ren'Py visual novel set in Purwokerto in 1947. The story follows Sumarno during the conflict and evacuation. The game scripts and story notes are primarily written in Indonesian.

## Run the game

1. Install the Ren'Py SDK from [renpy.org](https://www.renpy.org/).
2. Open the Ren'Py Launcher and add this project directory: `1947 Before the Mist`.
3. Select the project and choose **Launch Project**.

The current entry point is `label start` in `game/script.rpy`, which jumps to `label before_conflict`. No separate dependency manifest is present; `game/libs/` is reserved for third-party libraries if the project needs them.

## Project structure

```text
.
├── README.md                 Project overview and this guide
├── .vscode/                  Editor workspace settings
└── game/                     Ren'Py project content
    ├── script.rpy            Game entry point
    ├── options.rpy           Name, version, saves, audio, and build settings
    ├── gui.rpy               GUI dimensions, fonts, colors, and layout settings
    ├── screens.rpy           Ren'Py screens and interface styles
    ├── src/                  Implemented Ren'Py scripts and declarations
    │   ├── characters/       Character definitions and transforms
    │   ├── images/           Image aliases used by script
    │   └── main/             Story scripts by narrative section
    │       ├── 1_prologue/
    │       ├── 2_conflict/
    │       └── 3_consolidation/
    ├── stories/              Markdown story drafts and character notes
    │   ├── characters.md
    │   ├── 1_prologue/
    │   ├── 2_conflict/
    │   └── 3_consolidation/
    ├── images/               Background and character image assets
    │   ├── backgrounds/
    │   └── characters/
    ├── audio/                Music, sound effects, and voice assets
    ├── gui/                  GUI image assets and interface components
    ├── libs/                 Optional third-party Ren'Py libraries
    ├── tl/                   Translation files
    ├── saves/                Local save data
    └── cache/                Ren'Py-generated cache data
```

## Where to make changes

- **Story and dialogue:** Implement playable scenes in `.rpy` files under `game/src/main/`. Ren'Py labels are the scene entry points; the prologue currently starts at `before_conflict`.
- **Story planning:** Keep drafts and branching outlines in the matching section under `game/stories/`. These Markdown files are reference material and are not executed by Ren'Py.
- **Characters:** Declare character objects and reusable transforms in `game/src/characters/characters.rpy`.
- **Images:** Put image files under `game/images/`, then declare names for use in script in `game/src/images/images.rpy`. For example, the `gedung soetedja` image name refers to a background file.
- **Interface and settings:** Change `game/gui.rpy` for GUI layout and styling, `game/screens.rpy` for screen behavior, and `game/options.rpy` for game metadata and settings.

## Current implementation status

The entry point reaches the prologue scene, which currently contains an opening narration and Sumarno's meeting with his uncle. The Markdown prologue draft describes additional scenes and choices that are not yet implemented in the Ren'Py script. The conflict and consolidation `.rpy` files currently contain section comments only; their corresponding Markdown files are story drafts.

Ren'Py-generated compiled scripts (`.rpyc`), cache data, and save data are present in the workspace but are not the source of truth. Edit the `.rpy` and Markdown source files instead. The root `.gitignore` excludes save/cache data, compiled scripts, and several generated log/output files.

## Commit messages

Use one of these prefixes to describe the change:

- `docs:` Add or update story Markdown files.
- `scripts:` Add or update Ren'Py scripts.
- `chore:` Add or remove files unrelated to both story documentation and Ren'Py scripts.
- `feat:` Add or remove Ren'Py files.
- `refactor:` Refactor existing Ren'Py files.