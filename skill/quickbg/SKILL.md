---
name: quickbg
description: Use Jack's GitHub/PyPI-style QuickBG tool for local background removal with rembg. Trigger this when the user says quickbg, quick bg, local background removal, offline background removal, rembg-based cutout, or wants to use the jschof1/quickbg repo. Do not confuse this with bgremove-api, which is the separate remove.bg API-backed workflow.
---

# QuickBG

Use this skill when Jack wants the `jschof1/quickbg` repo or the local `rembg`-based background-removal package.

Canonical repo:

```text
/Users/jack/Documents/GitHub/quickbg
https://github.com/jschof1/quickbg
```

This tool is separate from:

```text
/Users/jack/Documents/GitHub/bgremove-api
```

`quickbg` uses local `rembg` processing. It does not use Jack's remove.bg API key.

## Default Workflow

1. Check command resolution:

   ```bash
   command -v quickbg
   quickbg --help
   ```

2. If the command or dependency is missing, work from the repo:

   ```bash
   cd /Users/jack/Documents/GitHub/quickbg
   python3 -m pip install -e .
   ```

3. Check the input exists:

   ```bash
   test -f "/path/to/image.jpg"
   ```

   For batch mode, use `test -d`.

4. Run the local processor:

   ```bash
   quickbg "/path/to/image.jpg" -o "/path/to/image-nobg.png"
   ```

5. Batch mode:

   ```bash
   quickbg -b "/path/to/images" -o "/path/to/images/nobg"
   ```

6. Verify output before reporting completion:

   ```bash
   test -s "/path/to/image-nobg.png"
   file "/path/to/image-nobg.png"
   ```

## Common Commands

```bash
quickbg photo.jpg
quickbg photo.jpg -o result.png
quickbg -b ./photos
quickbg -b ./photos -o ./photos/nobg
quickbg photo.jpg --alpha-matting
```

## Choosing Between Tools

Use `quickbg` when Jack says `quickbg`, wants the GitHub repo, wants local/offline processing, or does not mention remove.bg.

Use `bgremove-api` when Jack specifically mentions remove.bg, API-backed output, URL inputs, `--size hd/full`, `--bg-color`, or the existing remove.bg key.

Keep the two workflows separate in explanations, symlinks, commits, and docs.
