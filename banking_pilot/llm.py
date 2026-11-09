"""Thin Claude client wrapper: loads .env, runs one step, logs the exact prompt and output.

Every call is written to runs/<run_id>/ so reviewers (and compliance, per policy 7:
"document all prompts and workflows") can see exactly what was sent and returned.
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import TypeVar

import anthropic
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"
MODEL = os.environ.get("BANK_PILOT_MODEL", "claude-opus-5-5")

T = TypeVar("T", bound=BaseModel)


def _load_env() -> None:
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*([A-Z_]+)\s*=\s*(.*)\s*$", line)
            if m and m.group(2) and not os.environ.get(m.group(1)):
                os.environ[m.group(1)] = m.group(2)


_load_env()
_client = anthropic.Anthropic()


def prompt(name: str) -> str:
    return (PROMPTS / f"{name}.md").read_text(encoding="utf-8")


class Run:
    def __init__(self, label: str):
        self.dir = ROOT / "runs" / f"{time.strftime('%Y%m%d-%H%M%S')}-{label}"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.step = 0

    def save(self, name: str, content: str | dict | list) -> Path:
        path = self.dir / name
        if isinstance(content, (dict, list)):
            path.write_text(json.dumps(content, indent=2, ensure_ascii=False), encoding="utf-8")
        else:
            path.write_text(content, encoding="utf-8")
        return path

    def call(self, step_name: str, system: str, user: str, schema: type[T] | None = None,
             effort: str = "high") -> T | str:
        """One model step. Returns the parsed schema instance, or text when schema is None."""
        self.step += 1
        tag = f"{self.step:02d}_{step_name}"
        started = time.time()
        kwargs = dict(
            model=MODEL,
            max_tokens=64000,
            system=system,
            messages=[{"role": "user", "content": user}],
            output_config={"effort": effort},
        )
        if schema is not None:
            kwargs["output_format"] = schema
        # Streaming avoids HTTP timeouts on long fact sheets.
        with _client.messages.stream(**kwargs) as stream:
            resp = stream.get_final_message()
        if resp.stop_reason == "refusal":
            raise RuntimeError(f"{tag}: model refused ({resp.stop_details})")
        if resp.stop_reason == "max_tokens":
            raise RuntimeError(f"{tag}: hit max_tokens; output truncated")
        text = "".join(b.text for b in resp.content if b.type == "text")
        if schema is not None:
            result = schema.model_validate_json(text)
            out_text = result.model_dump_json(indent=2)
        else:
            result = out_text = text
        self.save(f"{tag}.prompt.md", f"# SYSTEM\n\n{system}\n\n# USER\n\n{user}\n")
        self.save(f"{tag}.output.{'json' if schema else 'md'}", out_text)
        self.save(f"{tag}.meta.json", {
            "model": resp.model, "effort": effort, "seconds": round(time.time() - started, 1),
            "input_tokens": resp.usage.input_tokens, "output_tokens": resp.usage.output_tokens,
        })
        return result
