from typing import Tuple, List
from pathlib import Path
from datetime import date


def generate_report(vault: Path, output_dir: Path, start: date, end: date, sections):
    created, updated = gather_files(vault, start, end)
    report = Report(vault, output_dir, start, end)
    print(f'Report will be saved to file: {report.path}')
    report.add_title(f'{start.isoformat()} – {end.isoformat()}')
    if sections in ['all', 'created']:
        print('Adding created files...')
        report.add_section('Created', created)
    if sections in ['all', 'updated']:
        print('Adding updated files...')
        report.add_section('Updated', updated)


def gather_files(dir: Path, start: date, end: date) -> Tuple[List[Path], List[Path]]:
    created = []
    updated = []
    files = sorted(dir.rglob('*.md'))
    for f in files:
        if '.trash' in f.parts:
            continue
        create_time = date.fromtimestamp(f.stat().st_ctime)
        update_time = date.fromtimestamp(f.stat().st_mtime)
        if start <= create_time <= end:
            created.append(f)
        elif start <= update_time <= end:
            updated.append(f)
    return created, updated


class Report:
    def __init__(self, vault: Path, output_dir: Path, start: date, end: date):
        report_path = output_dir / f'{start.isoformat()} - {end.isoformat()}.md'
        report_path.touch(exist_ok=True)
        self.path = report_path
        self.vault = vault

    def add_title(self, title: str):
        with self.path.open(mode='w') as report_file:
            report_file.write(f'# {title}\n\n')

    def add_section(self, heading: str, files: List[Path]):
        with self.path.open(mode='a') as report_file:
            report_file.write(f'## {heading}\n\n')
            if files:
                report_file.writelines(map(
                    self.path_to_list_item,
                    files
                ))
                report_file.write('\n\n')
            else:
                report_file.write('No files.\n\n')

    def path_to_list_item(self, path: Path) -> str:
        path_link = str(path.relative_to(self.vault).with_suffix(''))
        return f'- [[{path_link}]]\n'
