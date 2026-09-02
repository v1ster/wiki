#!/usr/bin/env python3
import re
import os
from pathlib import Path
import yaml

base = Path("/home/pi/playground/wiki")

# category mapping based on path
def infer_categories(rel_path: Path):
    # rel_path like docs/linux/distro/xxx.md
    parts = rel_path.parts # ('docs','linux','distro','file.md')
    if len(parts) < 3:
        return ["uncategorized"]
    top = parts[1]
    # map top to standardized categories
    mapping = {
        "linux": ["linux"],
        "embedded": ["embedded"],
        "git": ["git"],
        "network": ["network"],
        "tools": ["tools"],
        "programming": ["programming"],
        "windows": ["windows"],
        "cheatsheet": ["cheatsheet"],
    }
    return mapping.get(top, [top])

# tag normalization
def normalize_tag(t):
    if not isinstance(t, str):
        return str(t).strip().lower()
    t = t.strip()
    # lower except keep case for like c/cpp -> c/cpp lower is fine
    # special: Shell -> shell
    t = t.lower()
    # map some
    mapping = {
        "c/cpp": "c-cpp",
        "c++": "cpp",
        "shell": "shell",
        "cheatsheet": "cheatsheet",
        "www": "web", # but we will filter out? Actually www was erroneous category, not tag; tags rarely www
    }
    return mapping.get(t, t)

# files to process
files = list(base.glob("docs/**/*.md"))
# exclude index.md and blog/tags.md and assets?
exclude = []
processed = []

for f in files:
    if f.name == "index.md" and f.parent.name in ["docs", "linux","embedded","git","network","tools","programming","windows","cheatsheet","distro","filesystem","system","buildroot","yocto","kernel","hardware","proxy","apt","ssh","samba","misc","c-cpp","python","shell"]:
        # we will handle index separately, skip normalizing index if it's newly created; but existing index.md also skip?
        # For now skip all index.md
        continue
    if "blog/tags.md" in str(f):
        continue
    if "assets" in str(f):
        continue
    # also skip docs/index.md which we will rewrite separately
    if f == base / "docs/index.md":
        continue
    # check if file has frontmatter
    text = f.read_text(encoding="utf-8", errors="ignore")
    # detect frontmatter
    if not text.startswith("---"):
        print(f"SKIP no frontmatter: {f.relative_to(base)}")
        continue

    # split frontmatter
    # find second ---
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not m:
        print(f"SKIP bad frontmatter: {f.relative_to(base)}")
        continue
    fm_raw = m.group(1)
    body = text[m.end():]
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except Exception as e:
        print(f"YAML parse error {f}: {e}")
        # try fallback simple parse?
        continue

    original_fm = dict(fm)
    # Normalize keys
    # handle both category/categories
    cats = None
    if "categories" in fm:
        cats = fm.pop("categories")
    if "category" in fm:
        c = fm.pop("category")
        if cats is None:
            cats = c
        else:
            # merge
            if isinstance(cats, list) and isinstance(c, list):
                cats = cats + c
            elif isinstance(cats, list):
                cats = cats + [c]
            else:
                cats = [cats, c] if isinstance(c, str) else [cats] + c
    # also handle tags
    tags = fm.get("tags", [])
    if tags is None:
        tags = []
    if isinstance(tags, str):
        tags = [tags]
    # also categories normalization
    if cats is None:
        # infer from path
        cats = infer_categories(f.relative_to(base))
    else:
        if isinstance(cats, str):
            cats = [cats]
        # ensure list
        if not isinstance(cats, list):
            cats = list(cats)
        # flatten
        flat = []
        for c in cats:
            if isinstance(c, list):
                flat.extend(c)
            else:
                flat.append(c)
        cats = flat
    # normalize cats: lower, strip, map wrong ones
    cat_map = {
        "www": "linux", # Gentoo guide had www erroneously
        "c/cpp": "programming",
        "code": "programming",
        "tool": "tools",
        "system": "linux",
        "web": "linux",
        "v2ray": "network",
        "linux": "linux",
        "embedded": "embedded",
        "git": "git",
        "network": "network",
        "tools": "tools",
        "programming": "programming",
        "windows": "windows",
        "cheatsheet": "cheatsheet",
    }
    # For files under specific top, we want to ensure categories matches top
    inferred = infer_categories(f.relative_to(base))
    # If original cats contains inferred already, keep inferred; else replace erroneous
    # Decision: categories should be exactly inferred top category (single) to match directory
    # Except programming/c-cpp files should be programming, not c/cpp
    # So override cats to inferred
    # But we could keep sub-category as second element? For now keep single inferred
    # However we want to preserve intent: if inferred is programming but original had c/cpp, we keep programming
    # So set cats = inferred
    # But for embedded files, inferred is embedded, good
    # For linux/distro, inferred is linux
    # For network/proxy, inferred is network
    # For tools/*, inferred is tools
    cats = inferred

    # tags normalization
    # lower, dedup, remove WIP, abbrlink etc handled separately
    normalized_tags = []
    seen = set()
    for t in tags:
        nt = normalize_tag(t)
        # filter WIP and empty
        if nt in ("wip", ""):
            continue
        # also filter tags that are same as categories? Keep but dedup
        if nt not in seen:
            seen.add(nt)
            normalized_tags.append(nt)
    # Also add inferred subcategory tag based on subdir for discoverability
    # e.g., tools/apt files should have tags apt, tools; tools/ssh -> ssh
    # Add extra tags if not present
    rel_parts = f.relative_to(base).parts
    # rel_parts[2] is subdir like distro, buildroot, apt, ssh etc
    if len(rel_parts) >= 3:
        sub = rel_parts[2]
        # map sub to tag
        sub_tag_map = {
            "distro": None,
            "filesystem": "filesystem",
            "system": None,
            "buildroot": "buildroot",
            "yocto": "yocto",
            "kernel": "kernel",
            "hardware": "hardware",
            "proxy": "proxy",
            "apt": "apt",
            "ssh": "ssh",
            "samba": "samba",
            "misc": None,
            "c-cpp": "c-cpp",
            "python": "python",
            "shell": "shell",
        }
        extra = sub_tag_map.get(sub)
        if extra and extra not in seen:
            # only add if relevant
            normalized_tags.append(extra)
            seen.add(extra)
    # Ensure at least one tag, if empty add category
    if not normalized_tags:
        normalized_tags = cats.copy()
    # Sort tags alphabetically for consistency but keep original order? Sort
    # Keep sorted for determinism
    normalized_tags = sorted(set(normalized_tags))

    # Also fix abbrlink removal, draft, etc
    # Remove abbrlink, slug, etc if present
    for key in list(fm.keys()):
        if key in ("abbrlink", "slug"):
            fm.pop(key)
    # Ensure title and date exist
    title = fm.get("title")
    if not title:
        # infer from filename without extension
        fm["title"] = f.stem
    date = fm.get("date")
    # keep date as is, if missing skip

    # Rebuild fm with ordered keys: title, date, categories, tags
    new_fm = {}
    new_fm["title"] = fm.get("title")
    if date:
        new_fm["date"] = date
    # add categories
    new_fm["categories"] = cats
    new_fm["tags"] = normalized_tags
    # preserve other keys? like maybe not needed; but keep any other meaningful like draft?
    for k, v in fm.items():
        if k not in ("title", "date", "tags", "categories", "category"):
            # keep draft etc
            new_fm[k] = v

    # Only write if changed
    if original_fm.get("tags") != new_fm.get("tags") or original_fm.get("categories") != new_fm.get("categories") or original_fm.get("category") is not None or "abbrlink" in original_fm or sorted(original_fm.get("tags", [])) != sorted(new_fm.get("tags", [])):
        # write back
        # Serialize with yaml
        fm_yaml = yaml.safe_dump(new_fm, sort_keys=False, allow_unicode=True, default_flow_style=False).strip()
        new_text = f"---\n{fm_yaml}\n---\n\n{body.lstrip()}"
        f.write_text(new_text, encoding="utf-8")
        print(f"UPDATED {f.relative_to(base)} | categories: {new_fm['categories']} tags: {new_fm['tags']}")
        processed.append(str(f.relative_to(base)))
    else:
        # still need to ensure file is normalized even if no change? Check category key fix
        # ensure file has categories not category
        if "category" in original_fm or "categories" not in original_fm:
            fm_yaml = yaml.safe_dump(new_fm, sort_keys=False, allow_unicode=True, default_flow_style=False).strip()
            new_text = f"---\n{fm_yaml}\n---\n\n{body.lstrip()}"
            f.write_text(new_text, encoding="utf-8")
            print(f"FIXED {f.relative_to(base)}")
            processed.append(str(f.relative_to(base)))

print(f"\nProcessed {len(processed)} files")
