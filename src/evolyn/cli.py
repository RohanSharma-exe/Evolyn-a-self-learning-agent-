import argparse
import asyncio

from evolyn import Evolyn
from evolyn.observability import configure_observability


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Evolyn from the terminal.")
    parser.add_argument("task", nargs="+", help="Task for Evolyn")
    args = parser.parse_args()

    configure_observability()
    result = asyncio.run(Evolyn().run(" ".join(args.task)))

    print("\nEVOLYN\n")
    print(result.response)
    if result.experiences and result.experiences[0].lesson:
        print(f"\nLearned: {result.experiences[0].lesson}")
    if result.trace_url:
        print(f"\nTrace: {result.trace_url}")


if __name__ == "__main__":
    main()
