from pathlib import Path

DEV_MODE = False

if DEV_MODE:
    REPO_DIR = Path(__file__).parent.parent.parent
    JS_PATH = REPO_DIR / "js" / "script.js"
    CSS_PATH = REPO_DIR / "js" / "styles.css"
else:
    CURRENT_DIR = Path(__file__).parent
    JS_PATH = CURRENT_DIR / "static" / "script.js"
    CSS_PATH = CURRENT_DIR / "static" / "styles.css"
