import argparse
import calendar
from datetime import date
from pathlib import Path

from obsidian_progress_report.report import generate_report


def dir_path(path: str) -> Path:
    if Path(path).is_dir():
        return Path(path).absolute()
    else:
        raise argparse.ArgumentTypeError(f'{path} is not a valid directory path')


def date_arg(d: str) -> date:
    try:
        return date.fromisoformat(d)
    except ValueError:
        raise argparse.ArgumentTypeError(f'Given date \'{d}\' is not valid')


def main():
    parser = argparse.ArgumentParser(
        description='A simple command line app for generating progress report for contributions in the Obsidian vault.',
    )
    parser.add_argument(dest='vault', type=dir_path, help='Path where to find the Obsidian vault.')
    parser.add_argument(
        '-o', '--output', default='.',
        help='Where to save the generated report (relative to the vault\'s root). If not specified, root will be used.'
    )
    current_day: date = date.today()
    start_of_month = current_day.replace(day=1)
    _, last_day = calendar.monthrange(current_day.year, current_day.month)
    end_of_month = current_day.replace(day=last_day)

    parser.add_argument(
        '-s', '--start', type=date, default=start_of_month,
        help='Start of report period, by default is set to the start of current month. Format: "YYYY-MM-DD".'
    )
    parser.add_argument(
        '-e', '--end', type=date, default=end_of_month,
        help='End of report period, by default is set to the end of current month. Format: "YYYY-MM-DD".'
    )
    parser.add_argument(
        '-i', '--include', choices=['created', 'updated', 'all'], default='all',
        help='Which sections report should contain.'
    )
    args = parser.parse_args()
    output_dir: Path = (args.vault / args.output).absolute()
    print(f'Creating output directory: {output_dir}')
    output_dir.mkdir(parents=True, exist_ok=True)
    print('Start report generation...')
    generate_report(args.vault, output_dir, args.start, args.end, args.include)
    print('Report is generated!')


if __name__ == '__main__':
    main()
