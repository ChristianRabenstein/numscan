from numscan import FibonacciCounter, PrimeCounter, SquareCounter, PopCultureCounter, IntegerCounter

def print_top_counts(counter, name: str, top_n: int = 5):
    print(f"\nTop {top_n} matches for {name}:")
    counts = counter.counts
    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for number, count in top:
        if isinstance(counter, PopCultureCounter):
            description = counter.get_description(number)
            print(f"{number}: {count} times — {description}")
        else:
            print(f"{number}: {count} times")

def main():
    filepath = "example.txt"  # Replace with your actual file
    limit = 1000

    fib_counter = FibonacciCounter(filepath, limit)
    prime_counter = PrimeCounter(filepath, limit)
    square_counter = SquareCounter(filepath, limit)
    pop_counter = PopCultureCounter(filepath, limit)
    all_counter = IntegerCounter(filepath, limit)

    print_top_counts(fib_counter, "Fibonacci Numbers")
    print_top_counts(prime_counter, "Prime Numbers")
    print_top_counts(square_counter, "Square Numbers")
    print_top_counts(pop_counter, "Pop Culture Numbers")
    print_top_counts(all_counter, "All Integers")

if __name__ == "__main__":
    main()