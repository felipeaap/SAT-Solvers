import argparse

from brute_force.solver import brute_force_sat
from davis_putnam.solver import davis_putnam_sat
from DPLL.solver import dpll_sat
from CDCL.solver import cdcl_sat

from cnf import (
    benchmark,
    load_dimacs,
)

SOLVERS = {
    "brute_force": brute_force_sat,
    "davis_putnam": davis_putnam_sat,
    "dpll": dpll_sat,
    "cdcl": cdcl_sat,
}


def run_solver(solver_name: str,cnf_path: str):
    solver = SOLVERS[solver_name]
    cnf = load_dimacs(cnf_path)
    result = solver(cnf)
    status = "SAT" if result else "UNSAT"
    print(f"\nResult: {status}")


def run_benchmark(solver_name: str):
    solver = SOLVERS[solver_name]
    benchmark(solver)

def run_all_benchmarks():
    for name, solver in SOLVERS.items():
        print("\n"+ "=" * 60)
        print(f"BENCHMARK {name.upper()}")
        print("=" * 60)
        benchmark(solver)

def main():
    parser = argparse.ArgumentParser(description="SAT Solver Framework")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    solve_parser = subparsers.add_parser("solve")
    solve_parser.add_argument("solver", choices=SOLVERS.keys())
    solve_parser.add_argument("cnf_file")

    bench_parser = subparsers.add_parser("benchmark")
    bench_parser.add_argument(
        "solver",
        choices=[
            *SOLVERS.keys(),
            "all",
        ],
    )
    args = parser.parse_args()

    if args.command == "solve":
        run_solver(args.solver,args.cnf_file)
    elif args.command == "benchmark":
        if args.solver == "all":
            run_all_benchmarks()
        else:
            run_benchmark(args.solver)


if __name__ == "__main__":
    main()