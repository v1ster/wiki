#!/usr/bin/env python3
import re
from pathlib import Path

base = Path("/home/pi/playground/wiki")

def infer_categories(rel_path: Path):
    parts = rel_path.parts
    if len(parts) < 3:
        return ["uncategorized"]
    top = parts[1]
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

def normalize_tag(t):
    t = t.strip().lower()
    mapping = {
        "c/cpp": "c-cpp",
        "c++": "cpp",
        "www": "web",
    }
    return mapping.get(t.lower(), t.lower())

def parse_frontmatter(text):
    # returns dict, body
    if not text.startswith("---"):
        return None, text
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not m:
        return None, text
    fm_raw = m.group(1)
    body = text[m.end():]
    fm = {}
    current_key = None
    # simple line parse
    for line in fm_raw.splitlines():
        # skip empty
        if not line.strip():
            continue
        # list item?
        if re.match(r'^\s*-\s+', line):
            item = re.sub(r'^\s*-\s+', '', line).strip()
            # remove quotes if any
            item = item.strip('"\'')
            if current_key:
                if current_key not in fm or not isinstance(fm[current_key], list):
                    fm[current_key] = []
                fm[current_key].append(item)
            continue
        # key: value
        if ':' in line:
            k, v = line.split(':', 1)
            k = k.strip()
            v = v.strip()
            # if v is empty, it's a list header
            if v == "":
                fm[k] = []
                current_key = k
            else:
                # strip quotes
                v = v.strip('"\'')
                # handle inline list? like tags: [a, b] not present
                fm[k] = v
                current_key = k
        else:
            continue
    return fm, body

def dump_frontmatter(fm):
    # fm is dict with title, date, categories, tags etc
    lines = ["---"]
    # order: title, date, categories, tags, then others
    order = ["title", "date", "categories", "tags"]
    for k in order:
        if k in fm:
            v = fm[k]
            if isinstance(v, list):
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                # need to quote if contains colon?
                lines.append(f"{k}: {v}")
    # other keys
    for k, v in fm.items():
        if k in order:
            continue
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"

files = list(base.glob("docs/**/*.md"))
processed = []
for f in files:
    # skip index and blog/tags and assets
    if f.name == "index.md":
        continue
    if "blog/tags.md" in str(f):
        continue
    if "assets" in str(f):
        continue
    if f == base / "docs/index.md":
        continue
    text = f.read_text(encoding="utf-8", errors="ignore")
    fm, body = parse_frontmatter(text)
    if fm is None:
        print(f"SKIP no frontmatter: {f.relative_to(base)}")
        continue
    original = dict(fm)
    # handle both category/categories
    cats = None
    if "categories" in fm:
        cats = fm.pop("categories")
        if isinstance(cats, str):
            cats = [cats]
        elif not isinstance(cats, list):
            cats = [str(cats)]
    if "category" in fm:
        c = fm.pop("category")
        if isinstance(c, str):
            c = [c]
        elif not isinstance(c, list):
            c = [str(c)]
        if cats is None:
            cats = c
        else:
            # merge
            cats = cats + c
    # also pop tags
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    if tags is None:
        tags = []
    # ensure list
    if not isinstance(tags, list):
        tags = [tags]
    # Normalize cats to inferred
    inferred = infer_categories(f.relative_to(base))
    # For now force cats = inferred
    # But we want to log what original was if different
    new_cats = inferred

    # tags normalization
    normalized_tags = []
    seen = set()
    for t in tags:
        if t is None:
            continue
        nt = normalize_tag(str(t))
        if nt in ("wip", "", "abbrlink"):
            continue
        if nt not in seen:
            seen.add(nt)
            normalized_tags.append(nt)
    # also remove wip tag if present case insensitive
    # extra sub tags
    rel_parts = f.relative_to(base).parts
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
        "cheatsheet": None,
        "windows": None,
    }
    if len(rel_parts) >= 3:
        sub = rel_parts[2]
        extra = sub_tag_map.get(sub)
        if extra and extra not in seen:
            normalized_tags.append(extra)
            seen.add(extra)
        # also for deeper? like tools/apt, programming/c-cpp -> need level 3? Actually rel_parts[2] is already apt etc for tools, but for linux/distro it's distro, we already; but for tools we want apt/ssh also? Wait tools/apt -> parts = docs,tools,apt,file => sub=apt already
        # for programming/c-cpp -> sub=c-cpp
        pass
    # also ensure if file is under programming/python but tags doesn't have python, add
    # already handled via sub_tag_map

    if not normalized_tags:
        normalized_tags = new_cats.copy()
    # deduplicate and sort
    normalized_tags = sorted(set(normalized_tags))

    # Remove abbrlink, slug
    fm.pop("abbrlink", None)
    fm.pop("slug", None)
    # also remove old tags entry to rebuild
    fm.pop("tags", None)
    # preserve title/date
    title = fm.get("title")
    if not title:
        fm["title"] = f.stem
    # date keep as is if exists
    # Now rebuild fm with new categories/tags
    new_fm = {}
    new_fm["title"] = fm.get("title")
    if "date" in fm:
        new_fm["date"] = fm["date"]
    elif "date" in original:
        new_fm["date"] = original["date"]
    new_fm["categories"] = new_cats
    new_fm["tags"] = normalized_tags
    # preserve other keys except title/date/categories/tags
    for k, v in fm.items():
        if k not in ("title", "date"):
            new_fm[k] = v
    # Check if changed
    orig_tags_sorted = sorted([normalize_tag(str(t)) for t in original.get("tags", []) if normalize_tag(str(t)) != "wip"]) if original.get("tags") else []
    # also need to consider original categories vs new
    orig_cats = original.get("categories") or original.get("category") or []
    if isinstance(orig_cats, str):
        orig_cats = [orig_cats]
    # compare
    changed = False
    if set(normalized_tags) != set(orig_tags_sorted):
        changed = True
    if orig_cats != new_cats:
        # also if original had category vs categories
        changed = True
    if "category" in original:
        changed = True
    if "abbrlink" in original:
        changed = True
    # Also check if original had categories but not sorted?
    # Force write if inferred not matching
    # For WIP files that had no tags normalization, also fix

    # Always write to ensure consistent formatting (categories/tags lowercased, sorted)
    # But only if needed; we will write if changed or to fix formatting
    if changed or "categories" not in original or "category" in original or "abbrlink" in original:
        new_text = dump_frontmatter(new_fm) + body.lstrip()
        f.write_text(new_text, encoding="utf-8")
        print(f"UPDATED {f.relative_to(base)} | categories: {new_cats} tags: {normalized_tags} (orig cats: {orig_cats} orig tags: {original.get('tags')})")
        processed.append(str(f.relative_to(base)))
    else:
        # ensure we still rewrite if tags not sorted? check
        if original.get("tags") != normalized_tags:
            new_text = dump_frontmatter(new_fm) + body.lstrip()
            f.write_text(new_text, encoding="utf-8")
            print(f"FIXED order {f.relative_to(base)}")
            processed.append(str(f.relative_to(base)))

print(f"\nProcessed {len(processed)} files")
